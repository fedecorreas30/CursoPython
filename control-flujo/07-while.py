# numero = 1
# while numero < 100:
#     print(numero)
#     numero *= 2       #multiplica el número hasta el último que sea menor a 100

# comando =""

# while comando.lower() != "salir": # Le agregamos el lower para que no discrimine mayus o minus cuando escriba el usuario
#     comando = input("$ ")
#     print(comando)


while True: # Esto sería un Loop infinito, siempre debemos tener una claúsula de salida, sino se ejecutará
            # eternamente y nos terminará rompiendo la aplicación
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir": #claúsula de salida
        break
