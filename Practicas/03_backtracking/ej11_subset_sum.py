"""
================================================================================
GUÍA 3: BACKTRACKING
EJERCICIO 11: Suma de Subconjuntos (Subset Sum)
DIFICULTAD: (★)
================================================================================

ENUNCIADO:
Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros
positivos L y un entero n devuelva todos los subconjuntos de L que suman exactamente n.

Ejemplo:
L = [1, 2, 3, 4, 5], n = 5
Subconjuntos que suman 5:
[[5], [2, 3], [1, 4], [1, 2, 2] (si hubiera duplicados), etc.]
Para L = [1, 2, 3, 4, 5], n = 5:
-> [1, 4], [2, 3], [5]

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el problema fundacional de "Generación de combinaciones con restricción numérica".
- Enseña dos técnicas esenciales de poda numérica:
  1) Poda por exceso: si la suma actual supera n, podar (porque todos los elementos
     son positivos y seguir sumando solo empeorará).
  2) Ordenamiento previo: ordenar L ascendentemente permite cortar el bucle inmediatamente
     apenas un elemento excede el remanente.

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Ordenar la lista L:
   - Si `L` está ordenada de menor a mayor, al iterar los candidatos desde el índice
     actual, si `L[i] > n - suma_actual`, no solo podés descartar `L[i]`, sino que podés
     hacer un `break` (¡ningún elemento posterior entrará porque son aún mayores!).
2. Estructura recursiva de combinaciones:
   - Para no generar permutaciones duplicadas (ej: `[1, 4]` y `[4, 1]`), en cada nivel
     solo considerás elementos a partir del índice `inicio` en adelante.
   - Parámetros útiles en la función recursiva:
     * `inicio`: índice desde donde explorar en L.
     * `suma_actual`: acumulación de los elementos elegidos.
     * `camino_actual`: lista con los elementos elegidos hasta ahora.
3. Casos base y podas:
   - Si `suma_actual == n`: ¡Encontraste una solución! Agregá una copia (`list(camino_actual)`)
     a la lista de resultados y retorná.
   - Si `suma_actual > n`: retorná (poda por exceso).

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
Sea k la cantidad de elementos en L:
- Cantidad de subconjuntos posibles: 2^k.
- En el peor caso (por ejemplo, cuando todos los subconjuntos suman <= n), el árbol
  de exploración visita los 2^k estados.
- Al encontrar una solución válida de tamaño m, copiar la lista toma O(m) = O(k).

Complejidad Temporal Peor Caso: O(k * 2^k).
Complejidad Espacial: O(k) por la profundidad de la pila de llamadas y el camino actual
(sin contar el espacio necesario para almacenar las soluciones finales encontradas).
"""

from typing import List


def subset_sum_todos(L: List[int], n: int) -> List[List[int]]:
    """
    Encuentra TODOS los subconjuntos de L que suman exactamente n usando Backtracking.
    Retorna una lista de listas con los subconjuntos solución.
    """
    # TODO: Implementar el backtracking con podas por exceso y ordenamiento.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej11_subset_sum.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando solución de Ejercicio 11 (Subset Sum)...")

    L1 = [1, 2, 3, 4, 5]
    target1 = 5
    res1 = subset_sum_todos(L1, target1)

    print(f"L = {L1}, target = {target1}")
    print(f"Subconjuntos que suman {target1}: {res1}")

    # Deben estar: [1, 4], [2, 3], [5]
    # Normalizamos orden interno de cada subconjunto para comparar
    res1_normalizado = sorted([sorted(sub) for sub in res1])
    esperado1 = sorted([[1, 4], [2, 3], [5]])
    assert res1_normalizado == esperado1, f"Esperado {esperado1}, obtenido {res1_normalizado}"

    # Caso 2: Ningún subconjunto suma el objetivo
    res2 = subset_sum_todos([10, 20, 30], 25)
    assert res2 == [], f"Esperado [], obtenido {res2}"

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
