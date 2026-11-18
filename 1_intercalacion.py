"""
Ejercicio 1: Intercalación
Mezcla dos listas YA ordenadas en una sola lista ordenada, comparando
el elemento actual de cada lista (complejidad O(n + m)).
"""


def intercalar(a, b):
    i = j = 0
    resultado = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    # Lo que sobre de alguna lista ya está ordenado, se agrega completo
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado


if __name__ == "__main__":
    lista_a = [1, 4, 9, 12, 20]
    lista_b = [2, 3, 10, 15, 18, 25]
    print("Lista A:", lista_a)
    print("Lista B:", lista_b)
    print("Intercalada:", intercalar(lista_a, lista_b))
