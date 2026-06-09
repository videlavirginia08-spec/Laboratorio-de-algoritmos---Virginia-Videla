"""2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio."""



def cargarsueldos():
    sueldos = []
    for i in range(10):
        sueldo = int(input(f"Escriba el sueldo del empleado {i + 1}: "))
        sueldos.append(sueldo)
    return sueldos


def imprimir(sueldos):
    print("Lista de sueldos: ")
    for sueldo in sueldos:
        print(sueldo)


def mayores4000(sueldos):
    contador = 0
    for sueldo in sueldos:
        if sueldo > 4000:
            contador += 1
    return contador


def promedio(sueldos):
    return sum(sueldos) / len(sueldos)


def menorespromedio(sueldos, promedio):
    print("Sueldos por debajo del promedio: ")
    for sueldo in sueldos:
        if sueldo < promedio:
            print(sueldo)



sueldos = cargarsueldos()

imprimir(sueldos)

cantidad = mayores4000(sueldos)
print(f"Cantidad de personas con sueldo superior a 4000: {cantidad}")

promedio = promedio(sueldos)
print(f"Promedio de sueldos: {promedio}")

menorespromedio(sueldos, promedio)