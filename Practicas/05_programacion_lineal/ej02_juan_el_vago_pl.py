"""
================================================================================
GUÍA 5: PROGRAMACIÓN LINEAL
EJERCICIO 02: Juan el Vago en Programación Lineal Entera
DIFICULTAD: (★)
================================================================================

ENUNCIADO:
Implementar un modelo de programación lineal que resuelva el problema de Juan El Vago
(ejercicio 4 de Programación Dinámica).

Recordatorio del problema:
Juan dispone de ofertas diarias para trabajar durante n días consecutivos, ganando g_i
si trabaja el día i. No puede trabajar dos días seguidos. Se desea maximizar la ganancia
total.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Enseña la formulación de restricciones de EXCLUSIÓN MUTUA ADYACENTE en Programación Lineal:
  si dos actividades o elementos contiguos son incompatibles, su suma debe ser <= 1.
- Conecta con la solución por Programación Dinámica (Guía 4, Ej 4).

--------------------------------------------------------------------------------
GUÍA PARA PLANTEAR EL MODELO MATEMÁTICO:
--------------------------------------------------------------------------------
1. Variables de Decisión:
   Para cada día i in {0, 1, ..., n-1}:
     x_i in {0, 1}
     x_i = 1 si Juan trabaja el día i, 0 en caso contrario.

2. Función Objetivo:
   Maximizar la ganancia total obtenida:
     MAXIMIZAR  sum_{i=0}^{n-1} (g_i * x_i)

3. Restricciones:
   a. Restricción de no trabajar dos días seguidos:
      Para todo día i in {0, 1, ..., n-2}:
        x_i + x_{i+1} <= 1
      (Si x_i = 1, entonces x_{i+1} está obligada a ser 0. Si x_i = 0, x_{i+1} puede ser 0 o 1).
   b. Dominio de las variables:
      x_i in {0, 1} para todo i in {0, ..., n-1}.

--------------------------------------------------------------------------------
CÓMO CALCULAR LA CANTIDAD DE VARIABLES Y RESTRICCIONES:
--------------------------------------------------------------------------------
Sea n la cantidad de días:
- Variables de Decisión:
  Exactamente n variables binarias (x_0, ..., x_{n-1}).
  Orden: O(n).
- Restricciones:
  Exactamente (n - 1) inecuaciones de adyacencia (una por cada par de días consecutivos).
  Orden: O(n).
"""

from typing import List, Dict, Any


def modelar_juan_el_vago_pl(ganancias: List[float]) -> Dict[str, Any]:
    """
    Construye la descripción formal del modelo de programación lineal para Juan el Vago.
    Retorna un diccionario con:
      - 'tipo': 'MAXIMIZAR'
      - 'variables': ['x_0', 'x_1', ...]
      - 'dominio': 'Binaria'
      - 'funcion_objetivo': {var: coef}
      - 'restricciones': [{'expresion': ..., 'sentido': '<=', 'limite': 1}, ...]
      - 'cant_variables': int
      - 'cant_restricciones': int
    """
    # TODO: Implementar la construcción del modelo de PL
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA Y VERIFICACIÓN DEL MODELO
# Ejecutá en terminal: python3 ej02_juan_el_vago_pl.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando formulación de Ejercicio 02 (Juan el Vago en PL)...")

    ganancias = [10.0, 5.0, 2.0, 20.0, 15.0]
    modelo = modelar_juan_el_vago_pl(ganancias)

    print(f"Tipo: {modelo.get('tipo')}")
    print(f"Variables ({modelo.get('cant_variables')}): {modelo.get('variables')}")
    print(f"Restricciones ({modelo.get('cant_restricciones')}): {modelo.get('restricciones')}")

    assert modelo.get("tipo") == "MAXIMIZAR"
    assert modelo.get("cant_variables") == len(ganancias)
    assert modelo.get("cant_restricciones") == len(ganancias) - 1

    print("\n¡Excelente! El modelo de Programación Lineal está correctamente planteado.")
