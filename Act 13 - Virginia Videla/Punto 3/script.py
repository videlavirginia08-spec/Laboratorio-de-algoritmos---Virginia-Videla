#3. Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes &quot;Lista 1 mayor&quot;, &quot;Lista 2 mayor&quot;, &quot;Listas iguales&quot;) Tener en cuenta que puede haber dos o más estructuras repetitivas en un algoritmo.

lista1 = 0
lista2 = 0

print("Cargar valor de la lista 1")
for x in range(15):
    valor1 = int(input(f"Escriba el valor {x+1}: "))
    lista1 += valor1

print("Cargar valor de la lista 2")
for x in range(15):
    valor2 = int(input(f"Escruba el valor {x+1}: "))
    lista2 += valor2

if lista1 > lista2:
    print("Lista 1 mayor")

else:
    if lista2 > lista1:
        print("Lista 2 mayor")

    else:
        print("Listas iguales")