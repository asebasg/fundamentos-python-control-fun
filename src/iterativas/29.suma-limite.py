numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Lista de números impares
limite = 50  # Límite de suma
suma = 0  # Inicializa suma

for num in numeros:  # Itera sobre cada número
    # Ignoramos múltiplos de 3
    if num % 3 == 0:  # Si es múltiplo de 3
        print(f"Omitiendo {num} (múltiplo de 3)")  # Imprime mensaje
        continue  # Salta a la siguiente iteración

    # Sumamos el número
    suma += num  # Añade a suma
    print(f"Añadiendo {num}: suma = {suma}")  # Imprime suma actual

    # Si la suma supera el límite, terminamos
    if suma > limite:  # Si supera límite
        print(f"Límite de {limite} superado")  # Imprime mensaje
        break  # Rompe el bucle
