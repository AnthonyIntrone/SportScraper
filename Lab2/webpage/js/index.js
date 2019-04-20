// Authors: Anthony Introne
//          Mike Klein

var express = require('express'),
    app = express();
var port = 8080;
var path = require('path');

app.use(express.static(path.join(__dirname + "/../" + 'index.html')));

var bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.get('/',function(req,res){
    res.sendFile(path.join(__dirname + '/../index.html'));
  });

app.listen(port, () => {
    console.log("Server listening on port " + port);
});
console.log(__dirname);