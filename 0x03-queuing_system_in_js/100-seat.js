import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

const app = express();
const port = 1245;

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);
const setAsync = promisify(client.set).bind(client);

const queue = kue.createQueue();

let numberOfAvailableSeats = 50;
let reservationEnabled = true;

const reserveSeat = async (number) => {
  await setAsync('available_seats', number.toString());
};

const getCurrentAvailableSeats = async () => {
  const result = await getAsync('available_seats');
  return result ? parseInt(result, 10) : 0;
};

app.get('/available_seats', async (req, res) => {
  const availableSeats = await getCurrentAvailableSeats();
  res.json({ numberOfAvailableSeats: availableSeats });
});

app.get('/reserve_seat', (req, res) => {
  if (!reservationEnabled) {
    res.json({ status: 'Reservation are blocked' });
    return;
  }

  const job = queue.create('reserve_seat').save((err) => {
    if (!err) {
      res.json({ status: 'Reservation in process' });
    } else {
      res.json({ status: 'Reservation failed' });
    }
  });

  job.on('complete', (result) => {
    console.log(`Seat reservation job ${job.id} completed`);
  });

  job.on('failed', (errorMessage) => {
    console.log(`Seat reservation job ${job.id} failed: ${errorMessage}`);
  });
});

app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });

  queue.process('reserve_seat', async (job, done) => {
    const currentSeats = await getCurrentAvailableSeats();

    if (currentSeats === 0) {
      reservationEnabled = false;
      done(new Error('Not enough seats available'));
    } else {
      numberOfAvailableSeats--;
      await reserveSeat(numberOfAvailableSeats);

      if (numberOfAvailableSeats === 0) {
        reservationEnabled = false;
      }

      done();
    }
  });
});

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
