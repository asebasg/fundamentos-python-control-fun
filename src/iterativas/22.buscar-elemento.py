def buscar_elemento(lista, objetivo):  # Función para buscar elemento en lista
    for indice, elemento in enumerate(lista):  # Itera con índice y elemento
        if elemento == objetivo:  # Si encuentra el objetivo
            return indice  # Retorna el índice

    return -1  # Si no encuentra, retorna -1

numeros = [4, 7, 2, 9, 1, 5]  # Lista de números
posicion = buscar_elemento(numeros, 9)  # Busca el 9
print(f"El elemento se encuentra en la posición: {posicion}")  # Imprime la posición
