# Bucles

# BUCLE WHILE

#ejemplo
import math

numero = int(input("Digite un número: "))

while numero<0:
    print("Error -> Debería ser un número positivo")
    numero = int(input("Digite un número: "))

print(f"\nSu raíz cuadrada es: {(math.sqrt(numero)):.2f}")

#Mostrar un mensaje x veces
i = 0

while i < 10:
    print("Hola mundo")
    i += 1
#Mostrar numeros del 0-9
i = 0

while i < 10:
    print(i)
    i += 1

#BUCLE FOR

#ejemplo
for i in [1,2,3,4,5]: #no necesariamente deben ser numeros, puede ser cualquier elemento
    print("Hola mundo")

#Mostrar valor de variable iteradora
coleccion = [1,2,3,4,5]

for i in coleccion:
    print(f"Elemento: {i}")