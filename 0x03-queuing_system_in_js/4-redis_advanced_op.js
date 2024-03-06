import { createClient, print as redisPrint } from 'redis';

const myRedisClient = createClient();

myRedisClient.on('connect', function() {
  console.log('MyRedis client connected to the server');
});

myRedisClient.on('error', function(error) {
  console.log(`MyRedis client not connected to the server: ${error}`);
});

// set hash key-value in HolbertonSchools list
myRedisClient.hset('HolbertonSchools', 'Portland', '50', redisPrint);
myRedisClient.hset('HolbertonSchools', 'Seattle', '80', redisPrint);
myRedisClient.hset('HolbertonSchools', 'New York', '20', redisPrint);
myRedisClient.hset('HolbertonSchools', 'Bogota', '20', redisPrint);
myRedisClient.hset('HolbertonSchools', 'Cali', '40', redisPrint);
myRedisClient.hset('HolbertonSchools', 'Paris', '2', redisPrint);

// retrieve all elements stored in HolbertonSchools list
myRedisClient.hgetall('HolbertonSchools', function (error, result) {
  if (error) {
    console.log(error);
    throw error;
  }
  console.log(result);
});
