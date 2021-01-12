const os = require('os');

setInterval(() => {
  const totalMemory = os.totalmem();
  const freeMemory = os.freemem();

  const usedMemory = (totalMemory - freeMemory) / 1024 / 1024;

  console.log(usedMemory);
}, 1000);
