def es_primo(num):  # Función para verificar si un número es primo
    if num < 2:  # Si es menor a 2, no es primo
        return False
    for i in range(2, int(num**0.5) + 1):  # Se itera desde 2 hasta la raíz cuadrada
        if num % i == 0:  # Si es divisible, no es primo
            return False
    return True  # Si no se encontró divisor, es primo

primos = []  # Lista para almacenar números primos
for num in range(2, 20):  # Se itera desde 2 hasta 19
    if es_primo(num):  # Se verifica si es primo
        primos.append(num)  # Se agrega a la lista

print(f"Números primos entre 2 y 19: {primos}")  # Se imprime la lista de primos
