"""
================================================================================
GUÍA 3: BACKTRACKING
EJERCICIO 03: Problema de las N Reinas (N-Queens)
DIFICULTAD: (★)
================================================================================

ENUNCIADO:
Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que
ubique (si es posible) a n reinas de tal manera que ninguna pueda comerse con ninguna.
(Dos reinas se comen si comparten la misma fila, columna o diagonal).

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el arquetipo MUNDIAL de Backtracking en tableros y colocación exacta.
- Enseña a estructurar el árbol de decisiones fila por fila en lugar de probar casillas
  al azar, reduciendo el espacio de búsqueda de C(n^2, n) a n!.
- Enseña el concepto de "Poda por factibilidad en O(1)" mediante conjuntos de diagonales.

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Estructura del árbol:
   - Dado que no pueden compartir fila, colocamos exactamente 1 reina por fila:
     `fila = 0, 1, ..., n-1`.
   - Para la fila actual, iteramos probando cada columna `col` de `0` a `n-1`.
2. Detección de conflictos en O(1):
   - Mantené tres conjuntos (sets o arrays booleanos):
     * `cols`: columnas ocupadas.
     * `diag1`: valores de `fila - col` (diagonal descendente).
     * `diag2`: valores de `fila + col` (diagonal ascendente).
   - Si `col in cols` o `(fila - col) in diag1` o `(fila + col) in diag2`,
     ¡PODAR! (continue, esa posición no es válida).
3. Mecánica del Backtracking:
   - Tomar decisión: agregar columna a la solución actual y registrar en los sets.
   - Recursión: `if backtrack(fila + 1): return True` (si buscamos 1 solución).
   - Deshacer decisión: quitar de la solución y de los sets.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
- En el peor caso (árbol podado por columnas):
  * Fila 0: n opciones.
  * Fila 1: (n - 1) opciones.
  * Fila k: (n - k) opciones.
  Cantidad máxima de estados: O(n!).
- Con las podas de diagonales, la cantidad real de nodos explorados es una fracción
  diminuta de n!, lo que permite resolverlo en milisegundos para n=8 o n=10.
- Costo por nodo: O(1) con verificación en sets.

Complejidad Temporal Peor Caso: O(n!).
Complejidad Espacial: O(n) para almacenar el tablero y los sets de diagonales.
"""

from typing import List, Optional


def resolver_n_reinas(n: int) -> Optional[List[int]]:
    """
    Ubica n reinas en un tablero n x n sin conflictos.
    Retorna una lista de tamaño n donde la posición i contiene la columna de la reina en la fila i.
    Si no hay solución, retorna None.
    """
    # TODO: Implementar el algoritmo de Backtracking siguiendo los tips
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej03_n_reinas.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando solución de Ejercicio 03 (N-Reinas)...")

    for n in [4, 5, 8]:
        sol = resolver_n_reinas(n)
        assert sol is not None, f"Debió encontrar solución para n={n}"
        print(f"  OK: n={n} -> Solución (columnas por fila): {sol}")

        # Verificar que no haya conflictos
        for r1 in range(n):
            for r2 in range(r1 + 1, n):
                c1, c2 = sol[r1], sol[r2]
                assert c1 != c2, f"Conflicto de columna entre filas {r1} y {r2}"
                assert abs(r1 - r2) != abs(c1 - c2), f"Conflicto de diagonal entre filas {r1} y {r2}"

    assert resolver_n_reinas(2) is None, "Para n=2 no debe haber solución"
    assert resolver_n_reinas(3) is None, "Para n=3 no debe haber solución"
    print("  OK: n=2 y n=3 retornan None (no tienen solución)")

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
