# Crear una matriz de multiplicación 3x3
for i in range(1, 4):  # Bucle externo para filas
    for j in range(1, 4):  # Bucle interno para columnas
        print(f"{i} × {j} = {i*j}", end="\t")  # Se imprime el producto con tabulación
    print()  # Salto de línea después de cada fila
