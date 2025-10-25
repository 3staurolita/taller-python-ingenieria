
# Ejercicio1 : Modulo 2 

#  datos del sensor
reporte = "ID_SENSOR:T-21,LOC:Planta_Norte,TEMP:45.8,STATUS:OK"

# Separar el texto por comas (,) 
partes = reporte.split(',')


# valores de cada parte usando split(':')
id_sensor = partes[0].split(':')[1]   # toma lo que esta después de los :
ubicacion = partes[1].split(':')[1]
temperatura = float(partes[2].split(':')[1])  # se convierte  el texto a numero decimal
estado = partes[3].split(':')[1]

# resultado
print("*** REPORTE DE SENSOR ***")
print("ID:", id_sensor)
print("Ubicación:", ubicacion)
print("Temperatura:", temperatura, "°C")
print("Estado:", estado)
