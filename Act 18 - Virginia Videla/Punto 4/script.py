"""4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras &#39;a&#39; o &#39;A&#39;."""

def contador (lista):
    contador=0
    for letra in lista:
        if letra == "a" or letra == "A":
            contador+=1
    return contador
texto = input("Escriba un texto. ")
print("La cantidad de letras a o A en el texto es: ",contador(texto))



