# Función que crea un diccionario de usuario con parámetros opcionales
def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",  # Concatena nombre y apellido
        "edad": edad,
        "email": email,
        "activo": activo
    }

# Ejemplo de uso con argumentos por nombre para mayor claridad
usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)

print(usuario)  # Imprime el diccionario del usuario
