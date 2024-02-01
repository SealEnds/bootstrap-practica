<!--
    1. Personalizar:
        Color de fondo: selector de color
        Tipografía: al menos 5
        Tamaño letra: range slider
        Zona de muestra
    2. Página de muestra
        Hacer una página que podrá navegar entre esas dos páginas.
    3. Modos: normal, nocturno, alto contraste
        Mostrar modo seleccionado
    4. Validación: 
        Tipo de letra
        Color
        número entre 1 y 72
        Mensaje de error en la misma página
    5. Destruir sesión: restablecer estilos
    Method: GET

Voluntario: Los ajustes de los tres perfiles se guardarán en una variable de sesión que será un único vector y que permitirá que los ajustes se mantengan durante 2 minutos. Al caducar la sesión volvemos al estado inicial.
-->
<?php
session_start();
define("FUENTES", ["Arial", "nevis", "Trebuchet MS", "Courier New", "Verdana"]);
if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["modo"])) {
    $_SESSION["modo"] = $_GET["modo"];
}
if ($_SERVER["REQUEST_METHOD"] == "GET" && isset($_GET["estilosJSON"])) {
    $estilosJSON = $_GET["estilosJSON"];
    $_SESSION["estilos"] = json_decode($estilosJSON, true);

    $estilos = json_decode($estilosJSON, true);
}
if ($_SERVER["REQUEST_METHOD"] == "GET" && !empty($_GET["sessionDestroy"])) {
    session_destroy();
}

?>
<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sesiones</title>
    <style>
        .clearfix {
            clear: both;
            font-family: tre
        }

        #ajustes .float-left {
            float: left;
            border: 1px solid #ccc;
            margin: 10px;
            padding: 10px;
        }

        #cambiar .float-left {
            float: left;
            margin-right: 50px;
            border: none !important;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }

        #main {
            width: 80%;
            margin: auto;
        }

        #ajustes {
            float: left;
        }

        #preview-parent {
            float: right;
            width: 500px;
        }

        #preview {
            width: 500px;
            min-height: 300px;
            padding: 20px;
            height: fit-content;
            border: 3px solid black;
        }

        h2 {
            margin-top: 30px;
        }

        .btn-estilo {
            background-color: black;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 3px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .btn-estilo:hover {
            background-color: #1231b9;
        }

        label {
            display: block;
        }

        input[type="color"],
        input[type="range"],
        select {
            padding: 5px;
        }

        input[type="range"] {
            width: 80%;
        }

        input[type="color"] {
            width: 40px;
            height: 40px;
        }

        input[type="range"] {
            margin-top: 5px;
        }

        #cambiar {
            float: left;
        }

        #borrar {
            float: right;
        }

        @font-face {
            font-family: "nevis";
            src: url("fonts/nevis.eot");
            src: url("fonts/nevis.eot?#iesfix") format("embedded-opentype"),
                url("fonts/nevis.woff") format("woff"),
                url("fonts/nevis.ttf") format("truetype"),
                url("fonts/nevis.svg") format("svg");
            font-weight: normal;
            font-style: normal;
        }
    </style>
    <script>
        window.addEventListener('load', () => {


            const normal = document.getElementById('normal');
            const nocturno = document.getElementById('nocturno');
            const alto_contraste = document.getElementById('alto-contraste');
            const tipo_letra = document.getElementById("tipo-letra");
            const color = document.getElementById("color-fondo");
            const tam_letra = document.getElementById("tam-letra");
            const estilosJSON_input = document.getElementById('estilosJSON');
            const preview = document.getElementById('preview');
            const fuentes = ["Arial", "nevis", "Trebuchet MS", "Courier New", "Verdana"]
            const modo = document.getElementById('modo');

            console.log(estilosJSON_input.value);
            let estilos_value = JSON.parse(estilosJSON_input.value);
            let estilos = {
                "normal": {
                    "backgroundColor": estilos_value["normal"]["backgroundColor"],
                    "fontFamily": estilos_value["normal"]["fontFamily"],
                    "fontSize": estilos_value["normal"]["fontSize"],
                    "color": estilos_value["normal"]["color"]
                },
                "nocturno": {
                    "backgroundColor": estilos_value["nocturno"]["backgroundColor"],
                    "fontFamily": estilos_value["nocturno"]["fontFamily"],
                    "fontSize": estilos_value["nocturno"]["fontSize"],
                    "color": estilos_value["nocturno"]["color"]
                },
                "alto_contraste": {
                    "backgroundColor": estilos_value["alto_contraste"]["backgroundColor"],
                    "fontFamily": estilos_value["alto_contraste"]["fontFamily"],
                    "fontSize": estilos_value["alto_contraste"]["fontSize"],
                    "color": estilos_value["alto_contraste"]["color"]
                }
            };
            // console.log(JSON.parse(estilosJSON_input.value)["backgroundColor"]);
            console.log(estilosJSON_input.value);
            console.log(JSON.parse(estilosJSON_input.value));
            <?php if (!empty($_SESSION['modo']) && $_SESSION['modo'] == 'normal') : ?>
                // console.log("hola: "+JSON.parse(estilosJSON_input.value)["normal"]);
                estilos["normal"]["backgroundColor"] = JSON.parse(estilosJSON_input.value)["normal"]["backgroundColor"];
                estilos["normal"]["fontFamily"] = JSON.parse(estilosJSON_input.value)["normal"]["fontFamily"];
                estilos["normal"]["fontSize"] = JSON.parse(estilosJSON_input.value)["normal"]["fontSize"];
            <?php endif; ?>
            <?php if (!empty($_SESSION['modo']) && $_SESSION['modo'] == 'normal') : ?>
                estilos["nocturno"]["backgroundColor"] = JSON.parse(estilosJSON_input.value)["nocturno"]["backgroundColor"];
                estilos["nocturno"]["fontFamily"] = JSON.parse(estilosJSON_input.value)["nocturno"]["fontFamily"];
                estilos["nocturno"]["fontSize"] = JSON.parse(estilosJSON_input.value)["nocturno"]["fontSize"];
            <?php endif; ?>
            <?php if (!empty($_SESSION['modo']) && $_SESSION['modo'] == 'normal') : ?>
                estilos["alto_contraste"]["backgroundColor"] = JSON.parse(estilosJSON_input.value)["alto_contraste"]["backgroundColor"];
                estilos["alto_contraste"]["fontFamily"] = JSON.parse(estilosJSON_input.value)["alto_contraste"]["fontFamily"];
                estilos["alto_contraste"]["fontSize"] = JSON.parse(estilosJSON_input.value)["alto_contraste"]["fontSize"];
            <?php endif; ?>

            normal.onclick = function() {
                cambiarEstilo('normal', 'backgroundColor', estilos["normal"]["backgroundColor"]);
                cambiarEstilo('normal', 'color', '#444');
                cambiarEstilo('normal', 'fontFamily', estilos["normal"]["fontFamily"]);
                cambiarEstilo('normal', 'fontSize', estilos["normal"]["fontSize"]);
                normal.style.backgroundColor = "#ccc";
                nocturno.style.backgroundColor = "black";
                alto_contraste.style.backgroundColor = "black";
                modo.value = "normal";
            }
            nocturno.onclick = function() {
                cambiarEstilo('nocturno', 'backgroundColor', estilos["nocturno"]["backgroundColor"]);
                cambiarEstilo('nocturno', 'color', 'whitesmoke');
                cambiarEstilo('nocturno', 'fontFamily', estilos["nocturno"]["fontFamily"]);
                cambiarEstilo('nocturno', 'fontSize', estilos["nocturno"]["fontSize"]);
                nocturno.style.backgroundColor = "#ccc";
                normal.style.backgroundColor = "black";
                alto_contraste.style.backgroundColor = "black";
                modo.value = "nocturno";
            }
            alto_contraste.onclick = function() {
                cambiarEstilo('alto_contraste', 'backgroundColor', estilos["alto_contraste"]["backgroundColor"]);
                cambiarEstilo('alto_contraste', 'color', '#6700ff');
                cambiarEstilo('alto_contraste', 'fontFamily', estilos["alto_contraste"]["fontFamily"]);
                cambiarEstilo('alto_contraste', 'fontSize', estilos["alto_contraste"]["fontSize"]);
                alto_contraste.style.backgroundColor = "#ccc";
                nocturno.style.backgroundColor = "black";
                normal.style.backgroundColor = "black";
                modo.value = "alto_contraste";
            }
            tipo_letra.onchange = function() {
                let fuente_seleccionada = tipo_letra.options[tipo_letra.selectedIndex].value;
                if (fuentes.indexOf(fuente_seleccionada) > 0) {
                    if (modo.value == "normal") {
                        cambiarEstilo('normal', 'fontFamily', fuente_seleccionada);
                        estilos["normal"]["fontFamily"] == fuente_seleccionada;
                    } else if (modo.value == "nocturno") {
                        cambiarEstilo('nocturno', 'fontFamily', fuente_seleccionada);
                        estilos["nocturno"]["fontFamily"] == fuente_seleccionada;
                    } else if (modo.value == "alto_contraste") {
                        cambiarEstilo('alto_contraste', 'fontFamily', fuente_seleccionada);
                        estilos["alto_contraste"]["fontFamily"] == fuente_seleccionada;
                    }
                }
            }
            color.oninput = function() {
                let color_seleccionado = color.value;
                //https://stackoverflow.com/questions/48484767/javascript-check-if-string-is-valid-css-color
                if (modo.value == "normal") {
                    cambiarEstilo('normal', 'backgroundColor', color_seleccionado);
                    estilos["normal"]["color"] == color_seleccionado;
                } else if (modo.value == "nocturno") {
                    cambiarEstilo('nocturno', 'backgroundColor', color_seleccionado);
                    estilos["nocturno"]["color"] == color_seleccionado;
                } else if (modo.value == "alto_contraste") {
                    cambiarEstilo('alto_contraste', 'backgroundColor', color_seleccionado);
                    estilos["alto_contraste"]["color"] == color_seleccionado;
                }

            }
            tam_letra.oninput = function() {
                let tam_seleccionado = tam_letra.value;
                if (tam_seleccionado >= 1 && tam_seleccionado <= 72) {
                    if (modo.value == "normal") {
                        cambiarEstilo('normal', 'fontSize', tam_seleccionado + 'px');
                        estilos["normal"]["fontSize"] == tam_seleccionado;
                    } else if (modo.value == "nocturno") {
                        cambiarEstilo('nocturno', 'fontSize', tam_seleccionado + 'px');
                        estilos["nocturno"]["fontSize"] == tam_seleccionado;
                    } else if (modo.value == "alto_contraste") {
                        cambiarEstilo('alto_contraste', 'fontSize', tam_seleccionado + 'px');
                        estilos["alto_contraste"]["fontSize"] == tam_seleccionado;
                    }
                }
            }

            function cambiarEstilo(modo, propiedad, valor) {
                preview.style[propiedad] = valor;
                console.log(estilos);
                estilos[modo][propiedad] = valor;

                let estilosJSON_string = JSON.stringify(estilos);
                estilosJSON_input.value = estilosJSON_string;
            }

        });
    </script>
</head>
<?php if (!empty($estilos)) : ?>

    <?php if (isset($_SESSION["modo"]) && $_SESSION['modo'] == 'normal') : ?>

        <body style="background-color:<?= $estilos["normal"]["backgroundColor"] ?> !important; font-family:<?= $estilos["normal"]["backgroundColor"] ?> !important; font-size:'<?= $estilos["normal"]["fontSize"] ?>'; color: '<?= $estilos["normal"]["color"] ?>'">
        <?php elseif (isset($_SESSION["modo"]) && $_SESSION['modo'] == 'nocturno') : ?>

            <body style="background-color:<?= $estilos["nocturno"]["backgroundColor"] ?> !important; font-family:<?= $estilos["nocturno"]["fontFamily"] ?> !important; font-size:'<?= $estilos["nocturno"]["fontSize"] ?>'; color: <?= $estilos["nocturno"]["color"] ?>;">
            <?php elseif (isset($_SESSION["modo"]) && $_SESSION['modo'] == 'alto_contraste') : ?>

                <body style="background-color:<?= $estilos["alto_contraste"]["backgroundColor"] ?> !important; font-family:<?= $estilos["alto_contraste"]["backgroundColor"] ?> !important; font-size:<?= $estilos["alto_contraste"]["fontSize"] ?>; color: <?= $estilos["alto_contraste"]["color"] ?>">
                <?php endif; ?>
            <?php else : ?>

                <body>
                <?php endif; ?>
                <div id="main">
                    <div id="ajustes">
                        <h1>Sesiones</h1>
                        <?php if (!empty($error)) : ?>
                            <p><?= $error ?></p>
                        <?php endif; ?>
                        <div>
                            <h2>Modos</h2>
                            <div class="float-left">
                                <button class="btn-estilo" id="normal">Normal</button>
                            </div>
                            <div class="float-left">
                                <button class="btn-estilo" id="nocturno">Nocturno</button>
                            </div>
                            <div class="float-left">
                                <button class="btn-estilo" id="alto-contraste">Alto Contraste</button>
                            </div>
                            <div class="clearfix"></div>
                            <h2>Personalizar</h2>
                            <div class="float-left">
                                <label for="color-fondo">Color de fondo</label>
                                <input type="color" name="color-fondo" id="color-fondo" />
                            </div>
                            <div class="float-left">
                                <label for="tipo-letra">Tipografía</label>
                                <select name="tipo-letra" id="tipo-letra">
                                    <option value="Arial">Arial</option>
                                    <option value="nevis">Nevis</option>
                                    <option value="Trebuchet MS">Trebuchet MS</option>
                                    <option value="Courier New">Courier New</option>
                                    <option value="Verdana">Verdana</option>
                                </select>
                            </div>
                            <div class="float-left">
                                <label for="tam-letra">Tamaño letra</label>
                                <input type="range" name="tam-letra" id="tam-letra" min="1" max="72" />
                            </div>
                        </div>
                    </div>
                    <div id="preview-parent">
                        <h2>Preview</h2>
                        <div id="preview">
                            <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Et maxime molestias iusto incidunt culpa deserunt accusamus cumque nesciunt sunt aspernatur quaerat explicabo, sequi totam earum, tempora officiis optio asperiores eligendi.</p>
                        </div>
                    </div>
                    <div class="clearfix"></div>
                    <div id="cambiar">
                        <h2>Cambiar Estilos</h2>
                        <form action="index.php" method="get" class="float-left">
                            <?php if (isset($_SESSION['modo']) && isset($_SESSION['estilos'])) : ?>
                                <input type="hidden" name="estilosJSON" id="estilosJSON" value="<?= htmlspecialchars(json_encode($_SESSION['estilos'])) ?>" />
                            <?php else : ?>
                                <input type="hidden" name="estilosJSON" id="estilosJSON" value='{"normal": {"backgroundColor": "#fafafa", "fontFamily": "Arial", "fontSize": "16px", "color": "#444"}, "nocturno": {"backgroundColor": "#444", "fontFamily": "Arial", "fontSize": "16px", "color": "#fafafa"}, "alto_contraste": {"backgroundColor": "#FFDA94", "fontFamily": "Arial", "fontSize": "16px", "color": "#6700ff"}}' />
                            <?php endif; ?>
                            <input type="hidden" name="modo" id="modo" value="normal" />
                            <button type="submit" class="btn-estilo">Guardar Estilos</button>
                        </form>
                        <form action="muestra.php" method="get" class="float-left">
                            <button type="submit" class="btn-estilo">Ver página de muestra</button>
                        </form>
                    </div>
                    <div id="borrar">
                        <h2>Cerrar Sesión</h2>
                        <form action="index.php" method="get">
                            <input type="hidden" name="sessionDestroy" id="sessionDestroy" value="false" />
                            <button type="submit" class="btn-estilo">Cerrar Sesión</button>
                        </form>
                    </div>
                    <div class="clearfix"></div>
                </div>
                </body>

</html>