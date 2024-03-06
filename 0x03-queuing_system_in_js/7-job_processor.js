import kue from 'kue';

const blacklistedNumbers = ['4153518780', '4153518781'];

const queue = kue.createQueue({
  redis: {
    port: 6379, // Replace with your Redis port if it's different
    host: '127.0.0.1', // Replace with your Redis host
  },
});

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    return done(new Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  console.log(`Sending notification to ${phoneNumber} with message: ${message}`);
  done();
};

queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

queue.on('job enqueue', () => {
  console.log('Job enqueued');
});

queue.on('job complete', () => {
  console.log('Job completed');
});

queue.on('job failed', (id, errorMessage) => {
  console.log(`Job ${id} failed with error: ${errorMessage}`);
});

// Example jobs
const job1 = queue.create('push_notification_code_2', {
  phoneNumber: '1234567890',
  message: 'Hello, this is a notification!',
});

const job2 = queue.create('push_notification_code_2', {
  phoneNumber: '4153518780', // This number is blacklisted
  message: 'This job should fail',
});

// Save the jobs to the queue
job1.save();
job2.save();
