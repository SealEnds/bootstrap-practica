
# 06/11/2023
#Crea un programa llamado SlicingBox, visualizando con la carátula la fecha y hora de cuando lo empiezas, con tu nombre y apellidos, y dejando un hueco de 2 filas vacías, visualizando un recuadro con la misma forma gráfica que la caratula, dónde deberás visualizar todos los items de este ejercicio.

#NOTA: En este ejercicio no se pueden emplear Expresiones Regulares.

#Teniendo en cuenta que TODAS las variables y constantes de este ejercicio deberán llevar la nomenclatura de las iniciales de tu nombre y apellidos en mayúsculas seguido de guion bajo y la nomenclatura que deseas utilizar, descarga el siguiente archivo, si no lo descargaste en clase en el momento de su explicación:

#http://www.py4inf.com/code/mbox.txt

#Recorre todo el archivo y visualiza por pantalla, debidamente enmarcado tanto por arriba, como en los laterales y al finalizar la visualización de datos, lo siguiente:

#1) cuenta el número de líneas que empiezan por "Received:" (sin las comillas) y empleando la técnica de Slicing, graba en un archivo de texto llamado Received.txt el contenido de cada una de esas líneas sin la palabra "Received: ", visualizando por pantalla, en la columna 4 y línea 10, el texto: "Número de líneas con Received: " (sin las comillas) dicho número de líneas. En la última línea del archivo se debe almacenar el número de líneas que se ha visualizado por pantalla.

#2) cuenta el número de líneas que comienzan por "Return-Path" (sin las comillas), y empleando la técnica de Slicing, graba en un archivo de texto llamado Return-Path.txt el contenido de cada una de esas líneas sin la palabra "Return-Path: ", visualizando por pantalla, en la columna 4 y línea 12, el texto: "Número de líneas con Return-Path: " (sin las comillas) dicho número de líneas. En la última línea del archivo se debe almacenar el número de líneas que se ha visualizado por pantalla.

#3) cuenta el número de líneas que comienzan por "Details" (sin las comillas), y empleando la técnica de Slicing, graba en un archivo de texto llamado Details.txt el contenido de cada una de esas líneas sin la palabra "Details: ", visualizando por pantalla, en la columna 4 y línea 14, el texto: "Número de líneas con Details: " (sin las comillas) dicho número de líneas. En la última línea del archivo se debe almacenar el número de líneas que se ha visualizado por pantalla.

#4) cuenta el número de líneas que comienzan por "This automatic" (sin las comillas), y empleando la técnica de Slicing, graba en un archivo de texto llamado ThisAutomatic.txt el contenido de cada una de esas líneas sin la palabra "This automatic: ", visualizando por pantalla, en la columna 4 y línea 16, el texto: "Número de líneas con This automatic: " (sin las comillas) dicho número de líneas. En la última línea del archivo se debe almacenar el número de líneas que se ha visualizado por pantalla.

#Al finalizar la visualización por pantalla, se debe crear una línea que enmarque los resultados, y se deberá esperar, mediante el texto de "Pulsa una tecla para finalizar", su finalización.


# ____________________________________________________________________________________________________________________
import os
from caratula import *
# pip install colorama
# from colorama import Fore, Style
#1. clear pantalla
os.system('cls')

# ____________________________________________________________________________________________________________________
# Carátula: 
# para que funcione tiene que abrirse en la misma carpeta en la que se encuentra el archivo
# usar flag para que solo se ejecute una vez la función

# programa para mostar caratula
def programa(caratula):  
    for _ in caratula:
        print(_)
   
# nombre del archivo python ejecutandose sin extensión
NombreArchivo = os.path.basename(__file__).split('.')[0]
# comprabar si existe un archivo con el nombre del archivo py pero extensión .txt
if os.path.exists("{}.txt".format(NombreArchivo)):
    archivo = open("{}.txt".format(NombreArchivo), 'r') # leer el contenido
    data = archivo.readline()
    data = data.split("||") # separarlo en un array 
else:
    data = introducirDatos() # introducir datos pero solo si es la primera vez que se escribe
    
    RutaActual = os.getcwd() + '\\' # ruta actual
    archivo = open("{0}{1}.txt".format(RutaActual, NombreArchivo), "w", encoding="utf-8") # crear archivo
    archivo.write(data[0]+"||") # escribir en una línea los datos
    archivo.write(data[1]+"||")
    archivo.write(data[2]+"||")
    archivo.write(data[3])

archivo.close()
caratula = generarCaratula(data[0], data[1], data[2], data[3]) # generar caratula con los datos introducidos al crear el archivo la primera vez
programa(caratula) # mostar caratula

#___________________________________________________________________________________________________________________________

# tamaño cmd
size = os.get_terminal_size().columns # tomar tamaño de pantalla cmd
# ruta actual
RutaActual = os.getcwd() + '\\'
print(RutaActual+'received.txt')

# funcion para crear realizar busqueda de lineas
def buscarLineasYCrearArchivo(nombreArchivo, busqueda, mensaje):
    try:
        archivoConLineas = open("{0}{1}.txt".format(RutaActual, nombreArchivo), "w", encoding="utf-8")
                        
        # escribir las líneas que empiezan por "busqueda" quitando esa búsqueda
        search = busqueda # palabra que se busca
        contador_lineas = 0
        for linea in archivo:
            if linea.startswith(search): # si empieza por esa palabra
                contador_lineas = contador_lineas + 1 # cuenta la línea
                archivoConLineas.write(linea[len(search):]) # escribe el resto de la línea
        # los números hay que pasarlos a string para escribirlos.
        contador_lineas = str(contador_lineas)
        archivoConLineas.write(contador_lineas) # mostrar lineas en última fila
        espacios = ' ' * (size - len(mensaje) - len(contador_lineas) - 4)
        # añadir mensaje y borde
        print("\u2551  {0}{2}{1}\u2551".format(mensaje, espacios, contador_lineas))
        #cerrar porque si no daba error al hacer otra búsqueda
        archivoConLineas.close()
    except:
        print("Error al crear el archivo o escribir en el archivo")

# abrir archivo mbox como lectura
if os.path.exists("mbox.txt"):


    for __ in range(1,19):
        if __ == 1:
            # margen superior
            margenTop = '\u2550' * (size - 2)
            print(f"\u2554{margenTop}\u2557")
        elif __ == 10:
            try:
                archivo = open("mbox.txt", 'r')

                # # hay que dejar una línea de separación después de las líneas que se les aplica el try
                # # nº lineas que comienzan por "Received:"
                buscarLineasYCrearArchivo("Received", "Received: ", "Número de líneas con Received: ")
                archivo.close()
            except:
                print("Error al abrir el archivo")
        elif __ == 12:
            # volver a abrir el archivo para la nueva búsqueda
            try:
                archivo = open("mbox.txt", 'r')
        
                buscarLineasYCrearArchivo("Return-Path", "Return-Path:", "Número de líneas con Return-Path: ")
                archivo.close()
            except:
                print("Error al abrir el archivo")
        elif __ == 14:
            try:
                archivo = open("mbox.txt", 'r')

                buscarLineasYCrearArchivo("Details", "Details: ", "Número de líneas con Details: ")   
                archivo.close()
            except:
                print("Error al abrir el archivo")
        elif __ == 16:
            try:
                archivo = open("mbox.txt", 'r')
                
                buscarLineasYCrearArchivo("ThisAutomatic", "This automatic ", "Número de líneas con This automatic: ") 
                archivo.close()
            except:
                print("Error al abrir el archivo")
        elif __ == 18:
            # margen inferior
            margenTop = '\u2550' * (size - 2)
            print(f"\u255A{margenTop}\u255D")
        else:
            espacios = ' ' * (size - 2)
            print(f'\u2551{espacios}\u2551') 
    

# finalizar
print("Presiona una tecla para continuar")
os.system('pause>nul')
