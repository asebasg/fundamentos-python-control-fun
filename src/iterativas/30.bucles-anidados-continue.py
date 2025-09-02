for i in range(1, 4):  # Bucle externo para grupos
    print(f"Grupo {i}:")  # Imprime grupo

    for j in range(1, 6):  # Bucle interno para elementos
        if j == 3:  # Si es el elemento 3
            print("  Saltando el elemento 3")  # Imprime mensaje
            continue  # Salta solo el bucle interno

        print(f"  Elemento {j}")  # Imprime elemento

    print("Fin del grupo\n")  # Imprime fin de grupo
