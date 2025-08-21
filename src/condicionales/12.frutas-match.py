fruta = input("Introduzca una fruta: ") # Solicita al usuario que introduzca una fruta

match fruta: # Estructura match-case para comparar la fruta
    case "manzana": # Si la fruta es "manzana"
        print("La fruta es una manzana.") # Imprime que es manzana
    case "naranja": # Si la fruta es "naranja"
        print("La fruta es una naranja.") # Imprime que es naranja
    case "plátano": # Si la fruta es "plátano"
        print("La fruta es un plátano.") # Imprime que es plátano
    case _: # Para cualquier otro caso (default)
        print("Fruta desconocida.") # Imprime fruta desconocida
