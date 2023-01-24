## Recordemos algo importante sobre las listas
dir([])
pila = [1,2,3,4,5]
def agregarElementos(*args):
    for arg in args:
        pila.append(arg)

agregarElementos(7,8,9,10)
pila

pila.pop()
pila
pila.pop()
pila

##Entonces para emular las pilas no es necesario más que utilizar append() para las entradas y pop() para las salidas

