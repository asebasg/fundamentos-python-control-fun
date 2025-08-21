edad = 17 # Se declara la variable edad con valor 17
permiso_parental = True # Se declara la variable permiso_parental con valor True

if (edad >= 18) or (edad >= 16 and permiso_parental): # Verifica: edad >=18 O (edad >=16 Y permiso_parental)
    print("Puedes obtener la licencia de conducir.") # Si cumple alguna condición, imprime puede obtener licencia
else: # Si no cumple ninguna condición
    print("No cumples los requisitos para la licencia.") # Imprime que no cumple requisitos
