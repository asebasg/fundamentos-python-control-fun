# Función que convierte temperatura de Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Asignar una función a una variable
convertir = celsius_a_fahrenheit  # Se asigna la función a una variable para reutilización
temperatura_f = convertir(25)  # Se llama a la función a través de la variable
print(f"25°C equivalen a {temperatura_f}°F")  # Imprime la conversión de temperatura
