#Diccionarios, clave - valor. En otros lenguajes se conocen como arreglos asociativos

vacio  = {}
vacio
type(vacio)
dir(vacio)

#Hagamos un arreglo asociativo
vacio = {
    'name': 'william',
    'lastName': 'mcgregor',
    'edad': 29
}
vacio
vacio['name']
del(vacio['name'])
vacio
vacio['name'] = 'john'
vacio
for item in vacio:
    print(item)

##Ahora para imprimir tanto la clave como el valor

for clave,valor in vacio.items():
    print(clave, " => ", valor)


vacio.items()
