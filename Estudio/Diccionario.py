#Diccionarios ({"clave":"valor","clave2":"valor2"})

diccionario = {"azul":"blue","rojo":"red","verde":"green"}

#Mostrar todos los elementos del diccionario
print(diccionario)

#Poner Clave para mostrar su Valor
print(diccionario["azul"])
print(diccionario["rojo"])
print(diccionario["verde"])

#Agregar nuevos elementos al diccionario (["clave"] = "valor")
diccionario["amarillo"] = "yellow"
print(diccionario)

#Modificar un elemento en el diccionario
diccionario["azul"] = "BLUE"
print(diccionario)

#Eliminar un elemento en el diccionario
del(diccionario["verde"])
print(diccionario)

#Crear una Agenda Sencilla
diccionario = {"Sebastián":[18,1.78],"Matias":[20,1.70],"Vicente":[21,1.75]}
print(diccionario)

#
diccionario = {"Sebastián":{"edad":18,"estatura":1.78},"Matias":{"edad":20,"estatura":1.70},"Vicente":{"edad":21,"estatura":1.75}}
print(diccionario["Sebastián"])
print(diccionario["Matias"])
print(diccionario["Vicente"])

#
equipo = {10:"Lionel Messi",7:"Cristiano Ronaldo",9:"Erling Haaland"}
print(equipo)
print(equipo[7])

#Mostrar mensaje al pedir una Clave NO VÁLIDA
print(equipo.get(10,"No existe un jugador con ese dorsal dentro de este diccionario"))
print(equipo.get(6,"No existe un jugador con ese dorsal dentro de este diccionario"))

#Buscar un dato dentro del diccionario
print(11 in equipo)

#Mostrar TODAS las CLAVES de un Diccionario
print(equipo.keys())

#Mostrar los VALORES de un Diccionario
print(equipo.values())

#Poner elementos dentro de una lista con tuplas(método items)
print(equipo.items())

#Saber Cuantos elementos hay en un diccionario
print(len(equipo))

#VACIAR Diccionario
equipo.clear()
print(equipo)