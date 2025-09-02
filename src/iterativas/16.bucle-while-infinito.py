while True:  # Bucle infinito que se ejecuta hasta que se rompa
    respuesta = input("¿Quieres continuar? (s/n): ").lower()  # Solicita respuesta y la convierte a minúscula

    if respuesta == "n":  # Si la respuesta es 'n'
        print("Programa finalizado.")  # Imprime mensaje de finalización
        break  # Rompe el bucle

    if respuesta == "s":  # Si la respuesta es 's'
        print("Continuando...")  # Imprime mensaje de continuación
    else:  # Si la respuesta no es 's' ni 'n'
        print("Respuesta no válida. Introduce 's' o 'n'.")  # Imprime mensaje de error
