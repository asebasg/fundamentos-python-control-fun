def calcular_raiz_cuadrada(numero, precision=0.0001):  # Función para calcular raíz cuadrada
    aproximacion = numero / 2  # Valor inicial de aproximación
    while abs(aproximacion**2 - numero) > precision:  # Bucle hasta alcanzar precisión
        aproximacion = (aproximacion + numero/aproximacion) / 2  # Método de Newton
    return aproximacion  # Retorna la aproximación

print(f"Raíz cuadrada de 25: {calcular_raiz_cuadrada(25):.6f}")  # Imprime raíz de 25
print(f"Raíz cuadrada de 7: {calcular_raiz_cuadrada(7):.6f}")    # Imprime raíz de 7
