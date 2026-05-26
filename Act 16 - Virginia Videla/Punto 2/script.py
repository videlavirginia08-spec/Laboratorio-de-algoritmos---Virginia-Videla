"""
2. Una empresa registra los nombres de sus 5 vendedores y el total de ventas
realizadas por cada uno en un mes. Cargar los nombres y ventas en dos
vectores paralelos, ordenar los datos de mayor a menor según las ventas,
imprimir la lista ordenada con nombre y monto de la venta, e informar quien fue
el que menos vendió de los 5 empleados.
"""

nombres = []
ventas = []

for x in range(5):
    nombre = input(f"Escriba el nombre del vendedor {x+1}: ")
    venta = int(input(f"Escriba el total vendido por {nombre}: "))

    nombres.append(nombre)
    ventas.append(venta)

for x in range(5):
    for k in range(x + 1, 5):

        if ventas[x] < ventas[k]:

            auxventa = ventas[x]
            ventas[x] = ventas[k]
            ventas[k] = auxventa

            auxnombre = nombres[x]
            nombres[x] = nombres[k]
            nombres[k] = auxnombre

for x in range(5):
    print(nombres[x], ventas[x])

print("El empleado que menos vendió fue: ")
print(nombres[4], ventas[4])


