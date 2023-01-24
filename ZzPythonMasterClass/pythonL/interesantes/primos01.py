#Función que descarta para quedarnos con los primos
def generarPrimos(n):
    for i in range(2,n):
        for j in range(2,i):
            if(i%j == 0):
                print(i, " = ", j, " * ", i//j)
                primos.remove(i)
                break
    print(primos)

## Atributos globales
n = int(input("Introduce hasta qué número quieres conocer el primo (de 2 en adelante): "))
primos = list(range(2,n))

## Llamado de la función
generarPrimos(n)
