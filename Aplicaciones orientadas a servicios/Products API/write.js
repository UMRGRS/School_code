var fs = require('fs')

var arch = fs.readFileSync('test.json')

data = JSON.parse(arch)

var data3 = {
    "ID_producto_3":{
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

data["productos"].push(data3)

jsonData = JSON.stringify(data,null,4)

fs.writeFile('test.json', jsonData, 'utf8',function(err) {
    if (err) {
        console.log(err);
    }
});
