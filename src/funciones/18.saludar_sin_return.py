# Función que saluda pero no retorna nada explícitamente
def saludar(nombre):
    print(f"Hola, {nombre}")  # Imprime el saludo
    # No hay return explícito, por lo que retorna None

resultado = saludar("Laura")
print(f"La función devolvió: {resultado}")  # Imprime: La función devolvió: None
