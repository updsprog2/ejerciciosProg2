
import json

# Leer el archivo JSON y convertirlo en una lista de diccionarios
with open("datos.json", "r", encoding="utf-8") as archivo_json:
    datos_cargados = json.load(archivo_json)

# Mostrar el tipo de datos cargados
print(type(datos_cargados))          # <class 'list'>
print(type(datos_cargados[0]))       # <class 'dict'>
print(type(datos_cargados[0]['edad']))  # <class 'int'> ¡Tipo preservado!
