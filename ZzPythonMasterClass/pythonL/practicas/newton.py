def funcion(x):
    return  (x**3 + 4*x**2 -10)

def derivada(x):
    return (3*x**2 + 8*x)

## Datos iniciales
x0 = 100000 ## Valor inicial
tol = 10**(-15) ##Tolerancia
i = 1 ## Iteraciones

### Damos la primer iteración
x1 = x0 - (funcion(x0)/derivada(x0))

while(abs(x1-x0)> tol):
    x0 = x1
    x1 = x0 - (funcion(x0)/derivada(x0))
    i += 1

i
x1