def largo(texto):
    resultado = 0
    for _ in texto: #Cambiamos char por _ para que nos deje de dar el error
        resultado += 1
    return resultado


print("chanchito") 
l = largo("Hola Mundo")
print(l)