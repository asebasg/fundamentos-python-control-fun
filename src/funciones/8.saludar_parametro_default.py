def saludar(nombre, mensaje="¡Bienvenido!"):  # Función que saluda con mensaje predeterminado
    print(f"Hola {nombre}. {mensaje}")  # Imprime el saludo con nombre y mensaje

saludar("Carlos")  # Usa el mensaje predeterminado
# Imprime: Hola Carlos. ¡Bienvenido!

saludar("María", "¿Cómo estás hoy?")  # Usa el mensaje personalizado
# Imprime: Hola María. ¿Cómo estás hoy?
