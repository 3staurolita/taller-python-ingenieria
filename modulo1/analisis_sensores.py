# conversor de unidades
temperatura_celcius = 35.5
temperatura_fahrenheit = temperatura_celcius*(9/5) + 32
temperatura_kelvin = temperatura_celcius + 273.15 
print(f"La temperatura en celsius es {temperatura_celcius}, en fahrenheit es {temperatura_fahrenheit} y en Kelvin es {temperatura_kelvin}")

#monitor de seguridad de caldera 
temp_caldera = 200 #float
presion_caldera = 200 #float
operador_presente = True #bool

alarma_critica = True 
if temp_caldera > 100 and presion_caldera > 103.0:
    print("Alarma crítica activada")
elif temp_caldera > 105.0:
    operador_presente = False