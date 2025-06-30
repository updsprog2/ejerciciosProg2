
import json
import csv

datos = {
    "curso": "Prog II",
    "año": 2025,
    "estudiantes": ["Ana", "Juan", "Maria"]
}

# === Guardar en JSON ===
with open("datos.json", "w", encoding="utf-8") as archivo_json:
    json.dump(datos, archivo_json, indent=4, ensure_ascii=False)
    print("✅ datos.json creado")

# === Convertir a CSV simple (clave, valor) ===
with open("datos.csv", "w", newline="", encoding="utf-8") as archivo_csv:
    escritor = csv.writer(archivo_csv)
    for clave, valor in datos.items():
        escritor.writerow([clave, json.dumps(valor)])  # Convertimos listas a texto JSON
    print("✅ datos.csv creado en formato clave-valor")

# === Leer ambos para comparación ===
print("\n📄 Contenido JSON (estructurado):")
with open("datos.json", "r", encoding="utf-8") as archivo_json:
    print(archivo_json.read())

print("\n📄 Contenido CSV (clave-valor):")
with open("datos.csv", "r", encoding="utf-8") as archivo_csv:
    print(archivo_csv.read())
