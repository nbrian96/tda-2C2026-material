"""
================================================================================
GUÍA 1: DIVISIÓN Y CONQUISTA
EJERCICIO 14: Raíz por Teorema de Bolzano (Método de Bisección)
DIFICULTAD: (★★)
================================================================================

ENUNCIADO:
Se sabe, por el teorema de Bolzano, que si una función es continua en un intervalo
[a, b], y que en el punto a es positiva y en el punto b es negativa (o viceversa),
necesariamente debe haber (al menos) una raíz en dicho intervalo.
Implementar una función `raiz` que reciba una función (univariable) y los extremos
mencionados `a` y `b`, y devuelva una raíz dentro de dicho intervalo (si hay más de una,
simplemente quedarse con una). La complejidad de dicha función debe ser logarítmica
del largo del intervalo [a, b].
Asumir que por más que se esté trabajando con números enteros, hay raíz en dichos valores:
se puede trabajar con floats/tolerancia epsilon.
Justificar la complejidad de la función implementada.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Introduce la Búsqueda Binaria sobre espacios CONTINUOS (análisis numérico).
- Enseña a plantear la complejidad logarítmica no sobre el tamaño de un arreglo,
  sino sobre la precisión / tamaño del intervalo continuo (L / epsilon).

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Intuición matemática (Invariante de Bolzano):
   - Mantené siempre el invariante: `f(a) * f(b) <= 0` (tienen distinto signo).
   - Calculá el punto medio: `mid = (a + b) / 2.0`.
   - Si `f(mid) == 0.0` o `abs(f(mid)) < epsilon` o `(b - a) / 2.0 < epsilon`:
     encontraste una aproximación suficientemente precisa de la raíz.
   - De lo contrario:
     * Si `f(a) * f(mid) < 0`: el cambio de signo ocurre en `[a, mid]`. La raíz está ahí.
     * Si no: el cambio ocurre en `[mid, b]`. La raíz está en la otra mitad.
2. Parada con números flotantes:
   - En punto flotante, raramente `f(mid)` dará exactamente 0.0.
   - Usá una tolerancia `epsilon = 1e-7` para cortar la recursión cuando el intervalo
     se vuelva diminuto.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD (TEOREMA MAESTRO):
--------------------------------------------------------------------------------
Sea L = (b - a) la longitud inicial del intervalo, y epsilon la tolerancia final.
En cada paso:
- Se evalúa `f(mid)` en tiempo O(1) y se decide con qué mitad continuar.
- El intervalo se reduce a la mitad: L' = L / 2.

Ecuación de recurrencia:
    T(L) = 1 * T(L / 2) + O(1)

1. Teorema Maestro:
   - A = 1, B = 2, C = 0.
   - log_B(A) = log_2(1) = 0 == C.
   - Caso 2 del Teorema Maestro:
     T(L) = O(log L) = O(log((b - a) / epsilon)).

2. Cantidad de iteraciones:
   - Para que (b - a) / 2^k <= epsilon, se necesitan k = ceil(log_2((b - a) / epsilon)) pasos.
   - Por ende, la complejidad es logarítmica en el tamaño del intervalo: O(log(b - a)).
"""

from typing import Callable


def raiz(f: Callable[[float], float], a: float, b: float, epsilon: float = 1e-7) -> float:
    """
    Encuentra una raíz de f en el intervalo [a, b] tal que f(a) * f(b) <= 0.
    Debe ejecutarse en tiempo O(log(b - a)).
    Retorna el valor x tal que f(x) ≈ 0.
    """
    # TODO: Implementar la bisección recursiva o iterativa respetando Bolzano.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej14_bolzano_biseccion.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    import math

    print("Probando solución de Ejercicio 14...")

    # Test 1: f(x) = x^2 - 2 en [0, 2] -> Raíz: sqrt(2) ≈ 1.41421356
    f1 = lambda x: x**2 - 2
    r1 = raiz(f1, 0, 2)
    assert abs(r1 - math.sqrt(2)) < 1e-5, f"Fallo en sqrt(2): dio {r1}"
    print(f"  OK: x^2 - 2 en [0, 2] -> raíz {r1:.6f} (esperado {math.sqrt(2):.6f})")

    # Test 2: f(x) = x^3 - x - 2 en [1, 2] -> f(raíz) ≈ 0
    f2 = lambda x: x**3 - x - 2
    r2 = raiz(f2, 1, 2)
    assert abs(f2(r2)) < 1e-4, f"Fallo en x^3 - x - 2: f({r2}) = {f2(r2)}"
    print(f"  OK: x^3 - x - 2 en [1, 2] -> raíz {r2:.6f} con f(r)={f2(r2):.2e}")

    # Test 3: f(x) = cos(x) en [0, 3] -> Raíz: pi / 2 ≈ 1.5707963
    f3 = lambda x: math.cos(x)
    r3 = raiz(f3, 0, 3)
    assert abs(r3 - (math.pi / 2)) < 1e-5, f"Fallo en cos(x): dio {r3}"
    print(f"  OK: cos(x) en [0, 3] -> raíz {r3:.6f} (esperado {math.pi / 2:.6f})")

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
