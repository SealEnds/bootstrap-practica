#

# Clases privadas evitar repetir código, aplicar herencia simple:

# 1) Almacenar todos los datos de los clientes y proveedores, los cuales comparten caracterisicas y son:
#     - Nombre Comercial
#     - Apodo
#     - IdFiscal
#     - Dirección
#     - Teléfono
#     - Código Postal
#     - Poblacion
#     - Provincia
#     - Web
#     - Correo electrónico

# Mediante un menú similar a la imagen que se adjunta, y sobre el cual deberás colocar la cabecera que ya tienes desarrollada, se podrá seleccionar:
#     - Clientes
#         - Añadir cliente
#         - Modificar cliente
#         - Eliminar cliente
#         - Visualizar un cliente (con un formato bonito, recuadrado con un marco doble, de 80 columnas, por pantalla. Ver imagen adjunta).
#         - Listar todos los clientes (con un formato bonito, recuadrado con un marco doble, de 80 columnas, por pantalla. Ver imagen adjunta), enumerando cada uno tal como se muestra en la imagen
#         - Pantalla anterior
#     - Proveedores:
#         - Añadir proveedor
#         - Modificar proveedor
#         - Eliminar proveedor
#         - Visualizar un proveedor (similar al de clientes)
#         - Listar todos los proveedores (con un formato bonito, recuadrado con un marco doble, de 80 columnas, por pantalla, similar al de clientes mostrado), enumerando cada uno tal como se muestra en la imagen.

#     - Salir del programa

# La longitud máxima aceptada para cualquier dato introducido es de 65 caracteres. Si en algún momento se sobrepasa, se deberá notificar al usuario y deberá volver a introducir el dato.

# TODAS las clases y objetos deberá llevar las iniciales de tu nombre y apellidos.

# La clase de la que se hereda debe tener un método que visualiza, recuadrado con un marco doble, todo el contenido del elemento que se introduce, de la forma más bonita que seas capaz de visualizar.

# Se permite emplear el módulo keyboard para facilitar la interacción con el usuario.

# Como todo buen programa, se debe limpiar lo que haya en pantalla para un correcto funcionamiento al arrancar el mismo.

# Debes de incorporar 5 ejemplos de clientes y proveedores para probar el correcto funcionamiento del código que presentas.
# ________________________________________________________________________________________________________________________
import os
import sys
from caratula import *

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

objetosCliente = [
    {
        "NombreComercial": "Adefesio Martínez",
        "Apodo": "Adefesio",
        "IdFiscal": "1",
        "Direccion": "Calle Uva",
        "Telefono": "666666666",
        "CodigoPostal": "18012",
        "Poblacion": "Granada",
        "Provincia": "Granada",
        "Web": "adefesio.com",
        "CorreoElectronico": "adefesio@gmail.com"
    },
    {
        "NombreComercial": "Botarate Jiménez",
        "Apodo": "Botarate",
        "IdFiscal": "2",
        "Direccion": "Calle Doctor Iatrogenia",
        "Telefono": "666777888",
        "CodigoPostal": "10000",
        "Poblacion": "Sparta",
        "Provincia": "Sparta",
        "Web": "www.botarate.com",
        "CorreoElectronico": "botarate@gmail.com"
    },
    {
        "NombreComercial": "Petazeta Rodriguez",
        "Apodo": "Peta",
        "IdFiscal": "3",
        "Direccion": "Calle",
        "Telefono": "Adefesio Martínez",
        "CodigoPostal": "11000",
        "Poblacion": "Hargesia",
        "Provincia": "Somalilandia",
        "Web": "www.somalilandia.com",
        "CorreoElectronico": "somalilandia@gmail.com"
    },
    {
        "NombreComercial": "Winnie de Pu",
        "Apodo": "Pu",
        "IdFiscal": "4",
        "Direccion": "Cien Acres",
        "Telefono": "111000111",
        "CodigoPostal": "19000",
        "Poblacion": "Sussex",
        "Provincia": "Algo de Inglaterra",
        "Web": "www.elpu.com",
        "CorreoElectronico": "elpu@outlook.com"
    },
    {
        "NombreComercial": "Fresa Montoya",
        "Apodo": "Ichigo",
        "IdFiscal": "5",
        "Direccion": "Avenida Mondongo",
        "Telefono": "999888666",
        "CodigoPostal": "7000",
        "Poblacion": "Mondongo",
        "Provincia": "Perú",
        "Web": "www.mondongo.com",
        "CorreoElectronico": "mondongo@hotmail.com"
    }
]

objetosProveedores = [
    {
        "NombreComercial": "Proveedor Adefesio Martínez",
        "Apodo": "Adefesio",
        "IdFiscal": "1",
        "Direccion": "Calle Uva",
        "Telefono": "666666666",
        "CodigoPostal": "18012",
        "Poblacion": "Granada",
        "Provincia": "Granada",
        "Web": "adefesio.com",
        "CorreoElectronico": "adefesio@gmail.com"
    },
    {
        "NombreComercial": "Proveedor Botarate Jiménez",
        "Apodo": "Botarate",
        "IdFiscal": "2",
        "Direccion": "Calle Doctor Iatrogenia",
        "Telefono": "666777888",
        "CodigoPostal": "10000",
        "Poblacion": "Sparta",
        "Provincia": "Sparta",
        "Web": "www.botarate.com",
        "CorreoElectronico": "botarate@gmail.com"
    },
    {
        "NombreComercial": "Proveedor Petazeta Rodriguez",
        "Apodo": "Peta",
        "IdFiscal": "3",
        "Direccion": "Calle",
        "Telefono": "Adefesio Martínez",
        "CodigoPostal": "11000",
        "Poblacion": "Hargesia",
        "Provincia": "Somalilandia",
        "Web": "www.somalilandia.com",
        "CorreoElectronico": "somalilandia@gmail.com"
    },
    {
        "NombreComercial": "Proveedor Winnie de Pu",
        "Apodo": "Pu",
        "IdFiscal": "4",
        "Direccion": "Cien Acres",
        "Telefono": "111000111",
        "CodigoPostal": "19000",
        "Poblacion": "Sussex",
        "Provincia": "Algo de Inglaterra",
        "Web": "www.elpu.com",
        "CorreoElectronico": "elpu@outlook.com"
    },
    {
        "NombreComercial": "Proveedor Fresa Montoya",
        "Apodo": "Ichigo",
        "IdFiscal": "5",
        "Direccion": "Avenida Mondongo",
        "Telefono": "999888666",
        "CodigoPostal": "7000",
        "Poblacion": "Mondongo",
        "Provincia": "Perú",
        "Web": "www.mondongo.com",
        "CorreoElectronico": "mondongo@hotmail.com"
    }
]

class VPQBase:
    def __init__(self, Nombre, Apodo, IdFiscal, direc, tel, cp, pob, prov, web, email):
        self.__Nombre = Nombre
        self.__Apodo = Apodo
        self.__IdFiscal = IdFiscal
        self.__direc = direc
        self.__tel = tel
        self.__cp = cp
        self.__pob = pob
        self.__prov = prov
        self.__web = web
        self.__email = email
    def GetNombre(self):
        return self.__Nombre
    def SetNombre(self,Nombre):
        self.__Nombre = Nombre
    def GetApodo(self):
        return self.__Apodo
    def SetApodo(self,Apodo):
        self.__Apodo = Apodo
    def GetIdFiscal(self):
        return self.__IdFiscal
    def SetIdFiscal(self,IdFiscal):
        self.__IdFiscal = IdFiscal
    def GetDirec(self):
        return self.__direc
    def SetDirec(self,direc):
        self.__direc = direc
    def GetTel(self):
        return self.__tel
    def SetTel(self,tel):
        self.__tel = tel
    def GetCp(self):
        return self.__cp
    def SetCp(self,cp):
        self.__cp = cp
    def GetPob(self):
        return self.__pob
    def SetPob(self,pob):
        self.__pob = pob
    def GetProv(self):
        return self.__prov
    def SetProv(self,prov):
        self.__prov = prov
    def GetWeb(self):
        return self.__web
    def SetWeb(self,web):
        self.__web = web
    def GetEmail(self):
        return self.__email
    def SetEmail(self,email):
        self.__email = email

    def MostrarObjetoCreado(self):
        # mostrar objeto recién creado
        marcoSuperior()
        opciones = [
            "\u2551  Nombre Comercial   : {0}".format(self.GetNombre()), 
            "\u2551  Apodo              : {0}".format(self.GetApodo()),
            "\u2551  IdFiscal           : {0}".format(self.GetIdFiscal()),
            "\u2551  Dirección          : {0}".format(self.GetDirec()),
            "\u2551  Teléfono           : {0}".format(self.GetTel()),
            "\u2551  Código Postal      : {0}".format(self.GetCp()),
            "\u2551  Población          : {0}".format(self.GetPob()),
            "\u2551  Provincia          : {0}".format(self.GetProv()),
            "\u2551  Web                : {0}".format(self.GetWeb()),
            "\u2551  Correo Electrónico : {0}".format(self.GetEmail())
        ]
        marcoLateral(opciones)
        marcoInferior()

class VPQ_Cliente(VPQBase):
    # valores por defecto para no tener que pasarlos cuando solo se quiera acceder a un método
    def __init__(self, Nombre="null", Apodo="null", IdFiscal="null", direc="null", tel="null", cp="null", pob="null", prov="null", web="null", email="null") -> None:
        super().__init__(Nombre, Apodo, IdFiscal, direc, tel, cp, pob, prov, web, email)

    #las interacciones para modificar la datos los hago con métodos dentro de la clase
    def Add(self, objeto): 
        #añadir al cliente
        objetosCliente.append(objeto)
    def Delete(self, id):
        # elimina el objeto del array
        objetosCliente.pop(id)
    def Update(self, id, campoParaCambiar):
        #pasar el id que es la posición en el array del elemento y el valor para cambiar. Se cambia de uno a uno cada campo.
        objeto = objetosCliente[id]
        if(campoParaCambiar == '1'):
            cambios = input("Introduce el nuevo Nombre Comercial: ")
            # guardar cambio para leerlo luego y guardarlo al leerlo (pq es clase privada)
            self.SetNombre(cambios)
            objeto["NombreComercial"] = self.GetNombre()
            Clear()
            # muestra los cambios
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '2'):
            cambios = input("Introduce el nuevo Apodo: ")
            self.SetApodo(cambios)
            objeto["Apodo"] = self.GetApodo()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '3'):
            cambios = input("Introduce el nuevo Id Fiscal: ")
            self.SetIdFiscal(cambios)
            objeto["IdFiscal"] = self.GetIdFiscal()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '4'):
            cambios = input("Introduce el nuevo Dirección: ")
            self.SetDirec(cambios)
            objeto["Direccion"] = self.GetDirec()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '5'):
            cambios = input("Introduce el nuevo Teléfono: ")
            self.SetTel(cambios)
            objeto["Telefono"] = self.GetTel()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '6'):
            cambios = input("Introduce el nuevo Código Postal: ")
            self.SetCp(cambios)
            objeto["CodigoPostal"] = self.GetCp()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '7'):
            cambios = input("Introduce el nuevo Población: ")
            self.SetPob(cambios)
            objeto["Poblacion"] = self.GetPob()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '8'):
            cambios = input("Introduce el nuevo Provincia: ")
            self.SetProv(cambios)
            objeto["Provincia"] = self.GetProv()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '9'):
            cambios = input("Introduce el nuevo Web: ")
            self.SetWeb(cambios)
            objeto["Web"] = self.GetWeb()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '10'):
            cambios = input("Introduce el nuevo Correo Electrónico: ")
            self.SetEmail(cambios)
            objeto["CorreoElectronico"] = self.GetEmail()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '11'):
            Clear()
            pantallaClientes()
        else: 
            Clear()
            modificarCliente(objeto["IdFiscal"])

class VPQ_Proveedor(VPQBase):
    def __init__(self, Nombre="null", Apodo="null", IdFiscal="null", direc="null", tel="null", cp="null", pob="null", prov="null", web="null", email="null") -> None:
        super().__init__(Nombre, Apodo, IdFiscal, direc, tel, cp, pob, prov, web, email)
    def Add(self, objeto): 
        #añadir al proveedor
        objetosProveedores.append(objeto)
    def Delete(self, id):
        # elimina el objeto del array
        objetosProveedores.pop(id)
    def Update(self, id, campoParaCambiar):
        #pasar el id que es la posición en el array del elemento y el valor para cambiar. Se cambia de uno a uno cada campo.
        objeto = objetosProveedores[id]
        if(campoParaCambiar == '1'):
            cambios = input("Introduce el nuevo Nombre Comercial: ")
            # guardar cambio para leerlo luego y guardarlo al leerlo (pq es clase privada)
            self.SetNombre(cambios)
            objeto["NombreComercial"] = self.GetNombre()
            Clear()
            # muestra los cambios
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '2'):
            cambios = input("Introduce el nuevo Apodo: ")
            self.SetApodo(cambios)
            objeto["Apodo"] = self.GetApodo()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '3'):
            cambios = input("Introduce el nuevo Id Fiscal: ")
            self.SetIdFiscal(cambios)
            objeto["IdFiscal"] = self.GetIdFiscal()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '4'):
            cambios = input("Introduce el nuevo Dirección: ")
            self.SetDirec(cambios)
            objeto["Direccion"] = self.GetDirec()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '5'):
            cambios = input("Introduce el nuevo Teléfono: ")
            self.SetTel(cambios)
            objeto["Telefono"] = self.GetTel()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '6'):
            cambios = input("Introduce el nuevo Código Postal: ")
            self.SetCp(cambios)
            objeto["CodigoPostal"] = self.GetCp()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '7'):
            cambios = input("Introduce el nuevo Población: ")
            self.SetPob(cambios)
            objeto["Poblacion"] = self.GetPob()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '8'):
            cambios = input("Introduce el nuevo Provincia: ")
            self.SetProv(cambios)
            objeto["Provincia"] = self.GetProv()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '9'):
            cambios = input("Introduce el nuevo Web: ")
            self.SetWeb(cambios)
            objeto["Web"] = self.GetWeb()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '10'):
            cambios = input("Introduce el nuevo Correo Electrónico: ")
            self.SetEmail(cambios)
            objeto["CorreoElectronico"] = self.GetEmail()
            Clear()
            modificarCliente(objeto["IdFiscal"])
        elif(campoParaCambiar == '11'):
            Clear()
            pantallaClientes()
        else: 
            Clear()
            modificarCliente(objeto["IdFiscal"])

def pantallaInicio():
    # añadir borde superior
    marcoSuperior()
    opciones = ["\u2551   Selecciona una Opción", "\u2551   1. - Clientes", "\u2551   2. - Proveedores", "\u2551   3. - Salir del programa"]
    # añadir borde inferior pasando contenido de cada línea. Añade el contenido con espacios y borde final
    marcoLateral(opciones)
    # añadir borde inferior
    marcoInferior()

    opcion = input("")
    if opcion == '1':
        Clear()
        pantallaClientes()
    elif opcion == '2':
        Clear()
        pantallaProveedores()
    elif opcion == '3':
        sys.exit()
    else:
        Clear()
        pantallaInicio()

def pantallaClientes():
    # visualizar opciones reutiliza el mostrar las opciones para clientes y proveedores
    opcion = visualizarOpciones("Cliente")
    tipo = "cliente"
    if opcion == '1':
        Clear()
        print("añadir")
        addCliente(tipo)
        Clear()
        pantallaClientes()
    elif opcion == '2':
        Clear()
        print("modificar")
        idModificarCliente()
        pantallaClientes()
    elif opcion == '3':
        Clear()
        eliminarCliente("cliente")
        pantallaClientes()
    elif opcion == '4':
        Clear()
        verUnCliente()
        pantallaClientes()
    elif opcion == '5':
        Clear()
        verClientes(tipo)
        pantallaClientes()
    elif opcion == '6':
        Clear()
        pantallaInicio()
    else:
        Clear()
        pantallaInicio()

def pantallaProveedores():
    opcion = visualizarOpciones("Proveedores")
    tipo = "proveedor"
    if opcion == '1':
        Clear()
        print("añadir")
        addCliente(tipo)
        Clear()
        pantallaProveedores()
    elif opcion == '2':
        Clear()
        print("modificar")
        idModificarCliente()
        pantallaProveedores()
    elif opcion == '3':
        Clear()
        eliminarCliente("proveedor")
        pantallaProveedores()
    elif opcion == '4':
        Clear()
        verUnCliente()
        pantallaProveedores()
    elif opcion == '5':
        Clear()
        verClientes(tipo)
        pantallaProveedores()
    elif opcion == '6':
        Clear()
        pantallaInicio()
    else:
        Clear()
        pantallaInicio()

def visualizarOpciones(tipo):
    opciones = [f"\u2551 {tipo}", "\u2551   1. - Añadir", "\u2551   2. - Modificar", "\u2551   3. - Elminar", "\u2551   4. - Visualizar uno", "\u2551   5. - Visualizar todos", "\u2551   6. - Volver"]
    marcoSuperior()
    marcoLateral(opciones)
    marcoInferior()
    opcion = input("")
    return opcion

# función para el objeto que se va a añadir
# reutilizar función, pasando un parámetro que indique si es cliente o proveedor y llamar al método Add de cliente o proveedor. El método lo seguiré llamando addCliente igualmente aunque también sirva para proveedores
def addClienteCamposVacios():
    return {"NombreComercial": False, "Apodo": False, "IdFiscal": False, "Direccion": False, "Telefono": False, "CodigoPostal": False, "Poblacion": False, "Provincia": False, "Web": False, "CorreoElectronico": False}
def addCliente(tipo):
    # variable de control para completar el proceso solo si no hay errores
    correcto = True
    campos = addClienteCamposVacios()
    # para cada elemento de campos, pedir que se introduzcan los datos, mostrando el key del json
    for campo, value in campos.items():
        campos[campo] = input("{0}: ".format(campo))
        # si la longitud es mayor de 65, se rompe el proceso y se marca como error, el flag correcto
        if len(campos[campo]) > 65:
            correcto = False
            Clear()
            break
    # si no hay error, crea un objeto con los valores introducidos y, si el Id Fiscal es un valor distinto de vacío y no false, llama al método Add(), que lo guarda en el array principal, de cliente o proveedor
    if correcto==True:
        if campos["IdFiscal"]:
            if tipo == "cliente":
                VPQ_Cliente_Obj = VPQ_Cliente(campos["NombreComercial"], campos["Apodo"], campos["IdFiscal"], campos["Direccion"], campos["Telefono"], campos["CodigoPostal"], campos["Poblacion"], campos["Provincia"], campos["Web"], campos["CorreoElectronico"])
                VPQ_Cliente_Obj.Add(campos)
                Clear()
                print("Este es el objeto creado:")
                VPQ_Cliente_Obj.MostrarObjetoCreado()
            elif tipo == "proveedor":
                VPQ_Proveedor_Obj = VPQ_Proveedor(campos["NombreComercial"], campos["Apodo"], campos["IdFiscal"], campos["Direccion"], campos["Telefono"], campos["CodigoPostal"], campos["Poblacion"], campos["Provincia"], campos["Web"], campos["CorreoElectronico"])
                VPQ_Proveedor_Obj.Add(campos)
                Clear()
                print("Este es el objeto creado:")
                VPQ_Proveedor_Obj.MostrarObjetoCreado()
            input("Enter para continuar: ")
        else: 
            Clear()
            print("Error: El Id Fiscal es obligatorio")
            addCliente()
    else:
        # si había error en las condiciones de longitud, se vuelve a pedir los datos
        Clear
        print("Error: La longitud máxima es de 65 caracteres")
        campos = addClienteCamposVacios()
        addCliente()
    
# método para pedir un id para modificar
def idModificarCliente():
    clienteBuscado = input("Introduce el Id Fiscal del Cliente que se quiere modificar: ")
    modificarCliente(clienteBuscado)
def modificarCliente(clienteBuscado):
    # usar bandera para ver si se encuentra un resultado o no al final del for. Si no se encuentra, da la opción de salir o introducir otro valor
    coincidencia = False
    #enumerate para pasar el índice como parámetro al métdodo de cliente que interactua con los datos
    for index, objeto in enumerate(objetosCliente):
        # si se encuentra, crea un objeto y pide el campo que se quiere modificar
        if(objeto["IdFiscal"] == clienteBuscado):
            VPQ_Cliente_Obj = VPQ_Cliente(objeto["NombreComercial"], objeto["Apodo"], objeto["IdFiscal"], objeto["Direccion"], objeto["Telefono"], objeto["CodigoPostal"], objeto["Poblacion"], objeto["Provincia"], objeto["Web"], objeto["CorreoElectronico"])
            campoParaCambiar = input("Elige el campo que modificar:\n1. - Nombre Comercial = {0}\n2. - Apodo = {1}\n3. - IdFiscal = {2}\n4. - Dirección = {3}\n5. - Teléfono = {4}\n6. - Código Postal = {5}\n7. - Población = {6}\n8. - Provincia = {7}\n9. - Web = {8}\n10. - Correo Electrónico = {9}\n11. - Volver\n".format(objeto["NombreComercial"], objeto["Apodo"], objeto["IdFiscal"], objeto["Direccion"], objeto["Telefono"], objeto["CodigoPostal"], objeto["Poblacion"], objeto["Provincia"], objeto["Web"], objeto["CorreoElectronico"]))
            # modificar objeto mediante el método de la clase
            VPQ_Cliente_Obj.Update(index, campoParaCambiar)
    if coincidencia == False:
        Clear()
        print("Error 404: No encontrado")
        accion = input("1. - Introducir otro valor\n2. - Volver\n")
        if accion == "1":
            Clear()
            idModificarCliente()
        else: 
            input("Pulsa Enter para continuar: ")
    Clear()

def verClientes(tipo):
    # https://stackoverflow.com/questions/176918/how-to-find-the-index-for-a-given-item-in-a-list
    # para cada objeto, mostrar los valores
    if tipo == "cliente":
        datosParaUsar = objetosCliente
    elif tipo == "proveedor":
        datosParaUsar = objetosProveedores
    for index, objeto in enumerate(datosParaUsar):
        marcoSuperior()
        opciones = ["\u2551  Cliente Nº: {0}".format(index+1)]
        marcoLateral(opciones)
        marcoIntermedio()
        opciones = [
            "\u2551  Nombre Comercial   : {0}".format(objeto["NombreComercial"]), 
            "\u2551  Apodo              : {0}".format(objeto["Apodo"]),
            "\u2551  IdFiscal           : {0}".format(objeto["IdFiscal"]),
            "\u2551  Dirección          : {0}".format(objeto["Direccion"]),
            "\u2551  Teléfono           : {0}".format(objeto["Telefono"]),
            "\u2551  Código Postal      : {0}".format(objeto["CodigoPostal"]),
            "\u2551  Población          : {0}".format(objeto["Poblacion"]),
            "\u2551  Provincia          : {0}".format(objeto["Provincia"]),
            "\u2551  Web                : {0}".format(objeto["Web"]),
            "\u2551  Correo Electrónico : {0}".format(objeto["CorreoElectronico"])
            ]
        marcoLateral(opciones)
        marcoInferior()
    input("Introduce cualquier valor para volver: ")
    Clear()

def verUnCliente():
    # mostar los valores del objeto que coincida con el Id Fiscal buscado
    clienteBuscado = input("Introduce el Id Fiscal del Cliente que se quiere ver: ")
    # usar bandera para ver si se encuentra un resultado o no. Si no se encuentra, da la opción de salir o introducir otro valor
    coincidencia = False
    for objeto in objetosCliente:
        if(objeto["IdFiscal"] == clienteBuscado):
            coincidencia = True
            marcoSuperior()
            opciones = [
                "\u2551  Nombre Comercial   : {0}".format(objeto["NombreComercial"]), 
                "\u2551  Apodo              : {0}".format(objeto["Apodo"]),
                "\u2551  IdFiscal           : {0}".format(objeto["IdFiscal"]),
                "\u2551  Dirección          : {0}".format(objeto["Direccion"]),
                "\u2551  Teléfono           : {0}".format(objeto["Telefono"]),
                "\u2551  Código Postal      : {0}".format(objeto["CodigoPostal"]),
                "\u2551  Población          : {0}".format(objeto["Poblacion"]),
                "\u2551  Provincia          : {0}".format(objeto["Provincia"]),
                "\u2551  Web                : {0}".format(objeto["Web"]),
                "\u2551  Correo Electrónico : {0}".format(objeto["CorreoElectronico"])
            ]
            marcoLateral(opciones)
            marcoInferior()
            input("Pulsa Enter para continuar: ")
    if coincidencia == False:
        Clear()
        print("Error 404: No encontrado")
        accion = input("1. - Introducir otro valor\n2. - Volver\n")
        if accion == "1":
            Clear()
            verUnCliente()
        else: 
            input("Pulsa Enter para continuar: ")
    Clear()

def eliminarCliente(tipo):
    # buscar por Id Fiscal y pedir confirmación. Llamar método Delete() de la clase
    if tipo == "cliente":
        datosParaUsar = objetosCliente
    elif tipo == "proveedor":
        datosParaUsar = objetosProveedores 
    coincidencia = False
    clienteBuscado = input("Introduce el Id Fiscal del Cliente que se quiere eliminar: ")
    for index, objeto in enumerate(datosParaUsar):
        if(objeto["IdFiscal"] == clienteBuscado):
            coincidencia = True
            marcoSuperior()
            opciones = [
                "\u2551  Nombre Comercial   : {0}".format(objeto["NombreComercial"]), 
                "\u2551  Apodo              : {0}".format(objeto["Apodo"]),
                "\u2551  IdFiscal           : {0}".format(objeto["IdFiscal"]),
                "\u2551  Dirección          : {0}".format(objeto["Direccion"]),
                "\u2551  Teléfono           : {0}".format(objeto["Telefono"]),
                "\u2551  Código Postal      : {0}".format(objeto["CodigoPostal"]),
                "\u2551  Población          : {0}".format(objeto["Poblacion"]),
                "\u2551  Provincia          : {0}".format(objeto["Provincia"]),
                "\u2551  Web                : {0}".format(objeto["Web"]),
                "\u2551  Correo Electrónico : {0}".format(objeto["CorreoElectronico"]) ]
            marcoLateral(opciones)
            marcoInferior()
            # pedir confirmación para eliminar
            eliminar = input("¿Quieres eliminarlo definitivamente? (Y para eliminar): ")
            if(eliminar == "Y"):
                if tipo == "cliente":
                    VPQ_Cliente_Obj = VPQ_Cliente()
                    VPQ_Cliente_Obj.Delete(index)
                elif tipo == "proveedor":
                    VPQ_Proveedor_Obj = VPQ_Proveedor()
                    VPQ_Proveedor_Obj.Delete(index)
                    # métedo de la clase para eliminar
                Clear()
                print("Datos eliminados")
            else:
                Clear() 
                print("Datos mantenidos")
    # si no se han encontrado resultados
    if coincidencia == False:
        Clear()
        print("Error 404: No encontrado")
        accion = input("1. - Introducir otro valor\n2. - Volver\n")
        if accion == "1":
            Clear()
            eliminarCliente(tipo)
        else:
            input("Pulsa Enter para continuar: ")
    Clear()
# encuadre
def marcoHorizontal():
    linea = '\u2550' * 78
    return linea
def marcoSuperior():
    print("\u2554{0}\u2557".format(marcoHorizontal()))
def marcoInferior():
    print("\u255A{0}\u255D".format(marcoHorizontal()))
def marcoLateral(contenidoLineas):
    for linea in contenidoLineas:
        espacios = ' ' * int(79 - longitud(linea))
        print("{0}{1}\u2551".format(linea, espacios))
def marcoIntermedio():
    print("\u2560{0}\u2563".format(marcoHorizontal()))

def longitud(elemento):
    return len(elemento)

def Clear():
    os.system('cls')

# cargar configuración color fondo y letra
# def Config():
    # https://stackoverflow.com/questions/31730024/how-to-set-background-color-of-console-in-python
    # os.system('color 1f')

def Main():
    Clear()
    # Config()
    printCaratula()
    pantallaInicio()
if __name__ == '__main__':
    Main()