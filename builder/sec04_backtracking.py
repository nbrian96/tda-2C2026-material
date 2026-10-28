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

#### 1. Deducción Metodológica Formal (Los 5 Pasos de Backtracking)

1. **Paso 1: Definición del Estado y Vector Solución:**
   Colocamos exactamente una reina por fila, avanzando fila por fila desde $fila = 0$ hasta $fila = 7$. Esto elimina automáticamente la posibilidad de conflictos de fila.
   El vector solución es un arreglo unidimensional `solucion` de longitud 8, donde `solucion[i] = col` indica que en la fila $i$ la reina fue colocada en la columna `col`.
2. **Paso 2: Deducción Matemática del Mapeo de Diagonales en $O(1)$:**
   * **Columnas:** Arreglo booleano `col_ocupada[8]`. Si la columna $c$ tiene una reina, `col_ocupada[c] = True`.
   * **Diagonal Principal ($\setminus$):** Para todas las celdas $(f, c)$ que comparten una misma diagonal principal descendente, la diferencia $f - c$ es una constante invariante:
     $$-7 \le f - c \le 7$$
     Para mapear este rango de 15 valores a índices válidos de arreglo $[0, 14]$, aplicamos un desplazamiento de $+7$:
     $$\text{clave}_{\text{prin}}(f, c) = f - c + 7$$
     Estructura: arreglo booleano `diag_prin[15]`.
   * **Diagonal Secundaria ($/$):** Para todas las celdas $(f, c)$ que comparten una misma diagonal ascendente, la suma $f + c$ es una constante invariante:
     $$0 \le f + c \le 14$$
     Directamente mapea al rango $[0, 14]$:
     $$\text{clave}_{\text{sec}}(f, c) = f + c$$
     Estructura: arreglo booleano `diag_sec[15]`.
3. **Paso 3: Poda por Factibilidad en $O(1)$:**
   Una reina puede situarse en $(fila, col)$ si y solo si:
   $$\neg \, col\_ocupada[col] \quad \land \quad \neg \, diag\_prin[fila - col + 7] \quad \land \quad \neg \, diag\_sec[fila + col]$$
   Esta consulta involucra exactamente 3 accesos indexados a memoria en tiempo $O(1)$.
4. **Paso 4: Mecanismo de Backtracking (Restauración de Estado):**
   Al probar una columna factible, se marcan en `True` las 3 estructuras booleanas y se almacena `solucion[fila] = col`. Al retornar de la llamada recursiva (si esa rama no alcanzó solución), es **estrictamente obligatorio** restablecer los booleanos a `False` y `solucion[fila] = -1` antes de probar la siguiente columna.
5. **Paso 5: Complejidad:**
   * **Tiempo:** En el peor caso teórico sin podas el espacio sería $8^8 \approx 16.7$ millones de hojas. Al colocar una reina por fila y descartar columnas usadas, el árbol se reduce a $8! = 40.320$ permutaciones. Con las podas diagonales en tiempo real, el algoritmo explora apenas unos 876 nodos para hallar la primera solución. Complejidad asintótica: $O(N!)$ en el peor caso.
   * **Espacio Auxiliar:** $O(N)$ para la pila de recursión (profundidad 8) más $8 + 15 + 15 = 38$ booleanos de control.

#### 2. Explicación Directa de por qué el Chequeo Diagonal es O(1)

* **Diagonal Principal ($\setminus$, baja de izquierda a derecha):** Cuando nos movemos un casillero abajo y uno a la derecha (`fila + 1`, `col + 1`), la resta `fila - col` no cambia. Por lo tanto, todas las casillas de una misma diagonal principal tienen el mismo resultado en `fila - col`. Le sumamos `+ 7` solo para que el índice quede entre `0` y `14` y no dé negativo.
* **Diagonal Secundaria ($/$, sube de izquierda a derecha):** Cuando nos movemos un casillero arriba y uno a la derecha (`fila - 1`, `col + 1`), lo que se compensa y se mantiene siempre igual es la suma `fila + col` (entre `0` y `14`).
* Gracias a esto, para saber si una casilla `(fila, col)` está amenazada no hace falta recorrer el tablero: alcanza con mirar 3 posiciones fijas en los arreglos booleanos (`col_ocupada[col]`, `diag_prin[fila - col + 7]` y `diag_sec[fila + col]`) en tiempo `O(1)`.

#### 3. Ejemplo Concreto y Tabla de Traza Paso a Paso (Primeras Filas)

Búsqueda de la primera solución sobre el tablero $8 \times 8$:

| Fila | Columna Probada | Clave Col ($c$) | Clave Diag Prin ($f - c + 7$) | Clave Diag Sec ($f + c$) | Estado de Booleanos | Decisión |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **0** | $0$ | $0$ | $0 - 0 + 7 = 7$ | $0 + 0 = 0$ | Libres | **Colocar Reina en $(0, 0)$**, marcar |
| **1** | $0$ | $0$ | $1 - 0 + 7 = 8$ | $1 + 0 = 1$ | `col[0]=True` | **PODA** (conflicto columna 0) |
| **1** | $1$ | $1$ | $1 - 1 + 7 = 7$ | $1 + 1 = 2$ | `diag_prin[7]=True` | **PODA** (conflicto diag prin con $(0,0)$) |
| **1** | $2$ | $2$ | $1 - 2 + 7 = 6$ | $1 + 2 = 3$ | Libres | **Colocar Reina en $(1, 2)$**, marcar |
| **2** | $0$ | $0$ | - | - | `col[0]=True` | **PODA** (conflicto columna 0) |
| **2** | $1$ | $1$ | $2 - 1 + 7 = 8$ | $2 + 1 = 3$ | `diag_sec[3]=True` | **PODA** (conflicto diag sec con $(1,2)$) |
| **2** | $2$ | $2$ | - | - | `col[2]=True` | **PODA** (conflicto columna 2) |
| **2** | $3$ | $3$ | $2 - 3 + 7 = 6$ | $2 + 3 = 5$ | `diag_prin[6]=True` | **PODA** (conflicto diag prin con $(1,2)$) |
| **2** | $4$ | $4$ | $2 - 4 + 7 = 5$ | $2 + 4 = 6$ | Libres | **Colocar Reina en $(2, 4)$**, marcar |

*Primera solución completa hallada:*
`solucion = [0, 4, 7, 5, 2, 6, 1, 3]` (columnas por fila de 0 a 7).

#### 4. Diagrama del Árbol de Decisiones de Backtracking

```mermaid
graph TD
    R["Raíz: Fila 0"] --> C0["Reina (0,0)"]:::opt
    C0 --> F1_0["(1,0): Colisión Col"]:::bad
    C0 --> F1_1["(1,1): Colisión Diag Prin"]:::bad
    C0 --> F1_2["Reina (1,2)"]:::opt
    F1_2 --> F2_0["(2,0): Colisión Col"]:::bad
    F1_2 --> F2_1["(2,1): Colisión Diag Sec"]:::bad
    F1_2 --> F2_4["Reina (2,4)"]:::opt
    F2_4 --> SOL["... Avanza hasta completar Fila 7"]:::done
    classDef opt fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#fff
    classDef bad fill:#991b1b,stroke:#7f1d1d,stroke-width:1px,color:#fff
    classDef done fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 5. Pseudocódigo del Algoritmo (Estilo Examen Presencial)

```text
Algoritmo Resolver8Reinas():
    n = 8
    solucion = arreglo de tamaño n inicializado en -1
    col_ocupada = arreglo de tamaño n en Falso
    diag_prin = arreglo de tamaño (2n - 1) en Falso  // fila - col + (n - 1)
    diag_sec = arreglo de tamaño (2n - 1) en Falso   // fila + col

    si Resolver8ReinasBT(0, solucion, col_ocupada, diag_prin, diag_sec, n):
        devolver solucion
    sino:
        devolver "Sin solución"

función Resolver8ReinasBT(fila, solucion, col_ocupada, diag_prin, diag_sec, n):
    // Caso Base: se ubicaron las 8 reinas sin conflictos
    si fila == n:
        devolver Verdadero

    para col desde 0 hasta n - 1:
        dp = fila - col + (n - 1)
        ds = fila + col

        // Poda por Factibilidad en O(1)
        si no col_ocupada[col] y no diag_prin[dp] y no diag_sec[ds]:
            // 1. Marcar decisión
            solucion[fila] = col
            col_ocupada[col] = Verdadero
            diag_prin[dp] = Verdadero
            diag_sec[ds] = Verdadero

            // 2. Recursión a fila siguiente
            si Resolver8ReinasBT(fila + 1, solucion, col_ocupada, diag_prin, diag_sec, n):
                devolver Verdadero

            // 3. Deshacer decisión (Backtrack)
            solucion[fila] = -1
            col_ocupada[col] = Falso
            diag_prin[dp] = Falso
            diag_sec[ds] = Falso

    devolver Falso
```

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

#### 1. Deducción Metodológica Formal (Los 5 Pasos)

1. **Paso 1: Eliminación de Simetrías por Orden No Creciente:**
   Toda solución permutable representa la misma descomposición. Para evitar explorar las $4! = 24$ permutaciones repetidas de una misma tupla, forzamos la restricción de monotonía:
   $$w \ge x \ge y \ge z \ge 0$$
2. **Paso 2: Determinación Analítica en $O(1)$ del Cuarto Cuadrado:**
   No es necesario iterar en el cuarto nivel. Si ya asignamos $w, x, y$, el remanente obligatorio es $R = n - (w^2 + x^2 + y^2)$. El algoritmo simplemente verifica en $O(1)$ si $R$ es un cuadrado perfecto ($z = \lfloor\sqrt{R}\rfloor$ y $z^2 = R$) y si respeta $z \le y$. Si se cumplen ambas condiciones, la solución se completa con éxito sin bifurcaciones adicionales.
3. **Paso 3: Poda por Cota Superior (Factibilidad):**
   En el paso $k$ con remanente $R$, ningún valor $v$ puede superar $\lfloor\sqrt{R}\rfloor$, ni el valor asignado en el paso anterior $v_{\text{previo}}$:
   $$v \le \min(v_{\text{previo}}, \; \lfloor\sqrt{R}\rfloor)$$
4. **Paso 4: Poda por Cota Inferior (Optimalidad/Alcance):**
   Quedan $(4 - paso)$ términos por asignar. Como los valores son no crecientes, cada uno de los términos restantes aportará a lo sumo $v^2$. Si la suma máxima potencial es estrictamente menor al remanente requerido:
   $$(4 - paso) \cdot v^2 < R$$
   entonces es **matemáticamente imposible** alcanzar $R$ utilizando valores menores o iguales a $v$. Se interrumpe el bucle de prueba (`break`) podando todo el resto del subárbol de una sola vez.
5. **Paso 5: Complejidad:**
   * **Tiempo:** Sin podas, 4 bucles hasta $\sqrt{n}$ requerirían $O((\sqrt{n})^4) = O(n^2)$. Al resolver el cuarto término analíticamente en $O(1)$, la cota máxima cae a $O((\sqrt{n})^3) = O(n^{3/2})$. Con la poda de simetría ($w \ge x \ge y \ge z$) y la cota inferior $(4-k)v^2 < R$, el número real de estados explorados es una pequeña fracción de $n^{3/2}$, resolviendo $n = 10^6$ en milisegundos.
   * **Espacio Auxiliar:** $O(1)$ de memoria adicional fija más la pila de recursión de profundidad a lo sumo 4.

#### 2. Ejemplo Concreto y Traza Paso a Paso ($n = 31$)

Sea $n = 31$. Buscamos $w \ge x \ge y \ge z$ tales que $w^2 + x^2 + y^2 + z^2 = 31$.

| Nivel / Paso | Remanente ($R$) | Límite Superior ($v \le \min$) | Valor $v$ Probado | ¿Poda $(4-k)v^2 < R$? | Acción Siguiente |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **Paso 0 ($w$)** | $31$ | $\lfloor\sqrt{31}\rfloor = 5$ | $v = 5$ | $4 \cdot 5^2 = 100 \ge 31$ (OK) | Asignar $w = 5$, nuevo $R = 31 - 25 = 6$ |
| **Paso 1 ($x$)** | $6$ | $\min(5, \lfloor\sqrt{6}\rfloor) = 2$ | $v = 2$ | $3 \cdot 2^2 = 12 \ge 6$ (OK) | Asignar $x = 2$, nuevo $R = 6 - 4 = 2$ |
| **Paso 2 ($y$)** | $2$ | $\min(2, \lfloor\sqrt{2}\rfloor) = 1$ | $v = 1$ | $2 \cdot 1^2 = 2 \ge 2$ (OK) | Asignar $y = 1$, nuevo $R = 2 - 1 = 1$ |
| **Paso 3 ($z$)** | $1$ | - | $z = \lfloor\sqrt{1}\rfloor = 1$ | $1^2 = 1 == R$ y $1 \le 1$ | **¡ÉXITO EN EL 4TO TÉRMINO!** |

*Solución obtenida:* $(w, x, y, z) = (5, 2, 1, 1)$.
*Verificación:* $5^2 + 2^2 + 1^2 + 1^2 = 25 + 4 + 1 + 1 = 31$.
*Eficiencia:* Se halló la solución en exactamente 4 evaluaciones directas sin retrocesos.

#### 3. Diagrama Visual del Árbol de Lagrange

```mermaid
graph TD
    R["n = 31 | Términos restantes: 4"] --> W5["w = 5 | R = 6"]:::opt
    W5 --> X2["x = 2 | R = 2"]:::opt
    W5 --> X1["x = 1 - cota inferior 3 menor que 6 - PODA INFERIOR"]:::bad
    X2 --> Y1["y = 1 | R = 1"]:::opt
    Y1 --> Z1["z = sqrt(1) = 1 | SOLUCIÓN: (5, 2, 1, 1)"]:::done
    classDef opt fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#fff
    classDef bad fill:#991b1b,stroke:#7f1d1d,stroke-width:1px,color:#fff
    classDef done fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 4. Pseudocódigo del Algoritmo (Estilo Examen Presencial)

```text
Algoritmo CuatroCuadradosLagrange(n):
    solucion = arreglo [0, 0, 0, 0]
    limite_inicial = entero(raiz(n))

    si CuatroCuadradosBT(0, n, limite_inicial, solucion):
        devolver solucion
    sino:
        devolver "Sin solución"

función CuatroCuadradosBT(paso, remanente, max_limite, solucion):
    // En el 4to término, se calcula directamente por raíz exacta en O(1)
    si paso == 3:
        z = entero(raiz(remanente))
        si z * z == remanente y z <= max_limite:
            solucion[3] = z
            devolver Verdadero
        devolver Falso

    limite_sup = min(max_limite, entero(raiz(remanente)))

    para v desde limite_sup bajando hasta 0:
        // Poda por cota inferior: ni usando v en todos los restantes alcanzamos remanente
        terminos_restantes = 4 - paso
        si terminos_restantes * (v * v) < remanente:
            romper bucle // Ningún valor menor podrá alcanzarlo

        solucion[paso] = v
        si CuatroCuadradosBT(paso + 1, remanente - v * v, v, solucion):
            devolver Verdadero

    devolver Falso
```

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

#### 1. Deducción Metodológica Formal (Los 5 Pasos)

1. **Paso 1: Definición de Vertex Cover:**
   Un conjunto $C \subseteq V$ es un Vertex Cover de $G = (V, E)$ si para toda arista $(u, v) \in E$, se cumple que $u \in C \lor v \in C$. Buscamos minimizar $|C|$.
2. **Paso 2: Ramificación por Arista No Cubierta (Factor de Branching 2):**
   En lugar de ramificar vértice por vértice ($2^{|V|}$ hojas), buscamos una arista arbitraria $(u, v)$ que **aún no esté cubierta** por el conjunto actual $C$:
   * **Rama 1:** Incluir el vértice $u$ en $C$ y continuar la búsqueda.
   * **Rama 2:** Incluir el vértice $v$ en $C$ y continuar la búsqueda.
   Esto garantiza que cada bifurcación cubre al menos una arista nueva y acota la profundidad del árbol al tamaño del Vertex Cover mínimo $k$.
3. **Paso 3: Poda por Cota Superior (Branch and Bound):**
   Mantenemos el tamaño de la mejor cobertura factible hallada hasta el momento: `mejor_tamano = len(mejor_solucion)` (inicializada trivialmente en $|V|$).
   Si en cualquier nodo del árbol el tamaño de la cobertura actual satisface:
   $$|C_{\text{actual}}| \ge \text{mejor tamaño}$$
   se poda inmediatamente la rama. Ninguna extensión de $C_{\text{actual}}$ puede mejorar el récord actual.
4. **Paso 4: Caso Base y Actualización del Récord:**
   Si no quedan aristas sin cubrir, el conjunto actual $C_{\text{actual}}$ es un Vertex Cover válido y su tamaño es estrictamente menor a `mejor_tamano`. Se actualiza la mejor solución con una copia profunda de $C_{\text{actual}}$.
5. **Paso 5: Complejidad:**
   * **Tiempo:** $O(2^k \cdot |E|)$ en el peor caso, donde $k$ es el tamaño del Vertex Cover óptimo. Esto es exponencialmente superior al algoritmo ingenuo $O(2^{|V|} \cdot |E|)$, especialmente cuando $k \ll |V|$.
   * **Espacio Auxiliar:** $O(|V|)$ para almacenar el conjunto actual y la pila de recursión.

#### 2. Ejemplo Concreto y Traza Paso a Paso

Sea el grafo con 4 vértices $V = \{1, 2, 3, 4\}$ y aristas $E = \{(1, 2), (2, 3), (3, 4)\}$ (camino de 4 vértices).

| Paso / Rama | Cobertura Actual ($C$) | Cota Actual ($|C|$) | Arista No Cubierta Elegida | Decisión / Poda |
| :---: | :---: | :---: | :---: | :--- |
| **Inicio** | $\emptyset$ | $0$ | $(1, 2)$ | Mejor récord inicial: $|V| = 4$ |
| **Rama 1 (incluir 1)** | $\{1\}$ | $1 < 4$ | $(2, 3)$ | Ramificar con arista $(2, 3)$ |
| **Rama 1.1 (incluir 2)** | $\{1, 2\}$ | $2 < 4$ | $(3, 4)$ | Ramificar con arista $(3, 4)$ |
| **Rama 1.1.1 (incluir 3)** | $\{1, 2, 3\}$ | $3 < 4$ | Ninguna | **Cobertura válida hallada! Récord = 3** ($\{1, 2, 3\}$) |
| **Rama 1.1.2 (incluir 4)** | $\{1, 2, 4\}$ | $3 \ge 3$ | - | **PODA BRANCH & BOUND** ($|C| \ge 3$) |
| **Rama 1.2 (incluir 3)** | $\{1, 3\}$ | $2 < 3$ | $(3, 4)$ cubierta! Aristas libres: Ninguna! | **¡Nuevo Récord Óptimo = 2!** ($\{1, 3\}$) |
| **Rama 2 (incluir 2)** | $\{2\}$ | $1 < 2$ | $(3, 4)$ | Ramificar con arista $(3, 4)$ |
| **Rama 2.1 (incluir 3)** | $\{2, 3\}$ | $2 \ge 2$ | - | **PODA BRANCH & BOUND** ($|C| \ge 2$) |
| **Rama 2.2 (incluir 4)** | $\{2, 4\}$ | $2 \ge 2$ | - | **PODA BRANCH & BOUND** ($|C| \ge 2$) |

*Resultado óptimo final:* Vertex Cover de tamaño mínimo **$k = 2$** (por ejemplo $\{1, 3\}$ o $\{2, 3\}$).

#### 3. Diagrama Visual del Árbol de Branch & Bound

```mermaid
graph TD
    R["Raíz: C = {} | Récord = 4"] --> N1["Rama u=1: C = {1}"]:::opt
    R --> N2["Rama v=2: C = {2}"]
    N1 --> N1_2["Rama u=2: C = {1, 2}"]
    N1 --> N1_3["Rama v=3: C = {1, 3} | RÉCORD = 2"]:::done
    N1_2 --> N1_2_3["C = {1, 2, 3} | Récord = 3"]
    N1_2 --> N1_2_4["C = (1, 2, 4) - PODA (tamano al menos 3)"]:::bad
    N2 --> N2_3["C = (2, 3) - PODA (tamano al menos 2)"]:::bad
    N2 --> N2_4["C = (2, 4) - PODA (tamano al menos 2)"]:::bad
    classDef opt fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#fff
    classDef bad fill:#991b1b,stroke:#7f1d1d,stroke-width:1px,color:#fff
    classDef done fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 4. Pseudocódigo del Algoritmo (Estilo Examen Presencial)

```text
Algoritmo MinimoVertexCover(V, E):
    mejor_cobertura = copiar(V)  // Cota superior inicial (todos los vértices)
    actual = conjunto_vacío()

    mejor_cobertura = MinimoVertexCoverBT(actual, mejor_cobertura, E)
    devolver mejor_cobertura

función MinimoVertexCoverBT(actual, mejor_cobertura, E):
    // Poda Branch & Bound: si el tamaño actual ya iguala o supera al mejor récord
    si tamaño(actual) >= tamaño(mejor_cobertura):
        devolver mejor_cobertura

    arista = BuscarAristaNoCubierta(E, actual)
    si arista es nulo:
        // Todas las aristas cubiertas con un tamaño estrictamente menor
        devolver copiar(actual)

    (u, v) = arista

    // Rama 1: Incluir u
    agregar u a actual
    mejor_cobertura = MinimoVertexCoverBT(actual, mejor_cobertura, E)
    quitar u de actual  // Deshacer (Backtrack)

    // Rama 2: Incluir v
    agregar v a actual
    mejor_cobertura = MinimoVertexCoverBT(actual, mejor_cobertura, E)
    quitar v de actual  // Deshacer (Backtrack)

    devolver mejor_cobertura
```

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

#### 1. Deducción Metodológica Formal (Los 5 Pasos)

1. **Paso 1: Ordenamiento Previo para Poda en Bloque:**
   Se ordena la lista $L$ de forma ascendente: $L[0] \le L[1] \le \dots \le L[n-1]$ en $O(n \log n)$.
2. **Paso 2: Árbol Binario de Decisiones:**
   En cada nivel $i$ correspondiente al elemento $L[i]$ con remanente $R$ ($R = S - \text{suma acumulada}$):
   * **Rama Inclusión:** Tomar $L[i]$, reducir el remanente a $R - L[i]$ y avanzar al nivel $i+1$.
   * **Rama Exclusión:** Omitir $L[i]$, mantener el remanente $R$ y avanzar al nivel $i+1$.
3. **Paso 3: Poda por Ordenamiento (Corte Temprano):**
   Si en el índice actual $L[i] > R$, como la lista está ordenada ascendentemente, todos los elementos posteriores $L[j] \ge L[i] > R$ para $j > i$. Por ende, **ningún elemento posterior podrá ser incluido sin exceder $S$**. Se corta la búsqueda de inmediato retornando `False`.
4. **Paso 4: Caso Base:**
   * Si $R = 0$: Se alcanzó la suma exacta $S$. Se retorna `True` inmediatamente con la solución acumulada.
   * Si $i \ge n$ o $R < 0$: Se agotaron los elementos sin llegar a la suma. Retorna `False`.
5. **Paso 5: Complejidad:**
   * **Tiempo:** $O(2^n)$ en el peor caso teórico (cuando ningún subconjunto suma $S$ y las podas no pueden actuar hasta el final). Sin embargo, con $L$ ordenado, la poda temprana $L[i] > R$ reduce el espacio a una pequeña fracción.
   * **Espacio Auxiliar:** $O(n)$ para la pila recursiva y el arreglo de la solución.

#### 2. Ejemplo Concreto y Tabla de Traza Paso a Paso

Sea $L = [2, 3, 5, 7, 10]$ y objetivo $S = 14$.

| Nivel ($i$) | Elemento ($L[i]$) | Remanente ($R$) | Condición $L[i] > R$ | Decisión | Solución Parcial |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **0** | $2$ | $14$ | $2 > 14$ (No) | **Incluir 2** $\implies R = 12$ | $\{2\}$ |
| **1** | $3$ | $12$ | $3 > 12$ (No) | **Incluir 3** $\implies R = 9$ | $\{2, 3\}$ |
| **2** | $5$ | $9$ | $5 > 9$ (No) | **Incluir 5** $\implies R = 4$ | $\{2, 3, 5\}$ |
| **3** | $7$ | $4$ | $7 > 4$ (Sí) | **PODA TEMPRANA** ($7 > 4$) | Backtrack: Quitar 5 |
| **2** | $5$ (excluir) | $9$ | - | **Excluir 5** $\implies R = 9$ | $\{2, 3\}$ |
| **3** | $7$ | $9$ | $7 > 9$ (No) | **Incluir 7** $\implies R = 2$ | $\{2, 3, 7\}$ |
| **4** | $10$ | $2$ | $10 > 2$ (Sí) | **PODA TEMPRANA** ($10 > 2$) | Backtrack: Quitar 7 |
| **3** | $7$ (excluir) | $9$ | - | **Excluir 7** $\implies R = 9$ | $\{2, 3\}$ |
| **4** | $10$ | $9$ | $10 > 9$ (Sí) | **PODA TEMPRANA** ($10 > 9$) | Backtrack: Quitar 3 |
| **1** | $3$ (excluir) | $12$ | - | **Excluir 3** $\implies R = 12$ | $\{2\}$ |
| **2** | $5$ | $12$ | $5 > 12$ (No) | **Incluir 5** $\implies R = 7$ | $\{2, 5\}$ |
| **3** | $7$ | $7$ | $7 > 7$ (No) | **Incluir 7** $\implies R = 0$ | **¡ÉXITO: $R = 0$! Solución: $\{2, 5, 7\}$** |

*Verificación:* $2 + 5 + 7 = 14 = S$.

#### 3. Diagrama Visual del Árbol de Inclusión/Exclusión

```mermaid
graph TD
    R["R = 14"] --> I2["Incluir 2: R=12"]:::opt
    I2 --> I3["Incluir 3: R=9"]
    I3 --> I5["Incluir 5: R=4"]
    I5 --> P7["Probar 7: 7 supera a 4 - PODA TEMPRANA"]:::bad
    I2 --> E3["Excluir 3: R=12"]:::opt
    E3 --> I5_2["Incluir 5: R=7"]:::opt
    I5_2 --> I7_2["Incluir 7: R=0 | SOLUCIÓN {2, 5, 7}"]:::done
    classDef opt fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#fff
    classDef bad fill:#991b1b,stroke:#7f1d1d,stroke-width:1px,color:#fff
    classDef done fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 4. Pseudocódigo del Algoritmo (Estilo Examen Presencial)

```text
Algoritmo SubsetSumBacktracking(nums, target):
    // 1. Ordenar crecientemente para habilitar podas tempranas en O(n log n)
    ordenar nums de menor a mayor
    solucion = []

    si SubsetSumBT(0, target, nums, solucion):
        devolver solucion
    sino:
        devolver nulo

función SubsetSumBT(indice, remanente, nums, solucion):
    si remanente == 0:
        devolver Verdadero
    si indice >= longitud(nums) o remanente < 0:
        devolver Falso

    // Poda temprana: al estar ordenado, ningún elemento posterior entrará
    si nums[indice] > remanente:
        devolver Falso

    // Rama 1: Incluir nums[indice]
    agregar nums[indice] a solucion
    si SubsetSumBT(indice + 1, remanente - nums[indice], nums, solucion):
        devolver Verdadero
    quitar_ultimo(solucion)  // Deshacer (Backtrack)

    // Rama 2: Excluir nums[indice]
    si SubsetSumBT(indice + 1, remanente, nums, solucion):
        devolver Verdadero

    devolver Falso
```

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

#### 1. Idea y Explicación de las Podas en Lenguaje Natural

En lugar de asignar las 8 letras a ciegas y recién verificar la cuenta al final ($10^8$ casos), aplicamos **4 podas fundamentales** que reducen la búsqueda a casi cero:

1. **Poda por Dígitos No Repetidos (Alldifferent):**
   Llevamos un arreglo booleano `digito_usado[10]`. Si un dígito ya fue asignado a una letra anterior, no se prueba en ninguna otra letra (baja de $10^8$ a $10! / 2! = 1.814.400$ estados).
2. **Poda de Ceros a la Izquierda (Restricción de Dominio Inicial):**
   Por regla matemática, ninguna palabra puede empezar con `0`. Por lo tanto, restringimos desde el inicio **`S != 0`** y **`M != 0`**.
3. **Poda Analítica del Acarreo Más Significativo (`M = 1`):**
   Como sumamos dos números de 4 cifras (`SEND + MORE`) y el resultado `MONEY` tiene **5 cifras**, la letra `M` es el acarreo de la columna de los miles. Pero la suma máxima de dos dígitos más un acarreo previo ($9 + 9 + 1 = 19$) jamás puede dar un acarreo de 2. Por lo tanto, **fijamos directamente `M = 1`** antes de empezar ( y además deducimos que `S` debe ser `8` o `9` y `O` debe ser `0` o `1`).
4. **Poda Columna por Columna (Evaluación Incremental de Derecha a Izquierda):**
   En vez de elegir las letras en cualquier orden, las asignamos **por columnas de derecha a izquierda** (unidades $\to$ decenas $\to$ centenas $\to$ miles):
   - Primero asignamos `D`, `E` e `Y` y **verificamos en el acto** si `(D + E) % 10 == Y`. Si no coincide, **podamos la rama inmediatamente** sin siquiera tocar las otras 5 letras (y además podemos calcular directamente `Y = (D + E) % 10` y el acarreo `c1 = (D + E) // 10` sin hacer un ciclo para `Y`!).
   - Luego en las decenas asignamos `N` y `R` y verificamos en el acto `(N + R + c1) % 10 == E`, y así sucesivamente en cada columna.

---

### Errores Frecuentes en Exámenes sobre Backtracking

1. **Olvidar desmarcar el estado en el retorno (Backtrack):** Dejar variables modificadas al salir de una llamada arruina la exploración de las ramas hermanas.
2. **Validar restricciones recorriendo estructuras completas:** Usar bucles en cada nodo en vez de booleanos de control $O(1)$.
3. **No justificar la complejidad en el peor caso:** Afirmar que con podas el algoritmo pasa a ser polinomial. Las podas optimizan el caso promedio, pero el peor caso sigue siendo exponencial o factorial.
4. **No podar simetrías:** Permitir explorar permutaciones del mismo conjunto en problemas de combinatoria.
"""
