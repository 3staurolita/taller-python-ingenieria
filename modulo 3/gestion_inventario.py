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
