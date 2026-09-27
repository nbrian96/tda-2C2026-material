"""
================================================================================
GUÍA 2: ALGORITMOS GREEDY
EJERCICIO 04: Selección de Charlas (Interval Scheduling)
DIFICULTAD: (★★)
================================================================================

ENUNCIADO:
Dada un aula/sala donde se pueden dar charlas. Las charlas tienen horario de inicio y fin.
Implementar un algoritmo Greedy que reciba el arreglo de los horarios de las charlas,
representando en tuplas los horarios de inicios de las charlas, y sus horarios de fin,
e indique cuáles son las charlas a dar para maximizar la cantidad total de charlas.
Indicar y justificar la complejidad del algoritmo implementado.

--------------------------------------------------------------------------------
¿POR QUÉ FUE SELECCIONADO ESTE EJERCICIO? (CONCEPTO CLAVE):
--------------------------------------------------------------------------------
- Es EL PROBLEMA EMBLEMÁTICO de la técnica Greedy (Interval Scheduling).
- Enseña a comparar distintos criterios intuitivos (duración, inicio, conflictos) y
  demostrar rigurosamente por qué solo uno de ellos es óptimo ("Stays Ahead").
- Es pregunta obligada de examen en casi todas las cursadas.

--------------------------------------------------------------------------------
TIPS PARA RESOLVER EL PROBLEMA:
--------------------------------------------------------------------------------
1. Análisis de posibles criterios voraces:
   - ¿Charlas más cortas? -> FALSO. Contraejemplo: una charla corta en el medio bloquea
     a dos charlas que terminan en los extremos.
   - ¿Charlas que empiezan antes? -> FALSO. Contraejemplo: una que empieza temprano pero
     dura 10 horas bloquea a todas las demás.
   - ¿Charlas que TERMINAN ANTES? -> CORRECTO. Al terminar lo antes posible, el aula
     queda desocupada el mayor tiempo posible para admitir charlas posteriores.
2. Pasos de la resolución:
   - 1) Ordenar las charlas por horario de finalización creciente (`c[1]`).
   - 2) Inicializar una lista de seleccionadas y una variable `ultimo_fin = -inf`.
   - 3) Recorrer las charlas: si `inicio >= ultimo_fin`, agregarla y actualizar `ultimo_fin = fin`.
3. Demostración de optimalidad (Stays Ahead):
   - Por inducción sobre la i-ésima charla elegida: nuestra charla greedy g_i siempre termina
     antes o igual que la charla o_i de cualquier solución óptima (fin(g_i) <= fin(o_i)).
   - Esto garantiza que greedy nunca deja menos tiempo libre que el óptimo y, por lo tanto,
     puede incluir al menos tantas charlas como cualquier otra solución válida.

--------------------------------------------------------------------------------
CÓMO CALCULAR EL ORDEN DE COMPLEJIDAD:
--------------------------------------------------------------------------------
Sea n la cantidad de charlas:
1. Ordenar las n charlas por horario de fin:
   - Tiempo: O(n log n).
2. Bucle voraz de selección:
   - Se itera exactamente una vez sobre las n charlas ya ordenadas.
   - En cada iteración se hace una comparación de números O(1) y un append O(1).
   - Tiempo: O(n).

Complejidad Temporal Total:
    T(n) = O(n log n) [ordenamiento] + O(n) [recorrido lineal] = O(n log n).

Complejidad Espacial:
    O(n) para almacenar el arreglo ordenado y la lista de charlas seleccionadas.
"""

from typing import List, Tuple

Charla = Tuple[float, float]  # (inicio, fin)


def seleccionar_charlas(charlas: List[Charla]) -> List[Charla]:
    """
    Selecciona el subconjunto compatible máximo de charlas usando la estrategia Greedy óptima.
    Debe ejecutarse en tiempo O(n log n).
    Retorna la lista de charlas compatibles elegidas.
    """
    # TODO: Implementar el algoritmo voraz guiándote con los tips.
    raise NotImplementedError("¡Implementá esta función siguiendo los tips!")


# ------------------------------------------------------------------------------
# CASOS DE PRUEBA PARA VERIFICAR TU IMPLEMENTACIÓN
# Ejecutá en terminal: python3 ej04_seleccion_charlas.py
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    charlas_ejemplo = [
        (1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
        (6, 10), (8, 11), (8, 12), (2, 14), (12, 16),
    ]

    print("Probando solución de Ejercicio 04...")
    resultado = seleccionar_charlas(charlas_ejemplo)

    print(f"Charlas seleccionadas ({len(resultado)}): {resultado}")

    # Verificar compatibilidad (sin superposiciones)
    for i in range(len(resultado) - 1):
        assert resultado[i][1] <= resultado[i + 1][0], f"Superposición entre {resultado[i]} y {resultado[i+1]}"

    # En este ejemplo clásico, el número máximo de charlas compatibles es 4
    assert len(resultado) == 4, f"Se esperaban 4 charlas, se obtuvieron {len(resultado)}"

    print("\n¡Excelente! Todos los tests pasaron correctamente.")
