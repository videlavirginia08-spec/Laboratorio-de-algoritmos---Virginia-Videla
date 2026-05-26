"""
4. Cargar una lista con 5 elementos enteros. Ordenar de menor a mayor y
mostrarla por pantalla, luego ordenar de mayor a menor e imprimir
nuevamente.
"""

lista = []

for x in range(5):
    valor = int(input(f"Escriba el valor numero {x+1}: "))
    lista.append(valor)

for i in range(4):

    for k in range(4 - i):

        if lista[k] > lista[k + 1]:

            aux = lista[k]
            lista[k] = lista[k + 1]
            lista[k + 1] = aux

print("Lista ordenada de menor a mayor ")
print(lista)

for i in range(4):

    for k in range(4 - i):

        if lista[k] < lista[k + 1]:

            aux = lista[k]
            lista[k] = lista[k + 1]
            lista[k + 1] = aux

print("Lista ordenada de mayor a menor ")
print(lista)


