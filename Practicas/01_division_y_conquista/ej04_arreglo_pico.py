"""
================================================================================
GUÍA 1: DIVISIÓN Y CONQUISTA
EJERCICIO 04: Arreglo en forma de pico (Peak Element)
DIFICULTAD: (★)
================================================================================

ENUNCIADO:
Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente
creciente hasta una determinada posición p, y estrictamente decreciente a partir
de ella (con 0 < p < N - 1).
Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2.

Se pide:
a. Implementar un algoritmo de división y conquista de complejidad O(log n) que
   encuentre la posición p del pico.
b. Justificar la complejidad del algoritmo mediante el Teorema Maestro.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el arquetipo MÁS FRECUENTE de parciales en FIUBA sobre D&C.
- Enseña que NO es necesario que un arreglo esté totalmente ordenado para aplicar
  búsqueda binaria: basta con tener una propiedad local (comparación con vecinos)
  que permita discernir inequívocamente hacia qué lado descartar la mitad.

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Intuición / Puntos clave:
   - Mirá el punto medio `mid = (inicio + fin) // 2` y su vecino adyacente `mid + 1`:
     * Si `arr[mid] < arr[mid + 1]`: estamos en la ladera que va subiendo.
       El pico NO puede estar a la izquierda de `mid`, está estrictamente a la
       derecha. Nuevo rango: `[mid + 1...fin]`.
     * Si `arr[mid] > arr[mid + 1]`: estamos bajando o parados exactamente en el pico.
       El pico está en `mid` o a su izquierda.
       Nuevo rango: `[inicio...mid]`.
2. Caso base:
   - Cuando `inicio == fin`, el único elemento restante es necesariamente el pico.
3. Trampa común:
   - ¡Cuidado con hacer `mid - 1` sin verificar si `mid > 0`! Comparar `arr[mid]` con
     `arr[mid + 1]` es más seguro porque la división entera `(inicio + fin) // 2`
     garantiza que `mid < fin` mientras `inicio < fin`.
   - Recordá pasar `inicio` y `fin` como parámetros de la función recursiva.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD (TEOREMA MAESTRO):
--------------------------------------------------------------------------------
Ecuación de recurrencia:
    T(n) = A * T(n / B) + O(n^C)

1. Parámetros:
   - A = 1: en cada paso se explora una sola rama (la otra mitad se descarta).
   - B = 2: el subarreglo se reduce a la mitad.
   - C = 0: calcular `mid` y comparar `arr[mid]` con `arr[mid + 1]` toma O(1) = O(n^0).

2. Teorema Maestro:
   - log_B(A) = log_2(1) = 0.
   - Como log_B(A) == C (0 == 0), aplica el CASO 2 del Teorema Maestro:
     T(n) = O(n^C * log n) = O(n^0 * log n) = O(log n).

3. Espacio:
   - O(log n) recursivo (profundidad de pila) u O(1) si es iterativo.
"""

from typing import List


def buscar_pico(arr: List[int]) -> int:
    """
    Encuentra la posición p (índice) del elemento pico en arr.
    Debe ejecutarse en tiempo O(log n).
    Retorna el índice del pico.
    """
    # TODO: Implementar la búsqueda binaria del pico
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej04_arreglo_pico.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1, 0, -2], 2),
        ([0, 10, 5, 2], 1),
        ([1, 3, 5, 7, 9, 8, 4], 4),
        ([-5, -1, 10, 20, 15, 0], 3),
        ([1, 5, 4], 1),
    ]

    print("Probando solución de Ejercicio 04...")
    for arr, esperado in test_cases:
        resultado = buscar_pico(arr)
        assert resultado == esperado, f"Fallo con arr={arr}: esperado {esperado}, obtenido {resultado}"
        print(f"  OK: arr={arr} -> pico en índice {resultado} (valor = {arr[resultado]})")

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
