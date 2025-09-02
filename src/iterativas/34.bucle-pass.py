# Bucle que no hace nada para los números pares
for numero in range(1, 10):  # Itera del 1 al 9
    if numero % 2 == 0:  # Si es par
        pass  # No hace nada
    else:  # Si es impar
        print(f"Procesando número impar: {numero}")  # Imprime impar
