#Declarando mi primera función
def mi_primera_funcion():
    print("Esta es mi primera función")
mi_primera_funcion()

#Declarando una función y utilizando listas
print("\n Declarando una funcion y utilizando listas")
def concatenar(lista1,lista2):
    return lista1 + lista2

lista1 = [1,2,3]
lista2 = [4,5,6]

#concatenar
print(concatenar(lista1,lista2))

#Declarando una función multiplicación pasando parámetros
def mulptiplicacion (num1,num2):
    return num1*num2
print(mulptiplicacion(5,5))

#Ejemplo de una función
print("\n################## 04-FUNCIONES SUMA Y RESTA (POR TECLADO) ##################")

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

a = int(input("Ingrese el valor de a: "))
b = int(input("Ingrese el valor de b: "))

#Se llama a la función Suma
resultado = suma(a, b)
print("La suma es de:", resultado)

#Se llama a la función Resta
resultado2 = resta(a, b)
print("La resta es de:", resultado2)