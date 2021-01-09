const os = require('os');

//1
console.log(`plataforma: ${os.platform()}`);
console.log(`arquitetura: ${os.arch()}`);
console.log(`versão: ${os.release()}`);

//2
const cpus = os.cpus()
console.log(`CPU ${cpus.length} cores:`);

cpus.forEach((core, index) => {
  console.log(`Core ${index + 1} - Modelo: ${core.model} | Velocidade ${core.speed / 1000}GHz`)
});

//3
console.log(`Memória RAM total: ${os.totalmem() / 1024 / 1024 / 1024}GB`);
