#Ejercicio 5. Función es_anagrama
# Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden.

def es_anagrama(palabra1, palabra2):
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    return sorted(palabra1) == sorted(palabra2)

palabra1 = "Roma"
palabra2 = "lana"
palabra3 = " hola"
palabra4 = "amor"
print(es_anagrama(palabra1, palabra4))
