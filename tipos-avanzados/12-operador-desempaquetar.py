# DESEMPAQUETAMIENTO PARA LISTAS Y TUPLAS
lista1 = [1, 2, 3, 4]
print(1, 2, 3, 4)
print(*lista1) #De esta forma desempaquetamos los elementos sin la lista, también puede con las tuplas

lista2 = [5, 6]

combinada = ["Hola", *lista1, "mundo", *lista2, "chanchito"] #podemos combinar listas para obtener una nueva lista
print(combinada)

# DESEMPAQUETAMIENTO PARA DICCIONARIOS

punto1 = {"x": 19, "y": "Hola"}
punto2 = {"y": 15}
#La forma de asignar las propiedades es de derecha a izquierda. Siempre va a quedar la de la derecha
nuevoPunto = {**punto1, "lala": "hola mundo", **punto2, "z": "mundo"}

print(nuevoPunto)