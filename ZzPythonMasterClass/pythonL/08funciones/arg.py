## Argumentos indeterminados ARGS
## Por posición

def indeterminadosPosicion(*args):
    for arg in args:
        print(arg)

indeterminadosPosicion("Hola", 230.34, [1,2,3,4,5], {'hola':2}, (3,4,5))

## Por nombre {clave:valor} <-- Recuerda Javascript, jajaja

def claveValor(**kwargs):
    print(kwargs)
    for kwarg in kwargs:
        print(kwarg, "=>", kwargs[kwarg])

claveValor(a=5, b="saludo", c=[1,2,3,4,5])


## Por posición y nombre
## primero los indeterminados y luego los de nombre
def ambas(*args, **kwargs):
    for arg in args:
        print(arg)
    for kwarg in kwargs:
        print(kwarg, " => ", kwargs[kwarg])

ambas(1,2,3,4,5,6,7,8, a="name", b="discoLies")

##FUnciones integradas
int()
float()
str()
bin()
hex()
int("numero", "base")
abs()
round()
eval()
len()
help()