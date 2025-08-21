edad = 20 # Se declara la variable edad con valor 20

match edad: # Estructura match-case para analizar la edad
    case edad if edad < 18: # Si la edad es menor a 18 (con guardia)
        print("Eres menor de edad.") # Imprime menor de edad
    case edad if edad >= 18 and edad < 65: # Si la edad está entre 18 y 64
        print("Eres adulto.") # Imprime adulto
    case edad if edad >= 65: # Si la edad es 65 o más
        print("Eres adulto mayor.") # Imprime adulto mayor
