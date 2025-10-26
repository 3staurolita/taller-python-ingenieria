# Base de datos simple en memoria y análisis de conjuntos de experimentos


from typing import List, Dict, Tuple, Set


# -----------------------------
# Base de Datos de Componentes
# -----------------------------
# Lista llamada `inventario`. Cada elemento es un diccionario con las claves:
# "id" (str), "tipo" (str), "ubicacion" (str), "lecturas" (lista de 3 floats)


inventario: List[Dict[str, object]] = [
{
"id": "S-101",
"tipo": "Sensor",
"ubicacion": "Sala A",
"lecturas": [12.5, 13.0, 12.8],
},
{
"id": "M-210",
"tipo": "Motor",
"ubicacion": "Taller 1",
"lecturas": [230.0, 229.5, 231.2],
},
{
"id": "V-330",
"tipo": "Válvula",
"ubicacion": "Planta 2",
"lecturas": [0.75, 0.80, 0.78],
},
]

def promedio_lecturas_por_id(inventario: List[Dict[str, object]], componente_id: str) -> float:
    """Calcula el promedio de las lecturas para el componente con id `componente_id`.
    Lanza ValueError si no se encuentra el componente o si las lecturas no son válidas."""
    for comp in inventario:
        if comp.get("id") == componente_id:
            lecturas = comp.get("lecturas")
            if not isinstance(lecturas, list) or len(lecturas) == 0:
                raise ValueError(f"Lecturas inválidas para el componente {componente_id}")
            # convertir a float y calcular promedio
            try:
                valores = [float(x) for x in lecturas]
            except Exception as e:
                raise ValueError("Error al convertir lecturas a float: " + str(e))
            return sum(valores) / len(valores)
    raise ValueError(f"Componente con id '{componente_id}' no encontrado en el inventario")

# -----------------------------
# Análisis de Experimentos (Sets y Tuplas)
# -----------------------------
# IDs de experimentos exitosos (tuplas de (id_experimento, fecha))

equipo_A: Set[Tuple[str, str]] = {
    ("EXP-001", "2023-10-01"),
    ("EXP-002", "2023-10-02"),
    ("EXP-003", "2023-10-03"),
}

equipo_B: Set[Tuple[str, str]] = {
    ("EXP-002", "2023-10-02"),
    ("EXP-004", "2023-10-04"),
    ("EXP-001", "2023-10-01"),
}


def imprimir_resultados_experimentos(a: Set[Tuple[str, str]], b: Set[Tuple[str, str]]):
    interseccion = a & b
    union = a | b
    diferencia = a - b

    print("\n--- Análisis de Experimentos ---")
    print("Experimentos reportados por ambos (Intersección):")
    if interseccion:
        for exp in sorted(interseccion):
            print("  -", exp)
    else:
        print("  (ninguno)")

    print("\nTotal de experimentos exitosos únicos (Unión):", len(union))
    for exp in sorted(union):
        print("  -", exp)

    print("\nExperimentos que hizo equipo_A pero no equipo_B (Diferencia):")
    if diferencia:
        for exp in sorted(diferencia):
            print("  -", exp)
    else:
        print("  (ninguno)")


# -----------------------------
# Bloque principal: ejecución de ejemplos
# -----------------------------
if __name__ == "__main__":
    # Promedio de lecturas para un id específico
    buscado = "S-101"
    try:
        prom = promedio_lecturas_por_id(inventario, buscado)
        print(f"Promedio de lecturas para el componente {buscado}: {prom:.3f}")
    except ValueError as e:
        print("Error:", e)

    # Imprimir análisis de experimentos
    imprimir_resultados_experimentos(equipo_A, equipo_B)

    # Nota: cambiar los datos arriba si se desea probar con otros componentes o sets
