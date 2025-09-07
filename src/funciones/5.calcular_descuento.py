def calcular_descuento(precio, porcentaje=10):
    # La variable 'descuento' solo existe dentro de esta función (ámbito local)
    descuento = precio * (porcentaje / 100)  # Calcula el monto del descuento
    precio_final = precio - descuento  # Resta el descuento al precio original
    return precio_final  # Retorna el precio final

# Uso de la función con valor por defecto
precio_con_descuento = calcular_descuento(100)  # Aplica 10% de descuento por defecto
print(f"Precio con descuento: {precio_con_descuento}")  # Imprime: Precio con descuento: 90.0

# ! Nota: La siguiente línea causaría un error si se descomentara, ya que 'descuento' no existe fuera de la función
# print(descuento)  # Error: NameError: name 'descuento' is not defined
