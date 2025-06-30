import json

archivo = "datos.json"

def guardar_datos():
    datos = []
    while True:
        nombre = input("Ingresa el nombre: ")
        edad = int(input("Ingresa la edad: "))
        datos.append({"nombre": nombre, "edad": edad})
        continuar = input("¿Agregar otro? (s/n): ").lower()
        if continuar != "s":
            break

    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)
    print("✅ Datos guardados en datos.json")

def leer_datos():
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            datos = json.load(f)
            print("📄 Datos cargados:")
            for persona in datos:
                print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")
            print("\n🎯 Tipos:")
            print(f"Tipo de datos: {type(datos)}")
            print(f"Tipo de cada persona: {type(datos[0])}")
            print(f"Tipo de edad: {type(datos[0]['edad'])}")
    except FileNotFoundError:
        print("❌ No se encontró el archivo datos.json")

def menu():
    while True:
        print("\n📋 MENÚ")
        print("1. Guardar datos (JSON)")
        print("2. Leer datos")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            guardar_datos()
        elif opcion == "2":
            leer_datos()
        elif opcion == "3":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción no válida")

# Ejecutamos el menú
menu()
