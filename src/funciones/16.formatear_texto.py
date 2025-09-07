# Función que formatea texto con múltiples opciones opcionales
def formatear_texto(texto, mayusculas=False, prefijo="", sufijo="", separador=" "):
    # Aplicar mayúsculas si se solicita
    if mayusculas:
        texto = texto.upper()  # Convierte el texto a mayúsculas

    # Dividir el texto en palabras
    palabras = texto.split()  # Separa el texto en una lista de palabras

    # Aplicar prefijo y sufijo a cada palabra
    palabras_formateadas = [f"{prefijo}{palabra}{sufijo}" for palabra in palabras]  # Usa list comprehension para formatear

    # Unir las palabras con el separador especificado
    resultado = separador.join(palabras_formateadas)  # Une las palabras con el separador
    return resultado  # Retorna el texto formateado

# Ejemplos de uso
texto_original = "python es un lenguaje versátil"

# Uso básico sin modificaciones
print(formatear_texto(texto_original))
# Imprime: python es un lenguaje versátil

# Convertir a mayúsculas
print(formatear_texto(texto_original, mayusculas=True))
# Imprime: PYTHON ES UN LENGUAJE VERSÁTIL

# Añadir prefijo y sufijo
print(formatear_texto(texto_original, prefijo="«", sufijo="»"))
# Imprime: «python» «es» «un» «lenguaje» «versátil»

# Cambiar el separador
print(formatear_texto(texto_original, separador="-"))
# Imprime: python-es-un-lenguaje-versátil

# Combinación de opciones
print(formatear_texto(
    texto_original,
    mayusculas=True,
    prefijo="#",
    sufijo="!",
    separador="..."
))
# Imprime: #PYTHON!...#ES!...#UN!...#LENGUAJE!...#VERSÁTIL!
