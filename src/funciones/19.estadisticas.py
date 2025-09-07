# Función que calcula estadísticas básicas de una lista de números
def estadisticas(numeros):
    total = sum(numeros)  # Calcula la suma total
    promedio = total / len(numeros)  # Calcula el promedio
    minimo = min(numeros)  # Encuentra el mínimo
    maximo = max(numeros)  # Encuentra el máximo
    return total, promedio, minimo, maximo  # Retorna múltiples valores

datos = [4, 8, 15, 16, 23, 42]
suma, media, menor, mayor = estadisticas(datos)  # Desempaqueta los valores retornados

print(f"Suma: {suma}")        # Imprime: Suma: 108
print(f"Promedio: {media}")   # Imprime: Promedio: 18.0
print(f"Mínimo: {menor}")     # Imprime: Mínimo: 4
print(f"Máximo: {mayor}")     # Imprime: Máximo: 42
