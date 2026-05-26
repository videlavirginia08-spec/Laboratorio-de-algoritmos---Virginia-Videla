#Se ingresa por teclado un número positivo de uno o dos dígitos (1..99) mostrar un mensaje indicando si el número tiene uno o dos dígitos. (Tener en cuenta que condición debe cumplirse para tener dos dígitos un número entero)

numero = int(input("Escriba un numero."))

if numero>=1 and numero<10:
    print("Su numero tiene un digito")

else:
    if numero>=10 and numero<100:
        print("Su numero tiene dos digitos")

