"""
================================================================================
GUÍA 4: PROGRAMACIÓN DINÁMICA
EJERCICIO 08: Problema del Cambio de Monedas (Coin Change - Mínimas Monedas)
DIFICULTAD: (★★)
================================================================================

ENUNCIADO:
Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar “cambio” de una
determinada cantidad de plata. Se desea devolver el cambio pedido, usando la mínima
cantidad de monedas/billetes.
Implementar un algoritmo que, por programación dinámica, reciba un arreglo de valores
del sistema monetario, y la cantidad de cambio objetivo a dar, y devuelva qué
monedas/billetes deben ser utilizados para minimizar la cantidad total utilizada
(hacer la reconstrucción).
Indicar y justificar la complejidad del algoritmo implementado.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Enseña la diferencia entre sistemas monetarios CANÓNICOS (donde Greedy funciona) y
  sistemas arbitrarios (ej: monedas de 1, 3, 4 centavos para dar 6 centavos:
  Greedy daría 4 + 1 + 1 = 3 monedas, pero el óptimo es 3 + 3 = 2 monedas).
- Muestra el patrón de subproblemas no acotados (unbounded knapsack / coin change),
  donde cada subproblema itera sobre todas las denominaciones disponibles.

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Definición formal del estado:
   - Sea `OPT(m)` la MÍNIMA cantidad de monedas necesarias para formar el monto exacto `m`,
     para todo `0 <= m <= M` (donde M es el cambio objetivo).
2. Ecuación de recurrencia:
   - Para formar el monto `m`, probamos usar como última moneda cualquier denominación `c`
     disponible tal que `c <= m`:
       OPT(m) = 1 + min_{c in monedas, c <= m} (OPT(m - c))
   - Caso base:
     * `OPT(0) = 0` (para dar monto 0 se necesitan 0 monedas).
     * Si un monto no se puede formar, `OPT(m) = +inf`.
3. Reconstrucción de las monedas elegidas:
   - Mantené un arreglo auxiliar `ultima_moneda[m] = c` que guarde qué moneda `c`
     produjo el mínimo para el monto `m`.
   - Para reconstruir, empezá en `m = M` y hacé:
     * `c = ultima_moneda[m]`
     * Agregar `c` a la lista de cambio
     * `m = m - c`
     * Repetir mientras `m > 0`.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
Sea M el monto objetivo y K la cantidad de tipos de monedas disponibles:
- Cantidad de subproblemas (estados):
  M + 1 estados (de 0 a M).
- Costo por estado:
  Para calcular `OPT(m)`, se itera sobre las K denominaciones y se toma el mínimo:
  O(K).
- Llenado de la tabla DP:
  (M + 1) * O(K) = O(M * K).
- Reconstrucción:
  A lo sumo M pasos (en el peor caso de dar todo en monedas de valor 1): O(M).

Complejidad Temporal Total:
    O(M * K) — Complejidad Pseudo-polinomial (depende del valor numérico M).

Complejidad Espacial:
    O(M) para almacenar el arreglo `OPT` y el arreglo `ultima_moneda`.
"""

from typing import List, Tuple


def dar_cambio_dp(monedas: List[int], monto: int) -> Tuple[int, List[int]]:
    """
    Calcula la mínima cantidad de monedas para formar el monto y reconstruye cuáles usar.
    Retorna: (cantidad_minima_monedas, lista_de_monedas_usadas)
    Si no es posible formar el monto, retorna (inf, []).
    """
    # TODO: Implementar la tabla DP y la reconstrucción siguiendo los tips.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej08_cambio_monedas.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando solución de Ejercicio 08 (Cambio de Monedas DP)...")

    # Caso 1: Sistema NO canónico donde Greedy falla
    # Monedas: [1, 3, 4], Monto: 6
    # Greedy tomaría 4 + 1 + 1 (3 monedas).
    # DP óptimo debe dar 3 + 3 (2 monedas).
    monedas1 = [1, 3, 4]
    monto1 = 6
    cant1, usadas1 = dar_cambio_dp(monedas1, monto1)
    print(f"Monedas: {monedas1}, Monto: {monto1}")
    print(f"  Resultado: Mínimas monedas = {cant1}, Monedas usadas = {usadas1}")
    assert cant1 == 2, f"Esperado 2 monedas, obtenido {cant1}"
    assert sum(usadas1) == monto1, f"La suma de las monedas debe dar {monto1}"

    # Caso 2: Sistema estándar con monedas [1, 5, 10, 25, 50], Monto: 63
    # 50 + 10 + 1 + 1 + 1 (5 monedas)
    monedas2 = [1, 5, 10, 25, 50]
    monto2 = 63
    cant2, usadas2 = dar_cambio_dp(monedas2, monto2)
    print(f"Monedas: {monedas2}, Monto: {monto2}")
    print(f"  Resultado: Mínimas monedas = {cant2}, Monedas usadas = {usadas2}")
    assert cant2 == 6 or cant2 == 5  # 50 + 10 + 1*3 = 5 monedas
    assert sum(usadas2) == monto2

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
