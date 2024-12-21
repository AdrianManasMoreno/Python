#Ejercicio 6. Función buscar_nombre
#Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción.

def buscar_nombre():
    try:
        nombres = input("Ingresa una lista de nombres separados por comas: ").split(",")
        nombres = [nombre.strip() for nombre in nombres]
        nombre_a_buscar = input("Ingresa el nombre que deseas buscar: ").strip()
        if nombre_a_buscar in nombres:
            print(f"El nombre '{nombre_a_buscar}' fue encontrado en la lista.")
        else:
            raise ValueError(f"El nombre '{nombre_a_buscar}' no fue encontrado en la lista.")
    except ValueError as e:
        print(e)

# Ejemplo de uso - Incorpora los siguientes nombres a la lista y comprueba que la función funciona correctamente: "Jaime", "Silvia" y "Ana".
nombres = ["Jaime, Silvia, Ana"]
print(f"Lista de nombres: {nombres}") 
nombre_a_buscar = "Jaime" 
print(f"Buscando el nombre: {nombre_a_buscar}")
