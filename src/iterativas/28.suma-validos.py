datos = ["25", "error", "42", "texto", "17"]  # Lista con datos mixtos

suma = 0  # Inicializa suma
for valor in datos:  # Itera sobre cada valor
    if not valor.isdigit():  # Si no es dígito
        print(f"Valor no numérico ignorado: '{valor}'")  # Imprime mensaje
        continue  # Salta a la siguiente iteración

    suma += int(valor)  # Suma el valor convertido

print(f"La suma de los valores válidos es: {suma}")  # Imprime suma total
