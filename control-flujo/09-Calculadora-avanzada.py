print("Bienvenidos a la calculadora")
print("Para salir escribe salir")
print("Las operaciones son suma, resta, multi y div")

resultado = ""
while True: #definimos la variable para crear un loop infinito
    if not resultado:
        resultado = input("Ingrese número: ")
        if resultado.lower() == "salir":
            break   # el usuario ingresará números a menos que escriba salir
        resultado = int(resultado)
    op = input("Ingresa operación: ")
    if op.lower() == "salir":
        break        # el usuario ingresará operaciones a menos que escriba salir
    n2 = input("Ingrese siguiente número: ")
    if n2.lower() == "salir":
        break       # el usuario ingresará otro número a menos que escriba salir
    n2 = int(n2)

    if op.lower() == "suma":    #Luego definimos las operaciones disponibles
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("Operación no válida")
        break
    print(f"EL resultado es {resultado}") #finalmente imprimimos el resultado que será acompañado  
                                          # del loop infinito de operación y siguiente número