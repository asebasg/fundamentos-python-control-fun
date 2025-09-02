numeros = [1, 2, 0, 4, 0, 6, 7]  # Lista con ceros

for num in numeros:  # Itera sobre cada número
    if num == 0:  # Si es cero
        print("Omitiendo división por cero")  # Imprime mensaje
        continue  # Salta a la siguiente iteración

    resultado = 10 / num  # Calcula división
    print(f"10 / {num} = {resultado}")  # Imprime resultado
