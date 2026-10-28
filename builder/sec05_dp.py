"""Módulo 5: Programación Dinámica (PD)."""

def get_content():
    return r"""## 7. Tema 4: Programación Dinámica (PD)

### Conceptos Mínimos de Supervivencia

1. **Cuándo Usar Programación Dinámica:**
   * El problema exhibe **Subestructura Óptima**: la solución óptima global se compone de soluciones óptimas a sus subproblemas.
   * El problema tiene **Subproblemas Superpuestos**: los mismos subproblemas se resuelven una y otra vez (a diferencia de División y Conquista, donde los subproblemas son disjuntos).
2. **Los Cinco Pasos Obligatorios en el Examen de TDA:**
   Para obtener el puntaje completo en un ejercicio de Programación Dinámica, tu respuesta debe contener explícitamente:
   1. **Definición Formal del Estado:** ¿Qué significa exactamente $OPT(i, w)$ en el contexto del enunciado? (Ej: *"Valor máximo obtenible considerando un subconjunto de los primeros $i$ elementos con una capacidad restante de $w$ kilos"*).
   2. **Casos Base:** Valores donde la solución es trivial o inmediata (ej: $OPT(0, w) = 0$, $OPT(i, 0) = 0$).
   3. **Ecuación de Recurrencia:** La fórmula matemática cerrada que computa $OPT$ a partir de subproblemas más chicos, detallando las opciones consideradas y la función objetivo ($\min$ o $\max$).
   4. **Orden de Llenado de la Tabla:** Justificación de la dirección en que se itera la matriz (ej: *"De menor a mayor índice $i$, y para cada $i$ de menor a mayor capacidad $w$, asegurando que los valores requeridos ya hayan sido calculados"*).
   5. **Algoritmo de Reconstrucción de la Solución:** Procedimiento que recorre la tabla hacia atrás desde el resultado final para identificar qué elementos concretos componen la solución óptima.

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

**Qué está evaluando**  
Modelado del estado en 1D, razonamiento hacia atrás ($K \to 0$), planteo riguroso de la recurrencia con análisis de paridad, demostración formal de optimalidad y reconstrucción exacta de la secuencia de operaciones.

**Idea de resolución y Perspectiva Inversa**  
* *Perspectiva hacia atrás ($i \to 0$):* Pensar cómo llegar a un número $i$:
  * Siempre podemos llegar desde $i - 1$ aplicando la operación $+1$.
  * Si $i$ es par, también podemos llegar desde $i / 2$ aplicando la operación $\times 2$. Si $i$ es impar, es imposible haber llegado duplicando un entero.
* *Casos trampa iniciales:* Desde $0$, la operación $\times 2$ no genera avance ($0 \times 2 = 0$). El primer paso hacia adelante siempre debe ser $+1$ (hacia 1).

#### 1. Deducción Metodológica Formal (Los 5 Pasos de Programación Dinámica)

1. **Definición Formal del Estado:**  
   $$OPT(i) = \text{Mínima cantidad de operaciones necesarias para alcanzar el valor } i \text{ partiendo desde } 0.$$

2. **Casos Base:**  
   * $OPT(0) = 0$: Ya estamos en el origen, se requieren $0$ operaciones.  
   * $OPT(1) = 1$: Única transición válida es $0 + 1 = 1$, pues $0 \times 2 = 0$ no avanza.

3. **Ecuación de Recurrencia:**  
   Para todo $i \ge 1$:
   $$OPT(i) = \begin{cases} OPT(i - 1) + 1 & \text{si } i \text{ es impar} \\ \min\Big(OPT(i - 1) + 1, \; OPT\left(\frac{i}{2}\right) + 1\Big) & \text{si } i \text{ es par} \end{cases}$$

4. **Orden de Llenado de la Tabla:**  
   Iteración unidireccional creciente (*Bottom-Up*) desde $i = 1$ hasta $K$.  
   *Justificación:* Cada estado $i$ solo depende de $i - 1$ y $i / 2$. Como ambos predecesores son estrictamente menores que $i$, todos los subproblemas necesarios ya habrán sido resueltos y almacenados previamente en el DAG de dependencias.

5. **Algoritmo de Reconstrucción de la Secuencia:**  
   Retrocedemos desde $K$ hasta $0$ consultando el arreglo de predecesores `padre[i]`. Si $\text{padre}[i] = i / 2$, la operación fue $\times 2$; en caso contrario, fue $+1$. Se invierte la lista resultante para presentar la secuencia en orden cronológico de $0$ a $K$.

#### 2. Justificación Directa de Correctitud (Lista para Examen)

* **1. Solo hay dos formas de llegar a `i`:**
  * Si la última operación fue `+1`, vinimos sí o sí de `i - 1`.
  * Si la última operación fue `x2`, vinimos sí o sí de `i / 2` (y esto solo es posible cuando `i` es par).
* **2. Subestructura óptima:** Para llegar a `i` en la menor cantidad de pasos, necesitamos haber llegado primero a `i - 1` (o a `i / 2`) en la menor cantidad de pasos posible y sumarle `1` paso más.
* **3. Sin ciclos:** Como `i - 1` e `i / 2` son siempre más chicos que `i`, al llenar la tabla en orden desde `1` hasta `K` nos aseguramos de que ambos valores ya están calculados cuando los necesitamos.

#### 3. Diagrama de Flujo y Grafo Acíclico (DAG) de Decisiones

A continuación se representa el flujo de decisión iterativo y el grafo de transiciones óptimas para $K = 10$:

```mermaid
flowchart TD
    A(["Inicio: K = 10"]) --> B["DP[0] = 0"]
    B --> C["Bucle i de 1 hasta K"]
    C --> D["Candidato 1: DP[i-1] + 1 (Sumar 1)"]
    D --> E{"¿i es par?"}
    E -- No --> F["DP[i] = DP[i-1] + 1<br/>padre[i] = i - 1<br/>op[i] = '+1'"]
    E -- Sí --> G{"¿DP[i/2] + 1 es menor que DP[i]?"}
    G -- Sí --> H["DP[i] = DP[i/2] + 1<br/>padre[i] = i / 2<br/>op[i] = '*2'"]
    G -- No --> F
    F --> I{"¿i == K?"}
    H --> I
    I -- No --> C
    I -- Sí --> J["Backtracking desde K = 10 hasta 0"]
    J --> K(["Retornar DP[10] = 5 y secuencia"])
```

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
    N6 -->|+1| N7["7"]:::normal
    N8 -->|+1| N9["9"]:::normal
    N9 -->|+1| N10
```

<div class="visual-trace-container">
  <span class="trace-node start-node">0</span>
  <span class="trace-arrow"><span class="arrow-op">+1</span>➜</span>
  <span class="trace-node">1</span>
  <span class="trace-arrow"><span class="arrow-op">×2</span>➜</span>
  <span class="trace-node">2</span>
  <span class="trace-arrow"><span class="arrow-op">×2</span>➜</span>
  <span class="trace-node">4</span>
  <span class="trace-arrow"><span class="arrow-op">+1</span>➜</span>
  <span class="trace-node">5</span>
  <span class="trace-arrow"><span class="arrow-op">×2</span>➜</span>
  <span class="trace-node end-node">10</span>
</div>

#### 4. Tabla de Seguimiento Paso a Paso (Trace Table para $K = 10$)

| $i$ | Paridad | Opción $+1$ ($DP[i-1]+1$) | Opción $\times 2$ ($DP[i/2]+1$) | $DP[i]$ Óptimo | Decisión Tomada | `padre[i]` |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **0** | Par | — | — | **0** | Estado Inicial | — |
| **1** | Impar | $DP[0] + 1 = 0 + 1 = \mathbf{1}$ | No aplica ($1$ es impar) | **1** | $+1$ desde $0$ | 0 |
| **2** | Par | $DP[1] + 1 = 1 + 1 = 2$ | $DP[1] + 1 = 1 + 1 = \mathbf{2}$ | **2** | $\times 2$ desde $1$ | 1 |
| **3** | Impar | $DP[2] + 1 = 2 + 1 = \mathbf{3}$ | No aplica ($3$ es impar) | **3** | $+1$ desde $2$ | 2 |
| **4** | Par | $DP[3] + 1 = 3 + 1 = 4$ | $DP[2] + 1 = 2 + 1 = \mathbf{3}$ | **3** | $\times 2$ desde $2$ | 2 |
| **5** | Impar | $DP[4] + 1 = 3 + 1 = \mathbf{4}$ | No aplica ($5$ es impar) | **4** | $+1$ desde $4$ | 4 |
| **6** | Par | $DP[5] + 1 = 4 + 1 = 5$ | $DP[3] + 1 = 3 + 1 = \mathbf{4}$ | **4** | $\times 2$ desde $3$ | 3 |
| **7** | Impar | $DP[6] + 1 = 4 + 1 = \mathbf{5}$ | No aplica ($7$ es impar) | **5** | $+1$ desde $6$ | 6 |
| **8** | Par | $DP[7] + 1 = 5 + 1 = 6$ | $DP[4] + 1 = 3 + 1 = \mathbf{4}$ | **4** | $\times 2$ desde $4$ | 4 |
| **9** | Impar | $DP[8] + 1 = 4 + 1 = \mathbf{5}$ | No aplica ($9$ es impar) | **5** | $+1$ desde $8$ | 8 |
| **10** | Par | $DP[9] + 1 = 5 + 1 = 6$ | $DP[5] + 1 = 4 + 1 = \mathbf{5}$ | **5** | $\times 2$ desde $5$ | 5 |

**Detalle de Reconstrucción (Backtracking desde $K = 10$):**
1. En $10$: `padre[10] = 5`, operación = $\times 2$.
2. En $5$: `padre[5] = 4`, operación = $+1$.
3. En $4$: `padre[4] = 2`, operación = $\times 2$.
4. En $2$: `padre[2] = 1`, operación = $\times 2$.
5. En $1$: `padre[1] = 0`, operación = $+1$.
6. En $0$: Fin del recorrido.
* **Resultado exacto:** $5$ operaciones mínimas: `[+1, ×2, ×2, +1, ×2]`.

#### 5. Pseudocódigo Formal para Examen

```text
FUNCION MinimasOperacionesAK(K):
    SI K = 0:
        RETORNAR (0, lista vacía)

    // 1. Inicialización de la tabla DP y estructuras de reconstrucción
    INICIALIZAR DP como arreglo de tamaño (K + 1) en 0
    INICIALIZAR padre como arreglo de tamaño (K + 1) en 0
    INICIALIZAR op como arreglo de tamaño (K + 1) en cadenas vacías

    DP[0] <- 0

    // 2. Llenado Bottom-Up
    PARA i <- 1 HASTA K:
        // Opción por defecto: Sumar 1 desde (i - 1)
        DP[i] <- DP[i - 1] + 1
        padre[i] <- i - 1
        op[i] <- "SUMAR_1"

        // Opción alternativa: Duplicar desde (i / 2) si i es par
        SI (i MOD 2) = 0:
            SI DP[i / 2] + 1 < DP[i]:
                DP[i] <- DP[i / 2] + 1
                padre[i] <- i / 2
                op[i] <- "DUPLICAR"

    // 3. Reconstrucción en reversa del camino óptimo
    INICIALIZAR secuencia como lista vacía
    actual <- K
    MIENTRAS actual > 0:
        INSERTAR op[actual] AL INICIO DE secuencia
        actual <- padre[actual]

    RETORNAR (DP[K], secuencia)
```

**Complejidad**  
* **Temporal:** $\mathcal{O}(K)$. La tabla tiene $K + 1$ posiciones y cada una se calcula en tiempo constante $\mathcal{O}(1)$ comparando a lo sumo dos candidatos aritméticos. La reconstrucción realiza a lo sumo $K$ saltos (en la práctica $\le 2 \log_2 K$ saltos), lo que toma $\mathcal{O}(\log K) \subseteq \mathcal{O}(K)$.
* **Espacial:** $\mathcal{O}(K)$. Arreglos contiguos de tamaño $K + 1$ para almacenar los costos óptimos y punteros de retroceso.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Intentar duplicar desde 0:</strong> $0 \times 2 = 0$. Duplicar solo genera avance a partir de $x \ge 1$.</li>
    <li><strong>No incluir la reconstrucción de operaciones:</strong> Si el enunciado pide explícitamente <em>"y cómo son dichas operaciones"</em>, no devolver la secuencia descuenta la mitad del puntaje del ejercicio.</li>
    <li><strong>No justificar la paridad:</strong> Es indispensable explicitar en la recurrencia que la opción $\times 2$ solo se evalúa cuando $(i \pmod 2) = 0$.</li>
  </ul>
</div>

**Variación típica de parcial (Pregunta Clave: DP vs Greedy)**  
* *¿Se puede resolver con Greedy en tiempo $\mathcal{O}(\log K)$?*  
  **Sí:** Pensando de $K$ hacia $0$, si $K$ es par siempre conviene dividir por $2$; si es impar, restar $1$. Esto toma $\mathcal{O}(\log K)$ pasos.
* *¿Por qué entonces la cátedra exige Programación Dinámica?*  
  1. **Consigna estricta:** Si el enunciado impone DP, usar Greedy anula el ejercicio.  
  2. **Generalización ante variantes:** La formulación de DP es genérica y se adapta de inmediato si se introducen reglas más complejas donde Greedy fracasa (por ejemplo, si existieran transiciones como $+3$, $\times 3$, o costos no unitarios para cada operación). Con DP, simplemente se agrega un nuevo término a la función $\min()$:
     $$OPT(i) = \min\big(OPT(i-1) + c_{+1}, \; OPT(i/2) + c_{\times 2}, \; OPT(i-3) + c_{+3}\big)$$
     En cambio, un enfoque voraz requeriría una demostración formal de elección voraz (*Greedy Choice Property*) que con múltiples operaciones adicionales suele ser falsa.

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

**Qué está evaluando la cátedra**  
Mochila 2D (estado tridimensional $\text{elemento} \times \text{peso} \times \text{volumen}$) y manejo riguroso de restricciones lógicas XOR mediante bifurcación en dos subinstancias independientes o fijación de estado inicial.

#### 1. Deducción Metodológica Formal (Los 5 Pasos de Programación Dinámica)

1. **Reducción de la Restricción XOR y Definición del Estado:**
   Como los ítems $1$ y $2$ tienen una restricción XOR estricta ($\text{Guía } 1 \oplus \text{Guía } 2$), descomponemos el problema en dos casos mutuamente excluyentes sobre el subconjunto de ítems restantes $R = \{3, 4, \dots, n\}$ (de tamaño $m = n - 2$):
   * **Caso A (Fijar Guía 1):** Si $w_1 \le C \land v_1 \le L$, reservamos la Guía 1 y resolvemos una Mochila 2D estándar sobre los $m$ ítems restantes con capacidades remanentes $C_A = C - w_1$ y $L_A = L - v_1$, sumando $b_1$ al resultado.
   * **Caso B (Fijar Guía 2):** Si $w_2 \le C \land v_2 \le L$, reservamos la Guía 2 y resolvemos sobre los $m$ ítems restantes con capacidades remanentes $C_B = C - w_2$ y $L_B = L - v_2$, sumando $b_2$ al resultado.
   
   Para la Mochila 2D auxiliar sobre los $m$ elementos restantes, definimos el estado:
   $$OPT(i, p, v) = \text{Máximo beneficio obtenible usando un subconjunto de los primeros } i \text{ elementos de } R \text{ con peso disponible } p \text{ y volumen disponible } v.$$

2. **Casos Base:**
   $$OPT(0, p, v) = 0 \quad \forall p \in [0, C], \; \forall v \in [0, L]$$
   $$OPT(i, 0, v) = 0, \quad OPT(i, p, 0) = 0 \quad \text{(asumiendo } w_i, v_i > 0\text{)}$$

3. **Ecuación de Recurrencia:**
   Para cada elemento $i \in \{1, \dots, m\}$ con peso $w_i$, volumen $v_i$ y beneficio $b_i$:
   $$OPT(i, p, v) = \begin{cases} OPT(i - 1, p, v) & \text{si } w_i > p \lor v_i > v \\ \max\Big(OPT(i - 1, p, v), \; OPT(i - 1, p - w_i, v - v_i) + b_i\Big) & \text{si } w_i \le p \land v_i \le v \end{cases}$$
   El valor óptimo global del problema original es:
   $$OPT_{\text{total}} = \max\Big( b_1 + OPT(m, C - w_1, L - v_1), \;\; b_2 + OPT(m, C - w_2, L - v_2) \Big)$$

4. **Orden de Llenado de la Tabla:**
   Tres bucles anidados crecientes: índice de elemento $i$ desde $1$ hasta $m$, peso $p$ desde $0$ hasta $C_{\text{rem}}$ y volumen $v$ desde $0$ hasta $L_{\text{rem}}$.

5. **Reconstrucción de la Solución:**
   Se determina cuál de los dos casos ($A$ o $B$) alcanzó el máximo global, se agrega la guía correspondiente, y se retrocede desde $(m, C_{\text{rem}}, L_{\text{rem}})$ hasta $i = 1$ comparando si $DP[i][p][v] \neq DP[i-1][p][v]$.

#### 2. Diagrama Visual de Descomposición XOR + Mochila 2D

```mermaid
flowchart TD
    P(["Instancia Original: Capacidades (C, L) e Ítems {1..n}"]) --> CA["Caso A: Incluir Guía 1 (si w₁ ≤ C y v₁ ≤ L)<br/>Capacidad remanente: (C - w₁, L - v₁)"]:::branch
    P --> CB["Caso B: Incluir Guía 2 (si w₂ ≤ C y v₂ ≤ L)<br/>Capacidad remanente: (C - w₂, L - v₂)"]:::branch
    CA --> DPA["Mochila 2D sobre Ítems {3..n}<br/>Total A = b₁ + OPT(n-2, C-w₁, L-v₁)"]:::dp
    CB --> DPB["Mochila 2D sobre Ítems {3..n}<br/>Total B = b₂ + OPT(n-2, C-w₂, L-v₂)"]:::dp
    DPA --> MAX{"Comparar: max(Total A, Total B)"}
    DPB --> MAX
    MAX --> SOL(["Solución Óptima Global + Reconstrucción"]):::done
    classDef branch fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#fff
    classDef dp fill:#0284c7,stroke:#0369a1,stroke-width:2px,color:#fff
    classDef done fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 3. Ejemplo Concreto y Traza Paso a Paso

Sea una mochila con capacidad de peso $C = 5\text{ kg}$ y volumen $L = 5\text{ litros}$, y $n = 4$ ítems:

| Ítem | Descripción | Peso ($w_i$) | Volumen ($v_i$) | Beneficio ($b_i$) | Rol |
| :---: | :--- | :---: | :---: | :---: | :--- |
| **1** | Guía de Aves Patagónicas | $2$ | $2$ | $10$ | Guía 1 (XOR) |
| **2** | Guía de Aves Pampeanas | $4$ | $3$ | $18$ | Guía 2 (XOR) |
| **3** | Binoculares Profesionales | $3$ | $2$ | $15$ | Ítem libre ($R_1$) |
| **4** | Cámara Teleobjetivo | $2$ | $3$ | $12$ | Ítem libre ($R_2$) |

* **Evaluación Caso A (Llevar Guía 1):**
  * Consume $w_1 = 2, v_1 = 2$, aporta $b_1 = 10$. Capacidad remanente: $C_A = 3, L_A = 3$.
  * Entre los ítems libres $\{3, 4\}$:
    * Ítem 3 ($w=3, v=2 \le (3,3)$): entra y aporta $15$.
    * Ítem 4 ($w=2, v=3 \le (3,3)$): entra por sí solo ($12$), pero no junto con el 3 ($3+2 = 5 > 3$).
  * Óptimo remanente: $OPT(2, 3, 3) = 15$ (Binoculares).
  * **Total Caso A:** $10 + 15 = \mathbf{25}$ (Guía 1 + Binoculares, peso total $5$, volumen $4$).
* **Evaluación Caso B (Llevar Guía 2):**
  * Consume $w_2 = 4, v_2 = 3$, aporta $b_2 = 18$. Capacidad remanente: $C_B = 1, L_B = 2$.
  * Ninguno de los ítems $\{3, 4\}$ cabe en peso remanente $1$. $OPT(2, 1, 2) = 0$.
  * **Total Caso B:** $18 + 0 = \mathbf{18}$ (solo Guía 2).
* **Decisión Óptima:** $\max(25, 18) = \mathbf{25}$ llevando $\{\text{Guía 1}, \text{Binoculares}\}$.

#### 4. Pseudocódigo Formal (Estilo Examen Presencial)

```text
FUNCION MochilaPaoloCasanova(items, C, L):
    // items[0] es Guia 1, items[1] es Guia 2, items[2..n-1] son el resto
    beneficio_mejor <- -INFINITO
    INICIALIZAR mejor_solucion como lista vacía
    resto_items <- items[2 .. longitud(items) - 1]

    // --- CASO A: Llevar Guia 1 (items[0]) ---
    SI items[0].peso <= C Y items[0].volumen <= L:
        (ben_A, sol_A) <- Mochila2DEstandar(resto_items, C - items[0].peso, L - items[0].volumen)
        total_ben_A <- items[0].beneficio + ben_A
        SI total_ben_A > beneficio_mejor:
            beneficio_mejor <- total_ben_A
            INSERTAR items[0] AL INICIO DE sol_A
            mejor_solucion <- sol_A

    // --- CASO B: Llevar Guia 2 (items[1]) ---
    SI items[1].peso <= C Y items[1].volumen <= L:
        (ben_B, sol_B) <- Mochila2DEstandar(resto_items, C - items[1].peso, L - items[1].volumen)
        total_ben_B <- items[1].beneficio + ben_B
        SI total_ben_B > beneficio_mejor:
            beneficio_mejor <- total_ben_B
            INSERTAR items[1] AL INICIO DE sol_B
            mejor_solucion <- sol_B

    RETORNAR (beneficio_mejor, mejor_solucion)

FUNCION Mochila2DEstandar(elementos, MaxPeso, MaxVol):
    m <- longitud(elementos)
    INICIALIZAR DP como matriz 3D de (m + 1) x (MaxPeso + 1) x (MaxVol + 1) en 0

    PARA i <- 1 HASTA m:
        elem <- elementos[i - 1]
        PARA p <- 0 HASTA MaxPeso:
            PARA v <- 0 HASTA MaxVol:
                DP[i][p][v] <- DP[i - 1][p][v]
                SI elem.peso <= p Y elem.volumen <= v:
                    val_con_elem <- DP[i - 1][p - elem.peso][v - elem.volumen] + elem.beneficio
                    SI val_con_elem > DP[i][p][v]:
                        DP[i][p][v] <- val_con_elem

    // Reconstrucción
    INICIALIZAR seleccion como lista vacía
    rem_p <- MaxPeso
    rem_v <- MaxVol
    PARA i <- m BAJANDO HASTA 1:
        SI DP[i][rem_p][rem_v] != DP[i - 1][rem_p][rem_v]:
            elem <- elementos[i - 1]
            INSERTAR elem EN seleccion
            rem_p <- rem_p - elem.peso
            rem_v <- rem_v - elem.volumen

    RETORNAR (DP[m][MaxPeso][MaxVol], seleccion)
```

**Complejidad**  
* **Tiempo:** Resolvemos la tabla 3D a lo sumo dos veces (una por cada guía obligatoria). Cada llenado tiene dimensiones $(n-2) \times C \times L$ y operaciones $O(1)$ por celda: **$\Theta(n \cdot C \cdot L)$** (pseudo-polinomial).
* **Espacio:** Tabla 3D de tamaño **$\Theta(n \cdot C \cdot L)$**.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Permitir que la mochila quede sin guías o con ambas:</strong> Si se mete la Guía 1 y la Guía 2 en el bucle general de la mochila sin separar los casos, la recurrencia podría elegir ambas o ninguna.</li>
    <li><strong>No validar si la guía cabe individualmente:</strong> Antes de restar $C - w_1$ y $L - v_1$, es obligatorio verificar que $w_1 \le C \land v_1 \le L$ para no indexar capacidades negativas.</li>
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

**Qué está evaluando la cátedra**  
DP sobre prefijos de secuencias ($1 \dots i$), prueba exhaustiva del punto de inicio $j$ de la última línea y minimización de funciones de costo cuadrático.

#### 1. Deducción Metodológica Formal (Los 5 Pasos de Programación Dinámica)

1. **Definición Formal del Estado:**  
   $$OPT(i) = \text{Mínimo costo total (suma de cuadrados de sobrantes) de formatear el prefijo de palabras } W_1, \dots, W_i.$$
2. **Caso Base:**  
   $$OPT(0) = 0 \quad (\text{el texto vacío sin palabras tiene costo } 0)$$
3. **Ecuación de Recurrencia:**  
   Para formatear hasta la palabra $i$ ($1 \le i \le n$), la última línea debe contener algún sufijo válido de palabras $W_j, \dots, W_i$ con $1 \le j \le i$ tal que $\text{Longitud}(j, i) \le L$:
   $$OPT(i) = \min_{\substack{1 \le j \le i \\ \text{Longitud}(j, i) \le L}} \Big\{ OPT(j - 1) + \big(L - \text{Longitud}(j, i)\big)^2 \Big\}$$
4. **Orden de Llenado de la Tabla:**  
   De izquierda a derecha para $i = 1, 2, \dots, n$. Para cada $i$, iteramos $j$ hacia atrás ($j = i, i-1, \dots, 1$) acumulando $\text{Longitud}(j, i)$ en $O(1)$ y cortando el bucle interno apenas $\text{Longitud}(j, i) > L$.
5. **Reconstrucción de la Partición:**  
   Almacenamos en `corte[i]` el índice $j^*$ que minimizó $OPT(i)$. Luego retrocedemos desde $idx = n$: la línea actual abarca $[corte[idx], \; idx]$, y saltamos a $idx = corte[idx] - 1$ hasta llegar a $0$.

#### 2. Diagrama Visual de Transición de Prefijos (Word Wrap)

```mermaid
flowchart LR
    P0["OPT(0) = 0"] --> Pj["OPT(j - 1)<br/>Prefijo W₁..W_{j-1} óptimo"]:::prev
    Pj -->|"+ Costo última línea: Sobrante(j, i)²"| Pi["OPT(i)<br/>Mínimo sobre todo j válido"]:::curr
    classDef prev fill:#0284c7,stroke:#0369a1,stroke-width:2px,color:#fff
    classDef curr fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 3. Ejemplo Concreto y Tabla de Traza Paso a Paso

Sea un ancho máximo de línea $L = 6$ y $n = 4$ palabras con longitudes $C = [3, 2, 2, 3]$ (ej: `"SOL"`, `"DE"`, `"LA"`, `"PAZ"`):

| Prefijo $i$ | Palabra $W_i$ | Candidatos de última línea $[j..i]$ con $\text{Long}(j,i) \le 6$ | Cálculo $OPT(j-1) + \text{Sobrante}(j,i)^2$ | $OPT(i)$ Mínimo | `corte[i]` |
| :---: | :---: | :--- | :--- | :---: | :---: |
| **0** | — | — | Caso base | **$0$** | — |
| **1** | `"SOL"` ($3$) | $[1..1]$: $\text{Long}=3$, $\text{Sob}=3$ | $OPT(0) + 3^2 = 0 + 9 = 9$ | **$9$** | $1$ |
| **2** | `"DE"` ($2$) | $[2..2]$: $\text{Long}=2$, $\text{Sob}=4$<br/>$[1..2]$: $\text{Long}=3+1+2=6$, $\text{Sob}=0$ | $j=2: OPT(1) + 4^2 = 9 + 16 = 25$<br/>$j=1: OPT(0) + 0^2 = 0 + 0 = \mathbf{0}$ | **$0$** | $1$ |
| **3** | `"LA"` ($2$) | $[3..3]$: $\text{Long}=2$, $\text{Sob}=4$<br/>$[2..3]$: $\text{Long}=2+1+2=5$, $\text{Sob}=1$<br/>$[1..3]$: $\text{Long}=8 > 6$ (Poda) | $j=3: OPT(2) + 4^2 = 0 + 16 = 16$<br/>$j=2: OPT(1) + 1^2 = 9 + 1 = \mathbf{10}$ | **$10$** | $2$ |
| **4** | `"PAZ"` ($3$) | $[4..4]$: $\text{Long}=3$, $\text{Sob}=3$<br/>$[3..4]$: $\text{Long}=2+1+3=6$, $\text{Sob}=0$<br/>$[2..4]$: $\text{Long}=9 > 6$ (Poda) | $j=4: OPT(3) + 3^2 = 10 + 9 = 19$<br/>$j=3: OPT(2) + 0^2 = 0 + 0 = \mathbf{0}$ | **$0$** | $3$ |

*Reconstrucción:* `corte[4] = 3` $\implies$ Línea 2: $[W_3, W_4]$ (`"LA PAZ"`, largo 6, sobrante 0); luego `idx = 2`, `corte[2] = 1` $\implies$ Línea 1: $[W_1, W_2]$ (`"SOL DE"`, largo 6, sobrante 0). Costo total óptimo: $0$. (Observe que un Greedy voraz habría metido `"SOL DE"` en la línea 1, pero si $W_1=3, W_2=2, W_3=4$ con $L=6$, Greedy deja $W_3$ sola con costo $0^2 + 2^2 = 4$, mientras que DP equilibra).

#### 4. Pseudocódigo Formal (Estilo Examen Presencial)

```text
FUNCION JustificarTextoWordWrap(longitudes_palabras, L):
    n <- longitud(longitudes_palabras)

    // DP[i]: costo mínimo para las primeras i palabras
    INICIALIZAR DP como arreglo de tamaño (n + 1) con INFINITO
    INICIALIZAR corte como arreglo de tamaño (n + 1) con 0
    DP[0] <- 0

    // Llenado de DP para prefijos crecientes
    PARA i <- 1 HASTA n:
        longitud_acumulada <- 0

        // Probamos que la última línea comience en la palabra j
        PARA j <- i BAJANDO HASTA 1:
            SI j = i:
                longitud_acumulada <- longitudes_palabras[i - 1]
            SINO:
                longitud_acumulada <- longitud_acumulada + 1 + longitudes_palabras[j - 1]

            // Si excede el ancho de línea L, no caben más palabras hacia atrás
            SI longitud_acumulada > L:
                ROMPER

            sobrante <- L - longitud_acumulada
            costo_linea <- sobrante * sobrante

            SI DP[j - 1] + costo_linea < DP[i]:
                DP[i] <- DP[j - 1] + costo_linea
                corte[i] <- j

    // Reconstrucción de la partición en líneas
    INICIALIZAR lineas como lista vacía
    idx <- n
    MIENTRAS idx > 0:
        inicio_linea <- corte[idx]
        INSERTAR (inicio_linea, idx) AL INICIO DE lineas
        idx <- inicio_linea - 1

    RETORNAR (DP[n], lineas)
```

**Complejidad**  
* **Tiempo:** Hay $n$ estados. Para cada estado $i$, el bucle interno evalúa a lo sumo $i$ palabras (y como máximo $L / 2$ palabras antes de superar el ancho $L$). En el peor caso la complejidad es **$O(n^2)$** (o bien **$O(n \cdot L)$**).
* **Espacio:** Arreglos 1D de tamaño $n + 1$ para `DP` y `corte`: **$\Theta(n)$**.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Olvidar sumar 1 por cada espacio en blanco intermedio:</strong> Entre $W_j$ y $W_i$ hay exactamente $(i - j)$ espacios obligatorios. Omitirlos calcula mal la capacidad de la línea.</li>
    <li><strong>Permitir sobrantes negativos cuando $\text{Longitud}(j, i) > L$:</strong> Como el costo está elevado al cuadrado ($\text{sobrante}^2$), si no se corta el bucle cuando $\text{Longitud}(j, i) > L$, un sobrante negativo como $(-2)^2 = 4$ parecería válido y barato. Es obligatorio cortar o asignar $+\infty$.</li>
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

**Qué está evaluando la cátedra**  
Generalización formal de la mochila 0-1 a tres dimensiones de capacidad acumuladas simultáneamente (tabla 4D).

#### 1. Deducción Metodológica Formal (Los 5 Pasos de Programación Dinámica)

1. **Definición Formal del Estado:**  
   $$OPT(i, w, v, m) = \text{Máximo beneficio comercial seleccionando un subconjunto de los primeros } i \text{ paquetes con peso máximo } w, \text{ volumen máximo } v \text{ y seguro máximo } m.$$
   donde $0 \le i \le n$, $0 \le w \le C$, $0 \le v \le T$, $0 \le m \le M$.
2. **Casos Base:**  
   $$OPT(0, w, v, m) = 0 \quad \forall w \in [0, C], \; \forall v \in [0, T], \; \forall m \in [0, M]$$
3. **Ecuación de Recurrencia:**  
   Para el paquete $i$ con parámetros $(W_i, V_i, C_i, B_i)$:
   $$OPT(i, w, v, m) = \begin{cases} OPT(i - 1, w, v, m) & \text{si } W_i > w \lor V_i > v \lor C_i > m \\ \max\Big(OPT(i - 1, w, v, m), \; OPT(i - 1, w - W_i, v - V_i, m - C_i) + B_i\Big) & \text{si } W_i \le w \land V_i \le v \land C_i \le m \end{cases}$$
4. **Orden de Llenado de la Tabla:**  
   Cuatro bucles anidados crecientes: paquete $i$ de $1$ a $n$, peso $w$ de $0$ a $C$, volumen $v$ de $0$ a $T$ y seguro $m$ de $0$ a $M$.
5. **Reconstrucción de la Solución:**  
   Partiendo de $(n, C, T, M)$ y retrocediendo $i$ desde $n$ hasta $1$: si $DP[i][w][v][m] \neq DP[i-1][w][v][m]$, el paquete $i$ fue incluido y se actualizan $(w, v, m) \leftarrow (w - W_i, v - V_i, m - C_i)$.

#### 2. Diagrama Visual de Transición 4D del Estado

```mermaid
flowchart TD
    S["Estado Actual: OPT(i, w, v, m)"] --> COND{"¿Cabe en los 3 recursos?<br/>W_i ≤ w ∧ V_i ≤ v ∧ C_i ≤ m"}
    COND -- No --> EXCL["Excluir paquete i:<br/>OPT(i-1, w, v, m)"]:::no
    COND -- Sí --> MAX["max(<br/>  Excluir: OPT(i-1, w, v, m),<br/>  Incluir: OPT(i-1, w-W_i, v-V_i, m-C_i) + B_i<br/>)"]:::yes
    classDef no fill:#991b1b,stroke:#7f1d1d,stroke-width:1.5px,color:#fff
    classDef yes fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 3. Pseudocódigo Formal (Estilo Examen Presencial)

```text
FUNCION ResolverDeliveryMochila3D(paquetes, C, T, M):
    n <- longitud(paquetes)

    // Tabla 4D de dimensiones: (n + 1) x (C + 1) x (T + 1) x (M + 1)
    INICIALIZAR DP como arreglo 4D inicializado en 0

    // Llenado bottom-up
    PARA i <- 1 HASTA n:
        p <- paquetes[i - 1]
        PARA w <- 0 HASTA C:
            PARA v <- 0 HASTA T:
                PARA m <- 0 HASTA M:
                    // Opción 1: Excluir paquete i
                    DP[i][w][v][m] <- DP[i - 1][w][v][m]

                    // Opción 2: Incluir paquete i si no satura ningún recurso
                    SI p.peso <= w Y p.volumen <= v Y p.costo <= m:
                        val_con_p <- DP[i - 1][w - p.peso][v - p.volumen][m - p.costo] + p.beneficio
                        SI val_con_p > DP[i][w][v][m]:
                            DP[i][w][v][m] <- val_con_p

    // Reconstrucción de los paquetes seleccionados
    INICIALIZAR seleccionados como lista vacía
    curr_w <- C
    curr_v <- T
    curr_m <- M

    PARA i <- n BAJANDO HASTA 1:
        SI DP[i][curr_w][curr_v][curr_m] != DP[i - 1][curr_w][curr_v][curr_m]:
            p <- paquetes[i - 1]
            INSERTAR p EN seleccionados
            curr_w <- curr_w - p.peso
            curr_v <- curr_v - p.volumen
            curr_m <- curr_m - p.costo

    RETORNAR (DP[n][C][T][M], seleccionados)
```

**Complejidad**  
* **Tiempo:** Se llenan $(n + 1) \cdot (C + 1) \cdot (T + 1) \cdot (M + 1)$ celdas con $O(1)$ operaciones por celda: **$\Theta(n \cdot C \cdot T \cdot M)$** (Complejidad pseudo-polinomial).
* **Espacio:** **$\Theta(n \cdot C \cdot T \cdot M)$** para la matriz completa (u $O(C \cdot T \cdot M)$ si solo se pide el valor máximo iterando en reversa sobre una única tabla 3D).

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Olvidar una de las tres dimensiones en la guarda:</strong> Se debe verificar simultáneamente <code>p.peso &lt;= w Y p.volumen &lt;= v Y p.costo &lt;= m</code>.</li>
    <li><strong>No aclarar que la complejidad es pseudo-polinomial:</strong> Depende directamente de las magnitudes numéricas $C, T, M$ y es exponencial respecto a la cantidad de bits $\log_2(C \cdot T \cdot M)$.</li>
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

#### 1. Deducción Metodológica Formal (Los 5 Pasos de Programación Dinámica)

1. **Definición Formal del Estado:**  
   $$OPT(i) = \text{Ganancia máxima obtenible considerando los primeros } i \text{ días } (1 \le i \le n) \text{ sin trabajar dos días consecutivos.}$$
2. **Casos Base:**  
   $$OPT(0) = 0 \quad (\text{sin días}), \qquad OPT(1) = G[1] \quad (\text{conviene trabajar el único día disponible})$$
3. **Ecuación de Recurrencia:**  
   Para el día $i \ge 2$:
   * **Descansar el día $i$:** Mantiene la ganancia óptima hasta el día anterior: $OPT(i - 1)$.
   * **Trabajar el día $i$:** Suma $G[i]$, pero exige obligatoriamente haber descansado el día $i - 1$, por lo que suma el óptimo hasta $i - 2$: $OPT(i - 2) + G[i]$.
   $$OPT(i) = \max\Big(OPT(i - 1), \; OPT(i - 2) + G[i]\Big)$$
4. **Orden de Llenado de la Tabla:**  
   Secuencial creciente desde $i = 2$ hasta $n$ en tiempo $O(n)$.
5. **Reconstrucción de los Días Trabajados:**  
   Retrocediendo desde $i = n$: si $DP[i] == DP[i - 2] + G[i]$, Juan trabajó el día $i$ y saltamos a $i - 2$; en caso contrario descansó el día $i$ y pasamos a $i - 1$.

#### 2. Diagrama Visual de Decisión con Exclusión Adyacente

```mermaid
flowchart LR
    D2["OPT(i - 2)"] -->|"+ G[i] (Trabaja día i, descansa i-1)"| Di["OPT(i) = max(...)"]:::opt
    D1["OPT(i - 1)"] -->|"+ 0 (Descansa día i)"| Di
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 3. Ejemplo Concreto y Tabla de Traza Paso a Paso

Sean $n = 5$ días con ganancias $G = [10, 20, 15, 30, 10]$:

| Día $i$ | Ganancia $G[i]$ | Descansar: $OPT(i-1)$ | Trabajar: $OPT(i-2) + G[i]$ | $OPT(i)$ | Decisión en $i$ |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **0** | — | — | — | **$0$** | Caso base |
| **1** | $10$ | $0$ | $0 + 10 = 10$ | **$10$** | Trabaja día 1 |
| **2** | $20$ | $10$ | $0 + 20 = 20$ | **$20$** | Trabaja día 2 |
| **3** | $15$ | $20$ | $10 + 15 = 25$ | **$25$** | Trabaja días $\{1, 3\}$ |
| **4** | $30$ | $25$ | $20 + 30 = 50$ | **$50$** | Trabaja días $\{2, 4\}$ |
| **5** | $10$ | $50$ | $25 + 10 = 35$ | **$50$** | Descansa día 5 (mantiene $\{2, 4\}$) |

*Resultado óptimo:* Ganancia máxima **$50$** trabajando los días $2$ y $4$ ($20 + 30 = 50$).

#### 4. Pseudocódigo Formal (Estilo Examen Presencial)

```text
FUNCION JuanElVago(G):
    n <- longitud(G)
    SI n = 0:
        RETORNAR (0, lista vacía)
    SI n = 1:
        RETORNAR (G[0], [0])

    INICIALIZAR DP como arreglo de tamaño (n + 1) en 0
    DP[0] <- 0
    DP[1] <- G[0]

    PARA i <- 2 HASTA n:
        DP[i] <- maximo(DP[i - 1], DP[i - 2] + G[i - 1])

    // Reconstrucción
    INICIALIZAR dias como lista vacía
    idx <- n
    MIENTRAS idx > 0:
        SI idx = 1:
            INSERTAR 0 AL INICIO DE dias
            ROMPER
        SI DP[idx] = DP[idx - 2] + G[idx - 1]:
            INSERTAR (idx - 1) AL INICIO DE dias
            idx <- idx - 2
        SINO:
            idx <- idx - 1

    RETORNAR (DP[n], dias)
```

**Complejidad**  
* **Tiempo:** $\Theta(n)$ pues llena una tabla lineal de $n + 1$ posiciones con operaciones $O(1)$.
* **Espacio:** $\Theta(n)$ para reconstruir los días (u $O(1)$ usando solo dos variables escalares si únicamente se pide el monto máximo).

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

#### 1. Deducción Metodológica Formal (Los 5 Pasos de Programación Dinámica)

1. **Ordenamiento Previo y Función de Predecesor Compatible $p(i)$:**  
   Ordenamos los intervalos por tiempo de finalización creciente: $f_1 \le f_2 \le \dots \le f_n$ en $O(n \log n)$.  
   Para cada intervalo $i \in \{1, \dots, n\}$, definimos $p(i)$ como el mayor índice $j < i$ tal que el intervalo $j$ no se solapa con $i$ ($f_j \le s_i$). Si no existe tal intervalo, $p(i) = 0$. Como las fechas de fin están ordenadas, $p(i)$ se halla mediante **Búsqueda Binaria** en $O(\log n)$.
2. **Definición Formal del Estado:**  
   $$OPT(i) = \text{Beneficio máximo obtenible seleccionando un subconjunto de intervalos mutuamente compatibles dentro de } \{1, \dots, i\}.$$
3. **Caso Base:**  
   $$OPT(0) = 0$$
4. **Ecuación de Recurrencia:**  
   $$OPT(i) = \max\Big(OPT(i - 1), \;\; OPT(p(i)) + v_i\Big)$$
5. **Orden de Llenado y Reconstrucción:**  
   Se llena para $i = 1 \dots n$ en $O(n)$. Para reconstruir, desde $i = n$: si $DP[p(i)] + v_i \ge DP[i-1]$, se incluye el intervalo $i$ y se salta directamente a $i \leftarrow p(i)$; si no, se avanza a $i \leftarrow i - 1$.

#### 2. Diagrama Visual del Salto al Predecesor Compatible $p(i)$

```mermaid
flowchart LR
    P_i["OPT(p(i))<br/>Último j con f_j ≤ s_i (Búsqueda Binaria)"] -->|"+ v_i (Incluir intervalo i)"| OPT_i["OPT(i) = max(...)"]:::opt
    Prev["OPT(i - 1)<br/>Prefijo anterior"] -->|"+ 0 (Excluir intervalo i)"| OPT_i
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 3. Ejemplo Concreto y Tabla de Traza Paso a Paso

Consideremos $n = 4$ intervalos ya ordenados por $f_i$:

| Índice $i$ | Intervalo $[s_i, f_i]$ | Valor $v_i$ | Predecesor $p(i)$ ($f_j \le s_i$) | Excluir: $OPT(i-1)$ | Incluir: $OPT(p(i)) + v_i$ | $OPT(i)$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | $[1, 3]$ | $50$ | $0$ | $0$ | $0 + 50 = 50$ | **$50$** |
| **2** | $[2, 5]$ | $20$ | $0$ ($f_1=3 > 2$) | $50$ | $0 + 20 = 20$ | **$50$** |
| **3** | $[4, 6]$ | $100$ | $1$ ($f_1=3 \le 4$) | $50$ | $OPT(1) + 100 = 150$ | **$150$** |
| **4** | $[5, 8]$ | $70$ | $2$ ($f_2=5 \le 5$) | $150$ | $OPT(2) + 70 = 50 + 70 = 120$ | **$150$** |

*Solución óptima:* Intervalos $\{1, 3\}$ con ganancia total $50 + 100 = \mathbf{150}$.

#### 4. Pseudocódigo Formal (Estilo Examen Presencial)

```text
FUNCION IntervalSchedulingPonderado(intervalos):
    n <- longitud(intervalos)
    ORDENAR intervalos POR fin ASCENDENTE

    // Precalcular p(i) para cada i mediante búsqueda binaria en O(n log n)
    INICIALIZAR P como arreglo de tamaño (n + 1) en 0
    PARA i <- 1 HASTA n:
        P[i] <- BuscarUltimoCompatible(intervalos, i)

    INICIALIZAR DP como arreglo de tamaño (n + 1) en 0
    DP[0] <- 0

    PARA i <- 1 HASTA n:
        val_excluir <- DP[i - 1]
        val_incluir <- DP[P[i]] + intervalos[i - 1].valor
        DP[i] <- maximo(val_excluir, val_incluir)

    // Reconstrucción
    INICIALIZAR seleccion como lista vacía
    idx <- n
    MIENTRAS idx > 0:
        SI DP[P[idx]] + intervalos[idx - 1].valor >= DP[idx - 1]:
            INSERTAR intervalos[idx - 1] AL INICIO DE seleccion
            idx <- P[idx]
        SINO:
            idx <- idx - 1

    RETORNAR (DP[n], seleccion)

FUNCION BuscarUltimoCompatible(intervalos, i):
    ini <- 0
    fin <- i - 2
    res <- 0
    s_i <- intervalos[i - 1].inicio

    MIENTRAS ini <= fin:
        med <- (ini + fin) / 2
        SI intervalos[med].fin <= s_i:
            res <- med + 1 // Convertido a índice 1-based
            ini <- med + 1
        SINO:
            fin <- med - 1

    RETORNAR res
```

**Complejidad**  
* **Tiempo:** Ordenamiento en $O(n \log n) + n$ búsquedas binarias de $O(\log n)$ para calcular $p(i) +$ llenado lineal de DP en $O(n)$. Total: **$\Theta(n \log n)$**.
* **Espacio:** **$\Theta(n)$** para los arreglos `DP`, `P` y la reconstrucción.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Buscar $p(i)$ de forma lineal con un bucle hacia atrás:</strong> Si buscas el último intervalo compatible recorriendo desde $i-1$ hasta $1$, el preprocesamiento toma $O(n^2)$ en el peor caso, incumpliendo la cota exigida de $O(n \log n)$. Debe usarse Búsqueda Binaria sobre los tiempos de fin ordenados.</li>
    <li><strong>Ordenar por tiempo de inicio $s_i$ en vez de fin $f_i$:</strong> Para que el prefijo $1 \dots p(i)$ contenga exactamente todos los intervalos que terminan antes de $s_i$, el arreglo debe estar ordenado por $f_i$.</li>
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

#### 1. Idea y Justificación en Lenguaje Natural

* Modelamos el punto de partida (origen) como la posición $0$ con costo $OPT(0) = 0$, las $N$ estaciones intermedias como las posiciones $1, 2, \dots, N$ con tarifas $T[1 \dots N]$, y el objetivo final (destino) como la posición $N + 1$ con tarifa $T[N + 1] = 0$ (llegar al destino no cobra peaje de parada intermedia, pero estamos obligados a alcanzarlo).
* **Subestructura óptima y decisión hacia atrás:** Para llegar a cualquier estación $i$ (o al destino final $N + 1$), como por autonomía **a lo sumo podemos saltear 2 estaciones seguidas**, el último lugar donde el transporte se detuvo inmediatamente antes de $i$ tiene que haber sido obligatoriamente:
  1. La estación $i - 1$ (avanzó directo sin saltear ninguna estación),
  2. La estación $i - 2$ (salteó exactamente $1$ estación: la $i - 1$), o
  3. La estación $i - 3$ (salteó exactamente $2$ estaciones seguidas: la $i - 2$ y la $i - 1$).
* Como buscamos minimizar el gasto acumulado hasta $i$, debemos haber llegado de forma óptima a alguno de esos tres predecesores válidos y sumarle la tarifa $T[i]$ de la parada actual:
  $$OPT(i) = T[i] + \min\Big(OPT(i - 1), \; OPT(i - 2), \; OPT(i - 3)\Big)$$
* **Casos Base:**
  * $OPT(0) = 0$ (estamos en el origen sin costo).
  * $OPT(1) = T[1] + OPT(0) = T[1]$ (solo se puede llegar desde $0$).
  * $OPT(2) = T[2] + \min(OPT(1), \; OPT(0)) = T[2]$ (suponiendo tarifas no negativas $T[k] \ge 0$, saltar directo de $0$ a $2$ cuesta $T[2]$).

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
    // T[1..N] contiene las tarifas de las N estaciones intermedias
    // Posición 0 = Origen (costo 0), Posición N+1 = Destino Final (tarifa 0)
    INICIALIZAR DP como arreglo de tamaño (N + 2) en 0
    INICIALIZAR padre como arreglo de tamaño (N + 2) en 0

    // 1. Casos Base
    DP[0] <- 0
    SI N >= 1:
        DP[1] <- T[1]
        padre[1] <- 0
    SI N >= 2:
        // Puede venir de 0 (salteando la 1) o de 1
        SI DP[0] <= DP[1]:
            DP[2] <- T[2] + DP[0]
            padre[2] <- 0
        SINO:
            DP[2] <- T[2] + DP[1]
            padre[2] <- 1

    // 2. Llenado Bottom-Up desde i = 3 hasta N + 1
    PARA i <- 3 HASTA N + 1:
        tarifa_actual <- (T[i] SI i <= N SINO 0)

        // Buscamos el mejor predecesor entre i-1, i-2 e i-3
        mejor_prev <- i - 1
        SI DP[i - 2] < DP[mejor_prev]:
            mejor_prev <- i - 2
        SI DP[i - 3] < DP[mejor_prev]:
            mejor_prev <- i - 3

        DP[i] <- tarifa_actual + DP[mejor_prev]
        padre[i] <- mejor_prev

    // 3. Reconstrucción de las estaciones donde conviene detenerse
    INICIALIZAR paradas como lista vacía
    actual <- padre[N + 1]
    MIENTRAS actual > 0:
        INSERTAR actual AL INICIO DE paradas
        actual <- padre[actual]

    RETORNAR (DP[N + 1], paradas)
```

#### 3. Justificación de Complejidad

* **Complejidad Temporal:** **$\mathcal{O}(N)$**. La tabla `DP` tiene exactamente $N + 2$ estados (desde $0$ hasta $N + 1$). Para cada estado $i$, se calcula el mínimo entre a lo sumo $3$ posiciones anteriores (`i-1`, `i-2`, `i-3`), lo cual requiere únicamente $2$ comparaciones en tiempo constante $\mathcal{O}(1)$. La reconstrucción del camino recorre hacia atrás a lo sumo $N$ estaciones en $\mathcal{O}(N)$. Por lo tanto, el tiempo total es lineal $\mathcal{O}(N)$.
* **Complejidad Espacial:** **$\mathcal{O}(N)$** para almacenar los arreglos `DP` y `padre` de longitud $N + 2$ que permiten reconstruir las paradas elegidas (si solo se pidiera el valor numérico del costo mínimo sin reconstruir las estaciones, bastaría con mantener las últimas $3$ variables en espacio $\mathcal{O}(1)$).

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Devolver $DP[N]$ en lugar de $DP[N+1]$:</strong> El transporte no está obligado a detenerse en la estación $N$; si paró en $N-1$ o en $N-2$, puede saltear la estación $N$ y llegar directamente al destino final $N+1$. Olvidar el nodo destino $N+1$ (con $T[N+1]=0$) obliga erróneamente a pagar siempre la última estación.</li>
    <li><strong>Confundir "saltear 2 estaciones" con restar $2$ al índice:</strong> Si estás en la estación $i$ y salteaste las 2 estaciones anteriores ($i-1$ e $i-2$), tu parada previa fue $i-3$, no $i-2$.</li>
  </ul>
</div>

---

### Errores Frecuentes en Exámenes sobre Programación Dinámica

1. **No definir formalmente qué significa $OPT(\dots)$:** Escribir directamente una matriz sin explicar qué representan las filas y columnas anula la justificación.
2. **Olvidar los casos base:** No definir $OPT(0, w)$ o inicializar en $0$ cuando un valor inaccesible debería ser $-\infty$.
3. **No justificar el orden de llenado:** Asumir que se llena mágicamente sin decir que las filas se procesan de $0$ a $n$ y las capacidades de $0$ a $W$.
4. **Omitir la reconstrucción:** Quedarse con el número final $DP[n][W]$ cuando el problema pide "cuáles son los elementos".
"""
