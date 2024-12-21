#Ejercicio 8. Función encontrar_puesto_empleado
#Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.
empleados = [{'nombre': "Juan", 
              'apellido': "García", 
              'puesto': "Secretario"},
             {'nombre': "Mabel", 
               'apellido': "García", 
               'puesto': "Product Manager"},
             {'nombre': "Isabel", 
               'apellido': "Martín", 
               'puesto': "CEO"}]

def encontrar_puesto_empleado(nombre_completo, empleados):
    for empleado in empleados:
        nombre_completo_empleado = f"{empleado['nombre']} {empleado['apellido']}"
        if nombre_completo_empleado == nombre_completo:
            return f"{nombre_completo} trabaja como {empleado['puesto']}."
    return f"{nombre_completo} no trabaja aquí."

nombre_completo = 'Juan García'
print(encontrar_puesto_empleado(nombre_completo, empleados))
