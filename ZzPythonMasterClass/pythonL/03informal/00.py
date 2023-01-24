###Strings
##Algunas cosas con cadenas de texto
frase = "Esta es una frase con la que iniciaremos"
print(frase[99:])
##esto no funciona
##print(frase[99])
print(frase[:99])
## y aquí vemos el primer método para los strings
print(len(frase))

###Listas
##Las listas permiten hacer slicing para editarlas
letras = ['a','b','c','d','e','f']
print(letras)
letras[:3]=['A','B','C']
print(letras)
print("El tamaño de letras es de: " + str(len(letras)))

##Cosas importantes de esto:
lista = eval(input())
## Cuando te lo solicite pega esto --> [1,2,3,4,5,6,7,8]
print(lista)

numero = float(input("Introduce un número flotante: "))
print(numero)
