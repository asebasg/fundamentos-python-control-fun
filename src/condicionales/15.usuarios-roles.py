usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
] # Lista de diccionarios con información de usuarios

for usuario in usuarios: # Itera sobre cada usuario en la lista
    match usuario: # Estructura match-case para analizar el rol del usuario
        case {"rol": "admin"}: # Si el rol es "admin"
            print(f"{usuario['nombre']} tiene permisos de administrador.") # Imprime permisos de admin
        case {"rol": "moderador"}: # Si el rol es "moderador"
            print(f"{usuario['nombre']} puede moderar contenidos.") # Imprime permisos de moderador
        case {"rol": "usuario"}: # Si el rol es "usuario"
            print(f"{usuario['nombre']} es un usuario regular.") # Imprime usuario regular
        case _: # Para cualquier otro rol
            print(f"Rol de {usuario['nombre']} desconocido.") # Imprime rol desconocido
