"""
================================================================================
GUÍA 4: PROGRAMACIÓN DINÁMICA
EJERCICIO 04: Juan el Vago (Independent Set Ponderado en Camino / House Robber)
DIFICULTAD: (★★)
================================================================================

ENUNCIADO:
Juan es ambicioso pero también algo vago. Dispone de varias ofertas de trabajo diarias,
pero no quiere trabajar dos días seguidos.
Dado un arreglo con el monto esperado a ganar cada día, determinar, por programación
dinámica, el máximo monto a ganar, sabiendo que no aceptará trabajar dos días seguidos.
Hacer una reconstrucción para verificar qué días debe trabajar.
Indicar y justificar la complejidad del algoritmo implementado.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es EL PROBLEMA DE INTRODUCCIÓN OBLIGATORIA a la Programación Dinámica 1D.
- Enseña los 3 pilares indispensables de DP:
  1) Definición formal del estado en palabras.
  2) Ecuación de recurrencia y casos base.
  3) Algoritmo de reconstrucción de la solución óptima (no solo devolver el número,
     sino qué días trabajó).
- Aparece repetidamente conectado con Programación Lineal (Ejercicio 2 de la guía 5).

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Definición formal del subproblema / estado:
   - Sea `OPT(i)` la máxima ganancia posible considerando únicamente las ofertas
     desde el día 0 hasta el día `i`.
2. Decisiones para el día `i`:
   - Juan tiene 2 opciones:
     * OPCIÓN A: NO TRABAJAR el día `i`. La ganancia máxima será simplemente `OPT(i - 1)`.
     * OPCIÓN B: TRABAJAR el día `i`. Gana `ganancias[i]`, pero como no puede trabajar
       dos días seguidos, NO puede trabajar el día `i - 1`. Por lo tanto, se suma a la
       mejor ganancia hasta el día `i - 2`: `ganancias[i] + OPT(i - 2)`.
   - Ecuación de recurrencia:
       OPT(i) = max(OPT(i - 1), ganancias[i] + OPT(i - 2))
3. Casos base:
   - Si no hay días: ganancia = 0.
   - `OPT(0) = ganancias[0]` (si hay 1 solo día, trabaja ese día).
   - `OPT(1) = max(ganancias[0], ganancias[1])` (elige el mejor de los dos primeros días).
4. Reconstrucción de los días trabajados:
   - Para saber qué días trabajó, empezá desde el último día `i = n - 1` y retrocedé:
     * Si `OPT(i) == OPT(i - 1)`: significa que el día `i` NO se trabajó (la ganancia vino
       del día anterior). Avanzás a `i = i - 1`.
     * Si no (`OPT(i) == ganancias[i] + OPT(i - 2)`): significa que el día `i` SÍ se trabajó.
       Agregás `i` a la lista de días y saltás a `i = i - 2`.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
Sea n la cantidad de días:
- Cantidad de subproblemas (estados): n estados (de 0 a n - 1).
- Costo de resolver cada estado:
  Calcular `max(OPT(i - 1), ganancias[i] + OPT(i - 2))` toma O(1) operaciones aritméticas.
- Tiempo de llenado de la tabla (tabulación): n * O(1) = O(n).
- Tiempo de reconstrucción:
  El índice `i` decrece en al menos 1 unidad en cada paso hasta llegar a 0: O(n).

Complejidad Temporal Total:
    T(n) = O(n) [cómputo de la tabla] + O(n) [reconstrucción] = O(n).

Complejidad Espacial:
    O(n) para almacenar la tabla DP de tamaño n (o O(1) si solo se busca el valor máximo
    sin reconstruir, guardando las últimas 2 variables).
"""

from typing import List, Tuple


def juan_el_vago(ganancias: List[int]) -> Tuple[int, List[int]]:
    """
    Calcula la máxima ganancia sin trabajar dos días seguidos y reconstruye los días elegidos.
    - ganancias: lista donde ganancias[i] es lo que se gana trabajando el día i.
    Retorna: (ganancia_maxima, dias_trabajados)
    Donde dias_trabajados es la lista de índices de días elegidos (en orden cronológico).
    """
    # TODO: Implementar la tabulación y la reconstrucción siguiendo los tips.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej04_juan_el_vago.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando solución de Ejercicio 04 (Juan el Vago)...")

    # Caso 1: [10, 5, 2, 20, 15]
    # Días posibles: día 0 ($10) + día 3 ($20) = $30
    # O día 1 ($5) + día 4 ($15) = $20
    # O día 0 ($10) + día 4 ($15) = $25
    # Mejor: Día 0 y Día 3 -> Total 30
    ganancias1 = [10, 5, 2, 20, 15]
    max_gan1, dias1 = juan_el_vago(ganancias1)
    print(f"Ganancias: {ganancias1}")
    print(f"  Resultado: Ganancia máxima = {max_gan1}, Días = {dias1}")
    assert max_gan1 == 30, f"Esperado 30, obtenido {max_gan1}"
    assert dias1 == [0, 3], f"Esperado días [0, 3], obtenido {dias1}"

    # Caso 2: [50, 10, 10, 50] -> días 0 y 3 -> $100
    ganancias2 = [50, 10, 10, 50]
    max_gan2, dias2 = juan_el_vago(ganancias2)
    print(f"Ganancias: {ganancias2}")
    print(f"  Resultado: Ganancia máxima = {max_gan2}, Días = {dias2}")
    assert max_gan2 == 100
    assert dias2 == [0, 3]

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
