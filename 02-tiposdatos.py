#01-DATOS DE TIPO NUMERICO
estatura = 1.78
peso = 64
complejo = 1 +4j

print("Impresion del numero complejo:",complejo)

#OPERACION ARITMETICA BASICA
imc = peso/ (estatura**2)

print("Mi imc es de: {:2f}".format(imc),"\n")

#02- DATOS DE TIPO CADENA DE CARACTERES
asignatura = "Programación"
carrera = "Ingenieria Civil en Informatica"
print("Mi carrera es" ,carrera ,"y estoy en la asignatura de" ,asignatura)

#03- VALORES BOOLEANOS
ampolleta = False
interruptor = True

print(bool(0))
print(bool(""))
print(bool(None))
print(bool("False"))
print(bool(1))
print("\n")

#CON TYPE SABEMOS EL TIPO DE DATOS QUE ESTAMOS TRATANDO
print(type(ampolleta))

#04 DATOS DE TIPOS ARRAY (OBJETOS DE COLECCION)
estudiantes = ["Matias", "Marcos", "Cristobal", "Sebastian"]
print(estudiantes)
num = [1,2,3,4,5,6]
print(num)

print("Mi IMC es de: {:.2f}" .format(imc), "\n")

#Declarando e inicializando una lista
nueva_lista = list
print("Esta es una lista vacia",nueva_lista)

otra_lista =[]
print("Esta es otra lista vacia",otra_lista)
print(type(otra_lista))

#Declarando otras listas
estudiantes = ["Matias", "Marco", "Cristobal", "Sebastian"]
num = [1,2,3,4,5,6]
lenguaje = ["Python"]

#¿SE PUEDE REALIZAR UNA LISTA DE DATOS COMPUESTOS?
data = ['Osorno', {'UV': 'nivel bajando', 'Temp °C': 15}, (-40.5725)]
print("Lista de cadena de caracteres:", estudiantes)
print("Lista de números:", num)
print("Lista de un elemento:", lenguaje)
print("Esto igual es una lista:", data)
print(len(data))
print(num.count(6)) #CANTIDAD DE OCURRENCIAS DE UN ELEMENTO

print(estudiantes[0]) #correcto (primer elemento de la lista)
print(estudiantes[1]) #segundo elemento de la lista
#print(estudiantes[5]) #esto es incorrecto
print(estudiantes[-2]) #

estudiantes[3] = "Gabriela"
print("El arreglo de estudiantes es:",estudiantes)

#Inicializando otra lista de datos mixtos
data_asig = [10023,"Programacion",1,True]

#¿Se puede sumar listas?
print("Suma de listas",estudiantes + num)

#¿Qué hace estas funciones?
print(list("Python"))
print(list(range(10)))
print("\n")

# > En el fichero de listas se mostraran más funciones

#05 - Tuplas - (No mutables)
newtupla = tuple()
grupo1 = ("Daniel","Cristian","Felipe",200,100)


diccionario1 = dict()
diccionario2 = {}

datos_personales = {
    "Nombre":"Victor",
    "Institucion":"Ulagos",
    "Edad":29
    }

print(datos_personales)

datos_personales = {
    "Nombre":"Victor",
    "Institucion":"Ulagos",
    "Edad":29,
    "Asignaturas": {"Estructura de Datos", "Programacion"}
    }

print("Diccionario inicial:",datos_personales)

#Consulta la cantidad de elementos del Diccionario
print(len(datos_personales))

#Es facilmente accesible a los elementos dentro de un diccionario
print(datos_personales["Institucion"])

#¿Como actualizamos el valor de una clave dentro de un diccionario?
datos_personales["Institucion"] = "USS"
print("Diccionario actualizado:",datos_personales)

#Agregando un nuevo campo al diccionario
datos_personales["Ciudad"] = "Osorno"
print(datos_personales)
print("Diccionario con el nuevo campo:",datos_personales)

#Eliminando un campo del diccionario
del datos_personales["Ciudad"]
print("diccionario con el campo eliminado", datos_personales)