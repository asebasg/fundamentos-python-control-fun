a = True # Se declara la variable a con valor True
b = False # Se declara la variable b con valor False
c = not b # Se declara c como la negación de b (not False = True)

resultado = a or b and c # Se evalúa: a OR (b AND c) por precedencia de operadores
print(resultado)  # Imprime True (True OR (False AND True) = True OR False = True)
