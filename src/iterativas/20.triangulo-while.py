def imprimir_triangulo(altura):  # Función para imprimir triángulo
    fila = 1  # Inicializa fila en 1
    while fila <= altura:  # Bucle mientras fila sea menor o igual a altura
        print("*" * fila)  # Imprime asteriscos según fila
        fila += 1  # Incrementa fila

imprimir_triangulo(5)  # Llama a la función con altura 5
