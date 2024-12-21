#Ejercicio 3. Función encontrar_duplicado:
#Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

def primer_elemento_duplicado(lista):
    elementos_vistos = set()
    for numero in lista:
        if numero in elementos_vistos:
            return numero
        elementos_vistos.add(numero)
    return None

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
duplicado = primer_elemento_duplicado(numeros)
print(duplicado)
    
#el primero 3, none