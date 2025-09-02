def calcular_factorial(n):  # Función para calcular factorial
    resultado = 1  # Inicializa resultado en 1
    while n > 0:  # Bucle mientras n sea mayor que 0
        resultado *= n  # Multiplica resultado por n
        n -= 1  # Decrementa n
    return resultado  # Retorna el resultado

numero = 5  # Número para calcular factorial
print(f"El factorial de {numero} es {calcular_factorial(numero)}")  # Imprime el factorial
