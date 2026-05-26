#1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

mayores7 = 0
menores7 = 0

for i in range (10):
    valor = int(input("Escriba la nota de un alumno"))
    
    if valor>=7:
        mayores7 = mayores7 + 1

    else:
        menores7 = menores7 + 1


print(f"La cantidad de alumnos con nota mayor a 7 son: {mayores7}")
print(f"La cantidad de alumnos con nota menor a 7 son: {menores7}")

