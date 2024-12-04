#La palabra def es para definir funciones, siempre después del nombre de la función pondemos ()
def hola(nombre, apellido): #en este caso nombre y apellido son un parámetro
    #Podemos definir funciones con parámetros opciones por ejemplo apellido="Feliz"
    #Si no definimos el segundo argumento en algún lado, se utilizará la palabra Feliz
    print("Hola mundo")
    print(f"Bienvenido {nombre} {apellido}") #Acá estamos usando los parámetros 

hola("Federico", "Correas")    #En este caso Federico y Correas son argumentos
hola("León", "enjaulado")




hola(apellido="correas", nombre="Federico") #definimos en que orden va cada argumento