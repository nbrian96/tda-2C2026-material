"""
================================================================================
GUÍA 5: PROGRAMACIÓN LINEAL
EJERCICIO 01: Problema de la Mochila en Programación Lineal Entera
DIFICULTAD: (★)
================================================================================

ENUNCIADO:
Implementar un modelo de programación lineal que resuelva el Problema de la Mochila
de valor máximo (ejercicio 7 de Programación Dinámica).

Se tienen n elementos, cada uno con valor v_i > 0 y peso w_i > 0, y una mochila
con capacidad máxima W. Se busca seleccionar un subconjunto de elementos para
maximizar el valor total sin superar la capacidad W.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el "Hola Mundo" de la Programación Lineal Entera (PL / ILP).
- Conecta directamente con lo aprendido en Greedy (Guía 2, Ej 8) y Programación
  Dinámica (Guía 4, Ej 7), permitiendo ver el mismo problema resuelto con 3 paradigmas distintos.
- Enseña la variable binaria indicadora x_i in {0, 1} (tomar o no tomar).

--------------------------------------------------------------------------------
GUÍA PARA PLANTEAR EL MODELO MATEMÁTICO:
--------------------------------------------------------------------------------
1. Variables de Decisión:
   Para cada elemento i in {0, 1, ..., n-1}:
     x_i in {0, 1}
     x_i = 1 si el elemento i se guarda en la mochila, 0 en caso contrario.

2. Función Objetivo:
   Maximizar el valor acumulado de los elementos seleccionados:
     MAXIMIZAR  sum_{i=0}^{n-1} (v_i * x_i)

3. Restricciones:
   a. Restricción de capacidad (el peso total no puede exceder W):
        sum_{i=0}^{n-1} (w_i * x_i) <= W
   b. Dominio de las variables:
        x_i in {0, 1}  para todo i in {0, ..., n-1}

--------------------------------------------------------------------------------
CÓMO CALCULAR LA CANTIDAD DE VARIABLES Y RESTRICCIONES:
--------------------------------------------------------------------------------
Sea n la cantidad de elementos:
- Variables de Decisión:
  Exactamente n variables binarias (x_0, x_1, ..., x_{n-1}).
  Orden: O(n).
- Restricciones:
  * 1 restricción de capacidad (la sumatoria de pesos).
  * (Opcional según la notación de la cátedra: 2n cotas de dominio 0 <= x_i <= 1).
  Orden: O(1) restricciones estructurales (u O(n) considerando cotas de dominio).
"""

from typing import List, Tuple, Dict, Any


def modelar_mochila_pl(
    valores: List[float],
    pesos: List[float],
    capacidad: float,
) -> Dict[str, Any]:
    """
    Construye la descripción formal del modelo de programación lineal entera.
    Retorna un diccionario estructurado con:
      - 'tipo': 'MAXIMIZAR'
      - 'variables': lista de nombres de variables ['x_0', 'x_1', ...]
      - 'dominio': 'Binaria'
      - 'funcion_objetivo': coeficientes {var: coef}
      - 'restricciones': lista de inecuaciones {'expresion': ..., 'sentido': '<=', 'limite': W}
      - 'cant_variables': int
      - 'cant_restricciones': int
    """
    # TODO: Implementar la construcción del modelo de Programación Lineal
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA Y VERIFICACIÓN DEL MODELO
# Ejecutá en terminal: python3 ej01_mochila_pl.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando formulación de Ejercicio 01 (Mochila en PL)...")

    valores = [60.0, 100.0, 120.0]
    pesos = [10.0, 20.0, 30.0]
    W = 50.0

    modelo = modelar_mochila_pl(valores, pesos, W)

    print(f"Tipo: {modelo.get('tipo')}")
    print(f"Variables ({modelo.get('cant_variables')}): {modelo.get('variables')}")
    print(f"Función Objetivo: {modelo.get('funcion_objetivo')}")
    print(f"Restricciones ({modelo.get('cant_restricciones')}): {modelo.get('restricciones')}")

    assert modelo.get("tipo") == "MAXIMIZAR"
    assert modelo.get("cant_variables") == len(valores)
    assert modelo.get("cant_restricciones") >= 1

    print("\n¡Excelente! El modelo de Programación Lineal está correctamente planteado.")
