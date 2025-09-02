def analizar_datos(valores, umbral):  # Función para analizar valores con umbral
    tiene_advertencias = False  # Bandera de advertencias

    for valor in valores:  # Itera sobre valores
        if valor > umbral:  # Si excede umbral
            tiene_advertencias = True  # Marca advertencia
            print(f"Advertencia: valor {valor} excede el umbral {umbral}")  # Imprime advertencia
        else:  # Si no
            pass  # No hace nada
    else:  # Si terminó sin break
        if not tiene_advertencias:  # Si no hay advertencias
            print("Análisis completo: todos los valores están dentro del rango normal")  # Imprime OK
            return "OK"  # Retorna OK

    return "ADVERTENCIA"  # Retorna advertencia

# Probamos con diferentes conjuntos de datos
analizar_datos([10, 15, 20, 25], 30)  # Todos dentro del umbral
analizar_datos([10, 35, 20, 25], 30)  # ! Uno excede el umbral
