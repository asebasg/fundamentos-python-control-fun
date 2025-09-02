encontrado = False  # Bandera para indicar si se encontró el valor

for i in range(5):  # Bucle externo de 0 a 4
    for j in range(5):  # Bucle interno de 0 a 4
        if i * j > 10:  # Si el producto es mayor que 10
            print(f"Valor encontrado: {i} * {j} = {i*j}")  # Imprime el valor
            encontrado = True  # Marca como encontrado
            break  # Sale del bucle interno

    if encontrado:  # Si se encontró, sale del bucle externo
        break  # Sale del bucle externo
