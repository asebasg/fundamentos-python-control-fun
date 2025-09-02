saldo = 1000  # Saldo inicial
while saldo > 0:  # Bucle mientras haya saldo
    print(f"Saldo actual: {saldo}€")  # Muestra saldo actual
    gasto = float(input("Introduce la cantidad a gastar (0 para salir): "))  # Solicita gasto

    if gasto == 0:  # Si gasto es 0, salir
        break  # Rompe el bucle

    if gasto > saldo:  # Si gasto mayor que saldo
        print("No tienes suficiente saldo.")  # Mensaje de error
        continue  # Vuelve al inicio del bucle

    saldo -= gasto  # Resta el gasto del saldo

print(f"Saldo final: {saldo}€")  # Muestra saldo final
