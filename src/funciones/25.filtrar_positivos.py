# Función que filtra números positivos de una lista, con manejo de errores
def filtrar_positivos(numeros):
    if not isinstance(numeros, list):
        return []  # Lista vacía en caso de error
    return [num for num in numeros if num > 0]
