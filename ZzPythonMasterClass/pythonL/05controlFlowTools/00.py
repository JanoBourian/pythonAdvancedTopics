x = int(input("Ingresa un entero y trabajemos con if: "))
if x < 0:
    print("Es un número negativo")
elif x == 0:
    print("Es un cero")
else:
    print("Es un numero positivo")

## Los For ya los conocemos, sin embargo es tiempo de tratarlos

nombres = ['Juan', 'Paco', 'Pedro', 'Alberto']

for nombre in nombres:
    print(nombre)

#Ahora haremos dos cosas equivalentes

for indice in range(len(nombres)):
    print("El nombre "+ str(indice) + " es: " + nombres[indice]) 

for indice, nombre in enumerate(nombres):
    print(indice)
    print(nombre)
    print("*")

frase = "Esta es una frase que nos gusta mucho y por eso la mencionamos"
palabras = frase.split()
print(frase)
print(palabras)
for i, w in enumerate(palabras):
    print( str(i) + " " + w + " " + str(len(w)))

## Ahora hagamos algo interesante

primos = list(range(2,10))
print(primos)
for i in range(2,10):
    for j in range(2,i):
        if(i%j == 0):
            print(i, " no es un numero primo porque ", i , " = ", j , "*",i//j )
            primos.remove(i)
            break
print(primos)

##Veamos algunas cosas interesantes de las funciones:
def ask_ok(prompt, retries=4, reminder="Please try again"):
    while True:
        ok = input(prompt)
        if ok in ("y","ye", "yes"):
            return True
        if ok in ("n","no","nope"):
            return False
        retries -=1
        if retries < 0:
            raise ValueError("invalid user response")
        print(reminder)

##Veamos un poco de **kwargs y *args, pero en otro archivo.
