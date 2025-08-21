saldo = 300 # Se declara el saldo inicial de 300
retiro = 500 # Se declara el monto a retirar de 500
if saldo >= retiro: # Se verifica si el saldo es suficiente para el retiro
    saldo -= retiro # Si es suficiente, se resta el retiro del saldo
    print("Retiro exitoso.") # Imprime mensaje de retiro exitoso
    print(f"Nuevo saldo: {saldo}") # Muestra el nuevo saldo
else: # Si el saldo es insuficiente
    print("Fondos insuficientes.") # Imprime mensaje de fondos insuficientes
    print(f"Saldo actual: {saldo}") # Muestra el saldo actual
