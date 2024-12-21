#Ejercicio 4. Función enmascarado_datos
# Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres con el carácter '#', excepto los últimos cuatro.

def enmascarado_datos(variable):
  variable_str = str(variable)
  enmascarado = '#' * (len(variable_str) - 4) + variable_str[-4:]
  return enmascarado

contraseña1  = 'Micontraseña1234' 
print(enmascarado_datos(contraseña1))
contraseña2  = '123456789' 
print(enmascarado_datos(contraseña2))