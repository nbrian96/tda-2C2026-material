"""
================================================================================
GUÍA 3: BACKTRACKING
EJERCICIO 02: Coloreo de Grafos (k-Coloración)
DIFICULTAD: (★★)
================================================================================

ENUNCIADO:
Implementar un algoritmo que reciba un grafo y un número n (o k colores) que,
utilizando backtracking, indique si es posible pintar cada vértice con n colores
de tal forma que no hayan dos vértices adyacentes con el mismo color.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el problema arquetípico de "ASIGNACIÓN / MAPEO" en problemas NP-Completos.
- Es un problema de DECISIÓN (devuelve True o False tan pronto como encuentra
  una coloración válida).
- Enseña a podar inmediatamente cuando el color asignado a un vértice coincide con
  el color de un vecino ya pintado.

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Representación del estado:
   - Lista ordenada de vértices: `v_0, v_1, ..., v_{m-1}`.
   - Diccionario o lista `color_asignado = {}` que mapea cada vértice al color asignado
     (números de 1 a n).
2. Recursión paso a paso:
   - Función `backtrack(indice_vertice)`:
     * Si `indice_vertice == len(vertices)`: ¡Todos los vértices fueron pintados
       válidamente! Retornar `True`.
     * Tomar el vértice actual `v = vertices[indice_vertice]`.
     * Probar cada color `c` de `1` a `n`:
       - PODA POR FACTIBILIDAD: ¿Es válido pintar `v` con el color `c`?
         Verificar si algún vecino de `v` ya tiene asignado el color `c`.
         Si ningún vecino tiene el color `c`:
           - Asignar `color_asignado[v] = c`.
           - Si `backtrack(indice_vertice + 1)` retorna `True`: propagar `True` y cortar.
           - Deshacer: borrar la asignación de `v`.
     * Si se probaron los n colores y ninguno funcionó: retornar `False`.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
Sea V la cantidad de vértices, E la cantidad de aristas, y k (o n) la cantidad de colores:
- Cantidad de hojas en el árbol de recursión:
  Cada uno de los |V| vértices tiene hasta k posibles colores.
  El espacio de búsqueda es a lo sumo O(k^|V|).
- En cada nodo:
  Verificar que ningún vecino comparta el color toma O(grado(v)). En total a lo largo
  de un camino de la raíz a una hoja se recorren todas las aristas adyacentes: O(|V| + |E|).

Complejidad Temporal Peor Caso: O(k^|V| * (|V| + |E|)).
Complejidad Espacial: O(|V| + |E|) para la representación del grafo y O(|V|) para el
diccionario de colores y la pila de llamadas.
"""

from typing import Dict, List

Grafo = Dict[str, List[str]]


def es_k_coloreable(grafo: Grafo, k: int) -> bool:
    """
    Indica si es posible pintar el grafo con k colores tal que ningún par
    de vértices adyacentes comparta color.
    Retorna True si es coloreable con k colores, False en caso contrario.
    """
    # TODO: Implementar el algoritmo de backtracking con poda de vecinos adyacentes.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej02_coloreo_grafos.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando solución de Ejercicio 02 (k-Coloración)...")

    # Triángulo (K_3: A-B-C-A): requiere al menos 3 colores. Con 2 no se puede.
    triangulo = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B"],
    }
    assert es_k_coloreable(triangulo, 3) is True, "El triángulo debe ser 3-coloreable"
    assert es_k_coloreable(triangulo, 2) is False, "El triángulo NO puede ser 2-coloreable"
    print("  OK: Triángulo K_3 -> 3 colores: True, 2 colores: False")

    # Ciclo par (C_4: A-B-C-D-A): es bipartito, por lo tanto es 2-coloreable.
    c4 = {
        "A": ["B", "D"],
        "B": ["A", "C"],
        "C": ["B", "D"],
        "D": ["C", "A"],
    }
    assert es_k_coloreable(c4, 2) is True, "C_4 debe ser 2-coloreable"
    print("  OK: Ciclo C_4 -> 2 colores: True")

    # Grafo de Petersen: se sabe que tiene número cromático 3. No es 2-coloreable.
    assert es_k_coloreable(c4, 1) is False, "C_4 con aristas no puede ser 1-coloreable"
    print("  OK: C_4 -> 1 color: False")

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
