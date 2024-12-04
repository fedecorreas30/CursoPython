numeros = [1, 5 ,18, 3, 0, 100, 12, 7]

# numeros.sort(reverse=True)
numeros2 = sorted(numeros, reverse=True) #Creará una nueva lista sin afectar la anterior
print(numeros)
print(numeros2)

usuarios = [["Chanchito", 4], 
            ["Felipe", 1], 
            ["Pulga", 5]
]
#def ordena(elemento):
#    return elemento[1] #Le decimos que ordene los elementos por el elemento 1 en este caso el número

#usuarios.sort(key=ordena, reverse=True) #Tenemos que usar Key y el argumento para poder ordenarlo con sort en este caso
usuarios.sort(key=lambda el: el[1]) # nos ahorramos de usar la función e identifica lo que queremos ordenar

print(usuarios)