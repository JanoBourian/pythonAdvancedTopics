## Son colecciones desordenadas de elementos únicos utilizados para hacer pruebas de pertenencia
## a grupos y eliminación de elementos duplicados

conjunto = set()
conjunto

## Pero si incluimos elementos debemos crearlo entre llaves
conjunto = {1,2,4}
conjunto

## Ahora veamos porque son elementos únicos, y además son desordenados
conjunto.add(4)
conjunto.add(4)
conjunto.add(4)
conjunto.add(4)
conjunto

##Pertenencia o no pertenencia a un conjunto 
4 in conjunto
4 not in conjunto

## Recordemos algo sobre "in" & "not in"
valor = False
not valor
if(not valor):
    print("Hola")
else:
    print("Valor era falso")

## Ahora hagamos una conversión de listas a conjuntos

lista = [1,2,2,3,4,5,5,6,6,6,6,3,2,2,2,3,3,4,5]
lista
conjunto = set(lista)
conjunto
lista

## También se puede hacer con cadenas de texto

cadena = "Era una vez una frase con letras repetidas"
conjunto = set(cadena)
conjunto
dir(conjunto)