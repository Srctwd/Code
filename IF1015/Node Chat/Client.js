const net = require('net')
const readline = require('readline')
const client = new net.Socket()
var nome = ''

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


client.connect(4000, '127.0.0.1', () => {
    console.log('conectado') 
    rl.question('Nome: ', nome2 => {
        nome = nome2
    });
    rl.addListener('line', line => {
      client.write(nome+': '+line)  
    })
client.on('data', data => {
    console.log(data.toString())
    })    
})
