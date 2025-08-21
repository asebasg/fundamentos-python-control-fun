condiciones = [True, True, False, True] # Se crea una lista de condiciones booleanas

if all(condiciones): # La función all() devuelve True si TODOS los elementos son True
    print("Todas las condiciones son verdaderas.") # No se ejecuta porque hay un False
else: # Si all() devuelve False
    print("Al menos una condición es falsa.") # Se ejecuta porque hay al menos un False
