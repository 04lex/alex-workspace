let express = require('express');
let app = express();

console.log("Hello World")

// app.get('/', function(req, res) {
//     res.sendFile(__dirname + '/views/index.html');
// });

absolutePath = __dirname + '/views/index.html'
app.get('/', res.sendFile(absolutePath));

// app.use('/public', express.static(__dirname + '/public'));







module.exports = app;