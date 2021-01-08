const fs = require('fs')

const DISK_PATH = './disk'

class SecondaryMemory {
  load (value) {
    const disk = fs.readdirSync(DISK_PATH) // retorna um array com o nome de todos os arquivos da rota 'DISK_PATH'.

    const nextFileName = `${DISK_PATH}/cel${disk.length}`

    fs.writeFileSync(nextFileName, value); // cria um novo arquivo na rota 'nextFileName' com 'value' como conteúdo.
  }

  get (index) {
    const fileName = `${DISK_PATH}/cel${index}`

    return parseFloat(fs.readFileSync(fileName)) || 0; // retorna o conteúdo do arquivo 'filename'
  }

  clean () {
    fs.rmdirSync(DISK_PATH, { recursive: true })
    fs.mkdirSync(DISK_PATH)
  }
}

module.exports = SecondaryMemory
