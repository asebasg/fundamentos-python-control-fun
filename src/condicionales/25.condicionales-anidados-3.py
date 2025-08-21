edad = 30 # Se declara la variable edad con valor 30
estado_civil = 'soltero' # Se declara la variable estado_civil con valor 'soltero'

if edad >= 18: # Verifica si la edad es mayor o igual a 18
    if estado_civil == 'casado': # Si es adulto, verifica si está casado
        print('Eres un adulto casado.') # Si es adulto y casado, imprime este mensaje
    else: # Si es adulto pero no está casado
        print('Eres un adulto soltero.') # Imprime adulto soltero
else: # Si no es adulto (menor de 18)
    print('Eres menor de edad.') # Imprime menor de edad
