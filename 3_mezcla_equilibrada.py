"""
Ejercicio 3: Mezcla Equilibrada
Usa 4 secuencias (archivos simulados con listas): F1 y F2 de entrada, F3 y F4 de salida.
- Distribución inicial: la secuencia original se reparte en F1 y F2.
- Cada pasada mezcla las corridas (bloques ordenados) de F1 y F2 y las
  escribe de forma ALTERNADA en F3 y F4. Luego se invierten los papeles
  (F3 y F4 pasan a ser la entrada).
- Termina cuando todo queda en una sola corrida.
Complejidad O(n log n). Es la base del ordenamiento externo.
"""


def mezclar(b1, b2):
    i = j = 0
    res = []
    while i < len(b1) and j < len(b2):
        if b1[i] <= b2[j]:
            res.append(b1[i])
            i += 1
        else:
            res.append(b2[j])
            j += 1
    res.extend(b1[i:])
    res.extend(b2[j:])
    return res


def mezcla_equilibrada(datos):
    # Distribución inicial: corridas de tamaño 1 alternadas en F1 y F2
    entrada1 = [[x] for x in datos[0::2]]
    entrada2 = [[x] for x in datos[1::2]]
    pasada = 1

    while len(entrada1) + len(entrada2) > 1:
        salida1, salida2 = [], []
        destino = 1
        for idx in range(max(len(entrada1), len(entrada2))):
            c1 = entrada1[idx] if idx < len(entrada1) else []
            c2 = entrada2[idx] if idx < len(entrada2) else []
            corrida = mezclar(c1, c2)
            # Se alterna la salida entre las dos secuencias de destino
            (salida1 if destino == 1 else salida2).append(corrida)
            destino = 2 if destino == 1 else 1
        print(f"Pasada {pasada}: F_a={salida1} | F_b={salida2}")
        entrada1, entrada2 = salida1, salida2  # se invierten los papeles
        pasada += 1

    return entrada1[0] if entrada1 else entrada2[0]


if __name__ == "__main__":
    datos = [38, 27, 43, 3, 9, 82, 10, 15]
    print("Original:", datos)
    print("Ordenado:", mezcla_equilibrada(datos))
