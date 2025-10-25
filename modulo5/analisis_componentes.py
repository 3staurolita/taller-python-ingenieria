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
