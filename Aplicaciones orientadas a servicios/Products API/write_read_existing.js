//Importar el modulo para manejo de archivos
var fs = require('fs')

//Leemos el archivo ya existente
var arch = fs.readFileSync('test.json')

//Lo convertimos a un objeto de javascript
data = JSON.parse(arch)

//Creamos el diccionario de prueba
//Esto se convertirá en json
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

//Accedemos a la lista en la key productos y agregamos ambos diccionarios
//El mismo proceso del primer archivo
data["productos"].push(data3)

//Para guardar los datos primero hay que convertir nuestro objeto en json
jsonData = JSON.stringify(data,null,4)

//Writefile crea un nuevo archivo si no existe o sobrescribe el mismo si ya existe
fs.writeFile('test.json', jsonData, 'utf8',function(err) {
    if (err) {
        console.log(err);
    }
});
