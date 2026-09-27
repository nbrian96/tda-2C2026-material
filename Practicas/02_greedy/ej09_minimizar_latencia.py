"""
================================================================================
GUÍA 2: ALGORITMOS GREEDY
EJERCICIO 09: Minimizar la Latencia Máxima (Earliest Deadline First)
DIFICULTAD: (★★)
================================================================================

ENUNCIADO:
Tenemos tareas con una duración y un deadline (fecha límite), pero pueden hacerse
en cualquier momento, intentando que se hagan antes del deadline. Una tarea puede
completarse luego de su deadline, pero ello tendrá una penalización de latencia.
Para este problema, buscamos minimizar la latencia máxima en el que las tareas se ejecuten.
Es decir, dados los arreglos de: T (tiempo de duración de las tareas) y D (deadline de
cada tarea), si definimos que una tarea i empieza en S_i, entonces termina en F_i = S_i + T_i,
y su latencia es L_i = max(0, F_i - D_i). Nuestra latencia máxima será max_i L_i.

Implementar un algoritmo que defina en qué orden deben realizarse las tareas, sabiendo
que al terminar una tarea se puede empezar la siguiente inmediatamente.
Indicar y justificar la complejidad del algoritmo implementado.
Devolver un arreglo de tuplas, una por tarea, en el orden en que deben ser realizadas:
cada tupla indica (tiempo T_i de la tarea, latencia resultante L_i de esa tarea).
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.
¿Por qué se trata de un algoritmo Greedy? Justificar.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el caso canónico del método de demostración por "ARGUMENTO DE INTERCAMBIO"
  (Exchange Argument) para algoritmos Greedy.
- Muestra que ordenar por duración (Shortest Job First) o por holgura (Slack) NO funciona;
  la única regla óptima es Earliest Deadline First (EDF).

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Regla voraz:
   - Ordenar las tareas únicamente por su fecha límite creciente: `D_1 <= D_2 <= ... <= D_n`.
2. Cálculo de tiempos y latencias:
   - Mantener una variable `tiempo_actual = 0`.
   - Para cada tarea con duración `T_i` y deadline `D_i`:
     * Tiempo de finalización: `F_i = tiempo_actual + T_i`.
     * Latencia: `L_i = max(0, F_i - D_i)`.
     * Avanzar `tiempo_actual = F_i`.
3. Esquema del Argumento de Intercambio (para justificar en el examen):
   - Cualquier solución con una inversión adyacente (tarea i antes de j, con D_i > D_j)
     puede ser intercambiada sin aumentar la latencia máxima.
   - Dado que cualquier cronograma puede transformarse en el cronograma EDF mediante
     un número finito de intercambios adyacentes sin empeorar la solución, el orden
     EDF es óptimo.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
Sea n la cantidad de tareas:
1. Empaquetar y ordenar las n tareas por deadline D_i:
   - O(n log n).
2. Recorrido lineal calculando fin y latencia de cada una:
   - O(n).

Complejidad Temporal:
    T(n) = O(n log n).

Complejidad Espacial:
    O(n) para almacenar las tuplas y el cronograma planificado.
"""

from typing import List, Tuple


def planificar_min_latencia(
    duraciones: List[int],
    deadlines: List[int],
) -> Tuple[int, List[Tuple[int, int]]]:
    """
    Planifica tareas minimizando la latencia máxima usando EDF (Earliest Deadline First).
    Retorna: (latencia_maxima, [(duracion_i, latencia_i), ...])
    """
    # TODO: Implementar el algoritmo voraz EDF siguiendo los tips.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej09_minimizar_latencia.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    duraciones = [3, 2, 1, 4, 3, 2]
    deadlines = [6, 8, 9, 9, 14, 15]

    print("Probando solución de Ejercicio 09...")
    max_lat, plan = planificar_min_latencia(duraciones, deadlines)

    print(f"Latencia máxima obtenida: {max_lat}")
    print(f"Plan de tareas: {plan}")

    # En este caso clásico (Kleinberg & Tardos), la latencia máxima mínima posible es 1
    assert max_lat == 1, f"Se esperaba latencia máxima 1, se obtuvo {max_lat}"

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
