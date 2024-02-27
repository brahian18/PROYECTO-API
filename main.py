from api import obtener_datos
from ui import convertir_a_tabla

departamento = input("Ingrese el nombre del departamento (si ingresa una palabra no valida el programa no funcionará): ")
departamento = departamento.upper()
limite = int(input("Ingrese el límite de resultados (preferiblemente un numero no muy grande): "))

datos = obtener_datos(departamento, limite)

tabla = convertir_a_tabla(datos)

print(tabla)