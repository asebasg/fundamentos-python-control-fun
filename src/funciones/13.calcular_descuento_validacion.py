# Función que calcula el descuento con validación de argumentos
def calcular_descuento(precio, porcentaje):
    # Validación de argumentos
    if not isinstance(precio, (int, float)) or precio < 0:
        raise ValueError("El precio debe ser un número positivo")  # Lanza error si precio no es válido

    if not isinstance(porcentaje, (int, float)) or not (0 <= porcentaje <= 100):
        raise ValueError("El porcentaje debe ser un número entre 0 y 100")  # Lanza error si porcentaje no es válido

    # Cálculo del descuento
    descuento = precio * (porcentaje / 100)  # Calcula el monto del descuento
    return precio - descuento  # Retorna el precio final

try:
    precio_final = calcular_descuento(100, 15)
    print(f"Precio con descuento: {precio_final}")  # Imprime: Precio con descuento: 85.0

    # Esto lanzará un error
    precio_erroneo = calcular_descuento(-50, 10)
except ValueError as e:
    print(f"Error: {e}")  # Imprime: Error: El precio debe ser un número positivo
