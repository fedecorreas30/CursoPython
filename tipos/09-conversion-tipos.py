z = input("")

# int()
# str()
# float()
# bool() ## evalua en truthy o flasy ("", 0, none son los únicos valores que evalúan en false)

print(bool(""))
print(bool("0"))  # da true porque es un string que contiene el valor 0
print(bool(None))
print(bool(" "))  # da true porque contiene un espacio en el string
print(bool(0))
