# Ejercicio 2: modulo 2

# ingrese el código
codigo_lote = input("Ingrese el código de lote: ")

#espacios por si el usuario escribe alguno sin querer
codigo_lote = codigo_lote.strip()

#  condiciones
if len(codigo_lote) == 14 and codigo_lote.startswith("LOT-") and codigo_lote.endswith("-24") and (codigo_lote[8] == "X" or codigo_lote[8] == "Y"):
    print("El codigo es Válido")
else:
    print("El codigo es Inválido")
