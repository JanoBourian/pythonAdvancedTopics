### Para ciertos fines comienza a ser necesario
"""
Recordemos los tipos primitivos que por el momento nos apremian en Python
boolean
byte
list
tuple
dict
complex
float
long
string
int
class
"""
def menu():
    print("""
    0 salir
    1 boolean
    2 list
    3 tuple
    4 dict
    5 complex
    6 float
    7 string
    8 int
    """)
    opcion = int(input("cual es la opcion: "))
    return opcion

def imprimirValor(value):
    for item in value:
        print(item)

def mostrar(des):
    if(des==1):
        value = dir(True)
    if(des==2):
        value = (dir([]))
    if(des==3):
        value = (dir(()))
    if(des==4):
        value = (dir({}))
    if(des==5):
        value = (dir(5+3j))
    if(des==6):
        value = (dir(3.22222))
    if(des==7):
        value = (dir(''))
    if(des==8):
        value = (dir(1))
    imprimirValor(value)

def saludar():
    print("Hola mundo")

def recordar():
    print("Recuerda que con dir(Class) puedes obtener los métodos de forma rápida")

if __name__ == "__main__":
    saludar()
    recordar()
    des = menu()
    while (des!=0 and des<9):
        mostrar(des)
        des=menu()
    print("Fin de la ejecución")

input()
