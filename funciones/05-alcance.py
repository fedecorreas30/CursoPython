saludo = "Hola Global" #Variable global, se recomienda NO USAR


def saludar():
    global saludo #MALA PRÁCTICA
    saludo = "Hola Mundo"
    


def saludaChanchito():
    saludo = "Hola Chanchito" #esta variable es distinta a la de arriba es como si fueran a y b
    print(saludo)

print(saludo)
saludar()
print(saludo)