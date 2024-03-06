import kue from 'kue';

const queue = kue.createQueue();

function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  jobs.forEach((jobData) => {
    const notificationJob = queue.create('push_notification_code_3', jobData);

    notificationJob
      .save((err) => {
        if (!err) {
          console.log(`Notification job created: ${notificationJob.id}`);
        } else {
          console.log(`Error creating notification job: ${err}`);
        }
      })
      .on('complete', () => {
        console.log(`Notification job ${notificationJob.id} completed`);
      })
      .on('failed', (err) => {
        console.log(`Notification job ${notificationJob.id} failed: ${err}`);
      })
      .on('progress', (progress) => {
        console.log(`Notification job ${notificationJob.id} ${progress}% complete`);
      });
  });
}

// Example usage
const jobs = [
  { phoneNumber: '1234567890', message: 'Hello, this is job 1' },
  { phoneNumber: '9876543210', message: 'Greetings from job 2' },
];

createPushNotificationsJobs(jobs, queue);
