"""
5. Crear y cargar en un lista los nombres de 5 países y en otra lista paralela
la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir
los resultados. Por último ordenar con respecto a la cantidad de habitantes
(de mayor a menor) e imprimir nuevamente.
"""

paises = []
habitantes = []

for x in range(5):

    nombre = input(f"Escriba el nombre del país {x+1}: ")
    paises.append(nombre)

    cantidad = int(input(f"Escriba la cantidad de habitantes de {nombre}: "))
    habitantes.append(cantidad)

for i in range(4):

    for k in range(4 - i):

        if paises[k] > paises[k + 1]:

            auxpais = paises[k]
            paises[k] = paises[k + 1]
            paises[k + 1] = auxpais

            auxhab = habitantes[k]
            habitantes[k] = habitantes[k + 1]
            habitantes[k + 1] = auxhab

print("Paises ordenados alfabéticamente:")

for x in range(5):
    print(paises[x], habitantes[x])

for i in range(4):

    for k in range(4 - i):

        if habitantes[k] < habitantes[k + 1]:

            
            auxhab = habitantes[k]
            habitantes[k] = habitantes[k + 1]
            habitantes[k + 1] = auxhab

            auxpais = paises[k]
            paises[k] = paises[k + 1]
            paises[k + 1] = auxpais

print("Paises ordenados por cantidad de habitantes:")

for x in range(5):
    print(paises[x], habitantes[x])


