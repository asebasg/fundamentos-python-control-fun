# Función que calcula el promedio de una lista de números
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

# Uso
notas = [7, 8, 6, 9]
promedio = calcular_promedio(notas)
print(f"El promedio es: {promedio}")  # La impresión se hace fuera de la función
