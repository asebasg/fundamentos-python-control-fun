# Función que divide dos números con verificación de división por cero
def dividir_seguro(a, b):
    # Verificación de seguridad
    if b == 0:
        print("Error: División por cero")  # Imprime mensaje de error
        return None  # Salida anticipada con None

    # Este código solo se ejecuta si b no es cero
    resultado = a / b  # Realiza la división
    return resultado  # Retorna el resultado

print(dividir_seguro(10, 2))   # Imprime: 5.0
print(dividir_seguro(10, 0))   # Imprime: Error: División por cero y luego None
