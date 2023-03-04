const express = require("express")
const { MongoClient } = require("mongodb")
const app = express()
const port = 3000

app.listen(port, () => {
    console.log(`Server starting on port ${port}`)
    })

app.get("/hello-world", (req, res) => {
    res.send("Hello World!")
  })

app.get("/NolanFincher",(req,res) => {
    async function getOne (){
        var client = new MongoClient("mongodb://localhost:27017/")
        var db = client.db('svelte-mongo');
        var movies = db.collection('movies');
        var cursor = await movies.find({"director":{"$in": [65,143]}}).toArray()
        res.send(cursor)
    }
    getOne()
})
//use mongoJS wrapper to simplify and have more redabable mongo querries (like in compass)