animal = "  chanCHito feliz  "
print(animal.upper())  # mayúsculas
print(animal.lower())  # Minúsculas
# borra espacioes y mayúscula la primer letra
print(animal.strip().capitalize())
print(animal.title())  # Mayúscula las primeras letras de cada palabra
print(animal.strip())  # borrar espacios izq y derecha
print(animal.lstrip())  # borrar espacios izq
print(animal.rstrip())  # borrar espacios der
print(animal.find("cH"))  # buscar dentro del string, nos dará el índice
print(animal.replace("nCH", "j"))  # reemplazar cadena de valores
print("nCH" in animal)  # nos dirá si se encuentra dentro del string - boolean
print("nCH" not in animal)
# nos dirá si NO se encuentra dentro del string - boolean
