<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Información Sobre Un Texto</title>
    <link rel="stylesheet" type="text/css" href="style.css">
    <script>
        window.onload = () => {
            let titulo_input = document.getElementById("titulo");
            let year_input = document.getElementById("year");
            let genero_input = document.getElementById("genre");
            let url_input = document.getElementById("url");

            let valores_enviar = document.getElementById("valores-enviar");
            let add = document.getElementById("add");
            // let delete_input = document.getElementById("delete-input");
            // let del = document.getElementsByTagName("button")[1];
            let resultado = document.getElementById("resultado");
            let enviar = document.getElementById("submit");
            let buscar = document.getElementById("buscar");
            let valor_buscar = document.getElementById("buscar-valor");
            let buscar_btn = document.getElementById("buscar-btn");
            let valores_busqueda = document.getElementById("valores-busqueda");
            let enviar_busqueda = document.getElementById("enviar-busqueda");
            let inicio = document.getElementById("inicio");

            let names = JSON.parse(valores_enviar.value);
            enviar.style.visibility = "hidden";
            console.log(names);
            names = JSON.parse(valores_enviar.value);
            add.onclick = () => {
                let titulo = titulo_input.value;
                let year = year_input.value;
                let genero = genero_input.value;
                let url = url_input.value;
                if (titulo.length > 2 && year.length > 0 && !isNaN(parseInt(year)) === true && year > 1888 && year < 2115 && genero.length > 0 && url.length > 0) {
                    let json = {
                        "title": titulo,
                        "year": year,
                        "genre": genero,
                        "url": url
                    };
                    names[names.length] = JSON.stringify(json);

                    enviar.style.visibility = "visible";
                    enviar.onclick = () => {
                        names_str = JSON.stringify(names);
                        valores_enviar.value = names_str;
                    }
                    valores_busqueda.value = '[]'; // volver a mostrar todos al añadir uno
                }
            }

            let buttons = document.getElementsByClassName("borrar");
            for (let button of buttons) {
                button.onclick = () => {
                    let btn_id = button.id;
                    names.splice(btn_id, 1);
                    valores_enviar.value = JSON.stringify(names);
                    valores_busqueda.value = '[]'; // volver a mostrar todos al quitar uno
                    enviar.click();
                }
            }

            buscar_btn.addEventListener('click', () => {
                let coincidencias = [];
                names.forEach(mov => {
                    let mov_json = JSON.parse(mov);
                    let busqueda = valor_buscar.value;
                    if (busqueda.length > 0) {
                        if (mov_json['title'].toLowerCase().indexOf(valor_buscar.value.toLowerCase()) >= 0) {
                            coincidencias.push(mov);
                        }
                    }
                });
                if (coincidencias.length > 0) {
                    valores_busqueda.value = JSON.stringify(coincidencias);
                    enviar.click();
                }
            });

            inicio.addEventListener('click', () => {
                valores_busqueda.value = '[]';
                enviar.click();
            });
        }
    </script>

    <?php
    // sesiones ___________________________________________________________________
    session_start();
    define("FUENTES", ["Arial", "Times New Roman", "Courier New", "Georgia", "Verdana"]);
    if (isset($_SESSION['estilos'])) {
        $estilos = $_SESSION['estilos'];
    }
    if (isset($_SESSION["modo"])) {
        $modo = $_SESSION["modo"];
    }
    if ($_SERVER["REQUEST_METHOD"] == "GET" && !empty($_GET["sessionDestroy"])) {
        session_destroy();
    }
    // ____________________________________________________________________________
    ?>
    <style>
        <?php if($modo == "nocturno"): ?>
        .color {
            color: #deecab;
        }
        <?php elseif($modo == "alto_contraste"): ?>
        .color {
            color: #FFDA94;
        }
        <?php else: ?>
        .color {
            color: #be8c2c;
        }
        <?php endif;?>
    </style>
</head>

<?php if (!empty($estilos) && !empty($modo)) : ?>
    <body style="background-color:<?= $estilos[$modo]["backgroundColor"] ?>; font-family:<?= $estilos[$modo]["backgroundColor"] ?>; font-size:<?= $estilos[$modo]["fontSize"] ?>; color: <?= $estilos[$modo]["color"] ?>">
    <?php else : ?>

        <body>
        <?php endif; ?>

        <?php

        if (isset($_POST["valores-enviar"]) && !empty($_POST["valores-busqueda"])) {
            $valores = $_POST["valores-enviar"];
            $names_json = json_decode($_POST["valores-enviar"], true);
            // var_dump($names_json, $_POST["valores-enviar"]);

            if (isset($_POST["valores-busqueda"])) {
                $valores_busqueda = $_POST["valores-busqueda"];
                $busqueda_json = json_decode($_POST["valores-busqueda"], true);
                // var_dump($busqueda_json, $_POST["valores-busqueda"]);
            } else {
                $valores_busqueda = '[]';
            }
        } else {
            $valores = '["{\"title\":\"El Chico y la Garza\",\"year\":\"2023\",\"genre\":\"Animación\",\"url\":\"https://somoskudasai.com/wp-content/uploads/2022/12/kimitachihadouikiruka_202212.jpg\"}","{\"title\":\"La Princesa Mononoke\",\"year\":\"1997\",\"genre\":\"Animación\",\"url\":\"https://image.tmdb.org/t/p/original/gzlJkVfWV5VEG5xK25cvFGJgkDz.jpg\"}","{\"title\":\"Susurros del Corazón\",\"year\":\"1995\",\"genre\":\"Animación\",\"url\":\"https://cdn.hobbyconsolas.com/sites/navi.axelspringer.es/public/styles/gallery_big/public/media/image/2017/02/susurros-corazon_0.jpg?itok=LlMbkfYq\"}","{\"title\":\"La Colina de las Amapolas\",\"year\":\"2011\",\"genre\":\"Animación\",\"url\":\"https://comiqueros.cl/wp-content/uploads/2020/10/La-Colina-de-las-Amapolas-2-1024x1536.jpg\"}"]';
            $names_json = json_decode($valores, true);
            $valores_busqueda = '[]';
        }

        ?>
        <h1>
            <button id="inicio">Pelist</button>
        </h1>
        <div id="main">
            <div id="gestion">
                <h2 class="title2">Añadir a Mi Lista</h2>
                <p>
                    <label for="titulo">Título</label>
                    <input type="text" name="titulo" id="titulo">
                </p>
                <p>
                    <label for="year">Año</label>
                    <input type="number" name="year" id="year">
                </p>
                <p>
                    <label for="genre">Género</label>
                    <input type="text" name="genre" id="genre">
                </p>
                <p>
                    <label for="url">url</label>
                    <input type="text" name="url" id="url">
                </p>
                <button class="btn" id="add">Añadir</button>
                <form action="" method="post">
                    <input type="text" name="valores-enviar" id="valores-enviar" style="visibility:hidden" value="<?= htmlspecialchars($valores) ?>">
                    <input type="text" name="valores-busqueda" id="valores-busqueda" style="visibility:hidden" value="<?= htmlspecialchars($valores_busqueda) ?>">
                    <input type="submit" value="Enviar" class="btn" id="submit">
                </form>
                <h2 class="title2">Buscar en Mi Lista</h2>
                <div id="buscar">
                    <input type="text" name="buscar" id="buscar-valor">
                    <button id="buscar-btn" class="btn">Buscar</button>
                </div>
            </div>
            <div id="resultado">
                <h2 class="title2">Mis Películas</h2>
                <?php if (isset($busqueda_json) && !empty($busqueda_json)) : ?>
                    <?php foreach ($busqueda_json as $index_mov => $mov) : ?>
                        <div class="pelicula">
                            <?php foreach (json_decode($mov) as $index => $value) : ?>
                                <?php if ($index === 'title') : ?>
                                    <h2 class="color"><?= $value ?></h2>
                                <?php elseif ($index === 'year') : ?>
                                    <p>Fecha de Estreno: <span class="color"><?= $value ?></span></p>
                                <?php elseif ($index === 'genre') : ?>
                                    <p>Género: <span class="color"><?= $value ?></span></p>
                                <?php elseif ($index === 'url') : ?>
                                    <img src="<?= $value ?>" class="img" />
                                <?php endif; ?>
                            <?php endforeach; ?>
                            <input type="button" value="Borrar" class="borrar btn" id="<?= $index_mov ?>" />
                        </div>

                    <?php endforeach; ?>
                <?php else : ?>
                    <?php if (isset($names_json) && !empty($names_json)) : ?>
                        <?php foreach ($names_json as $index_mov => $name) : ?>
                            <div class="pelicula">
                                <?php foreach (json_decode($name) as $index => $value) : ?>
                                    <?php if ($index === 'title') : ?>
                                        <h2 class="color"><?= $value ?></h2>
                                    <?php elseif ($index === 'year') : ?>
                                        <p>Fecha de Estreno: <span class="color"><?= $value ?></span></p>
                                    <?php elseif ($index === 'genre') : ?>
                                        <p>Género: <span class="color"><?= $value ?></span></p>
                                    <?php elseif ($index === 'url') : ?>
                                        <div class="img-div">
                                            <img src="<?= $value ?>" class="img" />
                                        </div>
                                    <?php endif; ?>
                                <?php endforeach; ?>
                                <input type="button" value="Borrar" class="borrar btn" id="<?= $index_mov ?>" />
                            </div>
                        <?php endforeach; ?>
                    <?php endif; ?>
                <?php endif; ?>
            </div>
            <div class="clearfix"></div>
        </div>
        </body>

</html>