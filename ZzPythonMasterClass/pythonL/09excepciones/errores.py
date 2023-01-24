"""
La sintaxis básica es
try:
    prueba todo esto
except:
    Y si no es válido lo anterior manda un aviso 
else:
    En caso de que la prueba sea correcta se ejecuta esto
finally:
    Y esto siempre se ejecuta
"""

##Múltiples excepciones
try:
    n = float(input("Introduce un número divisor: "))
    5/n
except TypeError:
    print("No se puede dividir el número entre una cadena")
except ValueError:
    print("Debes introducir una cadena que sea un número")
except ZeroDivisionError:
    print("No se puede dividir por cero, prueba otro número")
except Exception as e:
    print("Ha ocurrido un error no previsto", type(e).__name__ )

## uso de raise
def mi_funcion(algo=None):
    try:
        if algo is None:
            raise ValueError("Error! No se permite un valor nulo")
    except ValueError:
        print("Error! No se permite un valor nulo (desde la excepción)")

mi_funcion()

try:
    resultado = 10 + 50
except Exception as e:
    print(type(e).__name__)
else: 
    print("Pasó la prueba")
    resultado
finally:
    print("Siempre me ejecuto")




