numeros = [1, 2, 3, 4, 5] # Se crea una lista de números
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros] # List comprehension con operador ternario
print(paridad)  # Salida: ['impar', 'par', 'impar', 'par', 'impar'] # Imprime la lista resultante
