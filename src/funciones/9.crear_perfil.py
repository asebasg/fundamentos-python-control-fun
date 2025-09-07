# Correcto
def crear_perfil(nombre, edad, ciudad="Madrid"):  # Función que crea un perfil con parámetros opcionales
    return f"Perfil: {nombre}, {edad} años, {ciudad}"  # Retorna el perfil formateado

# ! Incorrecto - causaría un error de sintaxis
# def crear_perfil(nombre, ciudad="Madrid", edad):
#     return f"Perfil: {nombre}, {edad} años, {ciudad}"
