import kue from 'kue';
import chai from 'chai';
import { createPushNotificationsJobs } from './8-job'; // Adjust the import path accordingly

const { expect } = chai;

describe('createPushNotificationsJobs', () => {
  let queue;

  beforeEach(() => {
    queue = kue.createQueue();
    queue.testMode.enter();
  });

  afterEach(() => {
    queue.testMode.clear();
    queue.testMode.exit();
  });

  it('should throw an error if jobs is not an array', () => {
    const invalidCall = () => createPushNotificationsJobs('notAnArray', queue);
    expect(invalidCall).to.throw(Error, 'Jobs is not an array');
  });

  it('should create jobs in the queue', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Test job 1' },
      { phoneNumber: '9876543210', message: 'Test job 2' },
    ];

    createPushNotificationsJobs(jobs, queue);

    expect(queue.testMode.jobs.length).to.equal(2);
  });

  it('should log messages for job creation, completion, failure, and progress', () => {
    const jobs = [
      { phoneNumber: '1234567890', message: 'Test job 1' },
      { phoneNumber: '9876543210', message: 'Test job 2' },
    ];

    createPushNotificationsJobs(jobs, queue);

    // Trigger completion, failure, and progress events for the first job
    queue.testMode.jobs[0].emit('complete');
    queue.testMode.jobs[1].emit('failed', new Error('Test error'));
    queue.testMode.jobs[0].emit('progress', 50);

    // Log messages
    const logs = console.log.getCalls().map((call) => call.args.join(' '));
    expect(logs).to.include('Notification job created:');
    expect(logs).to.include('Notification job completed');
    expect(logs).to.include('Notification job failed:');
    expect(logs).to.include('Notification job PERCENT% complete');
  });
});
