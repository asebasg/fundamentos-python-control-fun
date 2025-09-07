# Función que formatea un nombre en formato apellido, nombre
def formato_nombre(nombre, apellido):
    return f"{apellido.upper()}, {nombre.capitalize()}"

print(formato_nombre("ana", "garcía"))  # Imprime: GARCÍA, Ana
