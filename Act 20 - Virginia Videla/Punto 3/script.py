"""3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas."""

l1 = []
l2 = []
l3 = []

def cargar():
    for x in range(10):
        lista = int(input(f"Esriba el valor numero {x+1}: "))
        l1.append(lista)
   
def vnegativos():
    for x in range(10):
        if l1[x] < 0:
            l2.append(l1[x])

def vpositivos():
    for x in range(10):
        if l1[x] > 0:
            l3.append(l1[x])

def imprimir():
    print(f"Lista negativa: {l2}")
    print(f"Lista positiva: {l3}")

cargar()
vnegativos()
vpositivos()
imprimir()


