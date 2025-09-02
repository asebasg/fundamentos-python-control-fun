def validar_edades(lista_edades):  # Función para validar lista de edades
    for edad in lista_edades:  # Itera sobre cada edad
        if not isinstance(edad, int) or edad < 0:  # Si no es int o negativa
            print(f"Edad inválida encontrada: {edad}")  # Imprime inválida
            break  # Sale del bucle
    else:  # Si no se encontró inválida
        print("Todas las edades son válidas")  # Imprime válidas
        return True  # Retorna True

    return False  # Retorna False si inválida

# Probamos con diferentes listas
validar_edades([25, 17, 30, 42])  # Todas válidas
validar_edades([25, -3, 30, 42])  # Una inválida