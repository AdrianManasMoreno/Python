#Ejercicio 11. Función numeros_pares usando lambdas y filter
#Crea una función lambda que filtre los números pares de una lista dada.

lista_numeros = [24, 56, 2.3, 19, -1, 0]
numeros_pares = lambda lista : list(filter(lambda x: x % 2 == 0, lista))
print(numeros_pares(lista_numeros))