# simulador llenado de un tanque
capacidad_tanque = 1000 # litros
volumen_actual = 0 #float
tasa_flujo = 50.5 # (litros/min)
tiempo = 0 # segundos

while volumen_actual < capacidad_tanque:
    volumen_actual = volumen_actual + tasa_flujo 
    tiempo = tiempo + 1
    print(f"Han transcurrido {tiempo} minutos y el voluimen del tanque es: {volumen_actual:.2f} L")

    #Alerta de tanque casi lleno
    if volumen_actual >= 950:
        print("ALERTA: Tanque casi lleno")
        break # rompe el bucle 
print(f"El tanque tardó {tiempo} minutos en llenar")