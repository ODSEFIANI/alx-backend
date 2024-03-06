import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
  phoneNumber: '1234567890', // Replace with the actual phone number
  message: 'Hello, this is a notification!', // Replace with the actual message
};

const notificationJob = queue.create('push_notification_code', jobData);

notificationJob
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${notificationJob.id}`);
    } else {
      console.log('Error creating notification job:', err);
    }
  })
  .on('complete', () => {
    console.log('Notification job completed');
    process.exit(0); // Exit the script after completing the job
  })
  .on('failed', () => {
    console.log('Notification job failed');
    process.exit(1); // Exit the script with an error code after a failed job
  });
