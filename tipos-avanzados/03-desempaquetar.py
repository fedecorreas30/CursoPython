numeros = [1, 2, 3]

# feo!
# primero = numeros[0]
# primero = numeros[1]
# primero = numeros[2]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#primero, segundo, *otros = numeros # estamos empaquetando el resto de los elementos de la lista con *otros
#primero, *otros = numeros # estamos empaquetando el resto de los elementos de la lista con *otros
primero, *otros, ultimo = numeros # estamos empaquetando el resto de los elementos de la lista con *otros
print(primero, ultimo, otros)