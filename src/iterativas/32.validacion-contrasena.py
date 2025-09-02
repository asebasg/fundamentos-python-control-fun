def validar_contraseña(contraseña):  # Función para validar contraseña
    if len(contraseña) < 8:  # Si longitud menor a 8
        return False  # No válida

    tiene_mayuscula = False  # Bandera mayúscula
    tiene_minuscula = False  # Bandera minúscula
    tiene_numero = False  # Bandera número

    for caracter in contraseña:  # Itera sobre cada carácter
        if caracter.isupper():  # Si es mayúscula
            tiene_mayuscula = True  # Marca
            continue  # Salta al siguiente

        if caracter.islower():  # Si es minúscula
            tiene_minuscula = True  # Marca
            continue  # Salta

        if caracter.isdigit():  # Si es dígito
            tiene_numero = True  # Marca

    return tiene_mayuscula and tiene_minuscula and tiene_numero  # Retorna si cumple todos

# Probamos algunas contraseñas
contraseñas = ["abc123", "Password", "Password1", "pass123", "PASS123"]  # Lista de pruebas
for pwd in contraseñas:  # Itera sobre cada contraseña
    if validar_contraseña(pwd):  # Si válida
        print(f"'{pwd}' es válida")  # Imprime válida
    else:  # Si no
        print(f"'{pwd}' NO es válida")  # Imprime no válida
