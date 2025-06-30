import json

# Lista de diccionarios que queremos guardar
datos_python = [{"nombre": "Ana", "edad": 20}, {"nombre": "Luis", "edad": 22}]

# Guardar como JSON
with open("datos.json", "w", encoding="utf-8") as archivo_json:
    json.dump(datos_python, archivo_json, indent=4, ensure_ascii=False)
