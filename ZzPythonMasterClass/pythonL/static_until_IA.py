"""
This is a new project impulsed and designed by @JanoBourian - @Supermath33 and
The Static Until IA project.
This document present an abstract of python, showing the most import information
according the basic course, the requeriments for software development and
artificial intelligence (final tesis).
I waited with patience and hope this moment. Is time to burded.
"""

#Introduction

"""
Autor: Francisco González Antonio [@JanoBourian]
Empresa: @Supermath33 - The Static Until IA project

Este resumen contiene los temas:
    - Números
    - Textos
    - Índices y slicing
    - Listas
    - Entrada y conversión de datos con input(), int() o float()
    - Tipos lógicos
    - Operadores relacionales
    - Operadores lógicos
    - Operador de asignación
    - Operadores para secuencia
    - Sentencias if, elif, else, while, for
    - Tuplas
    - Conjuntos
    - Diccionarios
    - Pilas y Colas (Que no son propias del lenguajes)
    - Tipos y conversión de cadenas
    - Entrada de datos
    - Salida de datos
    - Scripts
    - Programación de funciones:
        * Retorno de valores
        * Argumentos y parámetros
        * Recursividad
    - Manejo de excepciones
    - Iteradores y generadores
    - Docstring (Documentar el código)
    - Copia superficial y profunda de variables
    - Evaluar, ejecutar y compilar cadenas

Para la elaboración de este resumen se utilizaron las siguientes fuentes
que usted puede consultar:

Recursos web:

https://uniwebsidad.com/libros/python?from=librosweb
https://python-para-impacientes.blogspot.com/p/indice.html
https://pythonista.io/cursos/py101
https://www.w3schools.com/python/

Cursos online:

https://www.udemy.com/python-curso-completo/learn/v4/content
https://www.udemy.com/python-3-al-completo-desde-cero/learn/v4/content

Libros/manuales que circulan en la web (Sin referencia):

Ingeniería informática, Procesadores de lenguaje. Python: Conceptos básicos.
Manual de python3. Argentina.
Libro de Inmersión en Python.
Python Para Todos.

NOTA: Durante el desarrollo de este trabajo se anexaron notas importantes sobre
el desarrollo de scripts en python. Recuerda que este es un resumen definitivo
basado en la experiencia de los desarrolladores y sus trabajos previos.
"""

#BASIC TOPICS

print("Hello World!")
print("""Esto es un mensaje \ncon secuencias de escape y \\ cosas especiales
que utiliza varias lineas \n\n \t
para presentarse """)
print(r"Línea en crudo que imprime c:\n todo lo que se \" ' escriba")
input() #Espera hasta un enter pon pantalla

"""
Existen tres tipos de variables básicas:
int
float
str
Y se puede hacer conversión entre ellas. 
"""

#TIPO DE DATOS: Números

print(3 + 2)
print(3 - 2)
print(3*2)
print(3/2)
print(3%2)
print(3**2)
print(3//2)

#Complejos

c1 = 4 + 3j #Complejo escrito de manera explícita
c2 = complex(2 ,-3) #Genera un complejo

print(c1)
print(type(c1))

print(c2)
print(type(c2))

#Pequeña función para generar complejos
#La función retorna un valor. Para trabajar con él se debe asignar a una var

def crear_complejo():
    a = float(input("Ingrese la parte real: "))
    b = float(input("Ingrese la parte compleja: "))
    # c3 = complex(a,b)
    return complex(a,b) #también funciona return c3 con c3 = complex(a,b)

c3 = crear_complejo()

#Operaciones con complejos

print(c2)
print(c2 + c1) #Suma de complejos
print(c1*c2) #Multiplicación de complejos
print(c1 == c2)
print(c1.conjugate()) #Complejo conjugado
print(abs(c1)) #Valor absoluto de un complejo (Observar la función abs())
print(c1.real) #Parte real (método de los complejos)
print(c2.imag) #Parte imaginaria (Método de los complejos)

#Para realizar cambios de base, funciones predeterminadas en python
#Ojo: bin(num) retorna un str, sin embargo 0x29 retornará un entero

num = 25
print(bin(num))
print(oct(num))
print(hex(num))

#ahora hagamos una conversión

print(0b101010101) #Valor binario convertido a decimal
print(0x25) #Valor hexadecimal a decimal

#TIPO DE DATOS: TEXTO
#La forma correcta de presentar cadenas de textos es usando print

print('Hola mundo')
'Hola mundo 2'
print("Hola \"Mundo\"") #La diagonal invertida permite imprimir comillas dobles
print('Hola "Mundo" ') #O podemos alternar entre comillas simples y dobles

#Con tres comillas simples se imprimen varias líneas
print(""" Las cadenas
al igual que los numeros son datos
por lo cual se puede asignar a una variable""")

#Con una r antes de la cadena esta se imprime en crudo
print(r"C:\nombre\directorio")

"""
Verificar el uso de las siguientes funciones:

ord() devuelve el ordinal entero del carácter indicado
chr() devuelve el carácter (Unicode) que representa el número indicado
type() devuelde el tipo de dato de una variable
upper() devuelve una cadena en mayúscula
lower() devuelve una cadena en minúsculas
len() devuelve el tamaño de una cadena

Verificar el uso de los siguientes métodos para cadenas:

cadena.capitalize() devuelve una copia de la cadena con el primer caracter en mayúscula
cadena.center(width) devuelve la cadena centrada en una cadena de longitud width. Se rellena con espacios
cadena.count(sub, start, end) devuelve cuántas veces aparece sub en la cadena. start y end son opcionales
cadena.endswith(sufijo, start, end) devuelve Ture si la cadena finaliza/termina con el sufijo indicado
cadena.expandtabs(tabsize) devuelve una copia de la cadena con todos los tabuladores expandidos.
                           si no se indica el paso se toma como 8 espacios.
cadena.find(sub, start, end) devuelve el menor índice de la cadena para el que sub se encuentre, de tal modo
                             que sub se encuentre contenido en [start, end)
cadena.find(sub, start, end) como find pero lanza ValueError si no se encuentra
cadena.isalpha() devuelve True si todos los caracteres en la cadena son alfabéticos
cadena.isalnum() devuelve True si todos los caracteres en la cadena son alfanuméricos
cadena.isdecimal()
cadena.isdigit()
cadena.isnumeric() devuelven True si todos los caracteres son números
cadena.isspace() devuelve True si todos los caracteres son espacios en blanco
cadena.islower()
cadena.isupper() devuelve True si todos los caracteres son minúsculas o mayúsculas
cadena.istitle() Devuelve verdadero (True) si el primer carácter de la cadena es mayúsculas y el resto minúsculas
                 o en el caso de que haya palabras separadas por espacios en blanco que cumplan la misma regla.
cadena.join(seq) devuelve una cadena formada por la concatenación de todo los elementos de la secuencia seq
                 ej.: '*'.join(cadena)
cadena.ljust(width) devuelve la cadena justificada a la izquierda en una cadena de longitud width
cadena.lstrip() devuelve una copia de la cadena con el espacio inicial eliminado.
cadena.replace(old, new, maxsplit) devuelve una copia de la cadena en la que se han sustituido todas las apariciones
                                   de old por new. maxsplit nos indica cuántas de las primeras apariciones se modificarán
cadena.rfind(sub, star, end) devuelve el índice máximo de la cadena para el que se encuentra la subcadena sub
cadena.rindex() como rfind() pero lanza ValueError si no se encuentra sub
cadena.rjust(width) devuelve la cadena justificada a la derecha en una cadena de longitud width
cadena.rstrip() devuelve una copia de la cadena con el espacio final suprimido
cadena.split(sep, maxsplit) devuelve una lista de las palabras de la cadena, usando sep como delimitador de las palabras.
                            Si se indica maxsplit, se devolverán como mucho maxsplit valores (el último elemento contendrá el resto de la cadena).
                            Si no se especifica sep o es None, cualquier espacio en blanco sirve de separador.
cadena.splitlines(keepends) devuelve una lista de las líneas de la cadena, dividiendo por límites de línea.                            
cadena.swapcase() devuelve una copia de la cadena con las mayúsculas pasadas a minpusculas y viceversa.
cadena.strip() devuelve una copia de la cadena con el espacio inicial y final suprimido

Con .split() convertimos una cadena a lista
con .join() es posible convertir una lista a cadena
"""

#Se admiten caracteres de escape y concateación de cadenas, sin embargo las cadenas son inmutables
print("Hola, qué ha pasado?\n" + "Estas de acuerdo?\n" + "Tengamos en mente\n")

#Las cadenas se pueden multiplicar para reproducirlas varias veces

var = "Hola, cómo estás?"
var2 = "Pensemos en la suma de caracteres"

print(var + var + " " + var2 + var2)
print(2*var)

s = "Una cadena " "compuesta de " "tres cadenas"

print(s)

print(var, end="*") #Para indicar como termina la impresión de la cadena


#ÍNDICES Y SLICING (múltiples índices) DE UNA CADENA
#Cadena de caracteres no se pueden sustituir los elementos, es inmutable

palabra = "0123456789abcdefghijklmnopqrstuvwxyz"

print(palabra[0])
print(palabra[0:4])
print(palabra[-1])
print(len(palabra))
print(palabra[0:len(palabra)])

#Slicing: Múltiples índices

print(type(len(palabra)))

print(palabra[0:])
print(palabra[:36])
print(palabra[:4] + palabra[4:])
print(palabra[:1000000])
print(palabra[10000000:])

#CADENAS Strings

def acceso(var, contrseña):
    if var == contraseña:
        print("Bienvenido")
    else:
        print("Acceso Denegado")

contraseña = "3.uyei18903yhON"
var = input("Ingresa la contraseña: ")
acceso(var, contraseña)

#LISTAS

"""
Métodos en listas:

lista.append() este metodo permite agregar nuevos elementos a una lista
lista.extend() a diferencia de append() con ete método podemos agregar una lista  y cada elemento
               de dicha lista se agregara como un elemento independiente a lista
lista.remove() remueve un elemento que se le pase como parámetro en la lista que se esté aplicando
lista.index() devuelve el número de indice del elemento que le pasemos por parámetro
lista.count(sub) devuelve cuántas veces aparece sub en la cadena. 
lista.reverse() invierte los elementos de una lista
lista.clear() remueve todo los ítems en cadena
lista.copy() crea una copia de la lista
lista.insert(index, object) inserta object before index
lista.pop(index) remueve y retorna item at index (por defecto el último)
lista.sort (key = None, reverse = False) ordena según sea el caso. Ordenamiento rápido
"""
#Para crear una lista vacía utilizamos
lista = list()

#Para agregar al final de una lista utilizamos .append(qué queremos agregar)

var.append("Esto es agregado con append")
print(var)

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

print(letras)
print(letras[0])

letras[:3] = ['A', 'B', 'C']

print(letras)

#Listas anidadas, antes ya lo habíamos hecho

var[0] = letras
var[1] = var
var[4] = numeros
var[5] = datos
print(var)

a1 = [1,2,3]
a2 = [4,5,6]
a3 = [7,8,9]
matriz = [a1,a2,a3]
print(a1)
print(a2)
print(a3)
print(matriz)
print(matriz[0][0])

#Slices

numeros = [0,1,2,3,4,5,6,7,8,9,10]
print(numeros[1])
parte1 = numeros[3:6]
print(parte1)

if numeros[10] == numeros[-1]:
    print("Es verdad que numeros[10] == numeros[-1]")
else:
    print("Es verdad que numeros[10] != numeros[-1]")

print(numeros[0:len(numeros)])
print(numeros[-11:-1])
print(numeros[-11:])
print(numeros[0: :2])

print(numeros[::-1])#Invertir la lista

#Borrar con del

del numeros[3:6]
print(numeros)

numeros[3:4]=[3,4,5, numeros[3]]
print(numeros)

#LECTURA POR TECLADO "input"

valor = input()
print(type(valor))

valor = input()
print(type(valor))

valor = input()
print(type(valor))

valor = int(input("Introduce un valor entero: "))
print(type(valor))

valor = float(input("Ingresa un flotante: "))
print(type(valor))

#OPERADORES RELACIONALES

print(3 == 2)
var = True
var = False
print(var)

#Funciones

for i in range(0,10):
    print("hola", end= "*")
    print(f"{i}")

print("hola" == "HOLA")

#Operadores lógicos

print(not var)

#Conjunción y disyunción

#Une and (y lógico)

d = 0
e = 1
if (d == 0 and e ==1):
    print(True)

#Or (ó lógico)

if (d == 0 or d ==3):
    print(True)

#Expresiones anidadas

""" Orden de precedencia
Primero paréntesis, corchetes y llaves
Expresiones aritméticas:
    exponentes y raíces
    multiplicación y división
    suma y resta
Relacionales de izquierda a derecha
Expresiones lógicas de izquierda a derecha
"""

#Operadores de asignación

a = 0
b = 1
c = 2

#Suma en asignación 
a += 1
print(a)

#Resta en asignación
b-= 1
print(b)

#Multiplicación en asignación
c*=2
print(c)

#división en asignación
b/=2
print(b)

#Módulo en asignación
c%=2
print(c)

#Potencia en asignación

c **=10
print(c)

"""
n = 0
while n < 10:
    if (n%2) == 0:
        print(n, " es par")
    else:
        print(n, " es impar")
    n+=1

a = 2
while a < 1000:
    n = a
    contador = 0
    while n != 1:
        if (n%2) == 0:
            n = n/2
        else:
            n = 3*n + 1
        contador += 1
    print(a, "se reduce a: " ,n, " despues de ", contador, " iteraciones")
    a +=1
"""

#SENTENCIAS

"""Sentencias de control: Condicionales y Bucle"""

#Sentencia if

if True:
    print("Se cumple la condición")

if not True:
    print("Este no se imprimirá")
else:
    print("Pero sí entró al análisis")

# elif es para múltiples (Como switch pero no tanto, jajaja)

"""

if condición:
    expresión
elif condición:
    expresión
elif condición:
    expresión
else:
    expresión de salida (general)

"""

#Ciclo while

"""
while condición:
    expresión

"""

#También podemos utilizar break para romper
#También se puede utilizar continue para seguir con la ejecución
#rompe pero continua

numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0

while (indice < len(numeros)):
    print(numeros[indice])
    indice +=1

for i in numeros: #Recorre el valor de la lista
    print(i)
    
numeros = [1,2,3,4,5,6,7,8,9,10]
indice = 0

for numero in numeros:
    numeros[indice] *= 10
    indice +=1
print(numeros)

numeros = [2,3,5,7,11,13,17,19,23,29]

#Esta es otra forma que se supone mejor.

for indice,numero in enumerate(numeros):
    numeros[indice] *=10
    print("Este es el numero: ", numero)
    print("Este es el indice: " ,indice)
print(numeros)

#Trabajamos con cadenas

cadena = "¡Hola amigos!, ¿Cómo están?"
cadena2 = ""
for caracter in cadena:
    cadena2 += caracter

print(cadena)
print(cadena2)

for i in range(10):
    print(cadena[i])

#Convertir en lista un rango

print(list(range(10)))

#Ejercicios

num_1 = float(input("Ingresa el primer numero: "))
num_2 = float(input("Ingresa el segundo numero: "))

print("""¿Qué deseas hacer?:
1.- Sumar los dos números
2.- Restar los dos números
3.- Multiplicar los dos números
4.- Salir
""")
opcion = input("Paso: ")

if opcion== '1':
    print(num_1 + num_2)
elif opcion == '2':
    print(num_1 - num_2)
elif opcion == '3':
    print(num_1 * num_2)
elif opcion == '4':
    exit()
else:
    print("Opción no válida")

#Ejercicio 2

num_3 = int(input("Ingresa un numero entero impar: "))
while num_3%2 == 0:
    num_3 = int(input("Ingresa un numero entero impar: "))

    
#Ejercicio 3

suma = sum(range(0,100,2))
print(suma)

#Ejercicio 5

numeros = [1,3,6,9]

while True:
    numero = int(input("Ingresa un valor entre 0 y 9"))
    if numero >= 0 and numero <=9:
        break

if numero in numeros:
    print(True)
else:
    print(False)

#Ejercicio 7

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []
indice = 0

for i in lista_2:
    if (i == lista_1[indice]):
        lista_3.append(i)
    indice +=1
print(lista_3)

lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']
lista_3 = []

for letra in lista_1:
    if letra in lista_2 and letra not in lista_3:
        lista_3.append(letra)

"""Colecciones de datos: Tuplas, Conjuntos y Diccionarios, además Pilas y colas """

#Comenzamos con tuplas

"""

Tuplas similares a las listas, pero son inmutables
aceptan indexación y slicing(mostrar desde)
también se acepta len
checar lo métodos de las tuplas

No permite el método append.
"""

tupla_1 = (100, 'Hola', 100, 100, 100, [1,2,3,4,5,6,7,8,9,10], 'Menos cincuenta', -1.34)
print(tupla_1)

print(tupla_1.index(100)) #Nos da la posición
print(tupla_1.count(100)) #Nos indica cuántas veces se repite el valor


lista = [2,46,78,33,568,90,33,9]
print(lista)
lista.sort()
print(lista)

#TUPLAS

#Las tuplas no se pueden modificar. 

tupla_1 = (1,2,3,4,5,6,7,8,9,10)
print(tupla_1)
tupla_2 = 1,2,3,4,5,6,7,8,9,10
print(tupla_2)
tupla_3 = 1,
print(tupla_3)

tupla_1[0]
tupla_1[0:4]
tupla_1[0:4:2]
tupla_4 = (0, "string" , [0,1,2,3])

#CONJUNTOS

"""
Para operaciones con conjuntos:
- diferencia
| unión
& intersección
^ diferencia simétrica
"""

conjunto = set()
print(conjunto)
conjunto = {1,2,3}
print(type(conjunto))
print(conjunto)

#Método add

conjunto.add(4)
print(conjunto)

conjunto.add(0)
print(conjunto)

conjunto.add('A')
conjunto.add('a')
print(conjunto)

#Método discard

grupo = {"Hector", "Juan", "Mario", "Hector", "Juan", "Juan", "Hector"}
print("Hector" in grupo)
grupo.discard("Hector")

#Convertir una lista a conjunto y un conjunto a una lista

l = [1,2,2,2,2,3,4,3,4,5]
print(l)

c = set(l)

print(c)

l = list(c)
print(l)

l = [1,2,2,2,2,3,4,3,4,5]
l = list(set(l))

""" DICCIONARIOS """
#Arreglos asociativos

capitales = dict() #diccionario vacío
identificador = {1: "Ramón", 2:"Julio", 3:"Pedro"}
print(identificador[1])
identificador[1]="Sandra"
del identificador[1]

for i in identificador:
    print(i)

2 in identificador

for clave in identificador:
    print(clave, identificador[clave])

#Metodo correcto para el registro de los diccionarios

for clave, valor in identificador.items():
    print(clave, valor)

personajes = []
a = {"Alejandro" : "Gandalf", "Clase": "Mago", "Raza": "Humano"}
personajes.append(a)
b = {"Claudio": "Legolas", "Clase": "Arquero", "Raza": "Elfo"}
c = {"Pedro": "Gimli", "Clase":"Guerrero", "Raza": "Enano"}
personajes.append(b)
personajes.append(c)

for p in personajes:
    print(p["Clase"], p["Raza"])

#DICCIONARIOS

"""
diccionario.update(): Utilizamos el método update() para actualizar un diccionario
diccionario.keys(): Utilizamoos el método keys() para acceder a las llaves
diccionario.values(): Nos devuelve los valores
diccionario.items(): Nos devuelde una tupla por cada elemento en nuestro diccionario
"""

empleados_dias = { "Juan":20,  "Carlos":50, "Adrián":10, "Ernesto":90}
empleados_comisión = { "Juan": 0.20,  "Carlos": 0.50, "Adrián": 0.10, "Ernesto": 0.90}

empleados_dias["Andrés"] = 0

#creación de diccionario

nuevos = dict([["Luis", 20],["Karla", 60]])

#Para agregar al diccionario

empleados_dias["Luis"] = 20
empleados_dias["Karla"] = 60
del empleados_dias["Luis"]

#Para actualizar varios elementos

empleados_dias.update({"Julio": 30, "Pedro": 20, "Alejandro" : 30})
empleados_dias.update({"Juan": 30, "Carlos": 20, "Alejandra" : 30})

#Para recorrer un diccionario

#Aquí imprime las llaves
for nombre in empleados_dias:
    print(nombre)

#Aquí accedemos con la llave al valor

for nombre in empleados_dias:
    print(empleados_dias[nombre])

""" PILAS Y COLAS """

#PILAS

pila = [3,4,5]
pila.append(6)
pila.append(7)
print(pila)

#Sacar elementos por el final
pila.pop()
pila.append(8)
print(pila)

#COLAS

from collections import deque

cola = deque()
cola = deque(["Hector", "Juan", "Mateo", "Pedro"])

cola.append("Jaime")
cola.append("Tino")

cola.popleft()

"""
Guardar en archivo .csv

Argumentos para open
a = anexa información
w = borra y escribe de nuevo la información (sobreescribe)

numero = int(input("Introduce el numero: "))
archivo.write('numero = % s' %numero)


archivo = open("archivo.csv", "w")

texto = input("Introduce texto: ")
fecha = input("Introduce fecha: ")

archivo.write(texto)
archivo.write(",")
archivo.write(fecha)

archivo.close()
"""

#Aquí hay otro

"""
Guardar en archivo .txt



file = open("datos.txt", "a")
lista = open("lista.txt", "a")
texto = input("Introduce la nota: ")

file.write(texto)
file.write("\n")
file.close()

n = int(input("Cuántos deportes deseas anexar?: "))
deportes = list()
for i in range (n):
    deporte = input("Deporte: ")
    deportes.append(deporte)
    lista.write(deporte)
    lista.write(" ,")
print(deportes)
lista.close()

"""

#Vamos con Scripts y Formatos
"""
cadena.format(): Para ingresar valores dentro de una cadena
"""

v = "Un primer texto"
n = 10
c = " {}, un segundo texto y el número {}".format(v,n)
print(c)

c = " {1}, un segundo texto y el número {0}".format(v,n)
print(c)

c = " {b}, un segundo texto y el número {a}".format(b=v,a=n)
print(c)

#Alinear un texto con format

alinear = "Quiero alinear esta linea a la derecha"
print("{:>100}".format(alinear)) #Así sí es posible
print("{:>30}".format("alinear")) #Alinear a la derecha
print("{:30}".format("alinear")) #Alinear a la izquierda
print("{:^30}".format("alinear")) #Alinear al centro
print("{:.5}".format("alinear")) #Truncar
print("{:>30.3}".format("palabra"))

#Formateo de número enteros
#Formatear la salida de números alineados y además rellenados con algún valor


for i in range (3):
    print("{:>50}".format(i))

lista = [1,10,100,1000,10000]

for i in lista:
    print("{:>50}".format(i))

for i in lista:
    print("{:*>50}".format(i))

decimales = [3.14256, 2345.23456, 876369.090]

for i in decimales:
    print("{:09.7f}".format(i))

"""
Ahora trabajamos con funciones
"""

#Función sin argumentos

def saludar():
    print("Hola mundo")
    print("Aquí estamos en la función saludar")

#Función que ponga la tabla del número cinco

def dibujar_tabla():
    x = int(input("De que número deseas la tabla: "))
    for i in range(10):
        print(x, "*", (i+1), " = ", x*(i+1))

def test():
    o = 5
    print(o)

test()
o = 10
print(o) # "o" Son dos variabes completamente diferentes

#Retornar valores

def test():
    return "Retorno de cadena de texto" #LA función termina en return
print(test())
c = test()
print(c)

def test():
    return [0,1,2,3,4,5]

print(test())
print(test()[1])

def test():
    return "Una cadena", 20, [0,1,2,3]

test() #Esta es una tupla
c,n,l = test() #Asignación múltiple
print(c)
print(n)
print(l)

"""
Se pueden pasar por valor.
Por referencia directa a través de su nombre y valor
"""

#Asignar valores por defecto

def resta( a= None, b = None):
    if (a== None or b == None):
        print("Error, faltan valores")
        return
    return a - b

#Para recorrer obteniendo el índice y el valor en lista
lista = [0,1,2,3,4,5,6,7,8,9]

def doblar_valores(numeros):
    auxiliar = list()
    for i, n in enumerate (numeros):
        print("El índice es: ", i , " el valor de esa entrada es: ", n)
        auxiliar.append(n)
        numeros[i] *=2
        


        
doblar_valores(lista)
lista
doblar_valores(lista[:])

#Paso por referencia (Lista) No se puede mover.
#Parámetro iterable

def indeterminados_posicion(*args):
    print(args)

indeterminados_posicion(5,12,"Hola",[1,2,3,4]) #Esto de aquí es una tupla

def indeterminados_posicion(*args):
    for arg in args:
        print(arg)

"""

def indeterminados_posicion(*args):
    lista = list()
    for arg in args:
        lista.append(arg)
    return lista

"""

#Esto será un diccionario
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwargs)

def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg, " ", kwargs[kwarg])

indeterminados_nombre(n=10, l=[1,2,3,4], s="Hola Mundo")

def super_funcion(*args, **kwargs):
    t = 0
    for arg in args:
        t += arg
    print("La suma de los argumentos es" , t)
    for kwarg in kwargs:
        print(kwarg, " ", kwargs)

#Recursividad en funciones


def cuenta_atras(num):
    num -=1
    if num > 0:
        print (num)
        cuenta_atras(num)
    else:
        print("Boooooo!")

#Siempre se cierran todas la funciones

def factorial (num):
    print("Valor inicial de num -->", num)
    if num > 1:
        num = num * factorial (num)
    print("Valor final de num-->", num)
    return num

#Funciones integradas en python.

n = int("10")
f = float("10.5")

c = "Un texto y un numero" + str(10)

#COnverir a binario

bin(10)
hex(10)
int("0b1010",2)
abs(-123)
round(5.4334)
eval("2 + 5") #También soporta variables dentro de la cadena.
len("Hola, mundo")
help()

"""
Manejo de excepciones:
- Errores sintácticos.
"""

l=[0,1,2]
l.pop()
l.pop()
l.pop()

print("Este es el primer número{}/Este es el segundo número{}={}".format(4,4,4/4))

#La idea es crear estado de excepción para que el programa siga ejecutándose
#Excepción es una parte de código que nos permite manejar los errores
#Para evitar

while(True):
    try:
        n = float(input("Introduce el número"))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
        #break
    except:
        print("Ha ocurrido un error al introducir los datos")
    else:
        print("Todo ha funcionado correctamente: ")
        break
        #Aquí iría otro break si lo quitamos del try:
    finally: #Se ejecuta al final de todo try
        print("Final de la iteración del while")

#Múltiples excepnciones

try:
    n = input("Introduce un número:")
    5 / n
except Exception as e: #Guardamos excepción genérica en la variable e
    print("Error")
    print( type(e).__name__ )

try:
    n = float(input("Introduce un número:"))
    5 / n
except Exception as e: #Guardamos excepción genérica en la variable e
    print("Error")
    print( type(e).__name__ )

#ValueError, TypeError, ZeroDivisionError
#Podemos manejar la introducción de datos con los errores.

"""
Invocación de excepciones
"""

def mi_funcion(algo = None):
    if algo == None: #algo is None
        print("Error! no se permite un valor nulo")

def mi_funcion(algo = None):
    if algo == None: #algo is None
        raise ValueError("Error!no se permite un valor nulo")

def mi_funcion(algo = None):
    if algo == None: #algo is None
        raise ValueError("Error!no se permite un valor nulo")
    except ValueError:
        print("No se permite!")
    #sacar el identificador del error
























