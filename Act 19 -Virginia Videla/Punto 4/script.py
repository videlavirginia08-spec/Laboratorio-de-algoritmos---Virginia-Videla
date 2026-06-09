"""4. Elaborar una función que muestre la tabla de multiplicar del valor que le
enviemos como parámetro. Definir un segundo parámetro llamado termino
que por defecto almacene el valor 10. Se deben mostrar tantos términos de
la tabla de multiplicar como lo indica el segundo parámetro.
Llamar a la función desde el bloque principal de nuestro programa con
argumentos nombrados."""


def tabla(n, termino=10):
   for i in range(1, termino + 1):
       print(f"{n} x {i} = {n * i}")

tabla(n=2)
print()
tabla(n=8, termino=15)