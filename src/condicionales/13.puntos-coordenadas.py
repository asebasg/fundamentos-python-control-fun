punto = (0, 0) # Se define una variable indicando dos puntos

match punto: # Se hace un match case para determinar el punto
    case (0, 0): # Caso en donde el punto es 0,0
        print("El punto está en el origen.") # Muestra que el punto ingresado es el origen
    case (0, y): # Caso en donde el punto es 0,y
        print(f"El punto está en el eje Y en y={y}.") # Muestra que el punto ingresado es 0,y
    case (x, 0): # Caso en donde el punto es x,0
        print(f"El punto está en el eje X en x={x}.") # Muestra que el punto ingresado es x,0
    case (x, y): # Caso donde el punto es x,y
        print(f"El punto está en coordenadas x={x}, y={y}.") # Muestra que el punto ingresado es x,y
