# Función que verifica si una edad es mayor o igual a 18
def es_mayor_de_edad(edad):
    return edad >= 18

# Función que verifica si un email es válido (contiene @ y .)
def es_correo_valido(email):
    return "@" in email and "." in email

# Uso en condicionales
usuario_edad = 16
if es_mayor_de_edad(usuario_edad):
    print("Acceso permitido")
else:
    print("Acceso denegado")  # Imprime: Acceso denegado
