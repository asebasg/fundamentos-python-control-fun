temperaturas = [22, 19, 24, 25, 21, 23, 20]  # Lista de temperaturas diarias
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]  # Lista de días de la semana

# Encontrar el día más caluroso
max_temp = max(temperaturas)  # Se obtiene la temperatura máxima
indice_max = temperaturas.index(max_temp)  # Se obtiene el índice de la temperatura máxima
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")  # Se imprime el día y temperatura máxima

# Calcular la temperatura promedio
promedio = sum(temperaturas) / len(temperaturas)  # Se calcula el promedio sumando y dividiendo por la cantidad
print(f"Temperatura promedio: {promedio:.1f}°C")  # Se imprime el promedio con un decimal

# Días con temperatura superior al promedio
for i in range(len(dias)):  # Se itera sobre los índices de los días
    if temperaturas[i] > promedio:  # Se verifica si la temperatura es mayor al promedio
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")  # Se imprime el día y temperatura si es superior
