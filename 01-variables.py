print("Hola soy Sebastian")

#Declarando una variable
Nombre= "Sebastian"
name= "Vicente"

print(Nombre)
print("Hola soy", (Nombre))
print("Hola soy",(name))

#declarando una variable#
edad=18

print("Mi edad es",(edad))

#imprimiendo 2 variables en una misma sentencia#
#print("Hola mi nombre es"+ Nombre +"y mi edad es"+ edad+)
#print("Hola mi nombre es" + Nombre + "y mi edad es" + str(edad) +)
print("Hola mi nombre es " + Nombre + " y mi edad es " + str(edad))

#Actualizando la variable nombre#
nombre1="Carlos"
print("Mi nuevo nombre es",(nombre1))

#Utilizando la instruccion input#
nombre1 = input("¿Cual es tu nuevo nombre?\n")
print("Tu nombre es:",nombre1)

#06, VARIABLES EN UNA SOLA LINEA (NO ES RECOMENDABLE SOLO EN CIERTAS SITUACIONES)
ciudad, region, year = "Osorno", "Los Lagos", "2004"
print("Naci en la ciudad de " + ciudad + ", en la region de " + region + ", en el año " + year)