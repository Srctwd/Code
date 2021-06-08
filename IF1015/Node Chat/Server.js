const net = require('net')
const readline = require('readline')
const sockets = [];

const handleConnection = socket => {
    sockets.push(socket)
    console.log('alguem se conectou')
    socket.on('error', () => {
    console.log('desconectou')
    })

    socket.on('data', data => {
        const str = data.toString()
        if (str == 'end'){
            socket.end()
        }
        for (const skt of sockets) {
            skt.write(str)
        }
        console.log(str)
        })
}

const server = net.createServer(handleConnection)
server.listen(4000, '127.0.0.1')
