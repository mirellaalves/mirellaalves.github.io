/* Importando o pacote NET, responsável pela implementação dos sockets no Node. */
const net = require('net');

/* Criando o servidor com o método 'createServer', onde recebe uma conexao na qual são expostos os eventos que podemos manipular no nosso servidor. */
const server = net.createServer((connection) => {
  console.log('Cliente conectado');
  connections.push(connections); // Do ex.3, PARA QUE SERVE?

  //Ex.2: imprima quantas conexões estão de pé.
  server.getConnections((err, count) => {
    console.log(count);
  });

  /* Assim como um evento normal do Node.js, o método ".on()" escuta um evento em específico e, quando ele é ativado, nossa função de callback é chamada. */
  connection.on('end', () => {
    console.log('Cliente desconectado');
  });

  // Ex.3: Recebe mensagem do cliente
  connection.on('data', (data) => {
    console.log(`O cliente disse: ${data}`);
  });

  /* Nessa conexão que foi aberta, podemos fazer várias coisas. Uma delas é escrever/devolver uma mensagem para o cliente. */
  connection.write('Mensagem do servidor!\r\n');
  connection.pipe(connection); // Do conteúdo, PARA QUE SERVE?
});

/* Após termos programado o servidor, é só colocá-lo de pé */
server.listen(8080, () => {
  console.log('Servidor escutando na porta 8080');
});
