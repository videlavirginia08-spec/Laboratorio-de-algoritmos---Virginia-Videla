"""
2. Realizar un programa que pida la carga de dos listas numéricas enteras
de 4 elementos cada una. Generar una tercera lista que surja de la suma
de los elementos de la misma posición de cada lista. Mostrar esta tercera
lista.
"""

l1 = []
l2 = []
l3 = []

for x in range(4):
    valor1 = int(input(f"Escriba el valor de la lista 1 posición {x+1}: "))
    l1.append(valor1)

    valor2 = int(input(f"Escriba el valor de la lista 2 posición {x+1}: "))
    l2.append(valor2)

for x in range(4):
    suma = l1[x] + l2[x]
    l3.append(suma)

print("Tercera lista:")
print(l3)

