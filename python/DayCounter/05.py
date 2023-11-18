
#Crea un programa llamado DayCounter, visualizando con la carátula la fecha y hora de cuando lo empiezas, con tu nombre y apellidos, y dejando un hueco de 2 filas vacías, visualizando un recuadro con la misma forma gráfica que la caratula, dónde deberás visualizar todos los items de este ejercicio.

#El programa contará con un menú tal que:

# - Tenga una opción para introducir 2 fechas y visualizarlas por pantalla en todo momento, debidamente encuadrado en el recuadro inferior.

#- Opción para calcular el número de días que hay entre esas dos fechas, que se presentará por pantalla en color amarillo.

#- Opción para calcular el número de semanas que hay entre esas dos fechas, que se presentará por pantalla en color verde claro.

#- Opción que te visualice cual será el siguiente tras la segunda fecha año bisiesto cuyo 31 de agosto cae en domingo.

#- Tenga una opción que guarde en un archivo txt las dos fechas junto a las respuestas a las 3 cuestiones que se plantean.

#Si se necesita información sobre el tratamiento de fechas en Python, se sugiere investigar páginas como: https://codigofacilito.com/articulos/fechas-python
# ____________________________________________________________________________________________________________________
import os
import math
from datetime import datetime 
from colorama import Fore, Style
from caratula import *
import sys
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

def printCaratula():
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

# dejar filas vacías
def filasVacias():
    for __ in range(2):
        print("")

def DayCounter():
    # tamaño cmd
    size = os.get_terminal_size().columns # tomar tamaño de pantalla cmd
    # ruta actual
    RutaActual = os.getcwd() + '\\'
    # Pedir fechas
    date_str_1 = input("Introduce la primera fecha para comparar (formato dd/mm/YYYY): ")
    date_str_2 = input("Introduce la primera fecha para comparar (formato dd/mm/YYYY): ")
    # comprobar que son fechas
    try: 
        date_1 = datetime.strptime(date_str_1, '%d/%m/%Y') #strptime para pasar de string a tipo dato fecha
        date_2 = datetime.strptime(date_str_2, '%d/%m/%Y')
    except:
        print("ERROR al introducir las fechas")

    days_diff = abs((date_2 - date_1).days) # diferencia de días en valor absolute, .days después de restar
    weeks_diff = math.floor(abs((date_2 - date_1).days/7))
    # A partir de la segunda fecha, obtener los años bisiestos y comprobar si es 31 de agosto y si es domingo
    new_day = 31
    new_month = 8
    new_year = date_2.year 
    if date_2.month > 8: # si el mes es mayor que agosto, ese año ya no se mira, porque ese domingo 31 de agosto ya ha pasado
        new_year = date_2.year + 1
    next_date = datetime.strptime(f'{new_day}/{new_month}/{new_year}', '%d/%m/%Y') # crear nueva fecha con el nuevo año
    # información sobre calcular años bisiestos: https://www.mathsisfun.com/leap-years.html
    # para que sea bisiesto tiene que ser divisible entre 4 y no divisble entre 100, excepto si es divisible entre 400
    bisiesto = False
    while(bisiesto == False):
        if new_year%4 == 0:
            bisiesto = True
            if new_year%100 == 0:
                bisiesto = False
                if new_year%400 == 0:
                    bisiesto = True
        if bisiesto == False:
            new_year = new_year + 1 # sumar un año si es false, terminar bucle si es true
    leap_year = datetime.strptime(f'{new_day}/{new_month}/{new_year}', '%d/%m/%Y') # generar fecha con primer bisiesto cualquiera
    # comprobar si el día de la semana de ese 31 de agosto era domingo
    weekday = leap_year.weekday() # comprobar que es domingo
    while(weekday != 0): # si no es domingo, ya solo hay que sumar cuatro y crear la nueva fecha y comprobar si es domingo
        new_year = new_year + 4
        leap_year = datetime.strptime(f'{new_day}/{new_month}/{new_year}', '%d/%m/%Y')
        weekday = leap_year.weekday()
    # Crear archivo con la información
    archivo = open("{0}{1}.txt".format(RutaActual, "DayCounter"), "w", encoding="utf-8") # crear archivo
    archivo.write(f"Diferencia de días: {days_diff}\n") 
    archivo.write(f"Diferencia de semanas: {weeks_diff}\n")
    archivo.write(f"Primer año bisiesto con 31 de agosto que es domingo: {new_year}\n")

    # escribe un mensaje, pasa una variable, un estilo opcional de colorama y calcula espacios necesarios
    def printMessage(border, message, value="", color = ""):
        space = ' ' * (size - len(message) - len(str(value)) - 4) # 4 pq hay 2 bordes y 2 espacios mínimos
        print(f"{border} {message}{color}{value}{Style.RESET_ALL}{space} {border}")

    def printContent():
        margenTop = '\u2550' * (size - 2) 
        print(f"\u2554{margenTop}\u2557") # margen superior
        espacios_linea_vacia = ' ' * (size - 2)
        print(f"\u2551{espacios_linea_vacia}\u2551") # una línea entre medias
        printMessage("\u2551", "  Días de diferencia: (pulsa 1)")
        printMessage("\u2551", "  Semanas de diferencia: (pulsa 2)")
        printMessage("\u2551", "  1er bisiesto posterior con 31 de agosto domingo: (pulsa 3)")
        espacios = ' ' * (size - 2)
        print(f"\u2551{espacios_linea_vacia}\u2551") # una línea entre medias
        margenBot = '\u2550' * (size - 2) 
        print(f'\u255A{margenBot}\u255D') # margen inferior

   
        opcion = input("Elige una opción (1, 2, 3): ")
        if opcion == '1':
            print(f"Días de diferencia: {Fore.YELLOW}{days_diff}{Style.RESET_ALL}")
        elif opcion == '2':
            print(f"Semanas de diferencia: {Fore.GREEN}{weeks_diff}{Style.RESET_ALL}")
        elif opcion == '3':
            print(f"1er bisiesto posterior con 31 de agosto domingo: {new_year}")
        else:
            sys.exit()
        printContent()
    printContent()

if __name__ == '__main__':
    printCaratula()
    filasVacias()
    DayCounter()

