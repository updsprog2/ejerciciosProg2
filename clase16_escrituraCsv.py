import csv

# Datos que queremos guardar
datos = [
    {"nombre": "Ana", "edad": 20},
    {"nombre": "Luis", "edad": 22}
]

# Encabezados (nombres de columna)
encabezados = ["nombre", "edad"]

# Escribir el archivo CSV
with open("datos.csv", "w", newline="", encoding="utf-8") as archivo_csv:
    escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
    escritor.writeheader()         # Escribe la fila de encabezados
    escritor.writerows(datos)      # Escribe todos los diccionarios
