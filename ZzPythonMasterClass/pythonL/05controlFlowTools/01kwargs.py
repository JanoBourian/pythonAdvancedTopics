## Básicamente hay tres formas de pasar argumentos a una función:
#   - Convencionales
#   - De tamaño variable
#   - Asociados a un identificador

def imprimir(name, *arguments, **keywords):
    print("Tu nombre es: ", name)
    print("Tus frases célebres son: ")
    for arg in arguments:
        print(arg)
    print("*"*40)
    print("Tus atributos claves son: ")
    for kw in keywords:
        print(kw, " : ", keywords[kw])

imprimir("Alejandra Maldonado")
print("*"*40)
imprimir("Alejandra Maldonado", "Lo hecho está hecho, amigos")
print("*"*40)
imprimir("Alejandra Maldonado", "Lo hecho está hecho, amigos", edad = 25)

##Tiene mayor sentido al realizarlo con clases, pero ahora haremos un ejemplo
def promedio(*arguments) -> str:
    print(promedio.__annotations__)
    total = 0
    for arg in arguments:
        total += arg
    print(total/len(arguments))

promedio(1,2,3,4,5)
