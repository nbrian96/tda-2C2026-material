"""Módulo 4: Backtracking y Branch & Bound."""

def get_content():
    return r"""## 6. Tema 3: Backtracking y Branch & Bound

### Conceptos Mínimos de Supervivencia

1. **Definición del Paradigma:**
   Backtracking es una técnica de búsqueda exhaustiva sistemática sobre un **árbol de estados combinatorios**. Avanza construyendo soluciones candidatas paso a paso; en cuanto determina que el estado actual no puede completarse para dar una solución válida u óptima, retrocede (*backtrack*) al estado anterior deshaciendo los cambios.
2. **Las Dos Clases Fundamentales de Podas:**
   * **Poda por Factibilidad (Feasibility Pruning):** Se aplica tanto en problemas de decisión como de optimización. Descarta una rama si el estado actual viola una restricción obligatoria del problema (por ejemplo, dos reinas en la misma diagonal, o la suma actual supera el valor objetivo).
   * **Poda por Cota u Optimalidad (Branch and Bound):** Se aplica en problemas de optimización. Se calcula una cota teórica (superior para maximización, inferior para minimización) del mejor valor que podría lograrse explorando el subárbol actual. Si esa cota no mejora a la mejor solución factible ya registrada (`mejor_solucion`), la rama entera se descarta.
3. **Estructuras Auxiliares para Validación en O(1):**
   En los parciales es penalizado verificar restricciones recorriendo estructuras con bucles O(n) dentro de cada paso recursivo. Se deben emplear **arreglos o tablas booleanas auxiliares** para chequear y marcar ocupación en tiempo constante O(1) (ejemplo: columnas y diagonales en N-Reinas).
4. **Complejidad en el Peor Caso:**
   Aunque las podas reducen drásticamente el tiempo empírico, la complejidad asintótica en el peor caso sigue siendo exponencial (O(2ⁿ), O(kⁿ)) o factorial (O(n!)), dado que los problemas resueltos típicamente son NP-Hard.

---

### Patrón de Ejercicio 3.1: Posicionamiento en Tableros con Estructuras O(1)

Aparece en enunciados de colocación de piezas (reinas, caballos, torres) donde se exige explicitar las estructuras de datos que garantizan validaciones en tiempo constante.

---

### Ejercicio 9 — Problema de las 8 Reinas con Control de Conflictos en O(1)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2025-1-2 (17 de junio de 2025), Ejercicio 4 / Guía 03 Ejercicio 3

**Enunciado**  
Realizar un algoritmo que resuelva el problema de las 8 reinas mediante backtracking. El problema consiste en ubicar 8 reinas en un tablero de ajedrez de 8 × 8 de manera que no haya dos reinas en la misma fila, columna o diagonal. Indicar detalladamente las estructuras de datos utilizadas para representar el problema y la solución, garantizando que el chequeo de amenazas se realice en O(1).

**Qué está evaluando**  
Árbol de búsqueda fila por fila, uso de vectores booleanos para registrar columnas y diagonales directas e inversas, y manejo de backtracking con restauración de estado.

**Idea de resolución**  
* Colocamos exactamente una reina por fila, avanzando fila por fila (fila = 0, 1, ..., 7). Esto elimina automáticamente los conflictos de fila.
* Para chequear columnas en O(1): vector booleano `col_ocupada[8]`.
* Para diagonales:
  * Diagonal Principal (\): la diferencia `fila - col` es constante para todas las celdas de una misma diagonal. Varía entre -7 y +7. Con un desplazamiento de +7, mapeamos al rango [0, 14] mediante la clave `fila - col + 7`.
  * Diagonal Secundaria (/): la suma `fila + col` es constante para todas las celdas de una misma diagonal. Varía entre 0 y 14 mediante la clave `fila + col`.
* Al probar una columna válida en la fila actual, marcamos las estructuras, llamamos recursivamente a la fila siguiente, y al retornar **desmarcamos** las estructuras.

**Pseudocódigo**

```text
FUNCION Resolver8Reinas():
    INICIALIZAR solucion como arreglo de tamaño 8 lleno de -1
    INICIALIZAR col_ocupada como arreglo booleano de tamaño 8 en FALSO
    INICIALIZAR diag_prin como arreglo booleano de tamaño 15 en FALSO
    INICIALIZAR diag_sec como arreglo booleano de tamaño 15 en FALSO

    exito <- ReinasBT(0, solucion, col_ocupada, diag_prin, diag_sec)

    SI exito:
        RETORNAR solucion // solucion[i] indica la columna de la reina en la fila i
    SINO:
        RETORNAR "No existe solucion"

FUNCION ReinasBT(fila, solucion, col_ocupada, diag_prin, diag_sec):
    // Caso base: las 8 reinas fueron ubicadas con éxito
    SI fila = 8:
        RETORNAR VERDADERO

    PARA col <- 0 HASTA 7:
        d_prin <- fila - col + 7
        d_sec  <- fila + col

        // Poda por Factibilidad en O(1)
        SI NO col_ocupada[col] Y NO diag_prin[d_prin] Y NO diag_sec[d_sec]:
            // 1. Marcar decisión
            solucion[fila] <- col
            col_ocupada[col] <- VERDADERO
            diag_prin[d_prin] <- VERDADERO
            diag_sec[d_sec] <- VERDADERO

            // 2. Llamada recursiva a la siguiente fila
            SI ReinasBT(fila + 1, solucion, col_ocupada, diag_prin, diag_sec):
                RETORNAR VERDADERO

            // 3. Deshacer decisión (Backtrack)
            solucion[fila] <- -1
            col_ocupada[col] <- FALSO
            diag_prin[d_prin] <- FALSO
            diag_sec[d_sec] <- FALSO

    RETORNAR FALSO
```

**Explicación del algoritmo**  
El algoritmo recorre las columnas candidatas para la fila actual. Gracias a las tres tablas booleanas, la validación de no agresión toma O(1). Si una asignación conduce a un callejón sin salida en filas posteriores, la ejecución vuelve atrás, restaura los booleanos a `FALSO` y prueba la siguiente columna.

**Complejidad**  
* **Tiempo:** En el peor caso para N reinas es O(N!), ya que la primera fila tiene N opciones, la segunda a lo sumo N - 1, etc. Para N = 8, el espacio de búsqueda es menor a 8! = 40.320 nodos y con podas diagonales evalúa apenas unos pocos cientos de estados.
* **Espacio:** O(N) para la pila de recursión y los vectores de control booleanos (8 + 15 + 15 = 38 booleanos).

**Puntos donde puedo equivocarme**  
* Olvidar desmarcar las tablas booleanas al retornar de la recursión.
* Calcular mal el desplazamiento de la diagonal principal y provocar un índice negativo (`fila - col < 0`).
* Hacer un doble bucle para verificar si hay otra reina en el tablero, degradando el chequeo a O(N) en lugar de O(1).

**Variación típica de parcial**  
Pedir todas las soluciones posibles en lugar de la primera (se acumula una copia de `solucion` en una lista global y nunca se corta con `RETORNAR VERDADERO`).

---

### Patrón de Ejercicio 3.2: Descomposición Numérica con Cotas (Lagrange)

Problemas donde se debe descomponer un número entero en sumas de componentes (cuadrados, primos, monedas) bajo un número fijo de términos.

---

### Ejercicio 10 — Suma de Cuatro Cuadrados de Lagrange con Cotas y Podas

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-1 (5 de noviembre de 2024), Ejercicio 1

**Enunciado**  
El teorema de los cuatro cuadrados de Lagrange especifica que cualquier número entero no negativo n puede expresarse como la suma de cuatro cuadrados de enteros no negativos:
> **n = w² + x² + y² + z²**

Desarrollar un algoritmo que, dado el valor de n, indique cuáles son los cuatro enteros no negativos que lo componen. Indicar y justificar la complejidad del algoritmo implementado.

**Qué está evaluando**  
Diseño de un árbol de backtracking acotado a profundidad 4, imposición de orden no creciente para evitar ramas simétricas redundantes (w ≥ x ≥ y ≥ z), y poda por cota superior e inferior.

**Idea de resolución**  
* Buscamos una tupla (w, x, y, z) tal que w² + x² + y² + z² = n.
* Para no explorar permutaciones repetidas de la misma solución, forzamos:
  > **w ≥ x ≥ y ≥ z ≥ 0**
* Cotas y podas:
  1. En el paso k (con k ∈ {1, 2, 3, 4}), si nos queda un remanente R, el valor actual v no puede superar ⌊√R⌋.
  2. Además, v no puede ser mayor que el valor elegido en el paso anterior (v ≤ anterior).
  3. Cota inferior de poda: Los (4 - k + 1) términos restantes con valor máximo v deben ser capaces de alcanzar R. Si (4 - k + 1) · v² < R, es imposible llegar a R y se poda la rama.
  4. En el paso 4, no hace falta iterar: simplemente verificamos si el remanente R es un cuadrado perfecto (z = ⌊√R⌋ y z² = R).

**Pseudocódigo**

```text
FUNCION CuatroCuadradosLagrange(n):
    INICIALIZAR solucion como arreglo de tamaño 4 en 0
    max_posible <- PARTE_ENTERA(RAIZ(n))
    exito <- LagrangeBT(0, n, max_posible, solucion)
    SI exito:
        RETORNAR solucion
    RETORNAR "No encontrado"

FUNCION LagrangeBT(paso, remanente, max_limite, solucion):
    // Caso base: si asignamos 3 cuadrados, el 4to queda determinado
    SI paso = 3:
        z <- PARTE_ENTERA(RAIZ(remanente))
        SI z * z = remanente Y z <= max_limite:
            solucion[3] <- z
            RETORNAR VERDADERO
        RETORNAR FALSO

    // Determinamos el rango del valor actual v
    limite_sup <- MINIMO(max_limite, PARTE_ENTERA(RAIZ(remanente)))

    PARA v <- limite_sup BAJANDO HASTA 0:
        // Poda por cota: si los términos restantes no alcanzan el remanente
        terminos_restantes <- 4 - paso
        SI terminos_restantes * (v * v) < remanente:
            ROMPER // Como v baja, valores menores tampoco alcanzarán

        solucion[paso] <- v
        SI LagrangeBT(paso + 1, remanente - v * v, v, solucion):
            RETORNAR VERDADERO

    RETORNAR FALSO
```

**Explicación del algoritmo**  
El algoritmo explora a lo sumo 3 niveles de profundidad, calculando el cuarto término analíticamente en O(1). La condición v ≤ anterior elimina simetrías, y la condición `terminos_restantes * (v * v) < remanente` aborta inmediatamente ramas cuando los valores se vuelven demasiado pequeños para sumar n.

**Complejidad**  
* **Tiempo:** El primer término tiene a lo sumo √n opciones. El segundo tiene a lo sumo √n opciones. El tercero tiene a lo sumo √n opciones. El cuarto se determina en O(1). Por lo tanto, en el peor caso sin podas sería O((√n)³) = O(n^(3/2)). Con la poda de simetría w ≥ x ≥ y ≥ z y el corte temprano por cota inferior, el espacio de búsqueda se reduce a una fracción mínima de n^(3/2), resolviendo en milisegundos para números grandes.
* **Espacio:** O(1) de memoria adicional más una pila de recursión fija de profundidad 4.

**Puntos donde puedo equivocarme**  
* Iterar los 4 bucles hasta √n sin calcular el último término en O(1) (O(n²) vs O(n^(3/2))).
* No imponer el orden decreciente v ≤ anterior, multiplicando el tiempo por 4! = 24.

**Variación típica de parcial**  
Descomponer un número como suma de cubos positivos (problema de Waring) o suma de números primos con un máximo de k términos.

---

### Patrón de Ejercicio 3.3: Cobertura en Grafos con Branch and Bound (Vertex Cover)

Aparece cuando se solicita un algoritmo exacto para un problema NP-Hard sobre grafos no dirigidos.

---

### Ejercicio 11 — Vertex Cover Mínimo por Branch and Bound

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-2 (26 de noviembre de 2024), Ejercicio 1 / Guía 03 Ejercicio 13

**Enunciado**  
Implementar un algoritmo que dado un grafo no dirigido G = (V, E) devuelva un conjunto de vértices que represente un mínimo Vertex Cover del mismo. Explicar el árbol de decisiones, las podas aplicadas y la complejidad.

**Qué está evaluando**  
Estrategia de branching sobre aristas no cubiertas (al menos uno de los extremos debe pertenecer a la cobertura), poda por cota superior (*Branch and Bound*) descartando ramas que superen el mejor tamaño ya hallado.

**Idea de resolución**  
* Un Vertex Cover requiere que para cada arista (u, v) ∈ E, al menos u ∈ C o v ∈ C.
* *Branching inteligente:* En lugar de probar vértice por vértice arbitrariamente (2^|V|), buscamos una arista (u, v) que **aún no esté cubierta** por el conjunto actual:
  * Rama 1: Incluimos u en la cobertura y recursamos.
  * Rama 2: Incluimos v en la cobertura y recursamos.
* *Poda Branch and Bound:* Mantenemos el tamaño del mejor Vertex Cover encontrado hasta el momento (`mejor_tamano`). Si en el estado actual |C| ≥ mejor_tamano, podar inmediatamente la rama, porque cualquier solución derivada tendrá tamaño mayor o igual y no puede mejorar el récord actual.
* Caso base: Si no quedan aristas sin cubrir, C es un Vertex Cover válido y actualizamos la mejor solución.

**Pseudocódigo**

```text
FUNCION MinimoVertexCover(G):
    mejor_cobertura <- V(G) // Cota superior trivial inicial: todos los vértices
    INICIALIZAR cobertura_actual como conjunto vacío

    VertexCoverBT(G, cobertura_actual, mejor_cobertura)
    RETORNAR mejor_cobertura

PROCEDIMIENTO VertexCoverBT(G, actual, MEJOR):
    // Poda por cota superior (Branch and Bound)
    SI cardinal(actual) >= cardinal(MEJOR):
        RETORNAR

    // Buscar una arista no cubierta
    arista_libre <- BuscarAristaNoCubierta(G, actual)

    // Si no hay aristas libres, 'actual' cubre todas las aristas y es mejor
    SI arista_libre = NULO:
        MEJOR <- COPIAR(actual)
        RETORNAR

    u <- arista_libre.origen
    v <- arista_libre.destino

    // Rama 1: Incluir u
    AGREGAR u A actual
    VertexCoverBT(G, actual, MEJOR)
    QUITAR u DE actual // Backtrack

    // Rama 2: Incluir v
    AGREGAR v A actual
    VertexCoverBT(G, actual, MEJOR)
    QUITAR v DE actual // Backtrack

FUNCION BuscarAristaNoCubierta(G, cobertura):
    PARA CADA arista (u, v) EN E(G):
        SI u NO PERTENECE A cobertura Y v NO PERTENECE A cobertura:
            RETORNAR (u, v)
    RETORNAR NULO
```

**Explicación del algoritmo**  
Al ramificar sobre los dos extremos de una arista no cubierta, el árbol tiene factor de ramificación 2. Si el grafo tiene un Vertex Cover de tamaño k, la profundidad máxima explorada es k. La poda por cota superior asegura que apenas se encuentra una cobertura de tamaño k, ninguna rama de tamaño ≥ k es explorada.

**Complejidad**  
* **Tiempo:** En el peor caso la recursión genera O(2ᵏ · |E|) operaciones, donde k es el tamaño del Vertex Cover mínimo. Comparado con el espacio ingenuo O(2^|V|), esto es exponencialmente más veloz cuando k < |V|.
* **Espacio:** O(|V|) para almacenar el conjunto de la cobertura actual y la pila de recursión.

**Puntos donde puedo equivocarme**  
* Ramificar incluyendo ninguno de los dos extremos (eso violaría la definición de cobertura).
* No hacer una copia profunda (`COPIAR`) de `actual` al actualizar `MEJOR`.
* No podar con `>= cardinal(MEJOR)` permitiendo explorar soluciones con igual o peor tamaño.

**Variación típica de parcial**  
* *Independent Set Máximo:* Recordar la dualidad S es Independent Set ⟺ V \ S es Vertex Cover.
* Resolver el problema de decisión: ¿Existe un Vertex Cover de tamaño ≤ k? (Se corta la búsqueda con éxito en cuanto se halle uno de tamaño ≤ k).

---

### Patrón de Ejercicio 3.4: Suma de Subconjuntos (Subset Sum) con Podas

Exploración binaria de inclusión/exclusión de elementos para alcanzar un valor objetivo exacto.

---

### Ejercicio 12 — Suma de Subconjuntos con Podas Tempranas

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Guía de Ejercicios 03, Ejercicio 11 / Práctica

**Enunciado**  
Dada una lista de enteros positivos L y un entero objetivo S, implementar un algoritmo por backtracking que determine si existe un subconjunto de L cuya suma sea exactamente S, y en caso afirmativo devuelva dicho subconjunto. Indicar las podas aplicadas.

**Qué está evaluando**  
Árbol binario de inclusión/exclusión, poda por exceso de suma y optimización mediante ordenamiento previo.

**Idea de resolución**  
1. Ordenamos L de menor a mayor.
2. En el índice i, tenemos dos ramas:
   * **Incluir L[i]:** Sumamos L[i] y avanzamos al siguiente índice.
   * **Excluir L[i]:** Mantenemos la suma y avanzamos al siguiente índice.
3. **Podas:**
   * Si la suma actual supera S, podar inmediatamente (elementos positivos).
   * Al estar ordenado, si la suma actual más L[i] supera S, ningún elemento posterior entrará; se corta el bucle de prueba.

**Pseudocódigo**

```text
FUNCION SubsetSumBT(L, S):
    ORDENAR L ASCENDENTE
    INICIALIZAR solucion como lista vacía
    exito <- SubsetSumRec(L, 0, S, solucion)
    SI exito:
        RETORNAR solucion
    RETORNAR "No existe subconjunto"

FUNCION SubsetSumRec(L, indice, remanente, solucion):
    // Caso base: alcanzamos la suma exacta
    SI remanente = 0:
        RETORNAR VERDADERO

    // Caso base: sin elementos o remanente negativo
    SI indice >= longitud(L) O remanente < 0:
        RETORNAR FALSO

    // Poda por ordenamiento: si el elemento actual supera el remanente,
    // ninguno de los siguientes podrá entrar
    SI L[indice] > remanente:
        RETORNAR FALSO

    // Rama 1: Incluir L[indice]
    INSERTAR L[indice] EN solucion
    SI SubsetSumRec(L, indice + 1, remanente - L[indice], solucion):
        RETORNAR VERDADERO
    ELIMINAR_ULTIMO(solucion) // Backtrack

    // Rama 2: Excluir L[indice]
    SI SubsetSumRec(L, indice + 1, remanente, solucion):
        RETORNAR VERDADERO

    RETORNAR FALSO
```

**Complejidad**  
* **Tiempo:** O(2ⁿ) en el peor caso, pero fuertemente reducido por las podas con L ordenado.
* **Espacio:** O(n) por la pila de recursión y la lista de la solución.

---

### Errores Frecuentes en Exámenes sobre Backtracking

1. **Olvidar desmarcar el estado en el retorno (Backtrack):** Dejar variables modificadas al salir de una llamada arruina la exploración de las ramas hermanas.
2. **Validar restricciones recorriendo estructuras completas:** Usar bucles en cada nodo en vez de booleanos de control O(1).
3. **No justificar la complejidad en el peor caso:** Afirmar que con podas el algoritmo pasa a ser polinomial. Las podas optimizan el caso promedio, pero el peor caso sigue siendo exponencial o factorial.
4. **No podar simetrías:** Permitir explorar permutaciones del mismo conjunto en problemas de combinatoria.
"""
