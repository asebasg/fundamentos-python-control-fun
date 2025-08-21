a = 5 # Se declara la variable a con valor 5
b = 10 # Se declara la variable b con valor 10
c = 15 # Se declara la variable c con valor 15

if a > b: # Verifica si a es mayor que b
    if a > c: # Si a es mayor que b, verifica si también es mayor que c
        print('a es el mayor.') # Si a es mayor que ambos, imprime a es el mayor
    else: # Si a no es mayor que c
        if c > b: # Verifica si c es mayor que b
            print('c es el mayor.') # Si c es mayor que b, imprime c es el mayor
        else: # Si c no es mayor que b
            print('b es el mayor.') # Imprime b es el mayor
else: # Si a no es mayor que b
    if b > c: # Verifica si b es mayor que c
        print('b es el mayor.') # Si b es mayor que c, imprime b es el mayor
    else: # Si b no es mayor que c
        print('c es el mayor.') # Imprime c es el mayor
