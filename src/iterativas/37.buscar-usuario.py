def buscar_usuario(usuarios, nombre):  # Función para buscar usuario
    for usuario in usuarios:  # Itera sobre lista de usuarios
        if usuario["nombre"] == nombre:  # Si encuentra el nombre
            print(f"Usuario encontrado: {usuario}")  # Imprime encontrado
            return usuario  # Retorna el usuario
    else:  # Si no encontró
        print(f"Usuario '{nombre}' no encontrado, creando nuevo perfil...")  # Imprime no encontrado
        nuevo_usuario = {"nombre": nombre, "nivel": 1}  # Crea nuevo
        usuarios.append(nuevo_usuario)  # Agrega a lista
        return nuevo_usuario  # Retorna nuevo

base_usuarios = [  # Lista base de usuarios
    {"nombre": "Ana", "nivel": 5},
    {"nombre": "Carlos", "nivel": 3}
]

buscar_usuario(base_usuarios, "Ana")      # Existente
buscar_usuario(base_usuarios, "Roberto")  # Nuevo