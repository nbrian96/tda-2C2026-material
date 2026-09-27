"""
================================================================================
GUÍA 4: PROGRAMACIÓN DINÁMICA
EJERCICIO 07: Problema de la Mochila 0-1 (0-1 Knapsack)
DIFICULTAD: (★★★)
================================================================================

ENUNCIADO:
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene
un valor, y un peso que ocupa de la capacidad total.
Queremos maximizar el valor de lo que llevamos sin exceder la capacidad.
Implementar un algoritmo que, por programación dinámica, reciba los valores y pesos
de los elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia
total (hacer la reconstrucción).
Indicar y justificar la complejidad del algoritmo implementado.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el arquetipo MUNDIAL de Programación Dinámica en 2 Dimensiones.
- Enseña la diferencia entre complejidad polinomial y PSEUDO-POLINOMIAL: la complejidad
  depende numéricamente de la capacidad W (que se codifica en log W bits).
- Muestra la reconstrucción bidimensional retrocediendo a través de la matriz DP.
- Conecta directamente con la formulación en Programación Lineal (Ejercicio 1 de PL).

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Definición formal del estado:
   - Sea `OPT(i, w)` el máximo valor que se puede obtener considerando únicamente los
     primeros `i` elementos (con `0 <= i <= n`) y disponiendo de una capacidad máxima `w`
     (con `0 <= w <= W`).
2. Ecuación de recurrencia para el elemento `i` (con peso `peso_i` y valor `valor_i`):
   - Si `peso_i > w`: el elemento no entra en la mochila con capacidad `w`.
     * `OPT(i, w) = OPT(i - 1, w)`
   - Si `peso_i <= w`: tenemos dos opciones:
     * No tomar el elemento `i`: valor = `OPT(i - 1, w)`
     * Sí tomar el elemento `i`: valor = `valor_i + OPT(i - 1, w - peso_i)`
     * Por lo tanto:
       OPT(i, w) = max(OPT(i - 1, w), valor_i + OPT(i - 1, w - peso_i))
3. Casos base:
   - `OPT(0, w) = 0` para todo `w` (con 0 elementos el valor es 0).
   - `OPT(i, 0) = 0` para todo `i` (con capacidad 0 no entra nada).
4. Reconstrucción de la solución:
   - Empezá desde `i = n` y `w = W`:
     * Si `OPT(i, w) == OPT(i - 1, w)`: el elemento `i` no fue incluido en la solución.
       Avanzás a `i = i - 1`, manteniendo la misma capacidad `w`.
     * Si `OPT(i, w) != OPT(i - 1, w)`: el elemento `i - 1` (índice 0-based) SÍ fue tomado.
       Lo agregás a la lista de seleccionados y retrocedés a `i = i - 1` y `w = w - peso_{i-1}`.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
Sea n la cantidad de elementos y W la capacidad máxima entera de la mochila:
- Tamaño de la tabla DP:
  Matriz de dimensiones (n + 1) x (W + 1).
  Cantidad total de estados = (n + 1) * (W + 1).
- Costo por estado:
  Calcular el máximo entre dos valores es O(1).
- Tiempo de llenado de la matriz:
  O(n * W).
- Tiempo de reconstrucción:
  Se realiza a lo sumo n pasos hacia atrás: O(n).

Complejidad Temporal Total:
    O(n * W) — Complejidad PSEUDO-POLINOMIAL (polinomial respecto a n y W, pero
    exponencial respecto a la cantidad de bits necesarios para representar W).

Complejidad Espacial:
    O(n * W) para la matriz bidimensional de programación dinámica.
"""

from typing import List, Tuple


def mochila_01(
    valores: List[int],
    pesos: List[int],
    capacidad: int,
) -> Tuple[int, List[int]]:
    """
    Resuelve el problema de la Mochila 0-1 por Programación Dinámica.
    Retorna: (valor_maximo, indices_elementos_elegidos)
    Donde indices_elementos_elegidos son los índices originales de los items en valores/pesos.
    """
    # TODO: Implementar la matriz DP y la reconstrucción siguiendo los tips.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej07_mochila_01.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando solución de Ejercicio 07 (Mochila 0-1)...")

    # Caso del contraejemplo de Greedy:
    # W = 50
    # Items: (val=60, peso=10), (val=100, peso=20), (val=120, peso=30)
    # Greedy elegía 0 y 1 (peso 30, val 160).
    # DP Óptimo debe elegir 1 y 2 (peso 50, val 220).
    valores1 = [60, 100, 120]
    pesos1 = [10, 20, 30]
    W1 = 50

    val_max1, elegidos1 = mochila_01(valores1, pesos1, W1)
    print(f"Items: valores={valores1}, pesos={pesos1}, W={W1}")
    print(f"  Resultado: Valor máximo = {val_max1}, Indices elegidos = {elegidos1}")

    assert val_max1 == 220, f"Esperado 220, obtenido {val_max1}"
    assert sorted(elegidos1) == [1, 2], f"Esperado items [1, 2], obtenido {elegidos1}"

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
