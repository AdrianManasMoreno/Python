#Ejercicio 12. Función numeros_suma usando lambdas y map
#lambda que sume 3 a cada número de una lista dada.

lista_numeros = [24, 56, 2.3, 19, -1, 0]
numeros_suma = lambda lista: list(map(lambda x : x + 3, lista))
print(numeros_suma(lista_numeros))