usuario = 'admin' # Se declara la variable usuario con valor 'admin'
contrasena = '1234' # Se declara la variable contrasena con valor '1234'

if usuario == 'admin': # Verifica si el usuario es 'admin'
    if contrasena == '1234': # Si es admin, verifica si la contraseña es '1234'
        print('Acceso concedido.') # Si ambas condiciones se cumplen, imprime acceso concedido
    else: # Si la contraseña es incorrecta
        print('Contraseña incorrecta.') # Imprime contraseña incorrecta
else: # Si el usuario no es 'admin'
    print('Usuario no reconocido.') # Imprime usuario no reconocido
