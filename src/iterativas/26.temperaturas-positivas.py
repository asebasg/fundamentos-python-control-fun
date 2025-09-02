temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]  # Lista de temperaturas

print("Temperaturas positivas:")  # Imprime encabezado
for temp in temperaturas:  # Itera sobre cada temperatura
    if temp <= 0:  # Si es negativa o cero
        continue  # Salta a la siguiente iteración

    print(f"{temp}°C")  # Imprime temperatura positiva
