"""Módulo 5: Programación Dinámica (PD)."""

def get_content():
    return r"""## 7. Tema 4: Programación Dinámica (PD)

### Conceptos Mínimos de Supervivencia

1. **Cuándo Usar Programación Dinámica:**
   * El problema exhibe **Subestructura Óptima**: la solución óptima global se compone de soluciones óptimas a sus subproblemas.
   * El problema tiene **Subproblemas Superpuestos**: los mismos subproblemas se resuelven una y otra vez (a diferencia de División y Conquista, donde los subproblemas son disjuntos).
2. **Qué Escribir en la Hoja del Parcial (Estructura Directa de 3 Bloques):**
   Para obtener el puntaje completo en un ejercicio de Programación Dinámica de TDA, tu respuesta en papel debe incluir siempre:
   1. **Idea, Estado y Ecuación de Bellman:** Explicar en palabras qué representa $OPT(\dots)$, cuáles son los casos base, qué decisiones se toman en el paso $i$ y escribir la ecuación de recurrencia.
   2. **Semi-Pseudocódigo Simplificado:** Mostrar cómo se inicializa y llena la tabla `DP` en orden *Bottom-Up* (y cómo se reconstruye la solución si el enunciado pide devolver los elementos/operaciones).
   3. **Justificación de Complejidad:** Indicar el tiempo y espacio según la cantidad de celdas de la tabla y el costo de calcular cada celda (aclarando si es *pseudo-polinomial* cuando depende de magnitudes como peso o presupuesto).

---

### Patrón de Ejercicio 4.1: DP 1D Aritmética y Transición de Estados

Problemas de cálculo de pasos mínimos o secuencias de transformación entre dos valores numéricos dados ($0 \to K$ o $N \to 1$).

---

### Ejercicio 53 — Mínima Cantidad de Operaciones para Llegar de 0 a K (+1, × 2)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Parcial 2024-2-2 (26 de noviembre de 2024), Ejercicio 2 / Guía 04 Ejercicio 11

**Enunciado**  
Dado un número natural $K$, se desea obtener la mínima cantidad de operaciones para llegar desde $0$ hasta $K$, sabiendo que las operaciones permitidas son:  
(i) Aumentar el valor del operando en 1 ($x \leftarrow x + 1$).  
(ii) Duplicar el valor del operando ($x \leftarrow 2x$).  
Implementar un algoritmo que, por programación dinámica, obtenga la menor cantidad de operaciones a realizar y detalle la secuencia exacta de dichas operaciones. Desarrollar la ecuación de recurrencia. Indicar y justificar la complejidad temporal y espacial.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Definición del Estado:** Llamamos $OPT(i)$ a la **mínima cantidad de operaciones necesarias para llegar desde $0$ hasta el número $i$**.
* **Casos Base:**
  * $OPT(0) = 0$: Ya estamos en el valor inicial $0$, por lo que necesitamos $0$ operaciones.
  * $OPT(1) = 1$: Desde $0$ la única operación que avanza es sumar $1$ ($0 + 1 = 1$), ya que duplicar el cero da $0 \times 2 = 0$.
* **Decisiones en el paso $i$ (pensando hacia atrás desde $i$):**
  Para llegar al número $i$ en el último paso, solo existen dos posibilidades:
  1. **La última operación fue sumar $1$ ($+1$):** Entonces en el paso anterior estábamos sí o sí en $i - 1$. El costo total por este camino es $OPT(i - 1) + 1$.
  2. **La última operación fue duplicar ($\times 2$):** Esto **solo es posible si $i$ es par**. En ese caso, en el paso anterior estábamos sí o sí en $i / 2$, y el costo total por este camino es $OPT(i / 2) + 1$.
* **Ecuación de Bellman (Recurrencia):**
  Para todo $i \ge 1$:
  $$OPT(i) = \begin{cases} OPT(i - 1) + 1 & \text{si } i \text{ es impar} \\ \min\Big(OPT(i - 1) + 1, \; OPT(i / 2) + 1\Big) & \text{si } i \text{ es par} \end{cases}$$
* **Orden de llenado:** Llenamos el arreglo `DP` desde $i = 1$ hasta $K$. Como $i - 1$ e $i / 2$ son siempre estrictamente menores que $i$, al avanzar de menor a mayor nos aseguramos de que ambos valores ya están calculados cuando los necesitamos (no hay ciclos).

```mermaid
graph LR
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    classDef normal fill:#475569,stroke:#334155,stroke-width:1px,color:#fff

    N0["0"]:::opt -->|+1| N1["1"]:::opt
    N1 -->|x2| N2["2"]:::opt
    N2 -->|+1| N3["3"]:::normal
    N2 -->|x2| N4["4"]:::opt
    N3 -->|+1| N4
    N3 -->|x2| N6["6"]:::normal
    N4 -->|+1| N5["5"]:::opt
    N4 -->|x2| N8["8"]:::normal
    N5 -->|+1| N6
    N5 -->|x2| N10["10"]:::opt
```

#### 2. Semi-Pseudocódigo Simplificado

```text
FUNCION MinimasOperaciones(K):
    DP <- arreglo de tamaño (K + 1) inicializado en 0
    DP[0] <- 0

    // 1. Llenado de la tabla Bottom-Up
    PARA i <- 1 HASTA K:
        SI i es impar:
            DP[i] <- DP[i - 1] + 1
        SINO:
            DP[i] <- min(DP[i - 1] + 1, DP[i / 2] + 1)

    // 2. Reconstrucción de las operaciones ( de K hacia 0 )
    operaciones <- lista vacía
    actual <- K
    MIENTRAS actual > 0:
        SI (actual es par) Y (DP[actual] == DP[actual / 2] + 1):
            AGREGAR "x2" AL INICIO DE operaciones
            actual <- actual / 2
        SINO:
            AGREGAR "+1" AL INICIO DE operaciones
            actual <- actual - 1

    RETORNAR (DP[K], operaciones)
```

#### 3. Justificación de Complejidad

* **Complejidad Temporal:** $\mathcal{O}(K)$. La tabla `DP` tiene $K + 1$ posiciones y cada celda se calcula en tiempo constante $\mathcal{O}(1)$ comparando a lo sumo $2$ valores previos. La reconstrucción retrocede desde $K$ hasta $0$ dando a lo sumo $K$ pasos. *(Nota: respecto al tamaño en bits de la entrada $b = \log_2 K$, esta complejidad es **pseudo-polinomial**).*
* **Complejidad Espacial:** $\mathcal{O}(K)$ para almacenar el arreglo `DP[0..K]` y la lista de operaciones reconstruida.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Intentar duplicar desde 0:</strong> $0 \times 2 = 0$ no avanza. El primer paso desde $0$ hacia $1$ es siempre $+1$.</li>
    <li><strong>Olvidar reconstruir la secuencia:</strong> El enunciado pide la menor cantidad de operaciones <em>y detallar cuáles son</em>. No incluir el bucle de reconstrucción descuenta hasta la mitad del puntaje.</li>
    <li><strong>Usar Greedy cuando piden Programación Dinámica:</strong> Aunque dividir por $2$ cuando es par funciona en $\mathcal{O}(\log K)$ para $\{+1, \times 2\}$, si el examen pide explícitamente PD (o agrega operaciones como $+3$ donde Greedy falla), responder con Greedy anula el punto.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 4.2: Mochila 2D con Restricciones Lógicas

Aparece cuando la mochila tiene múltiples recursos acoplados (peso y volumen) y condiciones lógicas adicionales sobre subconjuntos específicos de elementos (exclusión mutua y obligatoriedad).

---

### Ejercicio 54 — Mochila 2D con Selección Obligatoria y Excluyente de Guías de Aves

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Parcial 2024-2-1 (5 de noviembre de 2024), Ejercicio 3

**Enunciado**  
Paolo Casanova llevará una mochila para el fin de semana con capacidad de peso $C$ kilos y volumen $L$ litros. Tiene una lista de $n$ elementos posibles, donde cada elemento $i$ tiene un peso $w_i$, un volumen $v_i$ y un beneficio $b_i$. Los ítems $1$ y $2$ son dos guías de observación de aves distintas. Por utilidad, **no tiene sentido llevar ambas guías, pero Paolo debe llevar obligatoriamente una de las dos** (es decir, debe elegir exactamente la guía $1$ o la guía $2$, nunca ninguna ni las dos). Desarrollar un algoritmo de Programación Dinámica que encuentre la combinación óptima de elementos que maximice el beneficio total respetando las capacidades.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Cómo manejar la restricción obligatoria y excluyente (XOR) de las guías:**
  Separamos los ítems $1$ y $2$ (las dos guías de aves) del resto de los elementos libres $R = \{3, 4, \dots, n\}$ (que son $m = n - 2$ elementos). Como Paolo está obligado a llevar **exactamente una** de las dos guías, resolvemos una única tabla de **Mochila 2D** (con peso y volumen) sobre los $m$ elementos libres, y al final comparamos los dos casos posibles:
  * **Caso A (Elegir la Guía 1):** Si entra en la mochila ($w_1 \le C$ y $v_1 \le L$), nos aporta $b_1$ y nos deja capacidad restante $(C - w_1, \; L - v_1)$ para llenar con los elementos libres: beneficio total $b_1 + OPT(m, C - w_1, L - v_1)$.
  * **Caso B (Elegir la Guía 2):** Si entra en la mochila ($w_2 \le C$ y $v_2 \le L$), nos aporta $b_2$ y nos deja capacidad restante $(C - w_2, \; L - v_2)$: beneficio total $b_2 + OPT(m, C - w_2, L - v_2)$.
* **Definición del Estado:** Llamamos $OPT(i, p, v)$ al **máximo beneficio obtenible considerando los primeros $i$ elementos libres (del conjunto $R = \{3 \dots n\}$) con un límite de peso $p$ y un límite de volumen $v$**.
* **Casos Base:** $OPT(0, p, v) = 0$ para todo $p, v$ (con $0$ elementos libres el beneficio es $0$), y $OPT(i, 0, v) = OPT(i, p, 0) = 0$.
* **Decisiones en el paso $i$ y Ecuación de Bellman (Recurrencia):**
  Para el $i$-ésimo elemento libre (con peso $w_i$, volumen $v_i$ y beneficio $b_i$):
  1. Si supera el peso $p$ o el volumen $v$ disponible ($w_i > p \lor v_i > v$), **no podemos llevarlo** y mantenemos $OPT(i - 1, p, v)$.
  2. Si entra en ambos recursos ($w_i \le p \land v_i \le v$), elegimos el máximo entre **no llevarlo** o **llevarlo** (sumando $b_i$ y restando su peso y volumen):
  $$OPT(i, p, v) = \begin{cases} OPT(i - 1, p, v) & \text{si } w_i > p \lor v_i > v \\ \max\Big(OPT(i - 1, p, v), \; OPT(i - 1, p - w_i, v - v_i) + b_i\Big) & \text{si } w_i \le p \land v_i \le v \end{cases}$$
* **Óptimo Global del Problema:**
  $$OPT_{\text{total}} = \max\Big( b_1 + OPT(m, C - w_1, L - v_1), \;\; b_2 + OPT(m, C - w_2, L - v_2) \Big)$$

```mermaid
flowchart TD
    P(["Instancia Original: Capacidades (C, L) e Ítems {1..n}"]) --> DP["Llenar Tabla DP 3D sobre Ítems Libres {3..n}<br/>OPT(i, p, v) para p ∈ [0..C], v ∈ [0..L]"]:::dp
    DP --> CA["Caso A: Incluir Guía 1 (si w₁ ≤ C y v₁ ≤ L)<br/>Total A = b₁ + DP[n-2][C - w₁][L - v₁]"]:::branch
    DP --> CB["Caso B: Incluir Guía 2 (si w₂ ≤ C y v₂ ≤ L)<br/>Total B = b₂ + DP[n-2][C - w₂][L - v₂]"]:::branch
    CA --> MAX{"Elegir max(Total A, Total B)"}
    CB --> MAX
    MAX --> SOL(["Reconstruir desde la capacidad remanente de la Guía ganadora"]):::done
    classDef branch fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#fff
    classDef dp fill:#0284c7,stroke:#0369a1,stroke-width:2px,color:#fff
    classDef done fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 2. Semi-Pseudocódigo Simplificado

```text
FUNCION MochilaPaolo(guia1, guia2, libres, C, L):
    m <- longitud(libres)   // libres contiene los ítems 3..n (m = n - 2)
    DP <- matriz 3D de (m + 1) x (C + 1) x (L + 1) inicializada en 0

    // 1. Llenar la tabla DP una sola vez con los m elementos libres
    PARA i <- 1 HASTA m:
        item <- libres[i]
        PARA p <- 0 HASTA C:
            PARA v <- 0 HASTA L:
                SI item.w > p O item.v > v:
                    DP[i][p][v] <- DP[i - 1][p][v]
                SINO:
                    DP[i][p][v] <- max(DP[i - 1][p][v], DP[i - 1][p - item.w][v - item.v] + item.b)

    // 2. Comparar Caso A (Guía 1) vs Caso B (Guía 2)
    total_A <- (guia1.b + DP[m][C - guia1.w][L - guia1.v]) SI (guia1.w <= C Y guia1.v <= L) SINO -INFINITO
    total_B <- (guia2.b + DP[m][C - guia2.w][L - guia2.v]) SI (guia2.w <= C Y guia2.v <= L) SINO -INFINITO

    SI total_A >= total_B:
        elegidos <- [guia1];  p_rem <- C - guia1.w;  v_rem <- L - guia1.v
    SINO:
        elegidos <- [guia2];  p_rem <- C - guia2.w;  v_rem <- L - guia2.v

    // 3. Reconstruir qué ítems libres se llevaron
    PARA i <- m BAJANDO HASTA 1:
        SI DP[i][p_rem][v_rem] != DP[i - 1][p_rem][v_rem]:
            AGREGAR libres[i] A elegidos
            p_rem <- p_rem - libres[i].w
            v_rem <- v_rem - libres[i].v

    RETORNAR (max(total_A, total_B), elegidos)
```

#### 3. Justificación de Complejidad

* **Complejidad Temporal:** $\mathcal{O}(n \cdot C \cdot L)$. La matriz tridimensional `DP` tiene dimensiones $(n - 1) \times (C + 1) \times (L + 1)$ y cada celda se calcula en $\mathcal{O}(1)$ comparando dos opciones. Evaluar ambas guías toma $\mathcal{O}(1)$ y reconstruir la solución toma $\mathcal{O}(n)$ pasos. Es una complejidad **pseudo-polinomial** porque depende de las magnitudes numéricas $C$ y $L$.
* **Complejidad Espacial:** $\mathcal{O}(n \cdot C \cdot L)$ para almacenar la tabla 3D necesaria para reconstruir los elementos elegidos.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Meter las guías 1 y 2 dentro de la bolsa general de la mochila:</strong> Si no se separan las dos guías en los Casos A y B, el algoritmo podría elegir ambas guías o ninguna de las dos, incumpliendo el enunciado.</li>
    <li><strong>No verificar que la guía quepa por sí sola:</strong> Antes de consultar <code>DP[m][C - w_1][L - v_1]</code> hay que chequear que $w_1 \le C$ y $v_1 \le L$ para no acceder a índices negativos.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 4.3: Partición de Secuencias y Formateo (Word Wrap)

Minimizar una penalidad cuadrática o no lineal sobre la partición de un arreglo de palabras en líneas de longitud fija.

---

### Ejercicio 55 — Justificación de Texto (Word Wrap / Knuth-Plass)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Parcial 2024-2-3 (10 de diciembre de 2024), Ejercicio 2

**Enunciado**  
Se tiene un texto formado por una sucesión de $n$ palabras $W_1, W_2, \dots, W_n$. Cada palabra $W_i$ tiene una longitud de $C_i$ caracteres ($C_i \le L$). Se quiere dividir el texto en líneas de ancho máximo $L$. Si se asignan las palabras contiguas $W_j, \dots, W_i$ a una misma línea, la longitud total ocupada es:
$$\text{Longitud}(j, i) = \sum_{k=j}^i C_k + (i - j)$$
donde $(i - j)$ representa el espacio en blanco simple obligatorio entre palabras contiguas. Una línea es válida si $\text{Longitud}(j, i) \le L$. Al valor sobrante de la línea se lo define como:
$$\text{Sobrante}(j, i) = L - \text{Longitud}(j, i)$$
Diseñar un algoritmo por Programación Dinámica que realice una partición del texto en líneas minimizando la suma de los cuadrados de los sobrantes de todas las líneas. Desarrollar la recurrencia, complejidad y reconstrucción.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Definición del Estado:** Llamamos $OPT(i)$ al **mínimo costo total (suma de los cuadrados de los espacios sobrantes) para formatear en líneas las primeras $i$ palabras ($W_1, \dots, W_i$)**.
* **Caso Base:** $OPT(0) = 0$ (si hay $0$ palabras para acomodar, el costo es $0$).
* **Decisiones en el paso $i$:**
  Para acomodar el prefijo de palabras $W_1 \dots W_i$, nos preguntamos: **¿en qué palabra $j$ ($1 \le j \le i$) empieza la última línea?**
  * Si decidimos que la última línea contenga las palabras desde $W_j$ hasta $W_i$ (lo cual solo es válido si $\text{Longitud}(j, i) \le L$), esa línea tendrá un costo de $\text{Sobrante}(j, i)^2 = (L - \text{Longitud}(j, i))^2$.
  * Las palabras anteriores ($W_1 \dots W_{j-1}$) deben haberse acomodado de la mejor forma posible, lo cual cuesta $OPT(j - 1)$.
  * Probamos todos los inicios $j$ posibles que no superen el ancho $L$ y nos quedamos con el que dé el mínimo costo total.
* **Ecuación de Bellman (Recurrencia):**
  Para todo $i \in \{1, \dots, n\}$:
  $$OPT(i) = \min_{\substack{1 \le j \le i \\ \text{Longitud}(j, i) \le L}} \Big\{ OPT(j - 1) + \big(L - \text{Longitud}(j, i)\big)^2 \Big\}$$

```mermaid
flowchart LR
    P0["OPT(0) = 0"] --> Pj["OPT(j - 1)<br/>Palabras 1..j-1 óptimas"]:::prev
    Pj -->|"+ (L - Longitud(j, i))²<br/>Última línea con palabras j..i"| Pi["OPT(i)<br/>Mínimo probando todo j válido"]:::curr
    classDef prev fill:#0284c7,stroke:#0369a1,stroke-width:2px,color:#fff
    classDef curr fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 2. Semi-Pseudocódigo Simplificado

```text
FUNCION WordWrap(C, n, L):
    DP <- arreglo de tamaño (n + 1) inicializado en +INFINITO
    inicio_linea <- arreglo de tamaño (n + 1) inicializado en 0
    DP[0] <- 0

    // 1. Llenado Bottom-Up para cada prefijo de i palabras
    PARA i <- 1 HASTA n:
        largo_actual <- 0
        // Probamos que la última línea empiece en j (yendo hacia atrás desde i hasta 1)
        PARA j <- i BAJANDO HASTA 1:
            SI j == i:
                largo_actual <- C[i]
            SINO:
                largo_actual <- largo_actual + 1 + C[j]   // +1 por el espacio entre palabras

            SI largo_actual > L:
                ROMPER   // Ya no entran más palabras en esta línea

            costo <- DP[j - 1] + (L - largo_actual)^2
            SI costo < DP[i]:
                DP[i] <- costo
                inicio_linea[i] <- j

    // 2. Reconstrucción de las líneas (de atrás hacia adelante)
    lineas <- lista vacía
    actual <- n
    MIENTRAS actual > 0:
        j <- inicio_linea[actual]
        AGREGAR rango (j .. actual) AL INICIO DE lineas
        actual <- j - 1

    RETORNAR (DP[n], lineas)
```

#### 3. Justificación de Complejidad

* **Complejidad Temporal:** $\mathcal{O}(n^2)$ (o más ajustadamente $\mathcal{O}(n \cdot L)$). La tabla `DP` tiene $n + 1$ celdas. Para calcular cada celda $i$, el bucle interno retrocede con el índice $j$ a lo sumo $i$ posiciones (y a lo sumo $L$ pasos antes de que `largo_actual` supere $L$), haciendo cuentas en $\mathcal{O}(1)$ en cada paso gracias a que acumulamos `largo_actual`.
* **Complejidad Espacial:** $\mathcal{O}(n)$ para guardar los arreglos `DP[0..n]` e `inicio_linea[1..n]`.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Olvidar el espacio en blanco entre palabras:</strong> Entre $W_j$ y $W_i$ hay $(i - j)$ espacios. Al agregar una palabra más a la línea siempre hay que sumar <code>1 + C[j]</code>.</li>
    <li><strong>No cortar cuando $\text{Longitud}(j, i) > L$:</strong> Como el sobrante se eleva al cuadrado, si no cortás el bucle cuando la línea se pasa de $L$, un sobrante negativo como $(-3)^2 = 9$ daría positivo y el algoritmo armaría líneas ilegales.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 4.4: Mochila 3D Multidimensional con Restricciones Presupuestarias

Aparece cuando el problema presenta 3 dimensiones de recursos simultáneas (peso, volumen, costo monetario o seguro) y exige definir un estado 4D.

---

### Ejercicio 56 — Problema del Delivery: Mochila 3D con Límite de Seguro Financiero

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Parcial 2025-1-1 (27 de mayo de 2025), Ejercicio 4

**Enunciado**  
Se tiene el problema del delivery. Para cada paquete $i$ de una lista de $n$ paquetes se conoce su peso $W_i$, su volumen $V_i$, su costo de seguro $C_i$ y su beneficio comercial $B_i$. El repartidor dispone de un vehículo con capacidad máxima de peso $C$ kilos y volumen máximo de $T$ litros. Además, por una cláusula estricta del seguro de transporte, la suma total de los costos de los productos transportados no puede superar los $M$ pesos. Desarrollar un algoritmo de Programación Dinámica que resuelva el problema maximizando el beneficio.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Definición del Estado:** Es una Mochila 0-1 con **tres capacidades simultáneas** (peso, volumen y monto de seguro). Definimos $OPT(i, w, v, m)$ como el **máximo beneficio comercial obtenible considerando un subconjunto de los primeros $i$ paquetes disponiendo de un peso máximo $w$, un volumen máximo $v$ y un monto de seguro máximo $m$**.
* **Casos Base:** $OPT(0, w, v, m) = 0$ para todo $w \in [0, C]$, $v \in [0, T]$ y $m \in [0, M]$ (sin paquetes para elegir, la ganancia es $0$).
* **Decisiones en el paso $i$:**
  Al evaluar el paquete $i$ (con peso $W_i$, volumen $V_i$, seguro $C_i$ y beneficio $B_i$):
  1. Si supera cualquiera de las tres capacidades disponibles ($W_i > w \lor V_i > v \lor C_i > m$), **no entra** en el vehículo y nos quedamos con $OPT(i - 1, w, v, m)$.
  2. Si entra en los tres recursos a la vez ($W_i \le w \land V_i \le v \land C_i \le m$), elegimos el máximo entre **no llevarlo** o **llevarlo** (sumando $B_i$ y descontando $W_i$, $V_i$ y $C_i$):
* **Ecuación de Bellman (Recurrencia):**
  $$OPT(i, w, v, m) = \begin{cases} OPT(i - 1, w, v, m) & \text{si } W_i > w \lor V_i > v \lor C_i > m \\ \max\Big(OPT(i - 1, w, v, m), \; OPT(i - 1, w - W_i, v - V_i, m - C_i) + B_i\Big) & \text{si } W_i \le w \land V_i \le v \land C_i \le m \end{cases}$$

```mermaid
flowchart TD
    S["Estado Actual: OPT(i, w, v, m)"] --> COND{"¿Cabe en los 3 recursos?<br/>W_i ≤ w ∧ V_i ≤ v ∧ C_i ≤ m"}
    COND -- No --> EXCL["No llevar paquete i:<br/>OPT(i-1, w, v, m)"]:::no
    COND -- Sí --> MAX["max(<br/>  No llevar: OPT(i-1, w, v, m),<br/>  Llevar: OPT(i-1, w-W_i, v-V_i, m-C_i) + B_i<br/>)"]:::yes
    classDef no fill:#991b1b,stroke:#7f1d1d,stroke-width:1.5px,color:#fff
    classDef yes fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 2. Semi-Pseudocódigo Simplificado

```text
FUNCION DeliveryMochila3D(paquetes, n, C, T, M):
    DP <- matriz 4D de (n + 1) x (C + 1) x (T + 1) x (M + 1) inicializada en 0

    // 1. Llenado Bottom-Up de los 4 índices
    PARA i <- 1 HASTA n:
        p <- paquetes[i]
        PARA w <- 0 HASTA C:
            PARA v <- 0 HASTA T:
                PARA m <- 0 HASTA M:
                    SI p.W > w O p.V > v O p.C > m:
                        DP[i][w][v][m] <- DP[i - 1][w][v][m]
                    SINO:
                        DP[i][w][v][m] <- max(DP[i - 1][w][v][m],
                                              DP[i - 1][w - p.W][v - p.V][m - p.C] + p.B)

    // 2. Reconstrucción de los paquetes seleccionados
    elegidos <- lista vacía
    w <- C;  v <- T;  m <- M
    PARA i <- n BAJANDO HASTA 1:
        SI DP[i][w][v][m] != DP[i - 1][w][v][m]:
            AGREGAR paquetes[i] A elegidos
            w <- w - paquetes[i].W
            v <- v - paquetes[i].V
            m <- m - paquetes[i].C

    RETORNAR (DP[n][C][T][M], elegidos)
```

#### 3. Justificación de Complejidad

* **Complejidad Temporal:** $\mathcal{O}(n \cdot C \cdot T \cdot M)$. Tenemos una tabla 4D con $(n + 1)(C + 1)(T + 1)(M + 1)$ celdas, y cada celda se resuelve en tiempo constante $\mathcal{O}(1)$ comparando dos opciones. La reconstrucción recorre $n$ pasos en $\mathcal{O}(n)$. Es una complejidad **pseudo-polinomial** porque depende de las magnitudes numéricas de las capacidades $C, T, M$.
* **Complejidad Espacial:** $\mathcal{O}(n \cdot C \cdot T \cdot M)$ para almacenar la tabla 4D.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Olvidar una dimensión en el estado:</strong> Tratar el seguro $M$ por fuera de la tabla o usar solo peso y volumen no garantiza optimalidad; cada restricción acumulativa exige su propio eje en la tabla `DP`.</li>
    <li><strong>No aclarar que es pseudo-polinomial:</strong> En todo problema de tipo Mochila siempre hay que mencionar que la complejidad es pseudo-polinomial respecto al tamaño de los números $C, T, M$.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 4.5: Exclusión Adyacente (House Robber / Juan el Vago)

Decisión sobre elementos consecutivos donde elegir un elemento prohíbe elegir a su vecino inmediato.

---

### Ejercicio 57 — Juan el Vago (Exclusión de Días Consecutivos)

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía de Ejercicios 04, Ejercicio 4 / Práctica

**Enunciado**  
Juan dispone de ofertas de trabajo para los próximos $n$ días. Cada día $i$ le ofrece una ganancia $G[i] > 0$. Sin embargo, Juan es vago y no está dispuesto a trabajar dos días seguidos. Diseñar un algoritmo por Programación Dinámica que determine la ganancia máxima que Juan puede obtener y qué días debe trabajar.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Definición del Estado:** Llamamos $OPT(i)$ a la **ganancia máxima que Juan puede obtener considerando los primeros $i$ días ($1 \le i \le n$) sin trabajar dos días consecutivos**.
* **Casos Base:**
  * $OPT(0) = 0$: Si hay $0$ días disponibles, la ganancia es $0$.
  * $OPT(1) = G[1]$: Si solo hay $1$ día disponible, como $G[1] > 0$, siempre le conviene trabajarlo.
* **Decisiones en el paso $i$:**
  Para el día $i$ ($i \ge 2$), Juan tiene solo dos opciones excluyentes:
  1. **Descansar el día $i$:** No suma ganancia hoy y conserva la mejor ganancia obtenida hasta el día anterior: $OPT(i - 1)$.
  2. **Trabajar el día $i$:** Cobra $G[i]$, pero por la restricción de no trabajar dos días seguidos **está obligado a haber descansado el día $i - 1$**, por lo que le suma la mejor ganancia acumulada hasta el día $i - 2$: $OPT(i - 2) + G[i]$.
* **Ecuación de Bellman (Recurrencia):**
  Para todo $i \ge 2$:
  $$OPT(i) = \max\Big(OPT(i - 1), \;\; OPT(i - 2) + G[i]\Big)$$

```mermaid
flowchart LR
    D2["OPT(i - 2)"] -->|"+ G[i] (Trabaja día i y descansa i-1)"| Di["OPT(i) = max(...)"]:::opt
    D1["OPT(i - 1)"] -->|"+ 0 (Descansa día i)"| Di
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 2. Semi-Pseudocódigo Simplificado

```text
FUNCION JuanElVago(G, n):
    DP <- arreglo de tamaño (n + 1) inicializado en 0
    DP[0] <- 0
    DP[1] <- G[1]

    // 1. Llenado Bottom-Up de la tabla
    PARA i <- 2 HASTA n:
        DP[i] <- max(DP[i - 1], DP[i - 2] + G[i])

    // 2. Reconstrucción de qué días trabajó
    dias_trabajados <- lista vacía
    i <- n
    MIENTRAS i >= 1:
        SI i == 1 O DP[i] == DP[i - 2] + G[i]:
            AGREGAR i AL INICIO DE dias_trabajados
            i <- i - 2   // Como trabajó el día i, salteamos el día i - 1
        SINO:
            i <- i - 1   // Descansó el día i, pasamos a revisar i - 1

    RETORNAR (DP[n], dias_trabajados)
```

#### 3. Justificación de Complejidad

* **Complejidad Temporal:** $\mathcal{O}(n)$. El arreglo `DP` tiene $n + 1$ posiciones y cada celda se calcula en $\mathcal{O}(1)$ haciendo una única comparación entre dos sumas. La reconstrucción recorre el arreglo hacia atrás en a lo sumo $n$ pasos ($\mathcal{O}(n)$).
* **Complejidad Espacial:** $\mathcal{O}(n)$ para almacenar el arreglo `DP[0..n]` y la lista de días trabajados.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>En la reconstrucción, restar 1 en vez de 2 cuando trabaja:</strong> Si se detecta que Juan trabajó el día $i$ (porque <code>DP[i] == DP[i-2] + G[i]</code>), el índice debe saltar a <code>i - 2</code>. Si pasás a <code>i - 1</code> podrías elegir dos días consecutivos.</li>
    <li><strong>Suponer que conviene elegir solo días pares o solo días impares:</strong> En casos como $G = [100, 1, 1, 100]$, el óptimo elige el día 1 y el día 4 ($200$), combinando un impar y un par.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 4.6: Interval Scheduling Ponderado (DP con Búsqueda Binaria)

Selección de intervalos con pesos o beneficios arbitrarios donde Greedy falla y se requiere DP con búsqueda logarítmica del predecesor compatible.

---

### Ejercicio 58 — Interval Scheduling Ponderado (DP + Búsqueda Binaria)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía de Ejercicios 04, Ejercicio 2 / Práctica

**Enunciado**  
Se tiene un conjunto de $n$ intervalos $[s_i, f_i]$, cada uno con un beneficio o peso $v_i > 0$. No se pueden seleccionar intervalos que se solapen. Diseñar un algoritmo que maximice la suma de los beneficios de los intervalos elegidos en tiempo $O(n \log n)$.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Ordenamiento Previo y Predecesor Compatible $p(i)$:**
  Primero ordenamos los $n$ intervalos por **tiempo de finalización creciente** ($f_1 \le f_2 \le \dots \le f_n$) en $\mathcal{O}(n \log n)$.
  Para cada intervalo $i$, definimos $p(i)$ como el **mayor índice $j < i$ que no se solapa con $i$** (es decir, el último intervalo que termina antes o justo cuando empieza $i$: $f_j \le s_i$; si no hay ninguno, $p(i) = 0$). Como los intervalos están ordenados por fin, hallamos $p(i)$ mediante **Búsqueda Binaria** en $\mathcal{O}(\log n)$.
* **Definición del Estado:** Llamamos $OPT(i)$ al **máximo beneficio obtenible seleccionando intervalos compatibles dentro del prefijo $\{1, \dots, i\}$**.
* **Caso Base:** $OPT(0) = 0$ (con $0$ intervalos el beneficio es $0$).
* **Decisiones en el paso $i$:**
  Para el intervalo $i$, tenemos dos opciones:
  1. **No elegir el intervalo $i$:** Nos quedamos con el mejor beneficio de los primeros $i - 1$ intervalos, que es $OPT(i - 1)$.
  2. **Elegir el intervalo $i$:** Ganamos $v_i$ y, para no solaparnos, debemos combinarlo con la mejor solución de los intervalos que terminan a más tardar en $s_i$, que es exactamente $OPT(p(i))$.
* **Ecuación de Bellman (Recurrencia):**
  Para todo $i \in \{1, \dots, n\}$:
  $$OPT(i) = \max\Big(OPT(i - 1), \;\; OPT(p(i)) + v_i\Big)$$

```mermaid
flowchart LR
    P_i["OPT(p(i))<br/>Último j con f_j ≤ s_i (Búsqueda Binaria)"] -->|"+ v_i (Incluir intervalo i)"| OPT_i["OPT(i) = max(...)"]:::opt
    Prev["OPT(i - 1)<br/>Prefijo anterior"] -->|"+ 0 (Excluir intervalo i)"| OPT_i
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 2. Semi-Pseudocódigo Simplificado

```text
FUNCION IntervalSchedulingPonderado(intervalos, n):
    ORDENAR intervalos[1..n] POR tiempo de fin f_i ASCENDENTE

    // 1. Precalcular p[i] con Búsqueda Binaria sobre los tiempos de fin
    p <- arreglo de tamaño (n + 1) en 0
    PARA i <- 1 HASTA n:
        p[i] <- BusquedaBinariaUltimoFinMenorIgual(intervalos[1 .. i-1], intervalos[i].s)

    // 2. Llenado Bottom-Up de la tabla DP
    DP <- arreglo de tamaño (n + 1) en 0
    DP[0] <- 0
    PARA i <- 1 HASTA n:
        DP[i] <- max(DP[i - 1], DP[p[i]] + intervalos[i].v)

    // 3. Reconstrucción de los intervalos elegidos
    elegidos <- lista vacía
    i <- n
    MIENTRAS i > 0:
        SI DP[p[i]] + intervalos[i].v >= DP[i - 1]:
            AGREGAR intervalos[i] A elegidos
            i <- p[i]    // Saltamos al último compatible
        SINO:
            i <- i - 1   // No se usó el intervalo i

    RETORNAR (DP[n], elegidos)
```

#### 3. Justificación de Complejidad

* **Complejidad Temporal:** $\mathcal{O}(n \log n)$.
  1. Ordenar los $n$ intervalos por tiempo de fin cuesta $\mathcal{O}(n \log n)$.
  2. Calcular $p(i)$ para los $n$ intervalos mediante búsqueda binaria cuesta $n \times \mathcal{O}(\log n) = \mathcal{O}(n \log n)$.
  3. Llenar la tabla `DP` de tamaño $n + 1$ cuesta $\mathcal{O}(1)$ por celda, sumando $\mathcal{O}(n)$, y la reconstrucción toma a lo sumo $n$ pasos ($\mathcal{O}(n)$).
  En total: $\mathcal{O}(n \log n) + \mathcal{O}(n \log n) + \mathcal{O}(n) = \mathcal{O}(n \log n)$.
* **Complejidad Espacial:** $\mathcal{O}(n)$ para almacenar los arreglos `DP[0..n]` y `p[1..n]`.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Buscar $p(i)$ recorriendo linealmente hacia atrás:</strong> Hacer un bucle desde $i-1$ hasta $1$ lleva el algoritmo a $\mathcal{O}(n^2)$, desaprobando la cota pedida de $\mathcal{O}(n \log n)$. Es obligatorio mencionar la <strong>Búsqueda Binaria</strong>.</li>
    <li><strong>Ordenar por tiempo de inicio $s_i$ en vez de fin $f_i$:</strong> Si ordenás por inicio, los intervalos compatibles con $i$ no forman un prefijo contiguo $1 \dots p(i)$ y la recurrencia falla.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 4.7: Saltos Acotados en Ruta con Costos por Parada

Problemas de recorrido unidireccional de $0$ a $N+1$ donde en cada paso se permite avanzar $1, 2, \dots, k$ posiciones pagando la tarifa del nodo donde se aterriza.

---

### Ejercicio 59 — Ruta de Transporte con Estaciones y Salto de Hasta 2 Paradas

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2026-2-1 (Enunciados), Ejercicio 3

**Enunciado**  
Un transporte debe recorrer una ruta hasta su objetivo final. Para hacerlo tiene $N$ estaciones intermedias donde puede detenerse a descansar y cargar combustible. Cada estación le cobrará una tarifa fija $T[i]$ por detenerse, conocida y posiblemente diferente para cada estación. Desde cada estación puede ir a la siguiente, o saltear una o dos estaciones para evitar pagar la tarifa correspondiente. Por su autonomía, no se pueden saltear más de dos estaciones consecutivas. Diseñar un algoritmo de PD que permita hallar el viaje con menor costo de paradas. Indicar la complejidad de dicho algoritmo.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Definición del Estado:** Representamos el punto de partida (origen) como la posición $0$, las $N$ estaciones intermedias como $1, 2, \dots, N$ con tarifas $T[1 \dots N]$, y el destino final como la posición $N + 1$ con tarifa $T[N + 1] = 0$.
  Llamamos $OPT(i)$ al **mínimo costo acumulado de paradas para llegar desde el origen $0$ hasta la posición $i$ (deteniéndose en $i$)**.
* **Casos Base:**
  * $OPT(0) = 0$: Estamos en el origen sin costo.
  * $OPT(1) = T[1]$: Solo se puede llegar desde el origen $0$.
  * $OPT(2) = T[2] + \min(OPT(1), \; OPT(0)) = T[2]$ (salteando la estación $1$ directo desde $0$).
* **Decisiones en el paso $i$ (pensando hacia atrás desde $i$):**
  Para llegar a la posición $i$, como por autonomía **no podemos saltear más de 2 estaciones seguidas**, la última parada inmediata anterior a $i$ tuvo que ser obligatoriamente una de estas tres opciones:
  1. La estación $i - 1$ (avanzó directo sin saltear ninguna),
  2. La estación $i - 2$ (salteó $1$ estación: la $i - 1$), o
  3. La estación $i - 3$ (salteó $2$ estaciones seguidas: la $i - 2$ y la $i - 1$).
  Elegimos el mínimo entre esos tres predecesores y le sumamos la tarifa $T[i]$ de la posición actual.
* **Ecuación de Bellman (Recurrencia):**
  Para todo $i \in \{3, \dots, N + 1\}$ (con $T[N + 1] = 0$):
  $$OPT(i) = T[i] + \min\Big(OPT(i - 1), \; OPT(i - 2), \; OPT(i - 3)\Big)$$

```mermaid
flowchart LR
    I3["OPT(i - 3)<br/>Saltea 2 estaciones"] -->|"+ T[i]"| I["OPT(i) = T[i] + min(...)"]:::opt
    I2["OPT(i - 2)<br/>Saltea 1 estación"] -->|"+ T[i]"| I
    I1["OPT(i - 1)<br/>Sin saltear"] -->|"+ T[i]"| I
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 2. Semi-Pseudocódigo Simplificado

```text
FUNCION RutaMenorCostoParadas(T, N):
    // Posición 0 = Origen, 1..N = Estaciones, N+1 = Destino Final (con T[N+1] = 0)
    T[N + 1] <- 0
    DP <- arreglo de tamaño (N + 2) inicializado en 0
    padre <- arreglo de tamaño (N + 2) inicializado en 0

    // 1. Casos Base
    DP[0] <- 0
    DP[1] <- T[1];  padre[1] <- 0
    DP[2] <- T[2];  padre[2] <- 0   // Conviene saltar de 0 a 2 (DP[0] = 0 <= DP[1])

    // 2. Llenado Bottom-Up desde i = 3 hasta el destino N + 1
    PARA i <- 3 HASTA N + 1:
        mejor_prev <- argmin entre {i - 1, i - 2, i - 3} según DP[...]
        DP[i] <- T[i] + DP[mejor_prev]
        padre[i] <- mejor_prev

    // 3. Reconstrucción de las estaciones donde se detuvo
    paradas <- lista vacía
    actual <- padre[N + 1]
    MIENTRAS actual > 0:
        AGREGAR actual AL INICIO DE paradas
        actual <- padre[actual]

    RETORNAR (DP[N + 1], paradas)
```

#### 3. Justificación de Complejidad

* **Complejidad Temporal:** $\mathcal{O}(N)$. La tabla `DP` tiene $N + 2$ celdas (desde $0$ hasta $N + 1$). Cada celda $i$ se calcula en tiempo constante $\mathcal{O}(1)$ comparando únicamente $3$ valores anteriores (`i-1`, `i-2`, `i-3`). La reconstrucción recorre hacia atrás a lo sumo $N$ estaciones en $\mathcal{O}(N)$.
* **Complejidad Espacial:** $\mathcal{O}(N)$ para almacenar los arreglos `DP` y `padre` de tamaño $N + 2$.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Devolver $DP[N]$ en lugar de $DP[N+1]$:</strong> El transporte no está obligado a parar en la estación $N$; si paró en $N-1$ o en $N-2$, puede saltear la estación $N$ y llegar directo a la meta $N+1$.</li>
    <li><strong>Confundir "saltear 2 estaciones" con restar $2$ al índice:</strong> Si estás en $i$ y salteás las 2 estaciones anteriores ($i-1$ e $i-2$), venís de la estación $i-3$.</li>
  </ul>
</div>

---

### Errores Frecuentes en Exámenes sobre Programación Dinámica

1. **No definir en palabras qué significa $OPT(\dots)$:** Escribir directamente una fórmula o código sin explicar qué representa el estado anula la justificación.
2. **Olvidar los casos base:** No definir $OPT(0)$ o inicializar mal los bordes de la tabla.
3. **No justificar el orden de llenado:** Aclarar siempre que la tabla se llena de menor a mayor subproblema (*Bottom-Up*) para que los estados previos ya estén calculados.
4. **Omitir la reconstrucción:** Quedarse solo con el valor numérico $DP[n]$ cuando la consigna pide indicar cuáles son los elementos u operaciones elegidas.
"""
