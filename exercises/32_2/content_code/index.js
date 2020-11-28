const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', (socket) => { //.on = "escuta do evento"
  console.log('Usuário conectado');
  socket.broadcast.emit('mensagemServer'); //emite mensagem para todos os clientes, exceto para o que enviou a mensagem (o cliente que está conectado neste momento(?))

  //Ex.2: GABARITO NÃO DEFINE 'users', O CÓDIGO ABAIXO APENAS NÃO RODA
  // const nickname = 'Usuario - ' + users.length;
  // socket.nickname = nickname;
  // users.push(socket.nickname);

  socket.on('mensagem', (msg) => { //cria o evento 'mensagem', que corresponde ao mesmo evento 'mensagem' do frontend(?)
    io.emit('mensagemServer', msg); //Ex.1: inclui 'broadcast' = envia mensagem recebida do cliente para todos os clientes, exceto para quem a enviou => DEU ERRO!
    console.log(`Mensagem ${msg}`);
  });

  socket.on('disconnect', () => {
    io.emit('adeus', { mensagem: 'Poxa, fica mais, vai ter bolo :)' }); //emite mensagem do server para o cliente
    console.log('Usuário desconectado');
  });
});

//io.on: recebe/ouve evento do cliente(?)
//io.emit: envia evento para o cliente conectado(?)
//socket.on: recebe/ouve evento de todos os clientes(?)
//socket.emit: envia evento para todos os clientes(?)

http.listen(3000, () => {
  console.log('Servidor ouvindo na porta 3000');
});
