import { createClient } from 'redis';

const subscriberClient = createClient();

subscriberClient.on('connect', () => {
  console.log('Redis client connected to the server');
  subscriberClient.subscribe('holberton school channel');
});

subscriberClient.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
});

subscriberClient.on('message', (channel, message) => {
  console.log(`Received message from channel ${channel}: ${message}`);
  if (message === 'KILL_SERVER') {
    subscriberClient.unsubscribe('holberton school channel');
    subscriberClient.quit();
  }
});
