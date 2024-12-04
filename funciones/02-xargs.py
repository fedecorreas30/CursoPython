def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado) #Muy importante la identación en en el lugar de resultado en este caso

suma (2, 5, 7) #iterables
suma (2, 5)
suma (2, 8, 7, 45, 32)