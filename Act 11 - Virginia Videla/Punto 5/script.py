#5. Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero)

numero = int(input("Escriba un numero"))

if numero>0:
    print(f"Su numero es positivo.")

else:
    if numero<0:
        print(f"Su numero es negativo.")
    else:
        print(f"Su numero es nulo.")