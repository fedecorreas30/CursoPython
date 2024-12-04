def no_space(texto): #Con esta función eliminamos los espacios y concatenamos todos los caracteres
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char #Acá nos va a ir sumando caracter por caracter que sea distino a un espacio
    return nuevo_texto

def reverse(texto): #Con esta función invertimos el texto ya que al poner primero char y luego el + concatena las letras en orden inverso 1) h 2)oh
    texto_al_reves =""
    for char in texto:
        texto_al_reves  = char + texto_al_reves 
    return texto_al_reves

def es_palindromo(texto): #Finalmente en esta función vemos si el texto es igual a la inversa y ponemos lower para evitar mayúsculas
    texto = no_space(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("Amo la paloma"))
print(es_palindromo("Hola Mundo"))
print(es_palindromo("Reconocer"))
print(es_palindromo("Somos o no Somos"))




#for char in texto:
#    print(char)

# for char in(reversed(texto)):
#    print(char)

#def es_palindromo(texto) =    

#def es_palindromo(texto):
#    for char in range(texto):
#        return char
    

#print("Amo la paloma", espacios("Amo la Paloma"))
#print("Hola Mundo", espacios("Hola Mundo"))
#print("Abba", espacios("Abba"))
#print("Reconocer", espacios("Reconocer"))