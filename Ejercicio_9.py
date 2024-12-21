#Ejercicio 9. Función cubo_numero usando lambdas
#Crea una función que calcule el cubo de un número dado mediante una función lambda

def cubo_numero(numero):
    cubo = lambda x: x ** 3
    return cubo(numero)
  
numero = 3
print(f"El cubo de {numero} es: {cubo_numero(numero)}")
