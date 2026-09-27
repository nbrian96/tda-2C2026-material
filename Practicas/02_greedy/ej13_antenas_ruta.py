"""
================================================================================
GUÍA 2: ALGORITMOS GREEDY
EJERCICIO 13: Cobertura de Casas con Antenas (Point Covering en 1D)
DIFICULTAD: (★★)
================================================================================

ENUNCIADO:
Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas.
En dichas casas vive gente que usa mucho sus celulares.
El intendente a cargo de la ruta debe renovar por completo el sistema de antenas,
teniendo que construir sobre la ruta nuevas antenas.
Cada antena tiene un rango de cobertura de R kilómetros (valor constante conocido).

Implementar un algoritmo Greedy que reciba las ubicaciones de las casas, en número de
kilómetro sobre esta ruta (números reales positivos) desordenadas, y devuelva los
kilómetros sobre los que debemos construir las antenas para que todas las casas tengan
cobertura, y se construya para esto la menor cantidad de antenas posibles.
Indicar y justificar la complejidad del algoritmo implementado.
Justificar por qué se trata de un algoritmo greedy.
¿El algoritmo da la solución óptima siempre?

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es el arquetipo de "Point Covering / Interval Covering en una dimensión".
- Es uno de los ejercicios de parcial más recurrentes en variantes como:
  antenas en ruta, patrullas en calles, faros en costas, o torres de vigilancia.
- Enseña la técnica voraz de "empujar la decisión lo más a la derecha posible".

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Regla voraz:
   - Ordenar las casas por kilómetro ascendente.
   - Tomar la primera casa que NO tiene cobertura, ubicada en `x`.
   - Como la antena debe cubrir a `x`, su posición `pos` debe cumplir `pos <= x + R`.
   - Para maximizar la cantidad de casas que cubre hacia adelante (a la derecha):
     colocar la antena EXACTAMENTE en `pos = x + R`.
   - Esta antena cubre el rango `[x, x + 2R]`.
   - Saltear todas las casas dentro de ese rango y repetir con la siguiente casa desprotegida.
2. Demostración de optimalidad:
   - Argumento de intercambio: cualquier solución que cubra `x` con una antena en `pos' < x + R`
     puede mover esa antena a `x + R` sin dejar a `x` sin señal y extendiendo la cobertura
     hacia adelante, por lo que nunca necesitará más antenas que la solución Greedy.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
Sea n la cantidad de casas:
1. Ordenar las casas por kilómetro: O(n log n).
2. Barrido lineal de izquierda a derecha (cada casa se inspecciona una vez): O(n).

Complejidad Temporal Total:
    T(n) = O(n log n).

Complejidad Espacial:
    O(n) para almacenar el ordenamiento y las posiciones de las antenas.
"""

from typing import List


def ubicar_antenas(casas: List[float], r: float) -> List[float]:
    """
    Determina las posiciones óptimas para construir la menor cantidad de antenas.
    - casas: lista de kilómetros donde hay casas (desordenadas).
    - r: radio de cobertura de cada antena en kilómetros.
    Retorna la lista de kilómetros donde construir antenas.
    """
    # TODO: Implementar el algoritmo voraz de cobertura en 1D
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej13_antenas_ruta.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    casas_test = [1.5, 4.0, 7.2, 2.0, 10.0, 15.0, 11.5, 20.0]
    radio = 3.0

    print("Probando solución de Ejercicio 13...")
    antenas = ubicar_antenas(casas_test, radio)
    print(f"Antenas construidas: {antenas}")

    # Verificar que toda casa tenga cobertura
    for c in casas_test:
        cubierta = any(abs(c - a) <= radio for a in antenas)
        assert cubierta, f"La casa en km {c} quedó sin cobertura!"

    # Para estas casas con r=3.0, el mínimo de antenas posibles es 3
    assert len(antenas) == 3, f"Se esperaban 3 antenas, se obtuvieron {len(antenas)}"

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
