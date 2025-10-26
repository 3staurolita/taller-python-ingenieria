# analizar un componente

def analizar_componente(componente_dict):
    #lista de lecturas del diccionario
    lecturas = componente_dict["lecturas"]

    # calcula valores
    promedio = sum(lecturas) / len(lecturas)
    maximo = max(lecturas)
    minimo = min(lecturas)

    # nuevo diccionario con los resultados
    return {"promedio": promedio, "max": maximo, "min": minimo}


# componente del inventario
componente1 = {
    "nombre": "Sensor_Temp_1",
    "lecturas": [45.8, 47.2, 44.9, 46.5, 45.3]
}

# llamar la función y guardamos el resultado
resultado = analizar_componente(componente1)

#resultados
print("Resultados del análisis:")
print("Promedio:", resultado["promedio"])
print("Máximo:", resultado["max"])
print("Mínimo:", resultado["min"])


# -----------------------------
# Filtrado y Mapeo Avanzado (Funciones lambda)
# -----------------------------
# A partir del inventario del módulo anterior

# Filtrado: sensores en la ubicación "Planta_Norte" y tipo "Sensor"
sensores_criticos = list(filter(
    lambda c: c["tipo"] == "Sensor" and c["ubicacion"] == "Planta_Norte",
    inventario
))

# Mapeo: obtener solo los IDs de esos sensores críticos
ids_sensores = list(map(lambda c: c["id"], sensores_criticos))

# Imprimir resultados
print("\n--- Filtrado y Mapeo Avanzado ---")
print("Sensores críticos encontrados:")
print(sensores_criticos if sensores_criticos else "No hay sensores críticos registrados.")
print("\nIDs de sensores críticos:")
print(ids_sensores if ids_sensores else "Lista vacía.")

# modulo5/analisis_componentes.py

# Importar inventario desde modulo 3
from modulo3.gestion_inventario import inventario

# --- Filtrado ---
# Sensores cuyo tipo sea "Sensor" y ubicados en "Planta_Norte"
sensores_criticos = list(filter(
    lambda c: c["tipo"] == "Sensor" and c["ubicacion"] == "Planta_Norte",
    inventario
))

# --- Mapeo ---
# Crear una lista con solo los IDs de los sensores críticos
ids_sensores = list(map(lambda c: c["id"], sensores_criticos))

# --- Mostrar resultados ---
print("\n--- Filtrado y Mapeo Avanzado ---")
print("Sensores críticos encontrados:")
if sensores_criticos:
    for s in sensores_criticos:
        print("  -", s)
else:
    print("  (No hay sensores críticos registrados)")

print("\nIDs de sensores críticos:")
if ids_sensores:
    print(ids_sensores)
else:
    print("  (Lista vacía)")
