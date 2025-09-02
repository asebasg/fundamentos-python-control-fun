def obtener_numero_en_rango(mensaje, minimo, maximo):  # Función para obtener número en rango
    while True:  # Bucle infinito hasta obtener valor válido
        try:  # Intenta convertir a entero
            valor = int(input(mensaje))  # Solicita entrada
            if minimo <= valor <= maximo:  # Verifica si está en rango
                return valor  # Retorna el valor
            print(f"Error: El número debe estar entre {minimo} y {maximo}.")  # Mensaje de error
        except ValueError:  # Si no es entero
            print("Error: Debes introducir un número entero.")  # Mensaje de error

edad = obtener_numero_en_rango("Introduce tu edad (0-120): ", 0, 120)  # Llama a la función
print(f"Edad registrada: {edad} años")  # Imprime la edad
