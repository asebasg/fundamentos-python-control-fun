def encontrar_raiz(numero, max_iteraciones=10):  # Función para encontrar raíz cuadrada
    aproximacion = numero / 2  # Aproximación inicial
    iteracion = 0  # Contador de iteraciones

    while abs(aproximacion**2 - numero) > 0.001 and iteracion < max_iteraciones:  # Mientras no converja y no exceda max
        aproximacion = (aproximacion + numero/aproximacion) / 2  # Método de Newton
        iteracion += 1  # Incrementa iteración
        print(f"Iteración {iteracion}: {aproximacion:.6f}")  # Imprime iteración
    else:  # Si terminó el while
        if iteracion < max_iteraciones:  # Si convergió
            print(f"Convergencia alcanzada en {iteracion} iteraciones")  # Imprime convergencia
            return aproximacion  # Retorna aproximación

    print("No se alcanzó convergencia en el número máximo de iteraciones")  # Imprime no convergió
    return aproximacion  # Retorna última aproximación

encontrar_raiz(25)  # Debería converger rápidamente
encontrar_raiz(612, 5)  # Probablemente no converja en 5 iteraciones
