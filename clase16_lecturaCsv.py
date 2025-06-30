import csv

# Lista donde guardaremos los diccionarios leídos
lista_leida = []

# Leer el archivo CSV
with open("datos.csv", "r", newline="", encoding="utf-8") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila_dict in lector:
        fila_dict['edad'] = int(fila_dict['edad'])  # Convertimos edad de string a entero
        lista_leida.append(fila_dict)

# Mostramos la lista leída
print(lista_leida)
