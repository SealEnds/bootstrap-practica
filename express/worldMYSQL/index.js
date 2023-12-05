/*
    01/12/2023

Con el volcado de la base de datos MySQL comprimido en ZIP que se acompaña a esta actividad, se os pide realizar una aplicación de Express enlazada a una base de datos de MySQL (que deberás volcar en tu XAMPP o en el sistema que emplees para trabajar con MySQL), que funcione en el puerto 31973; en el FrontEnd, debe mostrar en un cuadro desplegable (select) todos los países (country) que contiene la Base de datos y que, seleccionando uno de ellos, muestre sus ciudades en una tabla HTML

En el Backend del servidor, se deberá notificar cuantas veces se ha seleccionado el el país, así como el tiempo que lleva el servidor encendido, expresado en días, horas, minutos y/o segundos según corresponda (esto quiere decir que si no lleva un día, no tendrá que mostrarlo, al igual que las horas que no lleve).
===========================================================================================================================
- puerto 31973
FrontEnd:
    - select con todos los países
    - mostrar ciudades del país seleccionado en tabla
Backend:
    - veces que se selecciona el país
    - tiempo del servidor encendido
*/

const path = require('path');
const express = require("express");
const app = express();
const file = path.join(process.cwd(), "world-db/world.sql"); // ruta de world
// const sqlite3 = require('sqlite3').verbose();
// https://www.npmjs.com/package/mysql2
const mysql2 = require('mysql2');
// create the connection to database
const connection = mysql2.createConnection({
    host: "localhost",
    user: "admin",
    password: "6721",
    database: "world",
    multipleStatements: true  
});

// contar nº de interacciones con cada país
let interactions = [];

app.use(express.static('public')); // carpeta estática

app.set('host', 'localhost');
app.set('port', '31973');
app.set('NombreApp', 'World.DB');
app.set('view engine', 'ejs');

app.all('/', (req, res) => {

});

app.listen(app.get('port'), () => {
    console.log(app.get("NombreApp"));
    console.log(`Servidor funcionando en el puerto ${app.get('port')}`);
    // countTime();
});

function countTime(){
    let interval_time = 1000;
    let s = 0;
    let min = 0;
    let h = 0;
    let days = 0;
    let show_min = false;
    let show_h = false;
    let show_days = false;
    let interval = setInterval(() => {
        s += 1;
        if(s > 59){
            min += 1;
            s = 0;
            show_min = true;
        }
        if(min > 59){
            h += 1;
            min = 0;
            show_h = true;
        }
        if(h > 23){
            days += 1;
            h = 0;
            show_days = true;
        }
        running_time = `${s} seconds`;
        if(show_min == true){
            running_time = `${min} minutes - ` + running_time; 
        } 
        if(show_h == true){
            running_time = `${h} hours - ` + running_time; 
        }
        if(show_days == true){
            running_time = `${days} days - ` + running_time; 
        }
        
        if(s%10 === 0) {
            console.clear();
            console.log(running_time);
        }
    }, interval_time);
}
app.get('/index', (req, res) => {
    let sql_query = 'SELECT * FROM country';
    connection.query(
        sql_query,
        function(err, rows, metadada) {
          if(err) {
            console.log(err);
          } else {
            res.render(path.join(__dirname, 'public/views/index.ejs'), 
              {
                "countries": rows
              }
            );
          }
        }
    );
});
// tiene que ser función asíncrona para utilizar las promesas para poder usar los datos de connection.query fuera de esa función
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function
app.get('/pais/:id', async (req, res) => {
    let code = req.params.id;
    // añadir index al json para poder tomar la posición luego para el Promise.all(array)
    let result = {
        "countries": {
            "index": 0,
            "value": null
        },
        "cities": {
            "index": 0,
            "value": null
        }
    }
    let query = {
        'countries': 'SELECT * FROM country',
        "cities": `SELECT city.Name, country.name as country FROM city INNER JOIN country ON city.CountryCode = country.Code WHERE city.CountryCode = '${code}'`
    }
    https://stackoverflow.com/questions/23266854/node-mysql-multiple-statements-in-one-query
    // fuera se ejectua antes de que se realize la consulta, por eso no funcionaba. Hay que hacer una promesa.
    // https://www.w3schools.com/Js/js_promise.asp
    // https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects/Promise/all
    var queries = [null, null];
    // para cada campo, realizar una query a la base de datos
    try{
        for(let field in result){
                // guardar en queries con índice 0, 1
                queries[field["index"]] = await new Promise((resolve, reject) => {
                // connection.query para conectarse a mysql. Parámetros, consulta sql y función con rows como respuesta 
                connection.query(query[field], function(err, rows, metadada) {
                    if(err) {
                        console.log(err);
                    } else {
                        // guardar la respuesta en el array
                        result[field]["value"] = rows;
                        resolve();
                    }
                });
            });
        }
        // cuando se completen todas las promesas, renderiza la vista index.ejs mandando como valores "cities" y "countries"
        const completedQueries = Promise.all(queries);
        completedQueries.then( () => {
            console.log(result["cities"]["value"].length);
            res.render(path.join(__dirname, 'public/views/index.ejs'), 
                {
                    "cities": result["cities"]["value"],
                    "countries": result["countries"]["value"]
                }
            )
        }).catch(error => {
            console.error(error);
        });
    } catch (error) {
        console.error('Error: ', error);
    }
 
});