dividendo = 10 # Se declara el dividendo con valor 10
divisor = 0 # Se declara el divisor con valor 0

if divisor != 0 and dividendo / divisor > 1: # Cortocircuito: si divisor es 0, no evalúa la división
    print("El resultado de la división es mayor que 1.") # Esta línea no se ejecuta
else: # Si la condición es falsa
    print("No es posible dividir entre cero.") # Imprime mensaje de error
