# Crear una lista con los cuadrados de los números del 1 al 5
cuadrados = [x**2 for x in range(1, 6)]  # Se usa list comprehension para calcular cuadrados
print(cuadrados)  # Se imprime la lista de cuadrados

# Filtrar elementos usando una condición
pares = [x for x in range(10) if x % 2 == 0]  # Se filtra números pares usando condición
print(pares)  # Se imprime la lista de números pares
