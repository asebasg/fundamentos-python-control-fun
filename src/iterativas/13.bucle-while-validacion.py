entrada = ""  # Se inicializa la entrada como cadena vacía
while not entrada.isdigit():  # Se ejecuta el bucle mientras la entrada no sea un dígito
    entrada = input("Introduce un número: ")  # Se solicita entrada al usuario

print(f"Has introducido el número: {entrada}")  # Se imprime el número introducido
