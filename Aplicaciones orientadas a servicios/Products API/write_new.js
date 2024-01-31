//Importar el modulo para manejo de archivos
var fs = require('fs');

//Creamos un diccionario con la key "productos" y una lista como valor
var products = {"productos":[]}

//Creamos dos diccionarios de prueba
//Esto se convertirá en json
var data_1 = {
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

var data_2 = {
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

//Accedemos a la lista en la key productos y agregamos ambos diccionarios
products['productos'].push(data_1)

products['productos'].push(data_2)

//Para guardar los datos primero hay que convertir nuestro objeto en json
jsonData = JSON.stringify(products,null,4)

//Writefile crea un nuevo archivo si no existe o sobrescribe el mismo si ya existe
fs.writeFile('test.json', jsonData, 'utf8',function(err) {
    if (err) {
        console.log(err);
    }
});
