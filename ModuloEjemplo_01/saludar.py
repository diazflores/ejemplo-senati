# Existen 2 maneras de importar
import modulo_saludar as mSalud
#from modulo_saludar import saludar 
import math
#fom modulo_saludar import * #no es una buena practica
import modulo_fuera.calcular_edad as calEdad
# CREACION VARIABLE
variable_saludar =mSalud.despedida("juan")
variable_saludar = calEdad.calcularEdad(2006,2024)
variable_edad = calEdad.calcularEdad(1999,2024)

print(variable_saludar)
print(variable_edad)
print("El PI es. ",math.pi)