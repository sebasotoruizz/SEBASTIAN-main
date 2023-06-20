#Tuplas = Listas Inmutables

tupla = (4,"Hola",6.78,[1,2,3],4)

#NO SE PUEDEN AGREGAR MAS VALORES
#tupla.append(5)

#NO SE PUEDE MODIFICAR UN VALOR
#tupla[0] = 8

#NO SE PUEDE ELIMINAR UN VALOR
#tupla.pop()

#SI SE PUEDE BUSCAR UN VALOR(tambien sirven los índices negativos)
print(tupla[0])

#TAMBIEN SE PUEDE HACER SLICING
print(tupla[1:])

#SE PUEDE COMBPROBAR SI UN VALOR SE ENCUENTRA EN LA LISTA
print(4 in tupla)

#SE PUEDE BUSCAR CON EL MÉTODO INDEX y COUNT
print(tupla.index("Hola"))
print(tupla.count("4"))

#SE PUEDE BUSCAR CON EL MÉTODO LEN(para conocer la cantidad de elmentos que tiene)
print(len(tupla))

#TRANSFORMAR UNA TUPLA EN UNA LISTA
tupla = (4,"Hola",6.78,[1,2,3],4)
lista = list(tupla)

#O TRANSFORMAR UNA LISTA EN TUPLA
lista = [4,"Hola,6.78,[1,2,3],4"]
tupla = tuple(lista)