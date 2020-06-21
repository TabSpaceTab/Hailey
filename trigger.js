const express = require('express');
const app = express();
var fs = require('fs')
const exec = require("child_process").exec;
const port = 3000


const MyShellFile = exec('sh index.sh ' + `${process.argv[2]}`);

const Test = MyShellFile.stdout.on('data', (data) =>  {
    
    app.get('/', (req,res) => res.send(data))
    app.listen(port, () => console.log(`localhost:${port}/`))
})

