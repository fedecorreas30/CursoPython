mascotas = [
    "Wolfgang",
    "Pelusa", 
    "simba", 
    "Felipe", 
    "simba", 
    "Chanchito feliz"
]
mascotas.insert(1, "Melvin") #insertamos un elemento en el lugar 1
mascotas.append("Chanchito triste") #insertamos un elemento en el último lugar

mascotas.remove("simba") #eliminamos un elemento, si está duplicado sólo borarrá el primero
mascotas.pop() #eliminamos el último elemento
del mascotas [0] #eliminamos elementos con el índice
mascotas.clear() #eliminamos todo el listado
print(mascotas)