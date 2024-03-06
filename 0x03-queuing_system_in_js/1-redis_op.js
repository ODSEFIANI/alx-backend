import { createClient as createRedisClient } from 'redis';

function connectToRedis() {
  const redisClient = createRedisClient();

  redisClient.on('connect', function () {
    console.log('Redis client connected to the server');
  }).on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  });

  return redisClient;
}

function setNewSchool(redisClient, schoolName, value) {
  redisClient.set(schoolName, value, redis.print);
}

function displaySchoolValue(redisClient, schoolName) {
  redisClient.get(schoolName, (err, value) => {
    if (err) {
      console.log(`Error retrieving value for ${schoolName}: ${err}`);
    } else {
      console.log(`Value for ${schoolName}: ${value}`);
    }
  });
}

const redisClient = connectToRedis();

// Example usage
displaySchoolValue(redisClient, 'Holberton');
setNewSchool(redisClient, 'HolbertonSanFrancisco', '100');
displaySchoolValue(redisClient, 'HolbertonSanFrancisco');
