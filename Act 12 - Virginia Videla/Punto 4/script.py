#4. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer: a. La cantidad de valores ingresados negativos. b. La cantidad de valores ingresados positivos. c. La cantidad de múltiplos de 15. d. El valor acumulado de los números ingresados que son pares.

negativos = 0
positivos = 0
multiplos15 = 0
pares = 0

i = 1

while i <= 10:
    numero = int(input(f"Escriba número {i}: "))

    if numero < 0:
        negativos += 1
    else:
        if numero > 0:
            positivos += 1

    if numero % 15 == 0:
        multiplos15 += 1

    else:
        if numero % 2 == 0:
            pares += numero

    i += 1

print(f"Negativos: {negativos}")
print(f"Positivos:{ positivos}")
print(f"Múltiplos de 15: {multiplos15}")
print(f"Suma de pares: {pares}")


