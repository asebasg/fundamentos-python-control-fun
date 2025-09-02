def es_primo(n):  # Función para verificar si es primo
    if n < 2:  # Si n es menor que 2
        return False  # No es primo

    for i in range(2, int(n**0.5) + 1):  # Itera desde 2 hasta raíz cuadrada de n
        if n % i == 0:  # Si es divisible
            return False  # No es primo, sale

    return True  # Si llega aquí, es primo

# Ejemplo de uso
print(es_primo(7))  # True
print(es_primo(10))  # False
