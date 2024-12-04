# for sirve para Concatenar, buscar elementos, operaciones matemáticas, etc
buscar = 10
for numero in range(5): #range nos va a devolver una secuencia y ejecutará del 0 al 4, un número menos que el que ponemos
    print(numero)
    if numero == buscar:
        print("Encontrado", buscar)
        break
else:
    print("No encontré el número buscado :(")

for char in "Ultimate python": #nos deletrea los caracteres uno abajo del otro
    print(char)