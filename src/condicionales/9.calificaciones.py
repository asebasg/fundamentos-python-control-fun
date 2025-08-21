nota = 87 # Se declara la variable nota con valor 87

if nota >= 90: # Verifica si la nota es 90 o más
    print("Calificación: Sobresaliente") # Si es 90+, imprime Sobresaliente
elif nota >= 80: # Si no es 90+, verifica si es 80 o más
    print("Calificación: Notable") # Si es 80-89, imprime Notable
elif nota >= 70: # Si no es 80+, verifica si es 70 o más
    print("Calificación: Aprobado") # Si es 70-79, imprime Aprobado
else: # Si es menos de 70
    print("Calificación: Suspenso") # Imprime Suspenso
