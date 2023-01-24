"""
for i in range(10):
    print(i)

lista = [i for i in range(100) if i%2==0]

for j in lista:
    print(j)

a = 0
print(not a)
"""
## Esto es una ventaja, podemos utilizar operadores como: and, or y not

listaUno = [True, False]
listaDos = [True, False]

print("Tabla AND".rjust(15))
for i in listaUno:
    for j in listaDos:
        print(str(i).rjust(5) + " AND " + str(j).rjust(5) + " = " + str(i and j))

print("Tabla OR".rjust(15))
for i in listaUno:
    for j in listaDos:
        print(str(i).rjust(5) + " OR " + str(j).rjust(5) + " = " + str(i or j))
