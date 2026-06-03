"""1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)"""

def menor (v1,v2,v3):
    if v1<v2 and v1<v3:
        print(f"El mnenor es: {v1}")
    else:
        if v2<v3 and v2<v1:
            print(f"El menor es: {v2}")
        else:
            print(f"El menor es: {v3}")

def cargar ():
    v1 = int(input("Escriba un numero "))
    v2 = int(input("Escriba un numero "))
    v3 = int(input("Escriba un numero "))
    menor(v1,v2,v3)


cargar()