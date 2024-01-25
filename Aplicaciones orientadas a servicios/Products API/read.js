var fs = require('fs');

var dicSup = {"productos":[]}

var data1 = {
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

var data2 = {
    "ID_producto_2":{
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

dicSup['productos'].push(data1)

dicSup['productos'].push(data2)


jsonData = JSON.stringify(dicSup,null,4)

dictData = JSON.parse(jsonData)

fs.writeFile('test.json', jsonData, 'utf8',function(err) {
    if (err) {
        console.log(err);
    }
});
