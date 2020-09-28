const express = require('express')

const spawn = require('child_process').spawn

const process = spawn('python', ['./hello.py'])

const app = express()
const port = 3000


app.get('/', (req, res) => {
    child = spawn('python', ['./hello.py'])
    child.stdout.pipe(res);
})

app.listen(port, () => {
    console.log(`Server is up and running at port ${port}`)
})