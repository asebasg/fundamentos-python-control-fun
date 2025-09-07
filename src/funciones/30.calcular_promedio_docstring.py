def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Suma todos los números de la lista y divide el resultado
    entre la cantidad de elementos.

    Args:
        numeros: Una lista de valores numéricos

    Returns:
        El promedio como valor flotante

    Ejemplo:
        >>> calcular_promedio([1, 2, 3, 4])
        2.5
    """
    return sum(numeros) / len(numeros)

# * Acceder a los docstrings
# Acceder al docstring directamente
print(calcular_promedio.__doc__)
print("--------------------------")
# O usar la función help
help(calcular_promedio)