#Ejercicio 1. Función contar_caracteres
#Crea una función que cuente el número de caracteres en una cadena de texto dada.

def contar_caracteres(cadena):
    return len(cadena)

texto1 = "¡Hola alumnos! Bienvenidos a clase"
cantidad_caracteres = contar_caracteres(texto1)
print("El número de caracteres es:", cantidad_caracteres)

#Para cadena1, la función devolverá 34, para cadena2 lanzará un error.
