data = {
    "ID_producto":{
        "SKU":"Código de 6 cifras",
        "modelo":"Modelo del producto",
        "departamento":"Por ejemplo, hogar, ropa, comestibles, etc",
        "descripcion":"Descripción del producto",
        "valor":{
            "pesos":"Valor con punto decimal",
            "dolares":"Valor con punto decimal"
        },
        "reviews":{
            "ID_review":{
                "fecha":"Fecha y hora",
                "calificacion":"Entero con rango 1-5",
                "texto":"Texto de la review"
            }
        }
    }
}

console.log(data.ID_producto.reviews.ID_review.fecha)

jsonData = JSON.stringify(data,null,4)

dictData = JSON.parse(jsonData)

console.log(dictData.ID_producto.reviews.ID_review)

var fs = require('fs');
fs.writeFile('test.json', jsonData, 'utf8',function(err) {
    if (err) {
        console.log(err);
    }
});
/*var fs = require('fs');
fs.writeFile("test.json", jsonData, function(err) {
    if (err) {
        console.log(err);
    }
});*/