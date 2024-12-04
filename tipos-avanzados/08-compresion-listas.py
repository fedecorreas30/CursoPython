usuarios = [["Chanchito", 4], 
            ["Felipe", 1], 
            ["Pulga", 5]
]

#nombres = []
#for usuario in usuarios:
#    nombres.append(usuario[0])
#print(nombres)
#La función de abajo se conoce como MAP
#nombres = [usuario[0] for usuario in usuarios] # le estamos pidiendo que nos traiga el primer elemento de los usuarios

#La función de abajo se conoce como FILTER
#nombres = [usuario for usuario in usuarios if usuario[1] > 2] # estamos diciendo que nos devuelva los id mayores a 2
#nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2] # Estamos filtrando y transformando la lista

# nombres = list(map(lambda usuario: usuario[0], usuarios))

nombres = list(filter(lambda usuario: usuario[1] > 2, usuarios))

print(nombres)

# SE PUEDE UTILIZAR CUALQUIERA DE LAS DOS, LA COMPRESIÓN DE LISTAS O MAP Y FILTER