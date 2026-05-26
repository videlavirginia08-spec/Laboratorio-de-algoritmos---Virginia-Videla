#Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.

numero1 = int( input("Escriba un numero."))
numero2 = int( input("Escriba un numero."))

if numero1>numero2:
    suma = numero1+numero2
    resta = numero1-numero2
    print(f"El numero {numero1} es mayor.")
    print(f"Su suma da: {suma}")
    print(f"Su diferecia es: {resta}")


else:
    producto = numero1+numero2
    division = numero1/numero2
    print(f"El numero {numero2} es mayor.")
    print(f"Su producto da: {producto}")
    print(f"Su divion da: {division}")

