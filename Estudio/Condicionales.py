#CONDICIONALES

#ESTRUCTURA IF-ELIF-ELSE
numero = int(input("Digite un numero: "))

if numero > 0:
    print("El numero es positivo")
elif numero == 0:
    print("El numero es cero")
else:
    print("El numero es negativo")
print("Fin del programa")

#CONDICIONALES COMBINADOS
edad = int(input("Digite su edad: "))

if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#Condicionales anidados
edad = int(input("Digite su edad: "))

if edad > 0:
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")

#Combinados
edad = int(input("Digite su edad: "))

if edad > 0 and edad < 100:
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")

#Operadores Relacionales Combinados
edad = int(input("Digite su edad: "))

if 0 < edad < 100:
    print("Edad correcta")
    if edad >= 18:
        print("Es mayor de edad")
else:
    print("Edad incorrecta")

#EN PYTHON NO EXISTEN LOS CONDICIONALES MULTIPLES