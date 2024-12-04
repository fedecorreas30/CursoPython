# and, or, not

gas = False
encendido = False
edad = 18

# Se ejecuta primero lo que está entre parentesis
if not gas and (encendido or edad > 17):
    print("Puedes Avanzar")

# En el caso de and sí la primera operación da false python no evalúa la segunda ni las siguientes
# En el caso de or evalúa todas, ya que con una sola que tengamos True nos va alcanzar para que el usuario avance
