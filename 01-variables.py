print("Hola soy Sebastian")

#01 DECLARANDO VARIABLES DE TIPO CADENA DE TEXTO
nombre = "Sebastián"
name = "Vicente"

#02 IMPRIMIR DE UNA VARIABLE
print(name)
print("Hola soy",name)

#Declarando una tercera variable de tipo númerico
edad = 29

#03 IMPRIMIR TEXTO + VARIABLE
print("Mi edad es de", edad)

#04 IMPRIMIR 2 VARIABLES EN UNA MISMA LINEA 
print('Hola mi nombre es',nombre,"y tengo",edad) 
print("Hola mi nombre es"+" "+name+" "+"y tengo"+str(edad))
print(f"Hola mi nombre es {nombre} y tengo {edad} años")

#05 ACTUALIZANDO LA VARIABLE NOMBRE
nombre1="Carlos"
print("Mi nuevo nombre es",(nombre1))

#Utilizando la instruccion input
nombre1 = input("¿Cual es tu nuevo nombre?\n")
print("Tu nombre es:",nombre1)

#06 VARIABLES EN UNA SOLA LINEA (NO ES RECOMENDABLE SOLO EN CIERTAS SITUACIONES)
ciudad, region, year = "Osorno", "Los Lagos", "2004"
print("Naci en la ciudad de " + ciudad + ", en la region de " + region + ", en el año " + year)

#07 UTILIZANDO LA INSTRUCCIÓN INPUT
nombre1 = input("¿Cuál es tu nombre?\n")
edad1 = input("¿Cual es tu edad?\n")

print("Tu nombre es:",nombre1,"y tu edad es", edad1)

#08ACOTACIÓN CONSTANTES
'''En Python no existen las constantes, por convención se identifican y se declaran con mayusculas
como se muestra a continuación'''
PI = 3.14
CIUDAD = "Osorno"