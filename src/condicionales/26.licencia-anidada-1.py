edad = 16 # Se declara la variable edad con valor 16
permiso_padres = True # Se declara la variable permiso_padres con valor True

if edad >= 18: # Verifica si la edad es 18 o más
    print('Puedes obtener la licencia de conducir.') # Si es mayor de edad, imprime puede obtener licencia
else: # Si es menor de edad
    if edad >= 16: # Verifica si tiene al menos 16 años
        if permiso_padres: # Verifica si tiene permiso de padres
            print('Puedes obtener la licencia con permiso de tus padres.') # Si tiene permiso, imprime puede obtener con permiso
        else: # Si no tiene permiso
            print('Necesitas el permiso de tus padres para obtener la licencia.') # Imprime que necesita permiso
    else: # Si es menor de 16
        print('Eres demasiado joven para conducir.') # Imprime demasiado joven
