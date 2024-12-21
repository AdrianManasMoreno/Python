#Ejercicio 7. Función fibonacci
#Crea una función que calcule el término n de la serie de Fibonacci utilizando recursión.
#La secuencia de Fibonacci es una serie de números en la que cada número es la suma de los dos números anteriores, comenzando con 0 y 1. La posición 0 es la primera:
#Ejemplo para los primeros 5 términos de la función de Fibonacci: [0, 1, 1, 2, 3]
#Primer término: 0 (0)
#RETO-TEST PYTHON: ENUNCIADOS 3
#Segundo término: 1 (1)
#Tercer término: 1 (0 + 1)
#Cuarto término: 2 (1 + 1)
#Quinto término: 3 (1 + 2)

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

for i in range(11):
    print(f"El término {i} de la serie de Fibonacci es: {fibonacci(i)}")



