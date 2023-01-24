## Función necesaria para realizar las operaciones
def funcion(x):
    return (x**3 + 4*x**2 -10)

##Datos iniciales
tol = 10**(-15) ##Tolerancia
i = 1          ##Iteraciones

##Valores iniciales
a = -2
b = 5
m = (a+b)/2

##Evaluaciones iniciales

fa = funcion(a)
fb = funcion(b)
fm = funcion(m)

print("{:^10d} {:^10.7f} {:^10.7f} {:^10.7f} {:^10.7f} {:^10.7f} {:^10.7f} {:^10.7f}\n".format("i","a","m","b","fa","fm","fb","abs(a-b)"))
while(abs(a-b)>tol):
    print("{:^10d} {:^10.7f} {:^10.7f} {:^10.7f} {:^10.7f} {:^10.7f} {:^10.7f} {:^10.7f}\n".format(i,a,m,b,fa,fm,fb,abs(a-b)))
    if(fa*fm > 0):
        a,m,b = m,(a+b)/2,b
        fa = funcion(a)
        fb = funcion(b)
        fm = funcion(m)
    else:
        a,m,b = a,(a+b)/2,m
        fa = funcion(a)
        fb = funcion(b)
        fm = funcion(m)
    i += 1


m