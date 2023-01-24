"""
Este documento tiene como finalidad enlistar los métodos, más no trabajar con ellos

upper()
lower()
capitalize()
title()
count() # "Hola mundo".count('mundo') Cuenta las veces que aparece una subcadena
find() # "Hola mundo".find('mundo') Devuelve el índice en donde aparece la subcadena (-1 si no existe)
rfind() "Hola mundo mundo mundo".rfind('mundo')
isdigit() # True si la cadena es de números
isalnum() # True si la cadena es todo número o caracteres alfabéticos
isalpha() # True si toda la cadena son caracteres alfabéticos
islower()
isupper()
istitle()
isspace()
startswith() #True si comienza con la subcadena "Hola mundo".startswith("Mola")
endswith()

split() # Separa la cadena en subcadenas a partir de sus espacios y devuelve una lista
"Hola,mundo,mundo,otra,palabra".split(',') #Podemos indicar el separador

join() #une todos los caracteres de una cadena utilizando un caracter de union
",".join("Hola mundo")

strip() #Borra todos los espacios por delante y detrás de una cadena y la devuelve
"-----Hola mundo---".strip('-') #Se puede especificar otro caracter

replace() #Reemplaza una subcadena de una cadena por otra y la devuelve
"Hola mundo".replace('o','0')
"Hola mundo mundo mundo mundo mundo".replace(' mundo','',4) ## Indicar el límite de veces a reemplazar

"""