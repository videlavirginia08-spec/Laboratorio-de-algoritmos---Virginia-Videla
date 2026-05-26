#7. Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos)

numero1 = int(input("Escribas un numero"))
numero2 = int(input("Escribas un numero distinto al anterior"))
numero3 = int(input("Escribas un numero distinto al anterior"))

if numero1>numero2 and numero1>numero3:
    print(f"El numero {numero1} es el mayor")

else:
    if numero2>numero1 and numero2>numero3:
        print(f"El numero {numero2} es el mayor")

    else:
        print(f"El numero {numero3} es el mayor")


if numero1<numero2 and numero1<numero3:
    print(f"El numero {numero1} es el menor")

else:
    if numero2<numero1 and numero2<numero3:
        print(f"El numero {numero2} es el menor")

    else:
        print(f"El numero {numero3} es el menor")

