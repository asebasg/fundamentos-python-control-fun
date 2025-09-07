# Función que muestra información usando **kwargs
def mostrar_informacion(**datos):
    for clave, valor in datos.items():  # Itera sobre cada par clave-valor
        print(f"{clave}: {valor}")  # Imprime la clave y el valor

# Podemos pasar cualquier cantidad de argumentos por nombre
mostrar_informacion(nombre="Python", creador="Guido van Rossum", año=1991)
# Imprime:
# nombre: Python
# creador: Guido van Rossum
# año: 1991
