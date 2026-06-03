"""3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor."""


 

def mayorsup (base, altura):

    superficie = base * altura
    return superficie


base1 = int(input("Escriba el primer lado del primer rectangulo. "))
altura1 = int(input("Escriba el segundo lado del primer rectangulo. "))
base2 = int(input("Escriba el primer lado del segundo rectangulo. "))
altura2 = int(input("Escriba el segundo lado del seguno rectangulo. "))

if mayorsup(base1, altura1) > mayorsup(base2, altura2):
    print("El primer rectangulo tiene mayor superficie")
else:
    print("El segundo rectangulo es mayor")
    

mayorsup()



