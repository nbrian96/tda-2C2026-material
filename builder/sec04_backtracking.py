"""Módulo 4: Backtracking y Branch & Bound."""

def get_content():
    return r"""## 6. Tema 3: Backtracking y Branch & Bound

### Conceptos Mínimos de Supervivencia

1. **Definición del Paradigma:**
   Backtracking es una técnica de búsqueda exhaustiva sistemática sobre un **árbol de estados combinatorios**. Avanza construyendo soluciones candidatas paso a paso; en cuanto determina que el estado actual no puede completarse para dar una solución válida u óptima, retrocede (*backtrack*) al estado anterior deshaciendo los cambios aplicados.

2. **Las Dos Clases Fundamentales de Podas:**
   * **Poda por Factibilidad (Feasibility Pruning):** Se aplica tanto en problemas de decisión como de optimización. Descarta una rama si el estado actual viola una restricción obligatoria del problema (por ejemplo, dos reinas en la misma diagonal, o la suma acumulada supera el valor objetivo).
   * **Poda por Cota u Optimalidad (Branch and Bound):** Se aplica en problemas de optimización. Se calcula una cota teórica (superior para maximización, inferior para minimización) del mejor valor que podría lograrse explorando el subárbol actual. Si esa cota no supera a la mejor solución factible ya registrada (`mejor_solucion`), la rama entera se poda de raíz.

3. **Estructuras Auxiliares para Validación en $O(1)$:**
   En los parciales es fuertemente penalizado verificar restricciones recorriendo estructuras con bucles $O(n)$ dentro de cada paso recursivo. Se deben emplear **arreglos o tablas booleanas auxiliares** para chequear y marcar ocupación en tiempo constante $O(1)$ (ejemplo: columnas y diagonales directas e inversas en N-Reinas).

4. **Complejidad en el Peor Caso:**
   Aunque las podas reducen drásticamente el tiempo de ejecución empírico, la complejidad asintótica en el peor caso sigue siendo exponencial ($O(2^n), O(k^n)$) o factorial ($O(n!)$), dado que los problemas resueltos típicamente son NP-Hard.

---

### Patrón de Ejercicio 3.1: Posicionamiento en Tableros con Estructuras O(1)

Aparece en enunciados de colocación de piezas (reinas, caballos, torres) donde se exige explicitar las estructuras de datos que garantizan validaciones en tiempo constante.

---

### Ejercicio 39 — Problema de las N Reinas con Control de Conflictos en O(1)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2025-1-2 (17 de junio de 2025), Ejercicio 4 / Guía v1.0 (Curso Echevarría), Ejercicio 3.3

**Enunciado**  
Realizar un algoritmo que resuelva el problema de las 8 reinas mediante backtracking. El problema consiste en ubicar 8 reinas en un tablero de ajedrez de $8 \times 8$ de manera que no haya dos reinas en la misma fila, columna o diagonal. Indicar detalladamente las estructuras de datos utilizadas para representar el problema y la solución, garantizando que el chequeo de amenazas se realice en $O(1)$. Justificar la complejidad temporal y espacial.

**Qué está evaluando la cátedra**  
Construcción de un árbol de búsqueda fila por fila, uso de vectores booleanos de acceso directo para columnas y diagonales directas/inversas en $O(1)$, y gestión simétrica del estado (*hacer decisión $\to$ recursión $\to$ deshacer decisión*).

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Espacio de Búsqueda y Representación del Estado:**
  - Colocamos exactamente una reina por fila avanzando secuencialmente ($fila = 0, \dots, n-1$). Esto descarta automáticamente cualquier conflicto entre filas y reduce el espacio de búsqueda de $n^n$ a las $n!$ permutaciones de columnas.
  - El estado se representa con un arreglo unidimensional `solucion` de tamaño $n$, donde `solucion[i] = col` indica que en la fila $i$ la reina se ubica en la columna `col`.
* **Podas por Factibilidad con Verificación en $O(1)$:**
  Para validar en tiempo constante si una casilla $(fila, col)$ está amenazada sin recorrer el tablero con bucles $O(n)$, empleamos 3 arreglos booleanos de acceso directo:
  1. **Columnas (`col_ocupada[n]`):** Si la columna `col` ya tiene una reina, no se puede usar.
  2. **Diagonal Principal ($\setminus$, clave $fila - col + n - 1$):** Al movernos en diagonal descendente ($\Delta f = +1, \Delta c = +1$), la diferencia $fila - col$ permanece invariante en el rango $[-(n-1), n-1]$. Desplazamos con $+(n-1)$ para mapear a índices válidos $[0, 2n-2]$ en un arreglo booleano `diag_prin[2n - 1]`.
  3. **Diagonal Secundaria ($/$, clave $fila + col$):** Al movernos en diagonal ascendente ($\Delta f = -1, \Delta c = +1$), la suma $fila + col$ es invariante en el rango $[0, 2n-2]$. Usamos el arreglo booleano `diag_sec[2n - 1]`.
  - La casilla $(fila, col)$ es factible si y solo si los tres booleanos están en `Falso` (3 accesos indexados en tiempo $O(1)$).
* **Mecanismo de Backtracking (Restauración de Estado):**
  Al probar una columna factible, marcamos los 3 booleanos en `Verdadero` y asignamos `solucion[fila] = col`. Si la llamada recursiva no encuentra solución, es **estrictamente obligatorio** desmarcar los 3 booleanos en `Falso` y restaurar `solucion[fila] = -1` antes de probar la columna siguiente.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo NReinas(n):
    solucion = arreglo[-1] * n
    col_ocupada = arreglo[Falso] * n
    diag_prin = arreglo[Falso] * (2*n - 1)  // clave: fila - col + (n - 1)
    diag_sec = arreglo[Falso] * (2*n - 1)   // clave: fila + col
    si NReinasBT(0, solucion, col_ocupada, diag_prin, diag_sec, n):
        devolver solucion
    devolver "Sin solución"

función NReinasBT(fila, solucion, col_ocupada, diag_prin, diag_sec, n):
    si fila == n:
        devolver Verdadero  // Caso Base: se ubicaron las n reinas

    para col desde 0 hasta n - 1:
        dp = fila - col + (n - 1)
        ds = fila + col
        // Poda por factibilidad en O(1)
        si no col_ocupada[col] y no diag_prin[dp] y no diag_sec[ds]:
            solucion[fila] = col
            col_ocupada[col] = diag_prin[dp] = diag_sec[ds] = Verdadero
            si NReinasBT(fila + 1, solucion, col_ocupada, diag_prin, diag_sec, n):
                devolver Verdadero
            solucion[fila] = -1
            col_ocupada[col] = diag_prin[dp] = diag_sec[ds] = Falso  // Backtrack

    devolver Falso
```

#### 3. Justificación de Complejidad

* **Árbol de Recursión y Estado:**
  - El estado en cada llamada está determinado por la `fila` actual ($0 \le fila \le n$), con profundidad máxima $n$.
  - En la fila $0$ hay $n$ opciones; en la fila $1$, a lo sumo $n-1$ opciones libres; en la fila $k$, a lo sumo $n-k$ opciones.
* **Complejidad Temporal en Peor Caso:**
  - En el peor caso teórico (cuando no se poda o se buscan todas las soluciones), el árbol tiene a lo sumo $n!$ hojas. En cada nodo, las verificaciones y transiciones toman $O(1)$ gracias a los vectores booleanos. La cota superior asintótica en el peor caso es **$O(n!)$**.
* **Comportamiento Promedio con Podas:**
  - Las podas en $O(1)$ de las diagonales principales y secundarias descartan subárboles completos en los primeros niveles. Para $n = 8$, de las $8^8 \approx 16.7 \times 10^6$ configuraciones ingenuas y las $8! = 40.320$ permutaciones, el algoritmo evalúa apenas **876 nodos** para hallar la primera solución válida.
* **Complejidad Espacial:**
  - **$O(n)$** auxiliar: la pila de llamadas tiene profundidad $n$, el vector de solución requiere tamaño $n$, y los arreglos booleanos ocupan $n + 2(2n-1) = 5n - 2 = O(n)$ memoria contigua.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Olvidar desmarcar booleanos al retroceder:</strong> Si omites <code>col_ocupada[col] = False</code> tras retornar de la llamada recursiva, las ramas hermanas creerán que la columna continúa ocupada, causando que el algoritmo falle en encontrar soluciones válidas.</li>
    <li><strong>Verificar colisiones recorriendo las filas anteriores con un bucle:</strong> Hacer un bucle <code>for f in range(fila): if solucion[f] == col or ...</code> dentro de cada nodo agrega un costo $O(n)$ por estado, degradando la complejidad de verificación a $O(n \cdot n!)$ en lugar de $O(n!)$ con chequeo $O(1)$.</li>
    <li><strong>Error de signo en la diagonal principal:</strong> Olvidar el $+7$ en $f - col$ produce índices negativos (en Python mapea al final de la lista alterando otras diagonales; en C/Java arroja error de segmentación).</li>
  </ul>
</div>

---

### Patrón de Ejercicio 3.2: Descomposición Numérica con Cotas (Lagrange)

Problemas donde se debe descomponer un número entero en sumas de componentes (cuadrados, primos, monedas) bajo un número fijo de términos.

---

### Ejercicio 40 — Suma de Cuatro Cuadrados de Lagrange con Cotas y Podas

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2024-2-1 (5 de noviembre de 2024), Ejercicio 1 / Guía v1.0 (Curso Echevarría), Ejercicio 3.10

**Enunciado**  
El teorema de los cuatro cuadrados de Lagrange especifica que cualquier número entero no negativo $n$ puede expresarse como la suma de cuatro cuadrados de enteros no negativos:
$$n = w^2 + x^2 + y^2 + z^2$$

Desarrollar un algoritmo que, dado el valor de $n$, indique cuáles son los cuatro enteros no negativos que lo componen. Justificar detalladamente el árbol de decisiones, las podas aplicadas y la complejidad del algoritmo.

**Qué está evaluando la cátedra**  
Diseño de un árbol de backtracking acotado a profundidad 4, imposición de orden no creciente para eliminar ramas simétricas redundantes ($w \ge x \ge y \ge z$), poda por cota inferior y determinación analítica del último término en $O(1)$.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Espacio de Búsqueda y Definición del Estado:**
  - Se busca descomponer un entero $n \ge 0$ en la suma de 4 cuadrados no negativos: $n = w^2 + x^2 + y^2 + z^2$.
  - El árbol de búsqueda tiene profundidad fija de 4 niveles ($paso = 0, 1, 2, 3$). El estado en cada llamada se define por `(paso, remanente, max_limite)`.
* **Poda de Simetrías por Orden No Creciente:**
  - Para no evaluar las $4! = 24$ permutaciones equivalentes de la misma descomposición, imponemos la restricción monótona $w \ge x \ge y \ge z \ge 0$. Cada término $v$ a probar no puede superar el valor asignado en el paso anterior (`max_limite`).
* **Poda por Factibilidad (Cota Superior):**
  - Ningún término $v$ puede superar la raíz cuadrada entera del remanente actual $R$: $v \le \min(max\_limite, \lfloor\sqrt{R}\rfloor)$.
* **Poda por Cota Inferior (Optimalidad / Alcance):**
  - Quedan $terminos\_restantes = 4 - paso$ términos por asignar. Como los valores son no crecientes, cada uno aportará a lo sumo $v^2$. Si $(4 - paso) \cdot v^2 < R$, es matemáticamente imposible cubrir $R$ con valores menores o iguales a $v$. Se interrumpe el bucle de prueba (`break`), podando todo el subárbol inferior.
* **Poda Analítica del 4° Término en $O(1)$:**
  - Al llegar a $paso = 3$, no se itera. Se calcula en $O(1)$ si el remanente $R$ es un cuadrado perfecto: $z = \lfloor\sqrt{R}\rfloor$. Si $z^2 == R$ y $z \le max\_limite$, se asigna $solucion[3] = z$ y se retorna con éxito directamente.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo CuatroCuadradosLagrange(n):
    solucion = arreglo [0, 0, 0, 0]
    si LagrangeBT(0, n, entero(raiz(n)), solucion):
        devolver solucion
    devolver "Sin solución"

función LagrangeBT(paso, remanente, max_limite, solucion):
    // 4to término resuelto analíticamente en O(1)
    si paso == 3:
        z = entero(raiz(remanente))
        si z * z == remanente y z <= max_limite:
            solucion[3] = z
            devolver Verdadero
        devolver Falso

    limite_sup = min(max_limite, entero(raiz(remanente)))
    para v desde limite_sup bajando hasta 0:
        // Poda por cota inferior: ni usando v en los términos restantes alcanzamos remanente
        si (4 - paso) * (v * v) < remanente:
            romper bucle // Ningún valor menor podrá alcanzarlo

        solucion[paso] = v
        si LagrangeBT(paso + 1, remanente - v * v, v, solucion):
            devolver Verdadero

    devolver Falso
```

#### 3. Justificación de Complejidad

* **Árbol de Recursión y Estado:**
  - El árbol posee una profundidad constante de a lo sumo 4 niveles ($paso \in \{0, 1, 2, 3\}$).
  - En cada nivel $k$, la variable $v$ toma valores entre $0$ y $\lfloor\sqrt{n}\rfloor$.
* **Complejidad Temporal en Peor Caso:**
  - Sin optimizaciones, 4 bucles anidados hasta $\sqrt{n}$ requerirían $O((\sqrt{n})^4) = O(n^2)$.
  - Al resolver el último término analíticamente en $O(1)$ mediante raíz entera, el árbol se reduce a 3 niveles libres, acotando el peor caso teórico a **$O(n^{3/2})$**.
* **Comportamiento Promedio con Podas:**
  - La restricción de orden monótono $w \ge x \ge y \ge z$ divide el espacio de búsqueda por $4! = 24$.
  - La poda por cota inferior $(4 - paso) \cdot v^2 < R$ trunca de raíz las ramas infértiles, provocando que la búsqueda encuentre descomposiciones válidas casi de forma directa.
* **Complejidad Espacial:**
  - **$O(1)$** auxiliar: la pila recursiva tiene profundidad fija de 4 marcos y el arreglo de solución tiene 4 posiciones constantes.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Iterar el 4to cuadrado en un bucle:</strong> Si el alumno escribe 4 bucles anidados en lugar de resolver el último término con <code>isqrt(remanente)</code> en $O(1)$, la cátedra descuenta puntos por falta de optimización algorítmica.</li>
    <li><strong>No imponer $w \ge x \ge y \ge z$:</strong> Permitir que los valores crezcan nuevamente en niveles inferiores provoca que el algoritmo evalúe las 24 permutaciones de la misma suma, multiplicando innecesariamente el tiempo de cómputo.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 3.3: Cobertura en Grafos con Branch and Bound (Vertex Cover)

Aparece cuando se solicita un algoritmo exacto para un problema NP-Hard sobre grafos no dirigidos.

---

### Ejercicio 41 — Vertex Cover Mínimo por Branch and Bound

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2024-2-2 (26 de noviembre de 2024), Ejercicio 1 / Guía 03 Ejercicio 13

**Enunciado**  
Implementar un algoritmo que dado un grafo no dirigido $G = (V, E)$ devuelva un conjunto de vértices que represente un mínimo Vertex Cover del mismo. Explicar el árbol de decisiones, las podas aplicadas y la complejidad.

**Qué está evaluando la cátedra**  
Estrategia de ramificación sobre aristas no cubiertas (al menos uno de los dos extremos debe pertenecer a la cobertura), poda por cota superior (*Branch and Bound*) descartando ramas que alcancen o superen el mejor tamaño ya hallado.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Espacio de Búsqueda y Definición del Problema:**
  - Un Vertex Cover es un conjunto $C \subseteq V$ tal que toda arista $(u, v) \in E$ tiene al menos un extremo en $C$ ($u \in C \lor v \in C$). Buscamos minimizar $|C|$.
  - El espacio de búsqueda combinatorio de todos los subconjuntos tiene tamaño $2^{|V|}$.
* **Estrategia de Ramificación por Arista No Cubierta (Factor de Ramificación 2):**
  - En lugar de ramificar vértice por vértice, buscamos una arista $(u, v) \in E$ que aún no esté cubierta por la selección actual ($u \notin C \land v \notin C$).
  - Como obligatoriamente toda arista debe ser cubierta por una solución factible, al menos uno de sus dos extremos debe estar en $C$. Por ende, bifurcamos en exactamente dos ramas:
    1. **Rama 1:** Incluir el vértice $u$ en $C$ y continuar la búsqueda.
    2. **Rama 2:** Incluir el vértice $v$ en $C$ y continuar la búsqueda.
* **Poda por Optimalidad (Branch and Bound):**
  - Mantenemos la mejor cobertura factible encontrada hasta el momento (`mejor_solucion`), inicializada con $V$ (tamaño $|V|$).
  - Si en cualquier nodo del árbol $|C_{\text{actual}}| \ge |mejor\_solucion|$, **podamos la rama de inmediato**. Como los costos son no negativos, ninguna extensión de $C_{\text{actual}}$ podrá mejorar el récord actual.
* **Caso Base:**
  - Si no quedan aristas sin cubrir y $|C_{\text{actual}}| < |mejor\_solucion|$, se halló una cobertura válida estrictamente menor: se actualiza `mejor_solucion` con una copia profunda de $C_{\text{actual}}$.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo MinimoVertexCover(V, E):
    mejor_sol = copiar(V)  // Cota superior inicial
    actual = conjunto_vacio()
    VertexCoverBT(actual, mejor_sol, E)
    devolver mejor_sol

función VertexCoverBT(actual, ref mejor_sol, E):
    // Poda por optimalidad (Branch & Bound)
    si tamaño(actual) >= tamaño(mejor_sol):
        devolver

    arista = BuscarAristaNoCubierta(E, actual)
    si arista es nulo:  // Caso Base: todas las aristas cubiertas con menor tamaño
        mejor_sol = copiar(actual)
        devolver

    (u, v) = arista

    // Rama 1: Incluir u
    agregar u a actual
    VertexCoverBT(actual, mejor_sol, E)
    quitar u de actual  // Backtrack

    // Rama 2: Incluir v
    agregar v a actual
    VertexCoverBT(actual, mejor_sol, E)
    quitar v de actual  // Backtrack
```

#### 3. Justificación de Complejidad

* **Árbol de Recursión y Estado:**
  - El estado está definido por el conjunto `actual` de vértices seleccionados.
  - El árbol es binario (factor de ramificación 2). Cada bifurcación cubre al menos una arista nueva, por lo que la profundidad máxima del árbol está acotada por el tamaño del Vertex Cover óptimo $k = |C^*| \le |V|$.
* **Complejidad Temporal en Peor Caso:**
  - La cantidad de nodos del árbol es a lo sumo $2^{k+1} - 1$. En cada nodo se inspecciona el conjunto de aristas para hallar una no cubierta en $O(|E|)$.
  - Por lo tanto, la complejidad en el peor caso es **$O(2^k \cdot |E|)$** (algoritmo FPT - *Fixed Parameter Tractable*), exponencialmente superior al enfoque ingenuo de subconjuntos $O(2^{|V|} \cdot |E|)$ cuando $k \ll |V|$.
* **Comportamiento Promedio con Podas:**
  - La poda de Branch & Bound $|actual| \ge |mejor\_sol|$ elimina ramas completas en cuanto se iguala la cota. Inicializar la cota con una heurística rápida reduce todavía más los nodos evaluados.
* **Complejidad Espacial:**
  - **$O(|V| + |E|)$**: $O(|V|)$ para almacenar el conjunto actual y la mejor solución en la pila de recursión (profundidad $\le k \le |V|$), más el almacenamiento del grafo $G$.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Podar con <code>&gt;</code> en vez de <code>&gt;=</code>:</strong> La poda debe ser <code>len(actual) &gt;= len(mejor_cobertura)</code>. Si usas <code>&gt;</code>, el algoritmo continuará explorando ramas de tamaño igual al récord que jamás podrán mejorarlo, duplicando el tiempo de ejecución.</li>
    <li><strong>No copiar la solución óptima:</strong> Escribir <code>mejor_cobertura = actual</code> guarda una referencia al conjunto mutable. Al hacer backtracking, <code>mejor_cobertura</code> se vacía junto con <code>actual</code>. Se debe hacer siempre copia profunda con <code>set(actual)</code>.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 3.4: Suma de Subconjuntos (Subset Sum) con Podas

Exploración binaria de inclusión/exclusión de elementos para alcanzar un valor objetivo exacto.

---

### Ejercicio 42 — Suma de Subconjuntos con Podas Tempranas

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía de Ejercicios 03, Ejercicio 11 / Práctica

**Enunciado**  
Dada una lista de enteros positivos $L$ y un entero objetivo $S$, implementar un algoritmo por backtracking que determine si existe un subconjunto de $L$ cuya suma sea exactamente $S$, y en caso afirmativo devuelva dicho subconjunto. Indicar y justificar las podas de factibilidad aplicadas y la complejidad.

**Qué está evaluando la cátedra**  
Árbol binario de inclusión/exclusión, poda temprana por exceso de suma y optimización del espacio de búsqueda mediante ordenamiento previo de los elementos.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Espacio de Búsqueda y Definición del Estado:**
  - Dada una lista $L$ de $n$ enteros positivos y un entero objetivo $S$, se busca encontrar un subconjunto cuya suma sea exactamente $S$.
  - Árbol de decisiones binario de inclusión/exclusión: para cada elemento $L[i]$ se decide si formará parte del subconjunto o no. El estado se define por `(i, remanente)`.
* **Optimización Previa (Ordenamiento Ascendente):**
  - Se ordena la lista $L$ de menor a mayor en $O(n \log n)$. Esto garantiza que para todo $j > i$, $L[j] \ge L[i]$.
* **Poda por Factibilidad (Corte Temprano por Ordenamiento):**
  - Si en el índice actual $L[i] > remanente$, como la lista está ordenada crecientemente, todos los elementos posteriores satisfacen $L[j] \ge L[i] > remanente$. Por lo tanto, **ningún elemento posterior podrá ser incluido sin exceder la suma**. Se corta la búsqueda de inmediato retornando `Falso`, podando el subárbol completo.
* **Casos Base:**
  - Éxito: si $remanente == 0$, se alcanzó la suma exacta $S$; se devuelve `Verdadero`.
  - Fallo: si $i == \text{longitud}(L)$ (se agotaron los elementos) o $remanente < 0$, se devuelve `Falso`.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo SubsetSum(L, S):
    ordenar L de menor a mayor  // Habilita poda temprana en O(n log n)
    solucion = []
    si SubsetSumBT(0, S, L, solucion):
        devolver solucion
    devolver "Sin solución"

función SubsetSumBT(i, remanente, L, solucion):
    si remanente == 0:
        devolver Verdadero
    si i == longitud(L) o remanente < 0:
        devolver Falso

    // Poda temprana: al estar ordenado, ningún elemento posterior entrará
    si L[i] > remanente:
        devolver Falso

    // Rama 1: Incluir L[i]
    agregar L[i] a solucion
    si SubsetSumBT(i + 1, remanente - L[i], L, solucion):
        devolver Verdadero
    quitar_ultimo(solucion)  // Backtrack

    // Rama 2: Excluir L[i]
    si SubsetSumBT(i + 1, remanente, L, solucion):
        devolver Verdadero

    devolver Falso
```

#### 3. Justificación de Complejidad

* **Árbol de Recursión y Estado:**
  - El estado en cada llamada está determinado por el índice $i$ ($0 \le i \le n$) y el $remanente \ge 0$.
  - El árbol tiene altura $n$ y factor de ramificación 2 (inclusión y exclusión).
* **Complejidad Temporal en Peor Caso:**
  - En el peor caso teórico (cuando no existe solución y los elementos son muy pequeños, impidiendo que actúe la poda temprana hasta el final), el árbol genera a lo sumo $2^{n+1} - 1$ nodos.
  - Ordenar $L$ cuesta $O(n \log n)$, por lo que la cota asintótica en el peor caso es **$O(2^n)$**.
* **Comportamiento Promedio con Podas:**
  - Gracias al ordenamiento previo, la condición $L[i] > remanente$ actúa a niveles altos del árbol, eliminando ramas completas antes de llegar a las hojas y reduciendo drásticamente los nodos evaluados en instancias reales.
* **Complejidad Espacial:**
  - **$O(n)$** auxiliar: la pila recursiva alcanza una profundidad máxima de $n$ niveles y el vector `solucion` almacena a lo sumo $n$ elementos.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Aplicar la poda <code>L[i] &gt; remanente</code> sin ordenar:</strong> La poda por exceso solo es válida si la lista está previamente ordenada. Si la lista contiene números desordenados (por ejemplo $[10, 2]$ con $R = 5$), descartar por $10 > 5$ omitiría erróneamente al $2$.</li>
    <li><strong>Números negativos o nulos:</strong> Esta poda asume que todos los elementos son positivos ($L[i] > 0$). Si hubiera números negativos, sumar un elemento posterior podría reducir la suma actual y permitir alcanzar el objetivo.</li>
  </ul>
</div>

---

### Ejercicio 43 — Explorador en el Laberinto (Camino al Tesoro y Camino Más Corto)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2026-2-1 (Enunciados), Ejercicio 2

**Enunciado**  
Un explorador se encuentra en un laberinto representado por una matriz de $N \times M$. Debe encontrar un camino desde la Entrada hasta el tesoro. La matriz está codificada con `0` (casilla transitable), `1` (pared, intransitable), `E` (Entrada) y `T` (Tesoro). Puede moverse hacia arriba, abajo, izquierda o derecha, sin atravesar paredes ni visitar dos veces una misma casilla en el mismo camino.
1. Diseñar un algoritmo de backtracking que encuentre y devuelva un camino desde la entrada hasta el tesoro.
2. Indicar la complejidad del algoritmo.
3. Indicar cómo cambiarías el algoritmo si se pide **EL CAMINO MÁS CORTO** hasta el tesoro.

#### 1. Idea y Justificación en Lenguaje Natural

* **1. Para encontrar UN camino cualquiera:**
  - Desde la posición actual `(f, c)`, si estamos parados sobre `'T'` (el Tesoro), ¡éxito! Devolvemos `Verdadero`.
  - Si no, probamos movernos a cada una de las 4 casillas vecinas `(nf, nc)` (arriba, abajo, izquierda, derecha).
  - **Poda por Factibilidad:** Solo avanzamos a `(nf, nc)` si está dentro de los límites de la matriz, no es pared (`!= 1`) y no fue visitada todavía en el camino actual (`no visitado[nf][nc]`).
  - Marcamos la casilla como visitada, la agregamos al camino y llamamos recursivamente. Si esa llamada encuentra el tesoro, cortamos y devolvemos el camino; si no tiene salida, **desmarcamos la casilla (`visitado[nf][nc] = Falso`) y la sacamos del camino** (backtrack) para probar otra dirección.
* **2. Complejidad Temporal:**
  - En cada casilla tenemos hasta 4 direcciones posibles (3 reales porque no volvemos hacia la casilla de la que acabamos de venir), y la longitud máxima de un camino sin repetir casillas es $N \cdot M$. Por lo tanto, en el peor caso explora **$O(4^{N \cdot M})$** (o más ajustado **$O(3^{N \cdot M})$**) estados, con espacio auxiliar $O(N \cdot M)$.
* **3. ¿Cómo cambiaríamos el algoritmo si se pide EL CAMINO MÁS CORTO?**
  - **Con Backtracking (Branch & Bound):**
    1. En vez de frenar y devolver `Verdadero` al encontrar el primer camino a `'T'`, **guardamos ese camino como `mejor_camino`** (si es más corto que el `mejor_camino` registrado hasta ahora) y **seguimos explorando** el resto de las ramas.
    2. **Agregamos Poda por Optimalidad (Branch & Bound):** Si en cualquier momento el largo de nuestro `camino_actual` (más la distancia Manhattan hasta `T`) ya es **mayor o igual** al largo del `mejor_camino` que ya tenemos guardado (`longitud(camino_actual) >= longitud(mejor_camino)`), **podamos la rama inmediatamente** sin seguir avanzando.
  - *(Nota adicional para sumar puntos en el parcial: Como todas las aristas pesan 1 paso, el camino más corto en una grilla sin pesos también se puede resolver de forma óptima en tiempo polinomial $O(N \cdot M)$ cambiando la búsqueda a **BFS — Búsqueda a lo Ancho** con una cola).*

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo BuscarCaminoLaberinto(M, N_filas, M_cols):
    (f_ini, c_ini) = encontrarPosicion(M, 'E')
    visitado = matriz de N_filas x M_cols en Falso
    visitado[f_ini][c_ini] = Verdadero
    camino = [ (f_ini, c_ini) ]

    si ExplorarBT(M, f_ini, c_ini, visitado, camino):
        devolver camino
    devolver "No existe camino al tesoro"

función ExplorarBT(M, f, c, visitado, camino):
    // Caso base: llegamos al Tesoro
    si M[f][c] == 'T':
        devolver Verdadero

    direcciones = [ (-1, 0), (1, 0), (0, -1), (0, 1) ]  // Arriba, Abajo, Izq, Der

    para cada (df, dc) en direcciones:
        nf = f + df, nc = c + dc

        // Poda de factibilidad: dentro del mapa, no es pared y no fue visitada
        si esValida(nf, nc, M) y M[nf][nc] != 1 y no visitado[nf][nc]:
            // 1. Marcar paso
            visitado[nf][nc] = Verdadero
            agregar (nf, nc) a camino

            // 2. Explorar recursivamente
            si ExplorarBT(M, nf, nc, visitado, camino):
                devolver Verdadero

            // 3. Deshacer paso (Backtrack)
            quitar_ultimo(camino)
            visitado[nf][nc] = Falso

    devolver Falso
```

---

### Ejercicio 44 — Suma de Dados (Todas las Tiradas que Suman S)

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 3.1

**Enunciado**  
Implementar un algoritmo de backtracking que reciba una cantidad de dados $n$ y una suma $s$, y devuelva todas las tiradas posibles de $n$ dados (caras del 1 al 6) cuya suma sea exactamente $s$.

#### 1. Idea y Justificación en Lenguaje Natural

* En cada nivel decidimos qué valor (del 1 al 6) salió en el dado actual, restándolo de la suma que nos falta (`faltante`).
* **Podas claves para no explorar ramas inútiles:**
  If nos quedan `dados_restantes` por tirar:
  1. **Poda por suma mínima:** Si aun sacando puros `1` en todos los dados que faltan nos pasamos de lo que falta (`faltante < dados_restantes * 1`), podamos.
  2. **Poda por suma máxima:** Si ni siquiera sacando puros `6` en todos los dados que faltan llegamos a cubrir lo que falta (`faltante > dados_restantes * 6`), podamos.
* Complejidad en peor caso: **$O(6^n)$**.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo TiradasSumaDados(n, s):
    resultados = []
    actual = []
    DadosBT(n, s, actual, resultados)
    devolver resultados

función DadosBT(dados_restantes, faltante, actual, resultados):
    // Caso base: ya tiramos todos los dados
    si dados_restantes == 0:
        si faltante == 0:
            agregar copia(actual) a resultados
        devolver

    // Podas por mínimo (todos 1) y máximo (todos 6) alcanzables
    si faltante < dados_restantes * 1 o faltante > dados_restantes * 6:
        devolver

    para cara desde 1 hasta 6:
        agregar cara a actual
        DadosBT(dados_restantes - 1, faltante - cara, actual, resultados)
        quitar_ultimo(actual)   // Backtrack
```

---

### Ejercicio 45 — Maximizar Sumatoria sin Superar N

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 3.2

**Enunciado**  
Dada una lista de enteros positivos $L$ y un entero $n$, implementar un algoritmo de backtracking que devuelva un subconjunto de $L$ que sume exactamente $n$, o, en caso de no existir, que devuelva el subconjunto de suma máxima sin superar el valor de $n$.

#### 1. Idea y Justificación en Lenguaje Natural

* Es una versión de **Branch & Bound** de *Subset Sum*: llevamos registro de la `mejor_solucion` y su `mejor_suma` (inicialmente `0`) que nunca supere $n$.
* En cada elemento `L[i]` probamos incluirlo (si `suma_actual + L[i] <= n`) o excluirlo.
* **Podas:**
  1. **Corte inmediato por óptimo exacto:** Si `mejor_suma == n`, ya encontramos un subconjunto que suma exactamente $n$, así que cortamos todas las llamadas pendientes de inmediato.
  2. **Poda por cota superior (sufijo restante):** Si sumando `suma_actual` más todos los números que quedan de `i` en adelante (`suma_restante`) no superamos a `mejor_suma` (`suma_actual + suma_restante <= mejor_suma`), podamos la rama porque es imposible mejorar el récord.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo MaximizarSubconjunto(L, n):
    mejor_sol = []
    mejor_suma = 0
    actual = []
    MaxSumaBT(L, 0, n, 0, sumaTotal(L), actual, mejor_sol, mejor_suma)
    devolver mejor_sol

función MaxSumaBT(L, i, n, suma_act, resto_disp, actual, ref mejor_sol, ref mejor_suma):
    si suma_act > mejor_suma:
        mejor_suma = suma_act
        mejor_sol = copia(actual)

    // Si ya llegamos exacto a n, o se acabaron los números, o ni sumando todo lo que queda mejoramos:
    si mejor_suma == n o i == longitud(L) o (suma_act + resto_disp <= mejor_suma):
        devolver

    // Rama 1: Incluir L[i] (Poda de factibilidad: no pasarse de n)
    si suma_act + L[i] <= n:
        agregar L[i] a actual
        MaxSumaBT(L, i + 1, n, suma_act + L[i], resto_disp - L[i], actual, mejor_sol, mejor_suma)
        quitar_ultimo(actual)

    // Rama 2: Excluir L[i]
    si mejor_suma < n:
        MaxSumaBT(L, i + 1, n, suma_act, resto_disp - L[i], actual, mejor_sol, mejor_suma)
```

---

### Ejercicio 46 — Resolución de Sudoku por Backtracking

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 3.4

**Enunciado**  
Dada una matriz de $9 \times 9$ parcialmente completada (con `0` en las casillas vacías), implementar un algoritmo de backtracking que llene la matriz con números del 1 al 9 sin repetir número en cada fila, columna ni subgrupo de $3 \times 3$.

#### 1. Idea y Justificación en Lenguaje Natural

* Buscamos la primera celda vacía `(f, c)` del tablero (si no queda ninguna vacía, ¡el Sudoku ya está resuelto!).
* Probamos colocar cada número `num` del `1` al `9` en esa celda:
  - **Poda por Factibilidad:** Solo colocamos `num` si todavía no aparece en la fila `f`, ni en la columna `c`, ni en su bloque de $3 \times 3$ (cuyo inicio es `(f // 3) * 3` y `(c // 3) * 3`).
  - Lo escribimos y llamamos recursivamente. Si la recursión devuelve `Verdadero`, terminamos; si no, **borramos el número volviendo a poner `0`** (backtrack) y probamos el siguiente.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo ResolverSudoku(tablero):
    celda = buscarPrimeraCeldaVacia(tablero)
    si celda es nulo:
        devolver Verdadero   // No quedan casillas vacías: Sudoku completo

    (f, c) = celda
    para num desde 1 hasta 9:
        si esValidoSudoku(tablero, f, c, num):
            tablero[f][c] = num
            si ResolverSudoku(tablero):
                devolver Verdadero
            tablero[f][c] = 0    // Backtrack

    devolver Falso

función esValidoSudoku(tablero, f, c, num):
    // Verificar fila f, columna c y subcuadrante 3x3 de esquina (f - f%3, c - c%3)
    devolver (num no está en fila f) y (num no está en col c) y (num no está en bloque 3x3 de (f, c))
```

---

### Ejercicio 47 — Recorrido del Caballo (Knight Tour)

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 3.5

**Enunciado**  
Implementar un algoritmo de backtracking que, dado un caballo en un tablero de ajedrez de $8 \times 8$, determine la secuencia de movimientos en forma de $L$ para que el caballo pase por los 64 casilleros del tablero una única vez.

#### 1. Idea y Justificación en Lenguaje Natural

* Llevamos en la matriz `tablero[8][8]` el número de paso en que visitamos cada casilla (de `1` a `64`, y `0` si está libre).
* Si `paso == 64`, ya visitamos las 64 casillas y terminamos.
* Si no, desde la posición actual `(f, c)` probamos los **8 saltos posibles en forma de L** del caballo (`(±2, ±1)` y `(±1, ±2)`).
* **Poda de factibilidad:** Que la nueva casilla `(nf, nc)` esté dentro del tablero $8 \times 8$ y no haya sido visitada aún (`tablero[nf][nc] == 0`).

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo KnightTour(f_ini, c_ini):
    tablero = matriz de 8x8 inicializada en 0
    tablero[f_ini][c_ini] = 1   // Paso 1 en la casilla inicial

    si CaballoBT(tablero, f_ini, c_ini, 1):
        devolver tablero
    devolver "Sin solución"

función CaballoBT(tablero, f, c, paso):
    si paso == 64:
        devolver Verdadero

    saltos_L = [ (2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1) ]

    para cada (df, dc) en saltos_L:
        nf = f + df, nc = c + dc
        si 0 <= nf < 8 y 0 <= nc < 8 y tablero[nf][nc] == 0:
            tablero[nf][nc] = paso + 1
            si CaballoBT(tablero, nf, nc, paso + 1):
                devolver Verdadero
            tablero[nf][nc] = 0   // Backtrack

    devolver Falso
```

---

### Ejercicio 48 — Coloreo de Grafos con N Colores

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 3.6 / Guía 03, Ejercicio 2

**Enunciado**  
Implementar un algoritmo que reciba un grafo y un número $n$ que, utilizando backtracking, indique si es posible pintar cada vértice con $n$ colores de tal forma que no haya dos vértices adyacentes con el mismo color.

#### 1. Idea y Justificación en Lenguaje Natural

* Numeramos los vértices de `0` a `V - 1` y vamos pintando **un vértice por nivel recursivo**.
* Al estar en el vértice `v`, probamos asignarle cada color `c` desde `1` hasta `n`:
  - **Poda por Factibilidad:** Miramos a los vecinos de `v` en el grafo; si ningún vecino tiene puesto el color `c`, se lo asignamos a `v` y pasamos recursivamente al vértice `v + 1`.
  - Si la llamada falla, despintamos a `v` (`color[v] = 0`) y probamos el siguiente color.
* Complejidad en peor caso: **$O(n^{|V|})$**.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo ColorearGrafo(G, n_colores):
    vertices = G.obtenerVertices()
    color = diccionario inicializado en 0 para cada v en vertices
    devolver ColorearBT(G, vertices, 0, n_colores, color)

función ColorearBT(G, vertices, idx, n_colores, color):
    // Caso base: todos los vértices fueron pintados sin conflicto
    si idx == longitud(vertices):
        devolver Verdadero

    v = vertices[idx]
    para c desde 1 hasta n_colores:
        // Poda de factibilidad: ningún vecino adyacente debe tener el color c
        si para todo vecino w de v en G se cumple (color[w] != c):
            color[v] = c
            si ColorearBT(G, vertices, idx + 1, n_colores, color):
                devolver Verdadero
            color[v] = 0   // Backtrack

    devolver Falso
```

---

### Ejercicio 49 — Camino Hamiltoniano por Backtracking

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 3.7

**Enunciado**  
Un camino hamiltoniano es un camino de un grafo que visita todos los vértices del grafo una sola vez. Implementar un algoritmo de backtracking que encuentre un camino hamiltoniano de un grafo dado.

#### 1. Idea y Justificación en Lenguaje Natural

* Probamos iniciar el camino desde cada vértice `v` del grafo.
* En cada paso recursivo, si la lista `camino` ya tiene longitud `|V|`, visitamos todos los vértices una sola vez y devolvemos `Verdadero`.
* Si no, miramos los adyacentes del último vértice agregado (`actual`): para cada vecino `w` que **todavía no esté en `visitados`** (poda de factibilidad en $O(1)$ usando un set/arreglo booleano), lo marcamos como visitado, lo agregamos al camino y llamamos recursivamente. Si no llega a solución, lo sacamos y desmarcamos. Complejidad en peor caso: **$O(|V|!)$**.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo CaminoHamiltoniano(G):
    para cada v en G.vertices():
        camino = [ v ]
        visitados = { v }
        si HamiltonianoBT(G, v, camino, visitados):
            devolver camino
    devolver nulo

función HamiltonianoBT(G, actual, camino, visitados):
    si longitud(camino) == G.cantidadVertices():
        devolver Verdadero

    para cada vecino w en G.adyacentes(actual):
        si w no está en visitados:
            agregar w a visitados
            agregar w a camino

            si HamiltonianoBT(G, w, camino, visitados):
                devolver Verdadero

            quitar_ultimo(camino)     // Backtrack
            quitar w de visitados

    devolver Falso
```

---

### Ejercicio 50 — Maximum Independent Set (Conjunto Independiente Máximo)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 3.8 / Guía 03, Ejercicio 4

**Enunciado**  
Implementar un algoritmo que, dado un grafo no dirigido, devuelva un conjunto de vértices que represente un Maximum Independent Set del mismo (el subconjunto más grande posible de vértices donde ningún par sea adyacente entre sí).

#### 1. Idea y Justificación en Lenguaje Natural

* Es un problema de optimización (**Branch & Bound**): mantenemos el `mejor_conjunto` encontrado hasta el momento.
* En el vértice `idx` tenemos dos ramas:
  1. **Incluir el vértice `v`** en el conjunto actual, **solo si no es adyacente a ninguno de los ya incluidos** (Poda por Factibilidad).
  2. **Excluir el vértice `v`**.
* **Poda por Optimalidad (Branch & Bound):** Si el tamaño de nuestro conjunto `actual` más la cantidad de vértices que todavía quedan por evaluar (`restantes = |V| - idx`) **no supera al tamaño del `mejor_conjunto`** (`tamaño(actual) + restantes <= tamaño(mejor_conjunto)`), podamos la rama inmediatamente porque ni metiendo todos los vértices que quedan lograríamos superar el récord.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo MaxIndependentSet(G):
    vertices = G.vertices()
    mejor = []
    actual = []
    MisBT(G, vertices, 0, actual, mejor)
    devolver mejor

función MisBT(G, vertices, idx, actual, ref mejor):
    si longitud(actual) > longitud(mejor):
        mejor = copia(actual)

    restantes = longitud(vertices) - idx
    // Poda Branch & Bound: ni sumando todos los vértices restantes superamos a 'mejor'
    si idx == longitud(vertices) o (longitud(actual) + restantes <= longitud(mejor)):
        devolver

    v = vertices[idx]

    // Rama 1: Incluir v (Poda de factibilidad: sin aristas hacia los ya elegidos en actual)
    si para todo u en actual se cumple (no G.hayArista(v, u)):
        agregar v a actual
        MisBT(G, vertices, idx + 1, actual, mejor)
        quitar_ultimo(actual)   // Backtrack

    // Rama 2: Excluir v
    MisBT(G, vertices, idx + 1, actual, mejor)
```

---

### Ejercicio 51 — Isomorfismo de Grafos por Backtracking

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 3.9

**Enunciado**  
Implementar un algoritmo de backtracking que, dados dos grafos $G_1$ y $G_2$, determine si existe un Isomorfismo entre ambos (una correspondencia biyectiva entre sus vértices que preserve las adyacencias).

#### 1. Idea y Justificación en Lenguaje Natural

* Antes de empezar el backtracking aplicamos **filtros rápidos iniciales**: si $G_1$ y $G_2$ tienen distinta cantidad de vértices, distinta cantidad de aristas o distinta secuencia de grados ordenada, devolvemos `Falso` en el acto.
* Luego buscamos armar un diccionario `mapeo[u] = v` que asigne a cada vértice $u \in G_1$ un vértice $v \in G_2$ no usado aún:
  - **Poda por Grado:** Solo probamos mapear $u \to v$ si ambos tienen exactamente el **mismo grado** (`grado(G1, u) == grado(G2, v)`).
  - **Poda por Consistencia de Adyacencias:** Para todo vecino $u'$ de $u$ en $G_1$ que **ya haya sido mapeado**, su pareja `mapeo[u']` debe ser obligatoriamente vecina de $v$ en $G_2$ (y viceversa). Si falla, descartamos ese emparejamiento en el acto.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo SonIsomorfos(G1, G2):
    si G1.cantVertices() != G2.cantVertices() o G1.cantAristas() != G2.cantAristas():
        devolver Falso

    V1 = G1.vertices(), V2 = G2.vertices()
    mapeo = diccionario vacío      // u de G1 -> v de G2
    usados_G2 = conjunto vacío

    devolver IsomorfismoBT(G1, G2, V1, V2, 0, mapeo, usados_G2)

función IsomorfismoBT(G1, G2, V1, V2, idx, mapeo, usados_G2):
    si idx == longitud(V1):
        devolver Verdadero

    u = V1[idx]
    para cada v en V2:
        // Poda 1: v no usado y mismo grado que u
        si v no está en usados_G2 y G1.grado(u) == G2.grado(v):
            // Poda 2: preserva todas las aristas y no-aristas con los vértices ya mapeados
            si preservaAdyacencias(G1, G2, u, v, mapeo):
                mapeo[u] = v
                agregar v a usados_G2

                si IsomorfismoBT(G1, G2, V1, V2, idx + 1, mapeo, usados_G2):
                    devolver Verdadero

                quitar v de usados_G2   // Backtrack
                borrar mapeo[u]

    devolver Falso
```

---

### Ejercicio 52 — Podas para Criptoaritmética: SEND + MORE = MONEY

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 3.11

**Enunciado**  
Para el problema de fuerza bruta `"SEND + MORE = MONEY"` (asignar un dígito distinto de 0 a 9 a cada una de las 8 letras `S, E, N, D, M, O, R, Y` para que la suma sea válida), indicar **qué podas realizarías para agilizar su resolución por backtracking**. *(No se pide pseudocódigo, sólo explicar las podas).*

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Espacio de Búsqueda y Naturaleza del Problema:**
  - Asignar un dígito único $\{0, \dots, 9\}$ a cada una de las 8 letras $\{S, E, N, D, M, O, R, Y\}$ de modo que $SEND + MORE = MONEY$.
  - Una búsqueda exhaustiva ingenua sin podas evalúa $10^8 = 100.000.000$ asignaciones, o $P(10, 8) = 1.814.400$ permutaciones si se exige que no se repitan dígitos.
* **Podas Esenciales de Factibilidad y Dominio:**
  1. **Poda por Dígitos Únicos (Alldifferent en $O(1)$):** Arreglo booleano `usado[10]`. Ningún dígito puede asignarse a más de una letra.
  2. **Poda de Ceros a la Izquierda:** Como ningún número puede comenzar con cero, restringimos los dominios iniciales: $S \ne 0$ y $M \ne 0$.
  3. **Poda Analítica de Acarreo ($M = 1$ y $O = 0$):** Sumar dos números de 4 dígitos produce a lo sumo $9999 + 9999 = 19998$. La quinta cifra $M$ es el acarreo de los miles y debe ser **estrictamente $M = 1$**. Además, para que la columna de miles genere acarreo ($S + 1 + c_3 \ge 10$) con $S \le 9$, la letra resultante $O$ solo puede ser $0$ o $1$; como $M = 1$, forzosamente **$O = 0$** y $S \in \{8, 9\}$.
  4. **Poda Columna por Columna (Verificación Incremental de Derecha a Izquierda):**
     En lugar de asignar todas las letras y sumar al final, procesamos por columnas desde las unidades hacia los miles:
     - **Columna 0 (Unidades):** Asignar $D, E$. El dígito de $Y$ queda fijado analíticamente por $(D + E) \pmod{10}$ con acarreo $c_1 = (D + E) // 10$. Si $Y$ ya está usado o no coincide con una asignación previa, se poda la rama inmediatamente sin explorar las 5 letras restantes.
     - **Columnas 1, 2 y 3 (Decenas, Centenas, Miles):** Se valida incrementalmente en cada columna $(L_1 + L_2 + c_{prev}) \pmod{10} == L_3$. Al primer fallo se descarta el subárbol completo.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo CriptoSendMoreMoney():
    asignacion = mapa vacio  // letra -> digito
    usado = arreglo de 10 booleanos en Falso
    // Fijaciones analíticas iniciales obligatorias
    asignar('M', 1, asignacion, usado)
    asignar('O', 0, asignacion, usado)
    si CriptoBT(0, 0, asignacion, usado):
        devolver asignacion
    devolver "Sin solución"

función CriptoBT(col, acarreo, asignacion, usado):
    si col == 4:  // Caso Base: se validaron unidades, decenas, centenas y miles
        devolver (acarreo == asignacion['M'])

    (L1, L2, L3) = LetrasColumna(col)  // ej col 0: (D, E, Y)
    para cada d1 en Candidatos(L1, asignacion, usado):
        marcar(L1, d1, asignacion, usado)
        para cada d2 en Candidatos(L2, asignacion, usado):
            marcar(L2, d2, asignacion, usado)
            suma = d1 + d2 + acarreo
            d3, nuevo_ac = suma % 10, suma // 10
            // Poda por factibilidad de columna en O(1)
            si esValidoAsignar(L3, d3, asignacion, usado):
                marcar(L3, d3, asignacion, usado)
                si CriptoBT(col + 1, nuevo_ac, asignacion, usado):
                    devolver Verdadero
                desmarcar(L3, asignacion, usado)  // Backtrack
            desmarcar(L2, asignacion, usado)
        desmarcar(L1, asignacion, usado)

    devolver Falso
```

#### 3. Justificación de Complejidad

* **Árbol de Recursión y Estado:**
  - El estado se define por `(col, acarreo)`, con profundidad máxima acotada a las 4 columnas del problema.
* **Complejidad Temporal en Peor Caso:**
  - El espacio combinatorio sin podas es $P(10, 8) = \frac{10!}{2!} = 1.814.400$ permutaciones en el peor caso.
* **Comportamiento Promedio con Podas:**
  - Al fijar $M = 1$ y $O = 0$, reducir el dominio de $S \in \{8, 9\}$ y verificar la consistencia aritmética de cada columna de derecha a izquierda antes de ramificar, la gran mayoría de las combinaciones se descartan en el nivel 0 (unidades).
  - El número real de estados evaluados se reduce a menos de 50 llamadas recursivas, hallando la solución única $SEND = 9567, MORE = 1085, MONEY = 10652$ de forma prácticamente instantánea.
* **Complejidad Espacial:**
  - **$O(1)$** auxiliar: los arreglos de control de dígitos usados y asignación tienen tamaño 10 constante, y la pila recursiva alcanza una profundidad máxima de 4 marcos.

---

### Errores Frecuentes en Exámenes sobre Backtracking

1. **Olvidar desmarcar el estado en el retorno (Backtrack):** Dejar variables modificadas al salir de una llamada arruina la exploración de las ramas hermanas.
2. **Validar restricciones recorriendo estructuras completas:** Usar bucles en cada nodo en vez de booleanos de control $O(1)$.
3. **No justificar la complejidad en el peor caso:** Afirmar que con podas el algoritmo pasa a ser polinomial. Las podas optimizan el caso promedio, pero el peor caso sigue siendo exponencial o factorial.
4. **No podar simetrías:** Permitir explorar permutaciones del mismo conjunto en problemas de combinatoria.
"""
