#Keywords Args

def get_product(**datos):
    print(datos["id"], datos["name"])

get_product(id="23", 
            name="Iphone", 
            desc="Esto es un Iphone")