const express = require('express')

const spawn = require('child_process').spawn

const process = spawn('python', ['./hello.py'])

const app = express()
const port = 3000


app.get('/', (req, res) => {
    child = spawn('python', ['./printer.py'])
    child.stdout.pipe(res);
})

app.get('/file', (req, res) => {
    var filename = 'out'
    res.sendFile(__dirname + '/out.txt')
})

app.listen(port, () => {
    console.log(`Server is up and running at port ${port}`)
})