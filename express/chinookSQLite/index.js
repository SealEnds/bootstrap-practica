/*
18/11/2023

Con la base de datos de chinook.db de SQL que hemos utilizado en clase y que se encuentra en la plataforma, realizar una página cuyo Frontend en Express que se sirva en el puerto 65235 tal que cargue inicialmente todos los artistas que existen en la base de datos en un cuadro desplegable (select) de forma que, al seleccionar uno de ellos, muestre en una lista no ordenada de todos los álbums que están asociados a este artista. En caso de seleccionar otro artista de nuevo, deberá limpiar la lista y colocar de nuevo los álbums del nuevo artista seleccionado. 

*/
const path = require('path');
const express = require("express");
const app = express();
const file = path.join(process.cwd(), "chinook.db");
const sqlite3 = require('sqlite3').verbose();

app.use(express.static('public'));

app.set('host', 'localhost');
app.set('port', '65235');
app.set('NombreApp', 'Chinook.DB');
app.set('view engine', 'ejs');

app.listen(app.get('port'), () => {
    console.log(app.get("NombreApp"));
    console.log(`Servidor funcionando en el puerto ${app.get('port')}`);
});

app.get('/index', (req, res) => {
    const db = new sqlite3.Database(file);
    db.all('SELECT Name, ArtistId FROM artists', function (err, row) {
        if (err) {
            console.error(err.message);
        } else {
            res.render(
                path.join(__dirname, 'public/views/index.ejs'),
                {
                    "artists": row
                }
            );
        }
    });
    db.close();
});
app.get('/album/:id', (req, res) => {
    const db = new sqlite3.Database(file);
    let artists = "empty";
    let artist = "empty";
    let albums = "empty";
    let id = req.params.id;
    db.all('SELECT Name, ArtistId FROM artists', function (err, row) {
        if (err) {
            console.error(err.message);
        } else {
            artists = row;
        }
        db.all(`SELECT albums.Title, artists.Name FROM albums INNER JOIN artists ON albums.ArtistId = artists.ArtistId WHERE albums.ArtistId = ${id} `, function (err, row) {
            if (err) {
                console.error(err.message);
            } else if (row.length <= 0) {
                db.all(`SELECT Name FROM artists WHERE ArtistId = ${id}`, function (err, newrow) {
                    if (err) {
                        console.error(err.message);
                    } else if (newrow.length <= 0) {
                        renderView(artists, artist, albums);
                    } else {
                        artist = newrow;
                        renderView(artists, artist, albums);
                    }
                });
            } else {
                albums = row;
                renderView(artists, artist, albums);
            }
        });
    });
    function renderView(artists, artist, albums) {
        res.render(path.join(__dirname, 'public/views/index.ejs'),
        {
            "artists": artists,
            "artist": artist,
            "albums": albums
        });
    }
    db.close();
})