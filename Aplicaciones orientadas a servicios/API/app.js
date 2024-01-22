const express = require('express')
const app = express()
const port = 3000


let array=[1,2,3,4]


app.get('/:id',function(req,res){
    const id = req.params.id
    if(id>array.length-1){
        res.json({"Elemento":"No existe el elemento"})
    }
    else{
        res.json({"Elemento":array[id]})
    }
})


app.get('/', (req, res) => res.json("ejemplo"))
app.listen(port, () => console.log(`Example app listening on port ${port}!`))


