from time import time
import random


def medir_tiempo(name):
    def wrapper(function):
        def wrapper_2(*args, **kwargs):
            # print("Comenzando la ejecución...")
            inicio = time()
            resultado = function(*args, **kwargs)
            print(
                f"Finalizando la ejecución con {name} en {time() - inicio} segundos")
            return resultado
        return wrapper_2
    return wrapper


@medir_tiempo("for")
def generar_aleatorios(total_aleatorios):
    for i in range(total_aleatorios):
        random.random()


@medir_tiempo("while")
def generar_aleatorios2(total_aleatorios):
    i = 0
    while (i < total_aleatorios):
        random.random()
        i += 1


generar_aleatorios(10)
generar_aleatorios2(10)
