transacciones = [  # Lista de transacciones
    {"id": 1, "monto": 1200, "estado": "completada"},
    {"id": 2, "monto": -50, "estado": "error"},
    {"id": 3, "monto": 800, "estado": "pendiente"},
    {"id": 4, "monto": 1500, "estado": "completada"},
    {"id": 5, "monto": 0, "estado": "cancelada"}
]

total_procesado = 0  # Inicializa total

for t in transacciones:  # Itera sobre cada transacción
    # Ignoramos transacciones no completadas
    if t["estado"] != "completada":  # Si no completada
        print(f"Transacción {t['id']}: {t['estado']} - ignorada")  # Imprime ignorada
        continue  # Salta

    # Verificamos montos válidos
    if t["monto"] <= 0:  # Si monto inválido
        print(f"Transacción {t['id']}: monto inválido ({t['monto']})")  # Imprime inválido
        continue  # Salta

    # Procesamos la transacción
    total_procesado += t["monto"]  # Suma al total
    print(f"Transacción {t['id']}: {t['monto']}€ procesada")  # Imprime procesada

print(f"Total procesado: {total_procesado}€")  # Imprime total
