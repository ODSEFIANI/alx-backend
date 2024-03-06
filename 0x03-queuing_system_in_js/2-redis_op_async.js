import { createClient as createRedisClient } from 'redis';
import { promisify } from 'util';

const redisClient = createRedisClient();

const connectToRedis = () => {
  return new Promise((resolve, reject) => {
    redisClient.on('connect', () => {
      console.log('Redis client connected to the server');
      resolve(redisClient);
    }).on('error', (err) => {
      console.log(`Redis client not connected to the server: ${err}`);
      reject(err);
    });
  });
};

const setNewSchoolAsync = promisify(redisClient.set).bind(redisClient);
const getSchoolValueAsync = promisify(redisClient.get).bind(redisClient);

const setNewSchool = async (schoolName, value) => {
  const reply = await setNewSchoolAsync(schoolName, value);
  console.log(`Reply: ${reply}`);
};

const displaySchoolValue = async (schoolName) => {
  const value = await getSchoolValueAsync(schoolName);
  console.log(`Value for ${schoolName}: ${value}`);
};

(async () => {
  try {
    await connectToRedis();
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
  } catch (error) {
    console.error(`Error: ${error}`);
  } finally {
    redisClient.quit();
  }
})();
