# set signifca grupo o conjunto (no se puede repetir y no está ordenada)
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo =set(segundo)
print(segundo)

print(primer | segundo) # nos dará todos los números
print(primer & segundo) # nos dará los números que coinciden en ambos
print(primer - segundo) # nos dará los elementos que estén en el primero y NO en el segundo
print(primer ^ segundo) # no dará los elementos diferentes de cada set

#Con los set no podemos acceder a los elementos

#Sólo podemos a través de un if dar una orden

if 5 in segundo:
    print("Hola Mundo")