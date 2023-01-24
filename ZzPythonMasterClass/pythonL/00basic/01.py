### En algunos casos, en el sentido de las necesidades programador-usuario se deben
### copiar los valores de los arrays para evitar que se modifiquen 'intencionalmente'

##Hagamos un poco de recursión
#Factorial

def factorial(n):
    if(n>0):
        return n*factorial(n-1)
    else:
        return 1

def solicitarFactorial():
    n = int(input("De qué número quieres el factoria?: "))
    factor = factorial(n)
    print(factor)

des = 1
while des!=0:
    solicitarFactorial()
    des = int(input("0 para salir, otro para continuar: "))
input()
