# a(b) -> c
def funcion_a(funcion_b):
    def funcion_c():
        print("Before ejecution...")
        funcion_b()
        print("After ejecution...")
    return funcion_c


@funcion_a
def saludar():
    print("hola desde una función")


saludar()

"""
Otro caso más flexible
"""


def my_custom_decorator(function):
    def wrapper(*args, **kwargs):
        print("Before ejecution...")
        resultado = function(*args, **kwargs)
        print("After ejecution...")
        return resultado
    return wrapper


@my_custom_decorator
def suma(a, b):
    return a + b


print(suma(2, 3))


@my_custom_decorator
def saludar2():
    print("hola desde el decorador con argumentos")


saludar2()
