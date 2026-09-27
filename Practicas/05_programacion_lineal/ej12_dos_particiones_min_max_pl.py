"""
================================================================================
GUÍA 5: PROGRAMACIÓN LINEAL
EJERCICIO 12: Problema de las 2 Particiones (Linealización Min-Max)
DIFICULTAD: (★★)
================================================================================

ENUNCIADO:
El 2-Partition Problem como problema de optimización se describe tal que:
Dado un conjunto de n números positivos T = {T_1, T_2, ..., T_n}, se particionan los
números en dos subconjuntos S_1 y S_2 (con intersección vacía y unión = T) de forma de
minimizar la sumatoria del mayor de los subconjuntos:
    min  max( sum(S_1), sum(S_2) )

Implementar un modelo de programación lineal que dados los valores de los T_i nos
permita obtener la asignación óptima para S_1 y S_2.
Indicar la cantidad de inecuaciones definidas en el modelo.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Enseña el TRUCO CLAVE DE LINEALIZACIÓN DE FUNCIONES NO LINEALES (MIN-MAX).
- En Programación Lineal, los operadores `max(...)`, `min(...)` y `abs(...)` NO son
  lineales y NO se pueden escribir directamente en la función objetivo.
- Muestra cómo introducir una VARIABLE AUXILIAR Z acotada superiormente por las restricciones
  para transformar un objetivo no lineal en un problema 100% lineal.

--------------------------------------------------------------------------------
GUÍA PARA PLANTEAR EL MODELO MATEMÁTICO:
--------------------------------------------------------------------------------
1. Variables de Decisión:
   - Para cada elemento i in {1, ..., n}:
       x_i in {0, 1}
       x_i = 1 si T_i se asigna al subconjunto S_1, y 0 si se asigna a S_2.
   - Variable continua auxiliar:
       Z >= 0 (representa la cota superior del peso de cualquiera de los dos conjuntos).

2. Función Objetivo:
   Minimizar el valor de la variable auxiliar Z:
     MINIMIZAR  Z

3. Restricciones:
   Para que Z sea mayor o igual que la suma de S_1 y que la suma de S_2:
   a. Restricción para S_1:
        Z >= sum_{i=1}^n (T_i * x_i)
      Reordenando en forma estándar:
        Z - sum_{i=1}^n (T_i * x_i) >= 0

   b. Restricción para S_2:
      Como los elementos en S_2 son aquellos con (1 - x_i):
        sum(S_2) = sum_{i=1}^n T_i * (1 - x_i) = sum_{i=1}^n T_i - sum_{i=1}^n (T_i * x_i)
      Entonces:
        Z >= sum_{i=1}^n T_i - sum_{i=1}^n (T_i * x_i)
      Reordenando en forma estándar:
        Z + sum_{i=1}^n (T_i * x_i) >= sum_{i=1}^n T_i

   c. Dominio de las variables:
        x_i in {0, 1}  para todo i in {1, ..., n}
        Z >= 0

¿Por qué funciona este truco?
Como el objetivo es MINIMIZAR Z, el solver empujará a Z hacia abajo tanto como sea posible,
hasta que Z sea exactamente igual a max(sum(S_1), sum(S_2)).

--------------------------------------------------------------------------------
CÓMO CALCULAR LA CANTIDAD DE VARIABLES Y RESTRICCIONES:
--------------------------------------------------------------------------------
Sea n la cantidad de números en el conjunto T:
- Variables de Decisión:
  * n variables binarias (x_1, ..., x_n).
  * 1 variable continua (Z).
  Total de variables: n + 1. Orden: O(n).
- Restricciones:
  * Exactamente 2 inecuaciones lineales principales (una para acotar la suma de S_1
    y otra para acotar la suma de S_2).
  Total de inecuaciones estructurales: 2. Orden: O(1).
"""

from typing import List, Dict, Any


def modelar_2_partition_min_max_pl(T: List[float]) -> Dict[str, Any]:
    """
    Construye el modelo de PL linealizado para el 2-Partition Problem (min max(S1, S2)).
    Retorna un diccionario con:
      - 'tipo': 'MINIMIZAR'
      - 'variable_objetivo': 'Z'
      - 'variables_binarias': ['x_0', 'x_1', ...]
      - 'variable_continua': 'Z'
      - 'restricciones': [
          # Inecuación 1: Z >= sum(T_i * x_i)
          # Inecuación 2: Z >= Total - sum(T_i * x_i)
        ]
      - 'cant_variables': int
      - 'cant_restricciones': int
    """
    # TODO: Implementar la construcción del modelo con la variable auxiliar Z.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA Y VERIFICACIÓN DEL MODELO
# Ejecutá en terminal: python3 ej12_dos_particiones_min_max_pl.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando formulación de Ejercicio 12 (2-Partition Min-Max en PL)...")

    # Conjunto T = [3, 1, 1, 2, 2, 1]
    # Suma total = 10. La partición perfecta es S1 = 5, S2 = 5 -> max = 5.
    T = [3.0, 1.0, 1.0, 2.0, 2.0, 1.0]

    modelo = modelar_2_partition_min_max_pl(T)

    print(f"Tipo: {modelo.get('tipo')}")
    print(f"Variable a minimizar: {modelo.get('variable_objetivo')}")
    print(f"Cantidad de variables: {modelo.get('cant_variables')} (n binarias + 1 continua Z)")
    print(f"Cantidad de restricciones: {modelo.get('cant_restricciones')}")
    print(f"Restricciones:\n{modelo.get('restricciones')}")

    assert modelo.get("tipo") == "MINIMIZAR"
    assert modelo.get("variable_objetivo") == "Z"
    assert modelo.get("cant_variables") == len(T) + 1
    assert modelo.get("cant_restricciones") == 2

    print("\n¡Excelente! El modelo de Programación Lineal está correctamente planteado.")
