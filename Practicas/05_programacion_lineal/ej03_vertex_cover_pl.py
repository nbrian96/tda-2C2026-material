r"""
================================================================================
GUÍA 5: PROGRAMACIÓN LINEAL
EJERCICIO 03: Vertex Cover Mínimo en Programación Lineal Entera
DIFICULTAD: (★)
================================================================================

ENUNCIADO:
Implementar un modelo de programación lineal que resuelva el problema de Vertex Cover
mínimo (ejercicio 13 de Backtracking).

Recordatorio del problema:
Un Vertex Cover (cobertura de vértices) de un Grafo no dirigido G = (V, E) es un
subconjunto de vértices C subseteq V tal que TODA arista (u, v) in E tiene al menos
uno de sus extremos en C (es decir, u in C o v in C, o ambos).
Se busca encontrar un Vertex Cover de cardinalidad MÍNIMA.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el problema canónico de COBERTURA sobre Grafos en Programación Lineal.
- Enseña a traducir la condición lógica "al menos uno de los dos extremos debe estar
  elegido" a la inecuación lineal básica: `x_u + x_v >= 1`.
- Es el problema dual del Independent Set Máximo (IS = V \ VC).

--------------------------------------------------------------------------------
GUÍA PARA PLANTEAR EL MODELO MATEMÁTICO:
--------------------------------------------------------------------------------
1. Variables de Decisión:
   Para cada vértice v in V:
     x_v in {0, 1}
     x_v = 1 si el vértice v forma parte del Vertex Cover, 0 en caso contrario.

2. Función Objetivo:
   Minimizar la cantidad total de vértices en el Vertex Cover:
     MINIMIZAR  sum_{v in V} x_v

3. Restricciones:
   a. Restricción de cobertura de aristas:
      Para toda arista e = (u, v) in E:
        x_u + x_v >= 1
      (Garantiza que al menos uno de los dos extremos de la arista sea seleccionado).
   b. Dominio de las variables:
      x_v in {0, 1}  para todo v in V.

--------------------------------------------------------------------------------
CÓMO CALCULAR LA CANTIDAD DE VARIABLES Y RESTRICCIONES:
--------------------------------------------------------------------------------
Sea V la cantidad de vértices y E la cantidad de aristas del grafo:
- Variables de Decisión:
  Exactamente |V| variables binarias (una por cada vértice).
  Orden: O(|V|).
- Restricciones:
  Exactamente |E| inecuaciones (una por cada arista del grafo).
  Orden: O(|E|).
"""

from typing import List, Tuple, Dict, Any

GrafoListaAristas = Tuple[List[str], List[Tuple[str, str]]]  # (vertices, aristas)


def modelar_vertex_cover_pl(vertices: List[str], aristas: List[Tuple[str, str]]) -> Dict[str, Any]:
    """
    Construye la descripción formal del modelo de PL para Vertex Cover Mínimo.
    Retorna un diccionario con:
      - 'tipo': 'MINIMIZAR'
      - 'variables': [f'x_{v}' for v in vertices]
      - 'dominio': 'Binaria'
      - 'funcion_objetivo': {var: 1 for var in variables}
      - 'restricciones': [{'expresion': ..., 'sentido': '>=', 'limite': 1}, ...]
      - 'cant_variables': int
      - 'cant_restricciones': int
    """
    # TODO: Implementar la construcción del modelo de PL
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA Y VERIFICACIÓN DEL MODELO
# Ejecutá en terminal: python3 ej03_vertex_cover_pl.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando formulación de Ejercicio 03 (Vertex Cover Mínimo en PL)...")

    # Triángulo K_3: vértices A, B, C y aristas (A, B), (B, C), (A, C)
    vertices = ["A", "B", "C"]
    aristas = [("A", "B"), ("B", "C"), ("A", "C")]

    modelo = modelar_vertex_cover_pl(vertices, aristas)

    print(f"Tipo: {modelo.get('tipo')}")
    print(f"Variables ({modelo.get('cant_variables')}): {modelo.get('variables')}")
    print(f"Restricciones ({modelo.get('cant_restricciones')}): {modelo.get('restricciones')}")

    assert modelo.get("tipo") == "MINIMIZAR"
    assert modelo.get("cant_variables") == len(vertices)
    assert modelo.get("cant_restricciones") == len(aristas)

    print("\n¡Excelente! El modelo de Programación Lineal está correctamente planteado.")
