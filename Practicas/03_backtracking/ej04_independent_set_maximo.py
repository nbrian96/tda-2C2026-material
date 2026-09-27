"""
================================================================================
GUÍA 3: BACKTRACKING
EJERCICIO 04: Conjunto Independiente Máximo (Maximum Independent Set)
DIFICULTAD: (★★)
================================================================================

ENUNCIADO:
Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto
de vértices que representen un máximo Independent Set del mismo.
(Un Independent Set o Conjunto Independiente es un subconjunto de vértices tal que
ningún par de vértices en dicho subconjunto es adyacente entre sí).

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el arquetipo de "Subset Selection sobre Grafos" en problemas NP-Hard.
- Enseña la diferencia entre DOS tipos de poda:
  1) PODA POR FACTIBILIDAD: si agrego un vértice que es adyacente a otro ya elegido,
     la solución deja de ser válida.
  2) PODA POR OPTIMALIDAD (Branch and Bound): si la cantidad actual de vértices más
     todos los que faltan evaluar no supera al mejor récord histórico, podar la rama.

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Árbol binario de decisión (Inclusión / Exclusión):
   - Ordená los vértices en una lista `v_0, v_1, ..., v_{n-1}`.
   - En cada llamada recursiva analizás el vértice `v_i`:
     * OPCIÓN 1 (Incluir v_i):
       - Solo es factible si NINGÚN vecino de `v_i` está ya en el conjunto `actual`.
       - Si es factible: agregás `v_i` a `actual`, llamás a `backtrack(i + 1)` y luego
         lo removés (deshacer).
     * OPCIÓN 2 (Excluir v_i):
       - Simplemente llamás a `backtrack(i + 1)` sin agregar `v_i`.
2. Poda por Optimalidad (Branch and Bound):
   - `vertices_restantes = n - i`
   - Si `len(actual) + vertices_restantes <= len(mejor_solucion)`:
     ¡RETORNAR INMEDIATAMENTE! No vale la pena seguir buscando en esta rama porque
     es matemáticamente imposible superar el récord actual.
3. Variable global/nonlocal para el récord:
   - Mantené `mejor_solucion` para guardar una copia (`set(actual)`) cada vez que
     llegás a una hoja con un tamaño mayor.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
Sea V la cantidad de vértices y E la cantidad de aristas:
- Espacio de estados:
  El árbol de decisiones es un árbol binario de altura |V|.
  En el peor de los casos (un grafo sin aristas donde todos los vértices son independientes),
  el árbol tiene 2^|V| hojas.
- En cada nodo:
  * Verificar si algún vecino está en `actual`: O(grado(v_i)) o O(1) con sets.
  * Chequear la cota de poda: O(1).

Complejidad Temporal Peor Caso: O(2^|V| * |V|).
Complejidad Espacial: O(|V| + |E|) para el grafo, O(|V|) para el conjunto actual y la pila.
"""

from typing import Dict, List, Set

Grafo = Dict[str, List[str]]


def independent_set_maximo(grafo: Grafo) -> Set[str]:
    """
    Encuentra un conjunto independiente de cardinalidad máxima por Backtracking.
    Retorna el conjunto (Set) de vértices que forman el Independent Set Máximo.
    """
    # TODO: Implementar el backtracking con podas por factibilidad y optimalidad.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej04_independent_set_maximo.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando solución de Ejercicio 04 (Independent Set Máximo)...")

    # Caso 1: Ciclo de 5 (C_5: A-B-C-D-E-A). El IS máximo tiene tamaño 2.
    c5 = {
        "A": ["B", "E"], "B": ["A", "C"], "C": ["B", "D"],
        "D": ["C", "E"], "E": ["D", "A"],
    }
    res_c5 = independent_set_maximo(c5)
    print(f"  C_5 -> IS encontrado: {res_c5}")
    assert len(res_c5) == 2, f"Para C_5 se esperaba tamaño 2, dio {len(res_c5)}"

    # Caso 2: Grafo Bipartito K_3,3. El IS máximo tiene tamaño 3.
    k33 = {
        "X1": ["Y1", "Y2", "Y3"], "X2": ["Y1", "Y2", "Y3"], "X3": ["Y1", "Y2", "Y3"],
        "Y1": ["X1", "X2", "X3"], "Y2": ["X1", "X2", "X3"], "Y3": ["X1", "X2", "X3"],
    }
    res_k33 = independent_set_maximo(k33)
    print(f"  K_3,3 -> IS encontrado: {res_k33}")
    assert len(res_k33) == 3, f"Para K_3,3 se esperaba tamaño 3, dio {len(res_k33)}"

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
