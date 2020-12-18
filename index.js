const express = require('express')
const app = express()
var cors = require('cors');

const MongoClient = require('mongodb').MongoClient;
 
// Connection URL
const url = 'mongodb+srv://Vaishaliarora:Garden@cluster0.mu77t.mongodb.net/<dbname>?retryWrites=true&w=majority';
 
// Database Name
const dbName = 'Gardening';
let db;

app.use(cors());
 
// Use connect method to connect to the server
MongoClient.connect(url, function(err, client) {
  console.log("Connected successfully to server");
 
  db = client.db(dbName);
//   findDocuments(db, function(records) {
//     console.log(JSON.stringify(records, null, 4));
//   });
});

const findDocuments = function(collectionName, callback) {
    // Get the documents collection
    const collection = db.collection(collectionName);
    // Find some documents
    collection.find({}).toArray(function(err, docs) {
      //console.log("Found the following records");   
      //console.log(docs)
      callback(docs);
    });
  }

app.get('/', function (req, res) {
    res.send("connected");
});
 

app.get('/:collection_name', function (req, res) {
    findDocuments(req.params.collection_name, function(records) {
        res.send(records);
    })
});

app.listen(3000)