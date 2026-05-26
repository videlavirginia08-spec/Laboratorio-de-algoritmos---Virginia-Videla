#De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe: a. Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10 años, otorgarle un aumento del 20 %, mostrar el sueldo a pagar. b. Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %. c. Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.

sueldo = int(input("Escriba su sueldo."))
antiguedad = int(input("Escribas sus años de antiguedad"))

if sueldo<500 and antiguedad>=10:
    aumento20 = sueldo*1.2
    print(f"Su sueldo a cobrar es: {aumento20}")

else:
    if sueldo<500 and antiguedad<10:
        aumento5 = sueldo*1.05
        print(f"Su sueldo a cobrar es: {aumento5}")

    else:
        print(f"Su sueldo a cobrar es: {sueldo}")

