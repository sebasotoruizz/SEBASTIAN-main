#01-DATOS DE TIPO NUMERICO
estatura = 1.78
peso = 64
complejo = 1 +4j

print("Impresion del numero complejo:",complejo)

#OPERACION ARITMETICA BASICA
imc = peso/estatura**2

print("Mi imc es de:" ,imc)

#02- DATOS DE TIPO CADENA DE CARACTERES
asignatura = "Programación"
carrera = "Ingenieria Civil en Informatica"
print("Mi carrera es" ,carrera ,"y estoy en la asignatura de" ,asignatura)

#03- VALORES BOOLEANOS
ampolleta = False
interruptor = True

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