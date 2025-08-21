numeros = [1, 2, 3, 4] # Se declara una lista con 4 números

match numeros: # Estructura match-case para analizar la lista
    case []: # Si la lista está vacía
        print("La lista está vacía.") # Imprime lista vacía
    case [uno]: # Si la lista tiene un solo elemento
        print(f"Un solo elemento: {uno}.") # Imprime el elemento único
    case [uno, dos]: # Si la lista tiene exactamente dos elementos
        print(f"Dos elementos: {uno} y {dos}.") # Imprime los dos elementos
    case [uno, *resto]: # Para listas con más de dos elementos
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.") # Imprime primer elemento y resto
