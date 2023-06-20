#Operadores aritméticos(+,-,*,/)

#SUMA
num1 = 10
num2 = 5
resultado = num1 + num2
print(resultado)

#RESTA
num1 = 10
num2 = 5
resultado = num1 - num2
print(resultado)

#MULTIPLICACION
num1 = 10
num2 = 5
resultado = num1 * num2
print(resultado)

#DIVISION exacta
num1 = 10
num2 = 5
resultado = num1 / num2
print(resultado)

#DIVISION no exacta (entrega de resultado redondeado a la baja)
num1 = 10
num2 = 3
resultado = num1 // num2
print(resultado)

#MODULO (entrega el residuo o resto de la division)
num1 = 10
num2 = 3
resultado = num1 % num2
print(resultado)

#EXPONENCIACION
num1 = 2
num2 = 5
resultado = num1 ** num2
print(resultado)

'''PRIORIDAD EN LAS OPERACIONES ARITMÉTICAS
1- Paréntesis
2- Exponenciación
3- Multiplicación, División, Modulo
4- Suma, Resta
'''
#ejemplo

resultado = 3 ** 3 * (13/5 - (2 * 4))
print(resultado)


#Operadores Relacionales (>,<)

#MENOR QUÉ 
resultado = 10 < 20
print(resultado)

#MENOR o IGUAL
resultado = 10 <= 20
print(resultado)

#MAYOR QUÉ 
resultado = 10 > 20
print(resultado)

#MAYOR o IGUAL 
resultado = 10 >= 20
print(resultado)

#IGUALDAD
resultado = 10 == 20
print(resultado)

#DIFERENCIA
resultado = 10 != 20
print(resultado)

#Combinar operadores
a = 10
b = 20
c = 30
resultado = (a + b) == c
print(resultado)