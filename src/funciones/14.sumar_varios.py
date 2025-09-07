# Función que suma una cantidad variable de números usando *args
def sumar(*numeros):
    total = 0  # Inicializa el total en cero
    for numero in numeros:  # Itera sobre cada número recibido
        total += numero  # Suma cada número al total
    return total  # Retorna la suma total

# Podemos pasar cualquier cantidad de argumentos
print(sumar(1, 2))  # Imprime: 3
print(sumar(1, 2, 3, 4, 5))  # Imprime: 15
print(sumar())  # Imprime: 0
