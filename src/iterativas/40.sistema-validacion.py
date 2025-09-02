def validar_formulario(datos):  # Función para validar formulario
    campos_requeridos = ["nombre", "email", "edad"]  # Campos requeridos
    errores = []  # Lista de errores

    # Verificar campos requeridos
    for campo in campos_requeridos:  # Itera sobre requeridos
        if campo not in datos:  # Si falta campo
            errores.append(f"Falta el campo requerido: {campo}")  # Agrega error
            break  # Sale
        elif not datos[campo]:  # Si vacío
            errores.append(f"El campo {campo} no puede estar vacío")  # Agrega error
            break  # Sale
    else:  # Si todos requeridos OK
        # Ahora validamos el formato de cada campo

        # Validar email
        if "@" not in datos["email"]:  # Si no tiene @
            errores.append("Email inválido")  # Agrega error

        # Validar edad
        try:  # Intenta convertir a int
            edad = int(datos["edad"])  # Convierte
            if edad < 18 or edad > 120:  # Si fuera de rango
                errores.append("La edad debe estar entre 18 y 120")  # Agrega error
        except ValueError:  # Si no es número
            errores.append("La edad debe ser un número")  # Agrega error

    # Validaciones opcionales
    if "telefono" in datos:  # Si tiene teléfono
        if not datos["telefono"].isdigit():  # Si no es dígitos
            errores.append("El teléfono debe contener solo dígitos")  # Agrega error
    else:  # Si no tiene
        pass  # Explícitamente indicamos que es opcional

    # Resultado final
    if errores:  # Si hay errores
        return {"valido": False, "errores": errores}  # Retorna inválido con errores
    else:  # Si no
        return {"valido": True}  # Retorna válido

# Probamos con diferentes formularios
formulario1 = {  # Formulario válido
    "nombre": "Ana García",
    "email": "ana@ejemplo.com",
    "edad": "28"
}

formulario2 = {  # Formulario inválido
    "nombre": "Carlos López",
    "email": "carlosejemplo.com",  # Falta @
    "edad": "17"  # Menor de edad
}

print(validar_formulario(formulario1))  # Imprime válido
print(validar_formulario(formulario2))  # Imprime inválido
