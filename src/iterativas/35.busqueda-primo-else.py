# Buscar un número primo en una lista
numeros = [4, 6, 8, 9, 10, 12]  # Lista de números

for num in numeros:  # Itera sobre cada número
    if num % 2 != 0 and num % 3 != 0:  # Si no divisible por 2 ni 3 (posible primo)
        print(f"¡Encontrado un primo: {num}!")  # Imprime primo encontrado
        break  # Sale del bucle
else:  # Si no se encontró ningún primo
    print("No se encontró ningún número primo en la lista")  # Imprime mensaje
