while True:  # Bucle infinito
    entrada = input("Escribe algo (o 'salir' para terminar): ")  # Solicita entrada

    if entrada.lower() == 'salir':  # Si la entrada es 'salir'
        print("Programa terminado.")  # Imprime mensaje
        break  # Rompe el bucle

    print(f"Has escrito: {entrada}")  # Imprime lo escrito
