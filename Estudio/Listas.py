#Listas = Estructura de datos más felxibles

lista = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", 40, 5.67, [1,2,3], True]
print(lista)

#Si quiero mostrar un elemento concreto de la lista:
print(lista[0])
print(lista[3])
print(lista[4])

#Tambien podemos utilizar números negativos para buscar en la lista
print(lista[-2])
print(lista[-1])

#Además podemos trabajar con Sublistas
print(lista[0:3])
print(lista[1:4])
print(lista[:2])
print(lista[2:])

#Determinar cuantos elementos posee una lista
print(len(lista))

lista2 = [1,2,3,4,5]

#Agregar un elemento al FINAL de la lista
lista2.append(6)
print(lista2)

#Agregar un elemento en una posición específica
lista3 = [1,2,4,5]
lista3.insert(2,3)
print(lista3)

#Agregar varios elementos al final de la lista
lista4 = [1,2,3,4,5,6]
lista4.extend([7,8,9])
print(lista4)

#Sumar 2 listas
lista5 = ["a","b","c"]
lista6 = ["d","e","f"]
lista7 = lista5 + lista6
print(lista7)

#Preguntar si un valor se encuentra en la lista
lista8 = [1,2,3,4,5,"Sebastian"]
print(3 in lista8)
print("Sebastian" in lista8)
print(10 in lista8)

#Preguntar en qué indice se encuentra un elemento
print(lista8.index(5))
print(lista8.index("Sebastian"))

#Saber cuantas veces se repite un elemento en una lista
lista9 = [1,2,3,4,5,"Sebastian",1,2,3,1,"Sebastian",1]
print(lista9.count("Sebastian"))
print(lista9.count(1))

#Eliminar un elemento en una lista
lista10 = [1,2,3,4,5,"Seba"]
lista10.pop(2)
print(lista10)

#Eliminar un elemnto sin saber el índice
lista11 = [1,2,3,4,5,"Seba"]
lista11.remove(1)
print(lista11)

#Vaciar una lista
lista12 = [1,2,3,4,5,"Seba"]
lista12.clear()
print(lista12)

#Copiar una lista
lista13 = [1,2,3,4,5,"Seba"]*2
print(lista13)

#Ordenar elementos
lista14 = [5,4,-7,9,0,1,3]
lista.sort()
lista.sort(reverse=True)
print(lista14)