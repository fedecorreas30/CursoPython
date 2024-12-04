# Si vamos a utilizar estos for adentro de un for, tienen que tener un objetivo claro y definido
# Nunca deben ser la primera alternativa
for j in range(3): #outer for / loop
    for k in range(2): #inner for / loop
        print(f"{j}, {k}")