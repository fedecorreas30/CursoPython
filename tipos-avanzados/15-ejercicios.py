from pprint import pprint #ordena un poco los print con un width

string1 = "Bienvenidos a nuestra nueva nweb"
#Quitamos los espacioes de un string
def quita_espacios(texto):
    return [char for char in texto if char != " "]
#Contamos cuantas veces se repiten los caracteres de un string
def cuenta_caracteres(lista):
    chars_dict = {}
    for char in lista:
        if char in chars_dict: #Preguntamos si el caracter se encuentra en el diccionario
            chars_dict[char] += 1 #Accedemos al valor del diccionario y si está le sumamos 1
        else:
            chars_dict[char] = 1
    return chars_dict #Retornamos chars_dict
#Ordenamos de mayor a menor la cantidad que se repite cada letra
def ordenar(dict):
    return sorted(
        dict.items(),
        key=lambda key: key[1],
        reverse=True
    )

def mayores_tuplas(lista):
    maximo = lista[0][1] #accedo al primer elemento y del primer elemento accedo al valor, segundo de la tupla
    respuesta = {} #Creo un diccionario que tendrá los elementos de mayores números
    for orden in lista: 
        if maximo > orden [1]: #si máximo es mayor al primer elemento de orden terminamos la iteración, sin sigue
            break
        respuesta[orden[0]] = orden [1] #Tiene que contener el primer valor de la tupla y luego asignamos el segundo elemento que va a ser el valor de esta tupla
    return respuesta

def crea_mensaje(diccionario):
    mensaje = "Los que más se repiten son: \n"
    for key, valor in diccionario.items():
        mensaje += f"- {key} con {valor} repeticiones \n"
    return mensaje

sin_espacios = quita_espacios(string1)
print(sin_espacios)

caracteres_string = cuenta_caracteres(sin_espacios)
pprint(caracteres_string, width=1)

ordenados = ordenar(caracteres_string)
print(ordenados)

mayores = mayores_tuplas(ordenados)
print(mayores)

mensaje = crea_mensaje(mayores)
print(mensaje)