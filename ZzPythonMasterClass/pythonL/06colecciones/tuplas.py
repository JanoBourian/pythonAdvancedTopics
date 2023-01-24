##Las tuplas son inmutables. 
tupla = (3,"hola", [3,4,5,6,"Hola"])
for valor in tupla:
    print(valor)

len(tupla)

##Podemos averiguar si hay un valor dentro de la tupla y de existir nos regresa el index
tupla.index("hola")
tupla[tupla.index("hola")]
tupla.index(10) ##Esto nos dará error

##Ahora vamos a contar cuantas veces aparece un elemento y esto se puede combinar con .index()
tupla.count(10)

if(tupla.count(10)):
    print("Sí es un elemento")
    tupla.index(10)
else:
    print("No es un elemento")

def encontrarElemento(a, tupla):
    if(tupla.count(a)):
        print("Sí es un elemento")
        print("El index es: ", tupla.index(a))
    else:
        print("El elemento: ", a," no es un elemento de la tupla")

encontrarElemento(1, (1,3,5,"hola"))





