edad = 16 # Se declara la variable edad con valor 16
permiso_padres = True # Se declara la variable permiso_padres con valor True

if edad >= 18: # Verifica si la edad es 18 o más
    print('Puedes obtener la licencia de conducir.') # Si es mayor de edad, imprime puede obtener licencia
elif edad >= 16 and permiso_padres: # Si tiene entre 16-17 años Y tiene permiso
    print('Puedes obtener la licencia con permiso de tus padres.') # Imprime puede obtener con permiso
elif edad >= 16 and not permiso_padres: # Si tiene entre 16-17 años Y NO tiene permiso
    print('Necesitas el permiso de tus padres para obtener la licencia.') # Imprime que necesita permiso
else: # Si es menor de 16
    print('Eres demasiado joven para conducir.') # Imprime demasiado joven
