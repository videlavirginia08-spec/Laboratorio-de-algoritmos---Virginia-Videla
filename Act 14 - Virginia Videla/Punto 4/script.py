#4. Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float) Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.

alturas = []

for x in range(5):
    valor = float(input(f"Escriba la altura de la persona {x+1}: "))
    alturas.append(valor)

suma = 0

for x in range (5):
    suma += alturas[x]

promedio = suma / 5

altas = 0
bajas = 0

for x in range(5):
    if alturas[x] > promedio:
        altas += 1
    elif alturas[x] < promedio:
        bajas += 1

print(f"El promedio de todas las alturas es: {promedio}")
print(f"La cantidad de personas mas altas que el promedio es: {altas}")
print(f"La cantidad de personas mas bajas que el promedio es: {bajas}")



