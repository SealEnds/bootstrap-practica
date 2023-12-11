# La fecha será la del inicio del comienzo de la programación de cada programa.
#Además, la primera línea del código fuente deberá contener el nombre del alumno y la fecha extendida (es decir, contiene el día de la semana) de cuando comienzas a programarlo.

# Fecha: fecha actual                       Hora: hora actual
# Proyecto: nombre proyecto
# Developer: nombre

# Pedir nombre de proyecto y nombre
#https://docs.python.org/3/library/datetime.html
# https://stackoverflow.com/questions/19326004/access-a-function-variable-outside-the-function-without-using-global
# https://www.geeksforgeeks.org/python-os-get_terminal_size-method/
# https://stackoverflow.com/questions/227459/how-to-get-the-ascii-value-of-a-character

def generarCaratula(date_str, time_str, developer, proyect):
    import os 
    # pip install colorama
    os.system('color 1f')
    from colorama import Fore, Style, Back
    size = os.get_terminal_size().columns # tomar tamaño de pantalla cmd

    # ancho = print_window_info()
    string = '\u2550' # unicode doble línea horizontal
    fullstring = string * (size-2)

    print("\u2554{0}\u2557".format(fullstring)) 
    spaces1 = size - len(date_str) - len(time_str) - 7 - 6 - 4 # los espacios para añadir son el tamaño de la pantalla menos la longitud de la fecha menos la longitud de la hora menos la longitud y espacios de las palabras fecha: y hora: menos espacios de líneas verticales y líneas veticales
    space1 = " " * spaces1 # crear string de espacios
    spaces2 = size - len(proyect) - 10 - 4
    space2 = " " * spaces2
    spaces3 = size - len(developer) - 11 - 4
    space3 = " " * spaces3
    line1 = "\u2551 Fecha: {0}{1}Hora: {2} \u2551".format(date_str, space1, time_str)
    line2 = "\u2551"+Fore.YELLOW+" Proyecto: {0}{1} ".format(proyect, space2)+Style.RESET_ALL+"\u2551"
    line3 = "\u2551 Developer: {0}{1} \u2551".format(developer, space3)
    line4 = "\u255A{0}\u255D".format(fullstring)
    
    return [line1, line2, line3, line4]

def introducirDatos():
    import datetime

    datetime = datetime.datetime.now() 
    date = datetime.date()
    date_str = date.strftime("%d/%m/%Y".format(date)) # pasar fecha a string y formatear
    time = datetime.time()
    time_str = time.strftime("%H:%M:%S".format(time))

    developer = input("Nombre desarrollador: ")
    proyect = input("Nombre proyecto: ")

    return [date_str, time_str, developer, proyect]