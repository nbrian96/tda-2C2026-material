"""
================================================================================
GUÍA 4: PROGRAMACIÓN DINÁMICA
EJERCICIO 02: Selección de Charlas Ponderadas (Weighted Interval Scheduling)
DIFICULTAD: (★★★)
================================================================================

ENUNCIADO:
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin.
Además, cada charla tiene asociado un valor de ganancia (peso).
Implementar un algoritmo que, utilizando programación dinámica, reciba un arreglo que
en cada posición tenga una charla representada por una tripla (inicio, fin, valor),
e indique cuáles son las charlas a dar para maximizar la ganancia total obtenida
(realizando la reconstrucción).
Indicar y justificar la complejidad del algoritmo implementado.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Contrasta directamente con el Interval Scheduling no ponderado de Greedy (Guía 2, Ej 4).
  En cuanto las charlas tienen valores/ganancias arbitrarias, ¡GREEDY DEJA DE SER ÓPTIMO!
  Se requiere Programación Dinámica.
- Enseña la técnica híbrida: ORDENAMIENTO + BÚSQUEDA BINARIA + PROGRAMACIÓN DINÁMICA.
  Es uno de los algoritmos más elegantes de toda la materia, logrando tiempo O(n log n).

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Ordenamiento inicial:
   - Ordenar todas las charlas por horario de finalización creciente:
     `fin_1 <= fin_2 <= ... <= fin_n`.
2. Función de predecesor compatible p(i):
   - Para la charla `i`, definimos `p(i)` como el índice de la charla compatible
     más cercana que termina ANTES o IGUAL a que empiece la charla `i`:
       `p(i) = mayor j < i tal que fin_j <= inicio_i` (o 0 si no existe ninguna).
   - ¿Cómo calcular `p(i)` eficientemente?
     Como las charlas están ordenadas por horario de finalización, ¡podés encontrar
     `p(i)` usando BÚSQUEDA BINARIA en O(log n) en vez de un for lineal!
3. Ecuación de recurrencia (Estado 1D):
   - Sea `OPT(i)` la máxima ganancia usando un subconjunto de charlas compatibles
     elegidas entre las primeras `i` charlas.
   - Para la charla `i`:
     * Opción A (No incluir la charla i): ganancia = `OPT(i - 1)`
     * Opción B (Sí incluir la charla i): ganancia = `valor_i + OPT(p(i))`
     * Recurrencia:
         OPT(i) = max(OPT(i - 1), valor_i + OPT(p(i)))
   - Caso base: `OPT(0) = 0`.
4. Reconstrucción:
   - Retroceder desde `i = n`:
     * Si `OPT(i) == OPT(i - 1)`: la charla `i` no se tomó -> `i = i - 1`.
     * Si no: la charla `i` SÍ se tomó -> agregar a la lista y saltar a `i = p(i)`.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
Sea n la cantidad de charlas:
1. Ordenar las n charlas por horario de finalización:
   O(n log n).
2. Precalcular `p(i)` para cada charla i de 1 a n:
   Para cada una de las n charlas, una búsqueda binaria en la lista ordenada toma O(log n).
   Total para todas las charlas: n * O(log n) = O(n log n).
3. Llenado de la tabla DP (n estados):
   Cada estado hace 1 lookup y 1 max en O(1).
   Total: O(n).
4. Reconstrucción:
   A lo sumo n pasos: O(n).

Complejidad Temporal Total:
    T(n) = O(n log n) [ordenar y búsqueda binaria] + O(n) [DP y reconstrucción] = O(n log n).

Complejidad Espacial:
    O(n) para almacenar el ordenamiento, el arreglo p(i), y la tabla OPT.
"""

from typing import List, Tuple

# Representación: Tupla (inicio, fin, valor)
CharlaPonderada = Tuple[float, float, float]


def interval_scheduling_ponderado(
    charlas: List[CharlaPonderada],
) -> Tuple[float, List[CharlaPonderada]]:
    """
    Maximiza la ganancia total eligiendo charlas compatibles sin superposición horaria.
    Debe ejecutarse en tiempo O(n log n).
    Retorna: (ganancia_maxima, charlas_elegidas)
    """
    # TODO: Implementar el ordenamiento, búsqueda binaria de p(i), DP y reconstrucción.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej02_interval_scheduling_ponderado.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando solución de Ejercicio 02 (Weighted Interval Scheduling)...")

    # Charlas: (inicio, fin, valor)
    # Charla 1: (1, 4, 10)
    # Charla 2: (3, 5, 50)  <- Muy valiosa, dura de 3 a 5
    # Charla 3: (0, 6, 20)
    # Charla 4: (5, 7, 30)  <- Compatible con la 2 (empieza en 5)
    # Charla 5: (6, 9, 25)
    # Si tomamos Charla 2 ($50) y Charla 4 ($30), son compatibles (fin 5 <= inicio 5)
    # Total = $80. Cualquier otra combinación da menos.
    charlas_test = [
        (1, 4, 10),
        (3, 5, 50),
        (0, 6, 20),
        (5, 7, 30),
        (6, 9, 25),
    ]

    gan_max, elegidas = interval_scheduling_ponderado(charlas_test)
    print(f"Ganancia máxima obtenida: {gan_max}")
    print(f"Charlas elegidas: {elegidas}")

    assert gan_max == 80.0, f"Esperado 80.0, obtenido {gan_max}"

    # Verificar que no se superpongan
    elegidas_ordenadas = sorted(elegidas, key=lambda c: c[0])
    for i in range(len(elegidas_ordenadas) - 1):
        assert elegidas_ordenadas[i][1] <= elegidas_ordenadas[i + 1][0], "Superposición detectada!"

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
