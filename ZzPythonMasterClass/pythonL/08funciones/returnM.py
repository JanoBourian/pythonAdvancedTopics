def prueba():
    return "Hola", 12, [], {}, ()

prueba()

texto, numero, lista, dic, conjunto = prueba()

## OJITO AQUí
"""
Los tipos simples se pasan por valor: enteros, flotantes, cadenas, lógicos
los tipos compuestos se pasan por referencia: listas, diccionarios, conjuntos
"""