#Ejercicio 2. Función calcular_promedio:
#Crea una función que calcule el promedio de una lista de números.

def calcular_promedio(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)

numeros = [1, 2, 3, 4, 5]
promedio = calcular_promedio(numeros)
print("El promedio es:", promedio)

#Para numeros1, la función devolverá 3.0, para numeros2 devolverá 0.