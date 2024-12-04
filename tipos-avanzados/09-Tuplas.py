#Vamos a usar las tuplas cuando NO queramos modificar los elementos que se encuentran en un listado
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2]) #Recibe cualquier tipo de iterable
#Sólo se le pueden aplicar funciones que no modifiquen a la tupla
print(punto)
menosNumeros = numeros [:2]
print(menosNumeros)
primero, segundo, *otros = numeros
print(primero, segundo, otros)
for n in numeros:
    print(n)

#Para poder modificar a la tupla, debemos crear una nueva lista
ListaNumeros = list(numeros)
ListaNumeros[0] = "Chanchito Feliz"
print(ListaNumeros)