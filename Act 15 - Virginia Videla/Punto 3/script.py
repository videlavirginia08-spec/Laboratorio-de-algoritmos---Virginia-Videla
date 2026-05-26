"""
3. Solicitar por teclado la cantidad de empleados que tiene la empresa. Crear
y cargar una lista con todos los sueldos de dichos empleados. Imprimir la
lista de sueldos ordenamos de menor a mayor.
"""

sueldos = []

cantidad = int(input("Escriba la cantidad de empleados: "))


for x in range(cantidad):
    valor = int(input(f"Escriba el sueldo del empleado {x+1}: "))
    sueldos.append(valor)

for i in range(cantidad - 1):

    for k in range(cantidad - 1 - i):

        if sueldos[k] > sueldos[k + 1]:

            aux = sueldos[k]
            sueldos[k] = sueldos[k + 1]
            sueldos[k + 1] = aux

print("Sueldos ordenados de menor a mayor:")
print(sueldos)



