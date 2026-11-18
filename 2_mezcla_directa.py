"""
Ejercicio 2: Mezcla Directa
Usa 3 secuencias: la original (F) y dos auxiliares (F1 y F2).
Paso 1 (distribución): se reparten bloques de tamaño 'tam' alternadamente en F1 y F2.
Paso 2 (mezcla): se mezclan los bloques de F1 y F2 de regreso en F.
El tamaño del bloque se duplica (1, 2, 4, 8...) hasta que 'tam' >= n.
Complejidad O(n log n).
"""


def mezclar_bloques(b1, b2):
    """Mezcla dos bloques ordenados."""
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


def mezcla_directa(F):
    n = len(F)
    tam = 1
    while tam < n:
        # Distribución en F1 y F2
        F1, F2 = [], []
        for k in range(0, n, tam):
            bloque = F[k:k + tam]
            if (k // tam) % 2 == 0:
                F1.append(bloque)
            else:
                F2.append(bloque)
        # Mezcla de regreso en F
        F = []
        for idx in range(len(F1)):
            b2 = F2[idx] if idx < len(F2) else []
            F.extend(mezclar_bloques(F1[idx], b2))
        print(f"Bloques de tamaño {tam}: {F}")
        tam *= 2
    return F


if __name__ == "__main__":
    datos = [38, 27, 43, 3, 9, 82, 10, 15]
    print("Original:", datos)
    print("Ordenado:", mezcla_directa(datos))
