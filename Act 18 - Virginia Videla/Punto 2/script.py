"""2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida."""

def mayormenor (v1,v2,v3):
    if v1<v2 and v1<v2 and v2<v3:
        print(v1, v2,v3)
    else:
        if v1<v2 and v1<v3 and v3<v2:
            print(v1,v3,v2)
        else:
            if v2<v1 and v2<v3 and v1<v3:
                print(v2,v1,v3)
            else:
                if v2<v1 and v2<v3 and v3<v1:
                    print(v2,v3,v1)
                else:
                    if v3<v1 and v3<v2 and v1<v2:
                        print(v3,v1,v2)
                    else:
                        if v3<v1 and v3<v2 and v2<v1:
                            print(v3,v2,v1)


def cargar ():
    v1 = int(input("Escriba un numero "))
    v2 = int(input("Escriba un numero "))
    v3 = int(input("Escriba un numero "))
    mayormenor(v1,v2,v3)

cargar()
