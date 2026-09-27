"""
================================================================================
GUÍA 2: ALGORITMOS GREEDY
EJERCICIO 08: Mochila Fraccionaria vs Mochila 0-1 (Densidad de Valor)
DIFICULTAD: (★★)
================================================================================

ENUNCIADO:
Tenemos una mochila con una capacidad W. Hay elementos a guardar, cada uno tiene
un valor, y un peso que ocupa de la capacidad total. Queremos maximizar el valor de lo
que llevamos sin exceder la capacidad.
Implementar un algoritmo Greedy que reciba dos arreglos de valores y pesos de los
elementos, y devuelva qué elementos deben ser guardados para maximizar la ganancia total.
Indicar y justificar la complejidad del algoritmo implementado.
¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.
¿Por qué se trata de un algoritmo Greedy? Justificar.
¿Qué diferencias se perciben si en vez de tener que colocar los elementos completos,
se pueden fraccionar para nuestra conveniencia?

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el puente conceptual directo entre Greedy y Programación Dinámica.
- Enseña la diferencia fundamental entre problemas continuos (Mochila Fraccionaria,
  donde Greedy ES óptimo) y problemas combinatorios discretos (Mochila 0-1, donde
  Greedy FALLA y se necesita DP).
- Saber dar el CONTRAEJEMPLO exacto de por qué Greedy falla en Mochila 0-1 es una de las
  preguntas más repetidas en coloquios y finales de TDA.

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Criterio voraz (Densidad de Valor):
   - Calculá la relación `densidad = valor_i / peso_i` para cada elemento.
   - Ordená los elementos de mayor a menor densidad.
   - Tomá todo lo que puedas del elemento con mayor densidad disponible:
     * Si entra completo: tomalo al 100%.
     * Si no entra completo pero podés fraccionar: tomá la fracción exacta
       `fraccion = capacidad_restante / peso_i` y terminá.
2. El Contraejemplo para Mochila 0-1 (¡Memorizalo!):
   - Capacidad W = 50.
   - Item 1: Valor = $60,  Peso = 10kg -> Densidad = 6.0 $/kg
   - Item 2: Valor = $100, Peso = 20kg -> Densidad = 5.0 $/kg
   - Item 3: Valor = $120, Peso = 30kg -> Densidad = 4.0 $/kg
   * Greedy 0-1 toma Item 1 ($60, 10kg) e Item 2 ($100, 20kg). Capacidad restante = 20kg.
     El Item 3 (30kg) ya no entra. Total Greedy = $160.
   * ÓPTIMO 0-1 toma Item 2 e Item 3 (20kg + 30kg = 50kg). Total Óptimo = $220.
   * Conclusión: En Mochila 0-1, Greedy falla porque no puede prever el desperdicio
     de capacidad ociosa (espacio vacío que deja en la mochila).

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
Sea n la cantidad de elementos:
1. Calcular la densidad (valor / peso) para cada elemento: O(n).
2. Ordenar los n elementos de mayor a menor densidad: O(n log n).
3. Recorrer la lista ordenada cargando la mochila: O(n).

Complejidad Temporal:
    T(n) = O(n log n).

Complejidad Espacial:
    O(n) para almacenar las tuplas ordenadas y el resultado.
"""

from typing import List, Tuple, Dict, Any


def mochila_fraccionaria_greedy(
    valores: List[float],
    pesos: List[float],
    capacidad: float,
) -> Tuple[float, List[Dict[str, Any]]]:
    """
    Resuelve la Mochila Fraccionaria usando la regla voraz por densidad (valor / peso).
    Retorna: (valor_total_obtenido, lista_elementos_tomados)
    Donde cada elemento en la lista es un dict con:
      {'indice': int, 'fraccion': float, 'peso_usado': float, 'valor_aportado': float}
    """
    # TODO: Implementar el algoritmo voraz para mochila fraccionaria
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej08_mochila_fraccionaria.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    print("Probando solución de Ejercicio 08...")

    W = 50.0
    vals = [60.0, 100.0, 120.0]
    ps = [10.0, 20.0, 30.0]

    val_obtenido, items = mochila_fraccionaria_greedy(vals, ps, W)

    print(f"Valor obtenido: {val_obtenido}")
    print(f"Items tomados: {items}")

    # En mochila fraccionaria:
    # Item 0 (10kg, $60) completo + Item 1 (20kg, $100) completo + 20/30 de Item 2 ($80)
    # Total = 60 + 100 + 80 = 240.0
    assert abs(val_obtenido - 240.0) < 1e-4, f"Esperado 240.0, obtenido {val_obtenido}"

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
