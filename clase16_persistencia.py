
import csv
import json

# === Inventario original (Clase 12) ===
inventario = [
    {"producto": "Chocolate para Taza 'El Ceibo'", "stock": 50, "precio": 25.5},
    {"producto": "Café de los Yungas", "stock": 100, "precio": 30.0},
    {"producto": "Quinua Real en Grano", "stock": 80, "precio": 28.75}
]

# === Guardar en CSV ===
encabezados = ["producto", "stock", "precio"]

with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo_csv:
    escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
    escritor.writeheader()
    escritor.writerows(inventario)
    print("✅ Archivo CSV guardado como inventario.csv")

# === Cargar desde CSV ===
inventario_cargado_csv = []
with open("inventario.csv", "r", newline="", encoding="utf-8") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        fila["stock"] = int(fila["stock"])
        fila["precio"] = float(fila["precio"])
        inventario_cargado_csv.append(fila)

print("\n📄 Inventario cargado desde CSV:")
for item in inventario_cargado_csv:
    print(item)

# === Guardar en JSON ===
with open("inventario.json", "w", encoding="utf-8") as archivo_json:
    json.dump(inventario, archivo_json, indent=4, ensure_ascii=False)
    print("✅ Archivo JSON guardado como inventario.json")

# === Cargar desde JSON ===
with open("inventario.json", "r", encoding="utf-8") as archivo_json:
    inventario_cargado_json = json.load(archivo_json)

print("\n📄 Inventario cargado desde JSON:")
for item in inventario_cargado_json:
    print(item)

# Verificar tipos
print("\n🎯 Verificación de tipos:")
print("Desde CSV:", type(inventario_cargado_csv[0]["stock"]), type(inventario_cargado_csv[0]["precio"]))
print("Desde JSON:", type(inventario_cargado_json[0]["stock"]), type(inventario_cargado_json[0]["precio"]))

# Comparación
print("\n📊 Comparación:")
print("CSV -> Más simple pero convierte todo a texto. Tipos deben restaurarse manualmente.")
print("JSON -> Estructura más clara, mantiene tipos automáticamente.")
