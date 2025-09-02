import random  # Importa el módulo random para generar números aleatorios

objetivo = random.randint(1, 10)  # Número aleatorio entre 1 y 10
intentos = 0  # Contador de intentos
adivinado = False  # Estado de adivinanza

while not adivinado and intentos < 3:  # Bucle hasta adivinar o agotar intentos
    intentos += 1  # Incrementa el contador de intentos
    numero = int(input(f"Intento {intentos}/3: Adivina un número del 1 al 10: "))  # Solicita número al usuario

    if numero == objetivo:  # Verifica si el número es correcto
        print(f"¡Correcto! Has adivinado en {intentos} intentos.")  # Mensaje de éxito
        adivinado = True  # Cambia estado a adivinado
    else:
        pista = "mayor" if numero < objetivo else "menor"  # Da pista si el número es mayor o menor
        print(f"Incorrecto. El número es {pista} que {numero}.")  # Mensaje de pista

if not adivinado:  # Si no se adivinó
    print(f"Se acabaron los intentos. El número era {objetivo}.")  # Mensaje de fin de intentos
