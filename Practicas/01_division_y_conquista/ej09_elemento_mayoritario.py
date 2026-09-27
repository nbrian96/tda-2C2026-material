"""
================================================================================
GUÍA 1: DIVISIÓN Y CONQUISTA
EJERCICIO 09: Elemento Mayoritario (Majority Element)
DIFICULTAD: (★★★)
================================================================================

ENUNCIADO:
Implementar una función, que utilice división y conquista, de complejidad O(n log n)
que dado un arreglo de n números enteros devuelva True o False según si existe algún
elemento que aparezca estrictamente más de la mitad de las veces (> n / 2).
Justificar la complejidad de la solución.

Ejemplos:
[1, 2, 1, 2, 3]       -> False
[1, 1, 2, 3]          -> False
[1, 2, 3, 1, 1, 1]    -> True (el 1 aparece 4 veces de 6, 4 > 3)
[1]                   -> True

Aclaración de la cátedra:
Este ejercicio puede resolverse ordenando en O(n log n) o con tabla de hash en O(n).
Para cumplir con la consigna, resolver sin ordenar ni usar hash, sino PURAMENTE
por División y Conquista.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Ejemplifica la estructura clásica de D&C donde se resuelven DOS subproblemas
  independientes (A = 2) y la etapa de combinación requiere trabajo lineal (C = 1).
- Enseña la deducción lógica de subproblemas: si un elemento domina el total,
  por fuerza debe dominar al menos una de las dos mitades.

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Propiedad matemática de la mayoría:
   - Si un elemento X aparece más de n/2 veces en el arreglo completo, es IMPOSIBLE
     que aparezca <= (mitad/2) en ambas mitades.
   - Por ende: X DEBE ser el elemento mayoritario en la mitad izquierda, en la mitad
     derecha, o en ambas.
2. Esquema recursivo:
   - Dividir:
     * Llamar recursivamente a la mitad izquierda `[inicio...mid]` -> candidato_izq.
     * Llamar recursivamente a la mitad derecha `[mid+1...fin]` -> candidato_der.
   - Combinar:
     * Si `candidato_izq == candidato_der`: ese es el candidato del rango combinado.
     * Si son distintos: contar cuántas veces aparece `candidato_izq` y cuántas veces
       aparece `candidato_der` en `arr[inicio...fin]` (un recorrido lineal O(n)).
     * Si alguno aparece más de `(fin - inicio + 1) // 2` veces, ese es el ganador
       del subrango; de lo contrario, retornar `None`.
3. Verificación final:
   - Al retornar el candidato final en la llamada principal, verificar si efectivamente
     aparece más de `len(arr) // 2` en el arreglo completo.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD (TEOREMA MAESTRO):
--------------------------------------------------------------------------------
Ecuación de recurrencia:
    T(n) = A * T(n / B) + O(n^C)

1. Parámetros:
   - A = 2: se resuelven recursivamente 2 subproblemas (mitad izquierda y derecha).
   - B = 2: cada mitad tiene tamaño n / 2.
   - C = 1: en la combinación, contar las ocurrencias de los candidatos en el rango
     actual toma tiempo proporcional al tamaño del subarreglo: O(n) = O(n^1).

2. Teorema Maestro:
   - log_B(A) = log_2(2) = 1.
   - Como log_B(A) == C (1 == 1), aplica el CASO 2 del Teorema Maestro:
     T(n) = O(n^C * log n) = O(n^1 * log n) = O(n log n).

3. Espacio:
   - O(log n) por la profundidad del árbol de recursión.
"""

from typing import List


def tiene_elemento_mayoritario(arr: List[int]) -> bool:
    """
    Determina si existe un elemento que aparece estrictamente más de n // 2 veces.
    Debe resolverse por División y Conquista en O(n log n), sin ordenar ni usar hash.
    Retorna True si existe, False en caso contrario.
    """
    # TODO: Implementar la función recursiva que busca el candidato
    # y combina contando ocurrencias en O(n).
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej09_elemento_mayoritario.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 1, 2, 3], False),
        ([1, 1, 2, 3], False),
        ([1, 2, 3, 1, 1, 1], True),
        ([1], True),
        ([2, 2], True),
        ([3, 3, 4, 2, 4, 4, 2, 4, 4], True),  # 4 aparece 5 de 9
        ([1, 2, 3, 4, 5, 6], False),
    ]

    print("Probando solución de Ejercicio 09...")
    for arr, esperado in test_cases:
        resultado = tiene_elemento_mayoritario(arr)
        assert resultado == esperado, f"Fallo con arr={arr}: esperado {esperado}, obtenido {resultado}"
        print(f"  OK: arr={arr} -> ¿Mayoría?: {resultado}")

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
