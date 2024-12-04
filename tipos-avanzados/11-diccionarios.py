punto = { "x": 25, "y": 50} #Lo de la izq sí o sí es un string, el de la derecha cualquier dato
print(punto)
print(punto["x"]) # Debemos indicarle un string para rastrear, no podemos usar 0, 1 cómo en sets
print(punto["y"]) # Debemos indicarle un string para rastrear, no podemos usar 0, 1 cómo en sets

punto["z"] = 45
#print(punto, punto["lala"])
if "lala" in punto:
    print("encontre lala", punto["lala"])

print(punto.get("x"))
print(punto.get("lala", 97))
del punto["x"]
del(punto["y"])

print(punto)
punto["x"] = 25

for valor in punto: #para llamar a los valores tenemos que hacer lo siguiente
    print(valor, punto[valor])


for valor in punto.items(): #Nos devuelve tuplas
    print(valor)

for llave, valor in punto.items(): #Desempaquetamos las tuplas 
    print(llave, valor)

usuarios = [
    {"id": 1, "nombre": "Chanchito"},
    {"id": 2, "nombre": "Feliz"},
    {"id": 3, "nombre": "Nicolás"},
    {"id": 4, "nombre": "Felipe"},
]

for usuario in usuarios: #Llamamos solo el nombre de cada usuario
    print(usuario["nombre"])