acceso_registrado = True # Se declara acceso_registrado como True
acceso_permitido = False # Se declara acceso_permitido como False

if acceso_permitido or acceso_registrado: # Cortocircuito OR: si acceso_permitido es False, evalúa acceso_registrado
    print("Acceso concedido.") # Se ejecuta porque acceso_registrado es True
