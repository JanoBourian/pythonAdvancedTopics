### Hagamos un format avanzado

#Espacios a la izquierda
print("{:>30}".format("palabra"))

#Espacios a la derecha
print("{:30} {}".format("palabra", "saludo"))

#Alineamiento con espacios totales
print("{:^30}".format("Palabra"))

## Si queremos agregar truncamiento agregamos un punto y el total de elementos
print("{:^30.5}".format("Palabra"))

#Formateo de números con espacios vacíos
print("{:4}".format(10))
print("{:4}".format(100))
print("{:4}".format(1000))

##Formateo de números rellenados con ceros
print("{:04}".format(10))
print("{:04}".format(100))
print("{:04}".format(1000))