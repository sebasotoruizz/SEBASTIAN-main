#Ejercicio 2

lista_a = [10,80,15,30,20]
lista_b = [20,45,80,20,10]
lista_c = [20,35,60,90,20]

#A
def encontrar_valores(lista_a,lista_b,lista_c):
    comun = []
    for valor in lista_a:
        for valor in lista_b and valor in lista_c:
            comun.append(valor)
    return encontrar_valores
    comun = encontrar_valores(lista_a,lista_b,lista_c)
    print(comun)
#B
todas_listas = [lista_a + lista_b + lista_c]
print(todas_listas)
#C
def valor_dup(todas_listas):
    return list(set(todas_listas))
no_dup = valor_dup
print(no_dup)
#D
todas_listas.sort(reverse=True)
print(todas_listas)
#E
todas_listas[6] = 100
print(todas_listas)