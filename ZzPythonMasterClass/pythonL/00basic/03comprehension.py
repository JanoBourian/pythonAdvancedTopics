def getSquare():
    newList = []
    for x in range(20):
        newList.append(x*x)
    print(newList)
    
def getOther():
    lst = [9,2,3,4,56,7,8,9,4,5,6,8,2,3,4,24,5]
    lista = [i for i in lst if i%2==0] #Este es un buen ejemplo de compresión de listas
    #No se me ocurre otro
    print(lista)

getSquare()
print("Hola mundo")
getOther()