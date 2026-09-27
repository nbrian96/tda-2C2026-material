"""
================================================================================
GUÍA 1: DIVISIÓN Y CONQUISTA
EJERCICIO 02: Detección del primer fallo en tests (Git Bisect)
DIFICULTAD: (★)
================================================================================

ENUNCIADO:
Se tiene un arreglo en el que se registran los resultados de tests automáticos
de una porción de código. Este código se encontraba funcionando pero, debido a unos
cambios que se están realizando, en algún momento dejó de funcionar.
Se registra un 1 si pasa los tests, 0 en caso contrario.
De esta manera, el arreglo tendrá la forma [1, 1, 1, ..., 0, 0, ...] (es decir,
unos seguidos de ceros).

Se pide:
a. Una función de orden O(log n) que, por división y conquista, encuentre el índice
   del primer 0, de forma que se pueda reconocer rápidamente en qué modificación del
   código se dejó de pasar los tests. Si no hay ningún 0 (solo hay unos), debe devolver -1.
b. Demostrar con el Teorema Maestro que la función es, en efecto, O(log n).

Ejemplos:
[1, 1, 0, 0, 0] → 2
[0, 0, 0, 0, 0] → 0
[1, 1, 1, 1, 1] → -1

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el arquetipo de "Búsqueda Binaria de la Primera Condición de Cambio" (First-Occurrence
  Binary Search). Es el principio exacto con el que opera `git bisect` en la vida real.
- Enseña a manejar invariantes de búsqueda: no buscamos un valor exacto, sino la frontera
  de transición de 1 a 0.

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Intuición / Puntos clave:
   - Mirá el punto medio `mid = (inicio + fin) // 2`.
   - Si `arr[mid] == 0`:
     * Este test ya falló. Pero ¿es el PRIMERO? Podría serlo, o el primero podría estar
       más a la izquierda.
     * Por lo tanto, NO descartes `mid`: tu nuevo rango de búsqueda a la izquierda debe ser
       `[inicio...mid]`.
   - Si `arr[mid] == 1`:
     * Este test pasó. Como los 1s están al principio, todos los anteriores a `mid`
       también pasaron.
     * El primer 0 DEBE estar estrictamente a la derecha: nuevo rango `[mid + 1...fin]`.
2. Casos base / Bordes:
   - Si el arreglo no contiene ceros (ej: `arr[fin] == 1`), devolvé -1.
   - Si `inicio == fin`, verificá si `arr[inicio] == 0` (retornar `inicio`) o no (retornar -1).
3. ¡Cuidado con la complejidad en Python!:
   - NUNCA uses slicing (`arr[:mid]` o `arr[mid:]`) en la recursión; en Python eso copia
     el arreglo y cuesta O(n), arruinando el O(log n).
   - Pasá siempre índices `inicio` y `fin` como parámetros de tu función auxiliar.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD (TEOREMA MAESTRO):
--------------------------------------------------------------------------------
La ecuación de recurrencia tiene la forma:
    T(n) = A * T(n / B) + O(n^C)

1. Identificar A, B y C:
   - A = 1: en cada paso se hace exactamente UNA sola llamada recursiva (se descarta la otra mitad).
   - B = 2: el rango de búsqueda se reduce a la mitad (n / 2).
   - C = 0: el trabajo en cada nivel (calcular `mid`, comparar `arr[mid] == 0`) es O(1) = O(n^0).

2. Aplicar el Teorema Maestro:
   - Calculamos log_B(A) = log_2(1) = 0.
   - Comparamos con C:
     Como log_B(A) == C  (0 == 0), aplica el CASO 2 del Teorema Maestro:
     T(n) = O(n^C * log n) = O(n^0 * log n) = O(log n).

3. Complejidad Espacial:
   - O(log n) por la profundidad del árbol de llamadas recursivas (call stack).
   - O(1) si lo resolvés en forma iterativa (con un bucle `while inicio <= fin:`).
"""

from typing import List


def buscar_primer_fallo(arr: List[int]) -> int:
    """
    Encuentra el índice del primer 0 en un arreglo de 1s seguidos de 0s.
    Debe ejecutarse en tiempo O(log n).
    Retorna el índice del primer 0, o -1 si no hay ninguno.
    """
    # TODO: Implementar la función auxiliar recursiva (o iterativa)
    # usando inicio y fin para no copiar el arreglo.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej02_primer_cero_tests.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 0, 0, 0], 2),
        ([0, 0, 0, 0, 0], 0),
        ([1, 1, 1, 1, 1], -1),
        ([1, 0], 1),
        ([0], 0),
        ([1], -1),
        ([1, 1, 1, 1, 1, 1, 0], 6),
    ]

    print("Probando solución de Ejercicio 02...")
    for arr, esperado in test_cases:
        resultado = buscar_primer_fallo(arr)
        assert resultado == esperado, f"Fallo con arr={arr}: esperado {esperado}, obtenido {resultado}"
        print(f"  OK: arr={arr} -> primer 0 en índice {resultado}")

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
