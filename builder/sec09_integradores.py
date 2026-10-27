"""Módulo 9: Ejercicios Integradores Multi-Paradigma."""

def get_content():
    return r"""## 11. Ejercicios Integradores Multi-Paradigma

En los parciales más exigentes, la cátedra suele plantear un mismo escenario del mundo real y exigir resolverlo o compararlo a través de múltiples paradigmas distintos (Greedy vs Programación Dinámica vs Programación Lineal vs Redes de Flujo). Esta sección entrena la capacidad de conectar y contrastar estos enfoques.

---

### Ejercicio 32 — El Dilema del Transporte en Etapas: Greedy vs Programación Dinámica vs Programación Lineal

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Integrador Parcial 2025-1-2 (Ejercicios 2, 3 y 5 combinados)

**Enunciado Integrador**  
El INVAP debe transportar una carga de alta seguridad desde Ezeiza hasta Bariloche a través de un grafo de etapas donde las ciudades intermedias están agrupadas en días de viaje (máximo $400\text{ km/día}$, sin viajar de noche). Para cada tramo dirigido $(u, v)$ entre paradas consecutivas se conoce el costo de seguro $C_{uv} > 0$.  
1. **Paradigma Greedy:** Formular un algoritmo voraz. Demostrar formalmente mediante un contraejemplo por qué **no garantiza** la solución óptima.  
2. **Paradigma Programación Dinámica:** Desarrollar la solución óptima definiendo el estado $OPT(v)$, la ecuación de recurrencia, el algoritmo en pseudocódigo y la complejidad temporal.  
3. **Paradigma Programación Lineal:** Formular un modelo de PL que encuentre la ruta de mínimo costo indicando variables, función objetivo, restricciones y recuento exacto de las mismas.

---

#### 1. Resolución por Algoritmo Greedy y Contraejemplo de No-Optimalidad
* **Regla Voraz:** Desde la ciudad actual $u$, avanzar hacia la ciudad siguiente $v$ que tenga el menor costo de seguro inmediato $C_{uv}$.
* **Contraejemplo Minimal:**
  * Origen $E$ (Ezeiza). Opciones etapa 1: Ciudad $A$ (costo $10$), Ciudad $B$ (costo $20$).
  * Desde $A$ al destino Bariloche: costo $100$.
  * Desde $B$ al destino Bariloche: costo $5$.
  * *Resultado Greedy:* Elige $E \to A$ (costo $10$), luego $A \to \text{Bariloche}$ (costo $100$). $\text{Costo Total} = 110$.
  * *Ruta Óptima:* $E \to B \to \text{Bariloche}$. $\text{Costo Total} = 20 + 5 = 25$.
  * Como $110 > 25$, **Greedy falla**.

```mermaid
flowchart LR
    E(["Ezeiza (Origen)"]) -->|"C = 10 (Elige Greedy)"| A["Ciudad A (Etapa 1)"]:::bad
    E -->|"C = 20 (Ruta Óptima)"| B["Ciudad B (Etapa 1)"]:::opt
    A -->|"C = 100 (Trampa: Total 110)"| T(["Bariloche (Destino)"])
    B -->|"C = 5 (Óptimo: Total 25)"| T
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    classDef bad fill:#991b1b,stroke:#7f1d1d,stroke-width:2px,color:#fff
```

---

#### 2. Resolución Óptima por Programación Dinámica
* Como el grafo es por etapas (viajes de día sin ciclos), es un **DAG (Grafo Dirigido Acíclico)**.
* **Definición del Estado:**  
  $$OPT(v) = \text{Mínimo costo de seguro acumulado para llegar desde Ezeiza hasta la ciudad } v.$$
* **Casos Base:**  
  $$OPT(\text{Ezeiza}) = 0, \qquad OPT(v) = +\infty \quad \forall v \neq \text{Ezeiza}$$
* **Ecuación de Recurrencia:**  
  Para cualquier ciudad $v \in V \setminus \{\text{Ezeiza}\}$:
  $$OPT(v) = \min_{u \in \text{Predecesores}(v)} \Big\{ OPT(u) + C_{uv} \Big\}$$
* **Orden de Llenado:** Orden topológico de los vértices (etapa por etapa, del día $1$ al día final).

**Pseudocódigo de Programación Dinámica**

```text
FUNCION InvapCaminoOptimoPD(grafo_etapas, ezeiza, bariloche):
    INICIALIZAR DP como diccionario con INFINITO para todo nodo
    INICIALIZAR predecesor como diccionario con NULO para todo nodo
    DP[ezeiza] <- 0

    // Procesamos los nodos etapa por etapa (orden topológico)
    PARA CADA etapa k <- 1 HASTA TotalEtapas:
        PARA CADA v EN NodosDeEtapa(k):
            PARA CADA (u, costo) EN AristasHacia(grafo_etapas, v):
                SI DP[u] + costo < DP[v]:
                    DP[v] <- DP[u] + costo
                    predecesor[v] <- u

    // Reconstrucción del camino óptimo
    INICIALIZAR ruta como lista vacía
    actual <- bariloche
    MIENTRAS actual != NULO:
        INSERTAR actual AL INICIO DE ruta
        actual <- predecesor[actual]

    RETORNAR (DP[bariloche], ruta)
```

* **Complejidad:** Cada arista se recorre una sola vez al procesar su nodo destino. Tiempo: $\Theta(|V| + |E|)$. Espacio: $\Theta(|V|)$.

---

#### 3. Resolución por Programación Lineal
* **Variables:** $x_{uv} \ge 0$ (o $x_{uv} \in \{0, 1\}$; por Unimodularidad Total de la matriz de incidencia nodo-arco, la relajación continua produce soluciones enteras en $\{0, 1\}$) para cada arista dirigida $(u, v) \in E$.
* **Función Objetivo:**
  $$\min Z = \sum_{(u, v) \in E} C_{uv} \cdot x_{uv}$$
* **Restricciones de Conservación de Flujo Unitario:**  
  $$\sum_{w: (v, w) \in E} x_{vw} - \sum_{u: (u, v) \in E} x_{uv} = \begin{cases} +1 & \text{si } v = \text{Ezeiza} \\ -1 & \text{si } v = \text{Bariloche} \\ 0 & \forall v \in V \setminus \{\text{Ezeiza}, \text{Bariloche}\} \end{cases}$$
* **Conteo:** $|E|$ variables de decisión y $|V|$ restricciones lineales de balance.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>En PD, no mencionar el orden topológico por etapas:</strong> La recurrencia $OPT(v) = \min(OPT(u) + C_{uv})$ solo es válida sin ciclos (DAG). En un grafo con ciclos requeriría Dijkstra o Bellman-Ford.</li>
    <li><strong>En PL, olvidar las restricciones de conservación en los nodos intermedios:</strong> Sin el balance $\sum_{\text{salen}} - \sum_{\text{entran}} = 0$ en cada ciudad intermedia, el solver dejaría el camino desconectado.</li>
  </ul>
</div>

---

### Ejercicio 33 — Asignación de Recursos con Restricción de Capacidad: Redes de Flujo vs PLI

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Integrador Sistemas de Distribución / Asignación

**Enunciado Integrador**  
Una empresa dispone de $N$ servidores y $M$ tareas. Cada tarea $j$ requiere una cantidad de memoria $R_j$, y cada servidor $i$ tiene una capacidad máxima $C_i$. Se sabe qué tareas pueden ejecutarse en qué servidores.  
1. Si todas las tareas tienen requerimiento unitario ($R_j = 1$), ¿qué paradigma conviene usar para maximizar tareas asignadas? Modelarlo.  
2. Si las tareas tienen requerimientos heterogéneos ($R_j$ arbitrarios), ¿por qué Redes de Flujo estándar ya no puede modelar el problema directamente y se debe recurrir a Programación Lineal Entera?

**Resolución y Comparativa de Paradigmas**

#### 1. Caso Unitario ($R_j = 1$): Redes de Flujo
* Al ser las tareas de tamaño $1$, el problema se modela directamente con **Redes de Flujo**:
  * Super-fuente $s \to \text{Tarea } j$ con capacidad $1$.
  * $\text{Tarea } j \to \text{Servidor } i$ con capacidad $1$ (si es compatible).
  * $\text{Servidor } i \to \text{Super-sumidero } t$ con capacidad $C_i$.
* Se resuelve en tiempo polinomial estricto con Edmonds-Karp en $O(|V| \cdot |E|^2)$. El **Teorema de Integralidad** asegura que las tareas se asignan enteras sin fraccionamiento.

#### 2. Caso Heterogéneo ($R_j$ arbitrarios): Imposibilidad de Flujo y Formulación en PLI
* **Por qué falla Redes de Flujo:** En una red de flujo estándar, si mandamos $R_j$ unidades de flujo a través de una arista desde $s$ hacia la tarea $j$, el nodo de la tarea podría **bifurcar el flujo** entre dos servidores distintos (ej: enviar $3\text{ GB}$ al Servidor 1 y $2\text{ GB}$ al Servidor 2 para completar una tarea indivisible de $5\text{ GB}$). El flujo continuo conserva la suma, pero no puede imponer la condición de indivisibilidad (*all-or-nothing*) hacia un único servidor.
* **Modelo en Programación Lineal Entera (PLI):**
  * **Variables:** $x_{ji} \in \{0, 1\}$ ($1$ si la tarea $j$ se asigna íntegramente al servidor $i$, $0$ si no) para cada par compatible $(j, i)$.
  * **Función Objetivo:**
    $$\max Z = \sum_{j=1}^M \sum_{i=1}^N x_{ji}$$
  * **Restricciones:**
    * Unicidad de servidor por tarea: $\sum_{i=1}^N x_{ji} \le 1 \quad \forall j \in \{1, \dots, M\}$.
    * Capacidad de memoria por servidor: $\sum_{j=1}^M R_j \cdot x_{ji} \le C_i \quad \forall i \in \{1, \dots, N\}$.
    * Compatibilidad: $x_{ji} = 0$ si la tarea $j$ no es compatible con el servidor $i$.

```mermaid
flowchart TD
    Q(["Asignar M Tareas (demanda R_j) a N Servidores (capacidad C_i)"]) --> COND{"¿Cómo son las demandas R_j?"}
    COND -->|"Unitarias: R_j = 1 ∀j"| FL["🔴 REDES DE FLUJO (Edmonds-Karp)<br/>Polinomial O(V·E²) por Teorema de Integralidad"]:::fl
    COND -->|"Heterogéneas indivisibles: R_j > 1"| PLI["🔵 PROGRAMACIÓN LINEAL ENTERA (PLI)<br/>NP-Hard (Multiple Knapsack): Variables binarias x_{ji} ∈ {0, 1}"]:::pli
    classDef fl fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    classDef pli fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#fff
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Poner aristas de capacidad $R_j$ en Redes de Flujo para tareas indivisibles:</strong> Es un error clásico de parcial. Poner capacidad $R_j$ entre la tarea $j$ y cada servidor compatible permite que la tarea se parta en pedazos entre varios servidores.</li>
  </ul>
</div>

---

### Ejercicio 34 — Cobertura de Nodos en Redes: Vertex Cover por Backtracking, PLI y Aproximación 2

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Integrador Problemas NP-Hard (Vertex Cover)

**Enunciado Integrador**  
Para el problema de Vertex Cover Mínimo en un grafo $G = (V, E)$, comparar tres estrategias de abordaje:  
1. **Solución Exacta Combinatoria:** Backtracking con Branch and Bound.  
2. **Solución Exacta Matemática:** Formulación en Programación Lineal Entera.  
3. **Solución Heurística Polinomial:** Algoritmo de Aproximación con factor $2$ (basado en *Maximal Matching*).

**Comparativa Técnica Exhaustiva**

| Dimensión | 1. Backtracking con B&B | 2. Programación Lineal Entera (PLI) | 3. Algoritmo Aproximado (2-Aprox) |
| :--- | :--- | :--- | :--- |
| **Garantía de Solución** | Óptima exacta | Óptima exacta | Aproximada: $|C| \le 2 \cdot OPT$ |
| **Complejidad Temporal** | $O(2^k \cdot |E|)$ (peor caso exponencial) | Exponencial en el peor caso (*Branch & Cut*) | **$O(|V| + |E|)$** (lineal) |
| **Escalabilidad** | Eficiente solo para $k$ pequeño ($k \le 40$) | Eficiente para grafos medianos ($|V| \le 500$) | **Escala a millones de nodos y aristas** |
| **Formulación Central** | Ramificación en aristas no cubiertas: $u \in C$ o $v \in C$ con podas de tamaño. | $\min \sum x_v$ s.a. $x_u + x_v \ge 1, \; \forall (u, v) \in E$, con $x_v \in \{0, 1\}$. | Iterar sobre aristas: tomar **ambos extremos** de aristas disjuntas hasta cubrir el grafo. |

```mermaid
flowchart LR
    subgraph MatchingM [Emparejamiento Disjunto M]
        u1((u1)) ===|"e1 ∈ M"| v1((v1))
        u2((u2)) ===|"e2 ∈ M"| v2((v2))
    end
    MatchingM -->|"OPT debe usar ≥ 1 nodo por cada arista de M"| Cota1["Cota Inferior: OPT ≥ |M|"]:::opt
    MatchingM -->|"Algoritmo toma ambos extremos (u y v)"| Cota2["Solución C: |C| = 2·|M| ≤ 2·OPT"]:::approx
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    classDef approx fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#fff
```

**Pseudocódigo del Algoritmo 2-Aproximado para Vertex Cover**

```text
FUNCION VertexCoverAproximado2(G):
    INICIALIZAR C como conjunto vacío
    INICIALIZAR aristas_disjuntas como conjunto vacío

    // Recorremos todas las aristas
    PARA CADA (u, v) EN E(G):
        // Si la arista no está cubierta por los nodos ya elegidos
        SI u NO PERTENECE A C Y v NO PERTENECE A C:
            AGREGAR u A C
            AGREGAR v A C
            AGREGAR (u, v) A aristas_disjuntas

    RETORNAR C
```

**Demostración Directa de la Garantía de Aproximación 2:**  
1. Las aristas que fue eligiendo el algoritmo no se tocan entre sí (ninguna comparte vértices con otra). Si el algoritmo eligió `|M|` aristas disjuntas, **cualquier solución óptima tiene que elegir sí o sí al menos 1 vértice distinto por cada una de esas aristas** para poder cubrirlas (`OPT >= |M|`).
2. Como nuestro algoritmo agrega **los 2 extremos** de cada arista elegida, en total agarra `|C| = 2 * |M|` vértices.
3. Por lo tanto, `|C| = 2 * |M| <= 2 * OPT`: nunca usa más del doble de vértices que el óptimo y tarda `O(V + E)`.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Elegir solo 1 extremo en lugar de ambos en el 2-Aproximado:</strong> Si al tomar una arista $(u, v)$ agregas solo $u$ (o el de mayor grado), el algoritmo pierde la garantía de factor 2 (el greedy por mayor grado tiene factor $O(\log |V|)$, no 2). Es obligatorio agregar <strong>ambos extremos</strong> $u$ y $v$.</li>
  </ul>
</div>

---

### Ejercicio 35 — El Problema Canónico de la Mochila (Knapsack) Resuelto en Todos los Paradigmas Algorítmicos

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Problema Arquetípico Canónico de TDA / Evaluación Integral Multi-Paradigma

**Enunciado Integrador**  
Se dispone de una mochila con capacidad entera máxima de peso $W > 0$ y un conjunto de $n$ elementos disponibles, donde cada elemento $i \in \{1, \dots, n\}$ posee un peso entero $w_i > 0$ y un valor o beneficio entero $v_i > 0$.  
Resolver y contrastar el problema a través de todos los paradigmas algorítmicos fundamentales evaluados en la materia:
1. **Paradigma Greedy (Algoritmo Voraz):**
   * Resolver la **Mochila Fraccionaria (Continuous Knapsack)**: regla voraz por densidad de valor, pseudocódigo y demostración formal de optimalidad por técnica de intercambio.
   * Analizar la **Mochila 0-1 (Indivisible)**: contraejemplo formal de por qué la regla voraz falla arbitrariamente y desarrollo del **Algoritmo 1/2-Aproximado** con su demostración de cota garantizada.
2. **Paradigma Programación Dinámica (DP):**
   * Resolver la **Mochila 0-1 Estándar**: definición formal del subproblema $OPT(i, w)$, casos base, ecuación de recurrencia, pseudocódigo bottom-up con tabla $(n+1) \times (W+1)$, algoritmo de reconstrucción exacta de ítems y optimización de memoria espacial a $O(W)$. Demostración de su complejidad pseudo-polinomial frente al número de bits de la entrada.
   * Resolver la **Mochila No Acotada (Unbounded Knapsack)** con disponibilidad infinita de cada ítem en $O(n \cdot W)$ tiempo y $O(W)$ espacio.
3. **Paradigma Backtracking y Branch & Bound:**
   * Diseñar el árbol binario de decisiones, podas por factibilidad y podas por optimalidad con cota superior (*Branch and Bound*) mediante la relajación continua fraccionaria. Explicar cuándo este enfoque supera a la Programación Dinámica en la práctica.
4. **Paradigma Programación Lineal Entera (PLI):**
   * Modelar formalmente el problema indicando variables de decisión binarias, función objetivo, restricciones, conteo de variables/restricciones y su relación directa con la relajación lineal continua (*LP Relaxation*).
5. **Análisis de División y Conquista (DyC):**
   * Explicar teóricamente por qué División y Conquista puro fracasa o no es aplicable a la mochila 0-1 (subproblemas no disjuntos).
6. **Tabla Comparativa Maestra:**
   * Matriz comparativa multidimensional de complejidades, optimalidad y escenarios de examen.

---

#### Mapa Visual de Decisión para el Problema de la Mochila

```mermaid
flowchart TD
    K(["🎒 PROBLEMA DE LA MOCHILA (n ítems, capacidad W)"]) --> FRAC{"¿Los objetos se pueden fraccionar?"}
    FRAC -->|"SÍ (x_i ∈ [0, 1])"| GR_OPT["🔶 GREEDY FRACCIONARIO<br/>Ordenar por v_i / w_i decreciente<br/>✅ Óptimo en Θ(n log n)"]:::gr
    FRAC -->|"NO (Indivisibles 0-1)"| TIPO{"¿Se exige solución exacta o aproximación rápida?"}
    TIPO -->|"Aproximación Polinomial"| GR_APX["🔶 GREEDY 1/2-APROXIMADO<br/>max(V_greedy, v_crítico)<br/>⚡ Tiempo Θ(n log n) | Cota ≥ 1/2 OPT"]:::gr
    TIPO -->|"Exacta Óptima"| CAP{"¿Magnitud de W vs n?"}
    CAP -->|"W moderado (W ≤ 10⁶)"| DP_01["🟢 PROGRAMACIÓN DINÁMICA<br/>Tabla (n+1)×(W+1): OPT(i, w)<br/>✅ Exacto en Θ(n·W) pseudo-polinomial"]:::dp
    CAP -->|"W astronómico (W > 10⁹), n ≤ 40"| BB_01["🟣 BACKTRACKING + BRANCH & BOUND<br/>Cota superior con Relajación Fraccionaria<br/>✅ Exacto en O(2ⁿ) con podas masivas"]:::bt
    CAP -->|"Múltiples restricciones acopladas"| PLI_01["🔵 PROGRAMACIÓN LINEAL ENTERA<br/>Variables x_i ∈ {0, 1}, Σ w_i x_i ≤ W<br/>✅ Solver Branch & Cut"]:::pl

    classDef gr fill:#d97706,stroke:#b45309,stroke-width:2px,color:#fff
    classDef dp fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    classDef bt fill:#7c3aed,stroke:#6d28d9,stroke-width:2px,color:#fff
    classDef pl fill:#2563eb,stroke:#1d4ed8,stroke-width:2px,color:#fff
```

---

#### 1. Paradigma Greedy (Algoritmos Voraces)

##### A. Mochila Fraccionaria (Continuous Knapsack) — Solución Óptima en O(n log n)
En la versión fraccionaria se permite tomar una fracción $x_i \in [0, 1]$ de cada elemento $i$. El beneficio aportado es $x_i \cdot v_i$ y el peso consumido es $x_i \cdot w_i$.

* **Regla Voraz:** Ordenar los elementos de forma decreciente según su **densidad de valor por unidad de peso**:
  $$r_i = \frac{v_i}{w_i} \quad \text{tal que } r_1 \ge r_2 \ge \dots \ge r_n$$
* **Estrategia:** Tomar la mayor cantidad posible del elemento con mayor densidad disponible. Si el elemento cabe entero ($w_i \le \text{capacidad remanente}$), se toma completo ($x_i = 1$). Si no cabe entero, se toma exactamente la fracción que satura la mochila ($x_i = \frac{\text{capacidad remanente}}{w_i}$) y se finaliza el proceso.

**Pseudocódigo de la Mochila Fraccionaria**

```text
FUNCION MochilaFraccionariaGreedy(pesos, valores, n, W):
    // 1. Calcular densidades y ordenar en O(n log n)
    INICIALIZAR items como lista de tuplas (id=i, peso=pesos[i], valor=valores[i], ratio=valores[i]/pesos[i])
    ORDENAR items DECRECIENTE por campo ratio

    cap_restante <- W
    valor_total <- 0.0
    INICIALIZAR fraccion como arreglo de tamaño n en 0.0

    // 2. Selección voraz
    PARA i <- 0 HASTA n - 1:
        SI cap_restante = 0:
            ROMPER

        item_actual <- items[i]
        id <- item_actual.id

        SI item_actual.peso <= cap_restante:
            fraccion[id] <- 1.0
            valor_total <- valor_total + item_actual.valor
            cap_restante <- cap_restante - item_actual.peso
        SINO:
            // Tomamos la fracción que satura exactamente la mochila
            f <- cap_restante / item_actual.peso
            fraccion[id] <- f
            valor_total <- valor_total + f * item_actual.valor
            cap_restante <- 0

    RETORNAR (valor_total, fraccion)
```

**Demostración Directa de Optimalidad (Argumento de Intercambio):**
1. Supongamos que una solución óptima dejó afuera parte de un objeto $k$ que nuestro Greedy sí metió, y en su lugar llenó ese peso $\Delta w$ con pedazos de otros objetos $j$ que estaban más atrás en la lista.
2. Como la lista está ordenada por valor por kilo decreciente, el objeto $k$ rinde más (o igual) por cada kilo que cualquier objeto $j$ posterior ($r_k \ge r_j$).
3. Si en la solución óptima sacamos $\Delta w$ kilos del objeto $j$ y los cambiamos por $\Delta w$ kilos del objeto $k$, el peso total no cambia y el valor total sube o se mantiene igual.
4. Repitiendo este cambio, cualquier solución óptima se transforma en la solución de Greedy sin perder valor. Por lo tanto, **Greedy es óptimo**.
* **Complejidad:** Tiempo $O(n \log n)$ por el ordenamiento inicial; Espacio $O(n)$.

---

##### B. Mochila 0-1: Por qué Greedy Falla y Algoritmo 1/2-Aproximado
En la mochila 0-1 los objetos son indivisibles ($x_i \in \{0, 1\}$).

* **Contraejemplo Minimal de No-Optimalidad para Greedy por Densidad:**
  * Capacidad $W = 100$.
  * Ítem 1: peso $w_1 = 1$, valor $v_1 = 2 \implies r_1 = 2.0$.
  * Ítem 2: peso $w_2 = 100$, valor $v_2 = 100 \implies r_2 = 1.0$.
  * *Resultado Greedy:* Toma el ítem 1 (densidad $2.0$). Capacidad restante: $99$. El ítem 2 no cabe. **Valor Greedy = 2**.
  * *Solución Óptima:* Tomar únicamente el ítem 2. Peso $= 100 \le 100$. **Valor Óptimo = 100**.
  * La solución voraz logra un valor arbitrariamente alejado del óptimo (el ratio puede tender a $0$ si $v_2 \to \infty$).

* **Algoritmo Greedy 1/2-Aproximado para Mochila 0-1:**
  1. Ejecutar la regla voraz por densidad tomando ítems completos hasta el primer ítem $k$ que no quepa entero (ítem de corte). Sea $V_{\text{greedy}}$ el valor de los ítems tomados.
  2. Hallar el ítem individual más valioso que quepa en la mochila: $v_{\max} = \max \{ v_i : w_i \le W \}$.
  3. Retornar la mejor de las dos opciones:
     $$V_{\text{aprox}} = \max(V_{\text{greedy}}, \; v_{\max})$$

**Demostración Directa de la Garantía 1/2:**
1. La mochila fraccionaria siempre gana o empata contra la mochila 0-1 óptima (`OPT_01 <= V_frac`).
2. La mochila fraccionaria mete todos los objetos enteros que metió Greedy (`V_greedy`) más una fracción del primer objeto `k` que ya no entró entero (cuyo valor `v_k` es a lo sumo `v_max`).
3. Por lo tanto, el óptimo entero es menor que la suma de esas dos cosas: `OPT_01 < V_greedy + v_max`.
4. Como nuestro algoritmo se queda con el mayor entre `V_greedy` y `v_max`, ese mayor vale **al menos la mitad de la suma de ambos**, garantizando al menos el **50% del óptimo** (`V_aprox >= OPT_01 / 2`) en tiempo `O(n log n)`.

---

#### 2. Paradigma Programación Dinámica (Dynamic Programming)

##### A. Mochila 0-1 Estándar — Solución Óptima Exacta

* **Definición del Subproblema:**
  > **$OPT(i, w)$:** Beneficio máximo acumulable eligiendo un subconjunto de los primeros $i$ elementos ($1 \le i \le n$) tal que la suma de sus pesos no exceda la capacidad disponible $w$ ($0 \le w \le W$).
* **Casos Base:**
  * $OPT(0, w) = 0$ para todo $w \in [0, W]$ (sin elementos disponibles, beneficio 0).
  * $OPT(i, 0) = 0$ para todo $i \in [0, n]$ (con capacidad 0, no se puede cargar peso positivo).
* **Ecuación de Recurrencia:**
  Para el elemento $i$ con peso $w_i$ y valor $v_i$:
  1. Si $w_i > w$: el elemento $i$ no cabe con la capacidad actual.
     $$OPT(i, w) = OPT(i - 1, w)$$
  2. Si $w_i \le w$: se elige el máximo entre excluir el elemento o incluirlo:
     $$OPT(i, w) = \max \Big( OPT(i - 1, w), \; OPT(i - 1, w - w_i) + v_i \Big)$$
* **Orden de Llenado:** Celdas calculadas fila por fila ($i$ de $1$ a $n$), y para cada fila capacidad $w$ de $0$ a $W$.

**Pseudocódigo de Programación Dinámica con Reconstrucción**

```text
FUNCION Mochila01ProgramacionDinamica(pesos, valores, n, W):
    // Crear matriz de dimensiones (n + 1) x (W + 1) inicializada en 0
    INICIALIZAR DP como matriz de tamaño (n + 1) x (W + 1) en 0

    // Llenado de la tabla Bottom-Up
    PARA i <- 1 HASTA n:
        w_i <- pesos[i - 1]
        v_i <- valores[i - 1]
        PARA w <- 0 HASTA W:
            SI w_i > w:
                DP[i][w] <- DP[i - 1][w]
            SINO:
                excluir <- DP[i - 1][w]
                incluir <- DP[i - 1][w - w_i] + v_i
                SI incluir > excluir:
                    DP[i][w] <- incluir
                SINO:
                    DP[i][w] <- excluir

    // Reconstrucción exacta de los ítems elegidos
    INICIALIZAR seleccionados como lista vacía
    cap_actual <- W
    PARA i <- n BAJANDO HASTA 1:
        // Si el valor cambió respecto a la fila anterior, el elemento i fue incluido
        SI DP[i][cap_actual] != DP[i - 1][cap_actual]:
            INSERTAR (i - 1) AL INICIO DE seleccionados
            cap_actual <- cap_actual - pesos[i - 1]

    RETORNAR (DP[n][W], seleccionados)
```

**Optimización de Memoria Espacial a O(W):**
Como la fila $i$ solo depende estrictamente de la fila inmediata anterior $i - 1$, podemos utilizar un **único vector 1D** de tamaño $W + 1$.  
*Condición crítica de examen:* La capacidad $w$ debe recorrerse en **orden decreciente (de $W$ bajando hasta $w_i$)** para evitar que el mismo ítem se contabilice múltiples veces en la misma fila:

```text
FUNCION Mochila01EspacioOptimizado(pesos, valores, n, W):
    INICIALIZAR DP como arreglo de tamaño (W + 1) en 0
    PARA i <- 0 HASTA n - 1:
        w_i <- pesos[i]
        v_i <- valores[i]
        PARA w <- W BAJANDO HASTA w_i:
            DP[w] <- MAXIMO(DP[w], DP[w - w_i] + v_i)
    RETORNAR DP[W]
```

* **Complejidad:**
  * **Tiempo:** $O(n \cdot W)$ operaciones aritméticas elementales.
  * **Espacio:** $O(n \cdot W)$ con matriz para reconstrucción, o $O(W)$ con vector unidimensional.
  * **Análisis de Pseudo-Polinomialidad:** La longitud de la entrada en bits para representar el número $W$ es $L = \lceil \log_2 W \rceil$. Por ende, $W = 2^L$. La complejidad en función del tamaño de entrada es $O(n \cdot 2^L)$, lo cual es **exponencial en el tamaño de representación de $W$**. Si $W$ es astronómico ($W = 10^{12}$), DP es impracticable por tiempo y memoria.

---

##### B. Mochila No Acotada (Unbounded Knapsack) — Repetición Ilimitada
Si se dispone de cantidad ilimitada de cada ítem, el estado depende únicamente de la capacidad $w$:
* **Subproblema:** $OPT(w) =$ beneficio máximo que se puede obtener con capacidad exacta $w$.
* **Recurrencia:**
  $$OPT(w) = \max_{i: w_i \le w} \{ OPT(w - w_i) + v_i \}, \quad \text{con } OPT(0) = 0$$
* En este caso, el recorrido del vector 1D se realiza **de izquierda a derecha (creciente de $w_i$ a $W$)**, permitiendo explícitamente reutilizar el mismo ítem múltiples veces. Tiempo: $O(n \cdot W)$, Espacio: $O(W)$.

---

#### 3. Paradigma Backtracking y Branch & Bound (Búsqueda Exacta con Podas)

Cuando $W$ es gigantesco pero $n$ es moderado ($n \le 40$), la Programación Dinámica colapsa por memoria pero **Backtracking con Branch & Bound** resuelve en milisegundos.

* **Estructura del Árbol de Búsqueda:**
  Árbol binario de profundidad $n$. En el nivel $i$, decidimos si incluimos o no el elemento $i$ ($x_i \in \{0, 1\}$).
* **Las Dos Clases de Podas Obligatorias en Parcial:**
  1. **Poda por Factibilidad (Feasibility):**
     Si $\text{peso actual} + w_i > W$, podar la rama de inclusión de $i$.
  2. **Poda por Optimalidad (Branch and Bound con Relajación Continua Fraccionaria):**
     Para el estado actual en el elemento $i$, calculamos una **cota superior (Upper Bound)** del máximo valor que podría obtenerse en el subárbol:
     $$\text{CotaSuperior} = \text{valor actual} + \text{MochilaFraccionaria}(\text{elementos restantes desde } i+1, \; W - \text{peso actual})$$
     Si $\text{CotaSuperior} \le \text{mejor valor global}$, es matemáticamente imposible que este subárbol supere el récord actual ya hallado $\implies$ **podar inmediatamente toda la rama**.

**Pseudocódigo de Backtracking con Branch & Bound**

```text
FUNCION MochilaBranchAndBound(pesos, valores, n, W):
    // Preordenar elementos por densidad decreciente maximiza la efectividad de las podas
    ORDENAR elementos DECRECIENTE por (valor / peso)
    
    mejor_valor <- 0
    INICIALIZAR mejor_solucion como arreglo de tamaño n en 0
    INICIALIZAR solucion_actual como arreglo de tamaño n en 0

    MochilaBT(0, 0, 0, solucion_actual, mejor_solucion, mejor_valor, pesos, valores, n, W)
    RETORNAR (mejor_valor, mejor_solucion)

PROCEDIMIENTO MochilaBT(idx, peso_act, valor_act, sol_act, MEJOR_SOL, MEJOR_VAL, pesos, valores, n, W):
    // Caso base: se evaluaron los n elementos
    SI idx = n:
        SI valor_act > MEJOR_VAL:
            MEJOR_VAL <- valor_act
            MEJOR_SOL <- COPIAR(sol_act)
        RETORNAR

    // 1. Poda por Branch and Bound: Cota superior con relajación fraccionaria
    cota_sup <- valor_act + CalcularCotaFraccionaria(idx, W - peso_act, pesos, valores, n)
    SI cota_sup <= MEJOR_VAL:
        RETORNAR // Poda: imposible mejorar la mejor solución registrada

    // Rama 1: Intentar INCLUIR el elemento idx (si cabe: poda por factibilidad)
    SI peso_act + pesos[idx] <= W:
        sol_act[idx] <- 1
        MochilaBT(idx + 1, peso_act + pesos[idx], valor_act + valores[idx], 
                  sol_act, MEJOR_SOL, MEJOR_VAL, pesos, valores, n, W)
        sol_act[idx] <- 0 // Backtrack: restaurar estado

    // Rama 2: EXCLUIR el elemento idx
    sol_act[idx] <- 0
    MochilaBT(idx + 1, peso_act, valor_act, 
              sol_act, MEJOR_SOL, MEJOR_VAL, pesos, valores, n, W)

FUNCION CalcularCotaFraccionaria(inicio, cap_disponible, pesos, valores, n):
    cota <- 0.0
    cap <- cap_disponible
    PARA j <- inicio HASTA n - 1:
        SI cap = 0:
            ROMPER
        SI pesos[j] <= cap:
            cota <- cota + valores[j]
            cap <- cap - pesos[j]
        SINO:
            cota <- cota + valores[j] * (cap / pesos[j])
            cap <- 0
    RETORNAR cota
```

* **Complejidad:** Peor caso asintótico $O(2^n)$ (árbol binario exhaustivo). En la práctica, con la cota fraccionaria y ordenamiento previo por densidad, las podas eliminan más del $99\%$ de las ramas para $n \le 50$. Memoria: $O(n)$ en la pila de recursión.

---

#### 4. Paradigma Programación Lineal Entera (PLI)

* **Variables de Decisión:**
  $$x_i \in \{0, 1\} \quad \forall i \in \{1, \dots, n\}$$
  donde $x_i = 1$ si el elemento $i$ se introduce en la mochila, y $0$ en caso contrario.
* **Función Objetivo:**
  $$\text{MAXIMIZAR } Z = \sum_{i=1}^n v_i \cdot x_i$$
* **Restricción de Capacidad:**
  $$\sum_{i=1}^n w_i \cdot x_i \le W$$
* **Restricciones de Dominio:**
  $$x_i \in \{0, 1\} \quad \forall i \in \{1, \dots, n\}$$
* **Recuento Riguroso para Examen:**
  * **Variables:** Exactamente $n$ variables binarias.
  * **Restricciones:** Exactamente 1 restricción lineal de capacidad $+ n$ cotas de dominio binario.
* **Vínculo con la Relajación Lineal (LP Relaxation):**
  Si reemplazamos $x_i \in \{0, 1\}$ por $0 \le x_i \le 1$ (variables continuas), el problema de PL continuo resultante se resuelve en tiempo polinomial y **su solución óptima es idéntica a la Mochila Fraccionaria Greedy**.

---

#### 5. Por qué Falla División y Conquista (DyC) Puro en la Mochila

* En **División y Conquista** (como MergeSort o multiplicación de Strassen), el problema se divide en subproblemas **disjuntos e independientes** cuyas soluciones se combinan sin solapamiento.
* En la Mochila 0-1, si partiéramos el conjunto de $n$ elementos en dos mitades de tamaño $n/2$, no sabemos a priori **cuánta capacidad $W_1$ y $W_2$ asignar a cada mitad** tal que $W_1 + W_2 = W$.
* Para encontrar la partición óptima de capacidad, habría que probar todos los posibles valores de $w \in [0, W]$, generando subproblemas repetidos de forma masiva. Intentar resolverlo recursivamente sin memorización conduce a un árbol de llamadas de costo $O(2^n)$.
* La presencia de **subestructura óptima con superposición masiva de subproblemas** es precisamente la condición teórica que invalida DyC e impone **Programación Dinámica**.

---

#### 6. Tabla Comparativa Maestra: La Mochila en los 5 Paradigmas

| Paradigma | Variante | Complejidad Temporal | Complejidad Espacial | ¿Garantiza Óptimo? | Cuándo Usarlo en Parcial |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Greedy (Voraz)** | Fraccionaria | **$O(n \log n)$** | **$O(1) / O(n)$** | ✅ **SÍ (Óptimo)** | Cuando el enunciado permite fraccionar bienes (harina, combustible, tiempo). |
| **Greedy Aprox** | 0-1 (Indivisible) | **$O(n \log n)$** | **$O(n)$** | ❌ 1/2-Aprox ($V \ge \frac{1}{2}OPT$) | Cuando piden algoritmo rápido polinomial con garantía de calidad mínima. |
| **Prog. Dinámica** | 0-1 (Indivisible) | **$O(n \cdot W)$** | **$O(W) / O(n \cdot W)$** | ✅ **SÍ (Exacto)** | Cuando $W$ es razonable ($W \le 10^6$) y se exige el óptimo absoluto. |
| **Prog. Dinámica** | No Acotada | **$O(n \cdot W)$** | **$O(W)$** | ✅ **SÍ (Exacto)** | Cuando hay stock infinito de cada ítem (cambio de monedas, cortes de varilla). |
| **Backtracking (B&B)**| 0-1 (Indivisible) | **$O(2^n)$** peor caso | **$O(n)$** | ✅ **SÍ (Exacto)** | Cuando $W$ es astronómico ($W > 10^9$) pero $n$ es moderado ($n \le 40$). |
| **Prog. Lineal (PLI)**| 0-1 Multidimensional| Exponencial (peor caso) | Polinomial en modelo | ✅ **SÍ (Exacto)** | Cuando hay múltiples recursos acoplados (peso, volumen, costo, exclusiones). |
| **División y Conquista**| 0-1 | $O(2^n)$ (inviable) | $O(n)$ | ❌ Inadecuado | Demostrar en examen por qué subproblemas no disjuntos invalidan DyC. |

---

### Ejercicio 36 — El Problema del Viajante de Comercio (TSP) Resuelto en Todos los Paradigmas Algorítmicos

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Problema Arquetípico Canónico de Grafos y NP-Hard / Evaluación Integral Multi-Paradigma

**Enunciado Integrador**  
Dado un conjunto de $n$ ciudades numeradas $\{1, 2, \dots, n\}$ y una matriz de distancias o costos $C = [c_{ij}]$ no negativos entre cada par de ciudades, el **Problema del Viajante de Comercio (TSP - Travelling Salesperson Problem)** consiste en encontrar un circuito simple (tour cerrado) que visite **exactamente una vez cada ciudad y retorne a la ciudad de origen** minimizando la distancia total recorrida.  
Resolver y comparar este problema a través de todos los paradigmas algorítmicos fundamentales:
1. **Paradigma Backtracking y Branch & Bound (Búsqueda Exacta):**
   * Definir el árbol de permutaciones, podas por factibilidad, poda por cota superior actual y poda avanzada por **Cota Inferior basada en Árbol Generador Mínimo (MST / 1-Tree)**.
2. **Paradigma Programación Dinámica (Algoritmo de Bellman-Held-Karp):**
   * Identificar la subestructura óptima y superposición de estados. Definir formalmente el subproblema sobre subconjuntos de vértices $C(S, j)$, la ecuación de recurrencia, el algoritmo tabular y demostrar la reducción de complejidad factorial $O(n!)$ a exponencial $O(n^2 2^n)$.
3. **Paradigma Greedy y Heurísticas de Aproximación:**
   * Desarrollar la heurística voraz del **Vecino más Cercano (Nearest Neighbor)** y exhibir un contraejemplo demostrando por qué no es óptima.
   * Diseñar el **Algoritmo 2-Aproximado para TSP Métrico** (con desigualdad triangular) basado en Árbol Generador Mínimo y recorrido en preorden con atajos (*shortcuts*). Desarrollar la demostración formal paso a paso de la cota $\text{Costo}(\text{Tour}) \le 2 \cdot OPT$.
4. **Paradigma Programación Lineal Entera (PLI):**
   * Formular el modelo matemático exacto mediante la **formulación de Miller-Tucker-Zemlin (MTZ)** con variables de orden continuo $u_i$ para eliminar subtours desconectados. Recuento de variables y restricciones.
5. **Reducciones Polinomiales y Complejidad NP-Completa:**
   * Enunciar la versión de decisión de TSP. Demostrar formalmente que $\text{TSP} \in \text{NP}$ y que es NP-Completo mediante una reducción polinomial desde **Ciclo Hamiltoniano** ($\text{Ciclo Hamiltoniano} \le_P \text{TSP}$).
6. **Tabla Comparativa Maestra:**
   * Síntesis técnica de complejidades, optimalidad, garantías y casos de uso en parcial.

---

#### Mapa Visual de Abordaje para el Problema del Viajante (TSP)

```mermaid
flowchart TD
    TSP(["🚗 PROBLEMA DEL VIAJANTE (TSP en n ciudades)"]) --> OBJ{"¿Qué solicita la consigna del examen?"}
    OBJ -->|"Demostrar NP-Completitud"| RED["🟡 REDUCCIÓN DESDE CICLO HAMILTONIANO<br/>Grafo completo con pesos w=1 (arista en E) y w=2 (no en E), cota K=n"]:::npc
    OBJ -->|"Aproximación en tiempo polinomial (Métrico)"| APX["🔶 2-APROXIMACIÓN CON MST + PREORDEN<br/>Prim/Kruskal + DFS con atajos: Costo(T) ≤ 2·Costo(MST) ≤ 2·OPT en O(n²)"]:::gr
    OBJ -->|"Modelo Matemático PLI"| MTZ["🔵 PLI CON ELIMINACIÓN DE SUBTOURS (MTZ)<br/>Variables x_{ij} ∈ {0,1} + orden u_i: u_i - u_j + n·x_{ij} ≤ n-1"]:::pl
    OBJ -->|"Algoritmo Exacto"| EX{"¿Enfoque combinatorio o tabular?"}
    EX -->|"Subproblemas superpuestos (n ≤ 23)"| HK["🟢 PROGRAMACIÓN DINÁMICA (Held-Karp)<br/>Estado C(S, j): Reduce O(n!) a Θ(n²·2ⁿ)"]:::dp
    EX -->|"Árbol de búsqueda con podas"| BB["🟣 BACKTRACKING + BRANCH & BOUND<br/>Cota inferior con MST de no visitados en O(n!)"]:::bt

    classDef npc fill:#ca8a04,stroke:#a16207,stroke-width:2px,color:#fff
    classDef gr fill:#d97706,stroke:#b45309,stroke-width:2px,color:#fff
    classDef pl fill:#2563eb,stroke:#1d4ed8,stroke-width:2px,color:#fff
    classDef dp fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    classDef bt fill:#7c3aed,stroke:#6d28d9,stroke-width:2px,color:#fff
```

---

#### 1. Paradigma Backtracking y Branch & Bound (Exacto con Podas)

* **Espacio de Búsqueda:**
  Cualquier solución factible es una permutación de las $n$ ciudades que comienza y termina en la ciudad 1. Sin podas, el espacio tiene tamaño $(n - 1)! / 2$ (fijando el origen y evitando simetrías de sentido inverso).
* **Podas Esenciales en Parcial:**
  1. **Poda por Factibilidad:** Si entre la ciudad actual $u$ y la candidata $v$ no existe arista conectiva ($c_{uv} = \infty$), descartar $v$.
  2. **Poda por Cota Superior:** Mantener el mejor costo de tour cerrado completo hallado hasta el momento (`mejor_costo`). Si en el camino parcial actual:
     $$\text{costo parcial} \ge \text{mejor costo}$$
     podar inmediatamente la rama (ningún costo de arista es negativo).
  3. **Poda por Cota Inferior (Branch & Bound con MST / 1-Tree):**
     Para el conjunto de ciudades restantes aún no visitadas $V_{\text{restantes}}$, cualquier tour válido debe conectar estas ciudades formando al menos un árbol. Por ende:
     $$\text{CotaInferior} = \text{costo parcial} + \text{CostoMST}(V_{\text{restantes}}) + \min_{r \in V_{\text{restantes}}} c_{\text{actual}, r} + \min_{r \in V_{\text{restantes}}} c_{r, 1}$$
     Si $\text{CotaInferior} \ge \text{mejor costo} \implies$ podar toda la rama.

**Pseudocódigo de TSP por Backtracking con Branch and Bound**

```text
FUNCION TSP_BranchAndBound(ciudades, matriz_costos, n):
    INICIALIZAR visitado como arreglo booleano de tamaño n en FALSO
    INICIALIZAR ruta_actual como arreglo de tamaño n en 0
    INICIALIZAR mejor_ruta como arreglo de tamaño n en 0
    mejor_costo <- INFINITO

    // Fijamos la ciudad de partida en el nodo 0 para romper simetrías de rotación
    ruta_actual[0] <- 0
    visitado[0] <- VERDADERO

    TSP_BT(1, 0, 0, ruta_actual, mejor_ruta, mejor_costo, visitado, matriz_costos, n)
    RETORNAR (mejor_costo, mejor_ruta)

PROCEDIMIENTO TSP_BT(paso, actual, costo_acum, ruta_act, MEJOR_RUTA, MEJOR_COSTO, visitado, C, n):
    // Caso base: visitamos las n ciudades, cerramos el tour retornando al origen (nodo 0)
    SI paso = n:
        costo_cierre <- C[actual][0]
        SI costo_cierre != INFINITO:
            costo_total <- costo_acum + costo_cierre
            SI costo_total < MEJOR_COSTO:
                MEJOR_COSTO <- costo_total
                MEJOR_RUTA <- COPIAR(ruta_act)
        RETORNAR

    // Poda por cota superior básica
    SI costo_acum >= MEJOR_COSTO:
        RETORNAR

    // Probar cada ciudad candidata no visitada
    PARA candidata <- 1 HASTA n - 1:
        SI NO visitado[candidata] Y C[actual][candidata] != INFINITO:
            nuevo_costo <- costo_acum + C[actual][candidata]

            // Poda Branch & Bound: si con el costo directo ya superamos el récord
            SI nuevo_costo < MEJOR_COSTO:
                visitado[candidata] <- VERDADERO
                ruta_act[paso] <- candidata

                TSP_BT(paso + 1, candidata, nuevo_costo, ruta_act, MEJOR_RUTA, MEJOR_COSTO, visitado, C, n)

                // Backtrack: desmarcar estado
                visitado[candidata] <- FALSO
                ruta_act[paso] <- 0
```

* **Complejidad:** Peor caso asintótico $O(n!)$, pero con podas de cota inferior resuelve óptimamente instancias de hasta $n \approx 25$ ciudades. Espacio: $O(n)$ en pila de llamadas.

---

#### 2. Paradigma Programación Dinámica (Algoritmo de Bellman-Held-Karp)

* **Principio de Subestructura Óptima:**
  Para completar el tour desde la ciudad actual $j$, no importa el orden exacto en que se visitaron las ciudades anteriores; **solo importa qué ciudad es la actual y cuál es el subconjunto de ciudades ya visitadas**.
* **Definición Formal del Subproblema:**
  > **$C(S, j)$:** Longitud mínima de un camino simple que comienza en la ciudad 1, visita **exactamente** todas las ciudades del subconjunto $S \subseteq \{2, 3, \dots, n\}$ y finaliza en la ciudad $j \in S$.
* **Casos Base:**
  Para subconjuntos de tamaño 1 ($S = \{j\}$):
  $$C(\{j\}, j) = c_{1, j} \quad \forall j \in \{2, \dots, n\}$$
* **Ecuación de Recurrencia:**
  Para cualquier subconjunto $S$ de tamaño $|S| \ge 2$ y cualquier ciudad de llegada $j \in S$:
  $$C(S, j) = \min_{k \in S \setminus \{j\}} \left[ C(S \setminus \{j\}, k) + c_{kj} \right]$$
* **Cálculo del Tour Cerrado Óptimo:**
  Una vez calculada la tabla para el conjunto completo $V' = \{2, 3, \dots, n\}$:
  $$OPT = \min_{j \in \{2, \dots, n\}} \left[ C(\{2, \dots, n\}, j) + c_{j, 1} \right]$$

**Pseudocódigo de Held-Karp**

```text
FUNCION TSP_HeldKarp(C, n):
    // Hay 2^(n-1) subconjuntos posibles de ciudades intermedias {2, ..., n}
    INICIALIZAR DP como tabla indexada por (subconjunto_bits, ciudad_destino) con INFINITO
    INICIALIZAR padre como tabla para reconstrucción

    // Casos base: caminos de longitud 1 desde ciudad 1 a ciudad j
    PARA j <- 1 HASTA n - 1: // Índice base 0: ciudad 0 es el nodo 1
        mascara_unitaria <- 1 << (j - 1)
        DP[mascara_unitaria][j] <- C[0][j]

    // Iteramos por tamaño de subconjunto: s = 2, 3, ..., n - 1
    PARA tam <- 2 HASTA n - 1:
        PARA CADA mascara DE TAMAÑO tam EN SubconjuntosDeBits(n - 1):
            PARA CADA j EN ElementosDe(mascara):
                mascara_previa <- mascara SIN EL BIT DE j
                PARA CADA k EN ElementosDe(mascara_previa):
                    costo_cand <- DP[mascara_previa][k] + C[k][j]
                    SI costo_cand < DP[mascara][j]:
                        DP[mascara][j] <- costo_cand
                        padre[mascara][j] <- k

    // Cierre del tour hacia el origen 0
    mascara_completa <- (1 << (n - 1)) - 1
    optimo <- INFINITO
    ultimo_nodo <- -1

    PARA j <- 1 HASTA n - 1:
        costo_total <- DP[mascara_completa][j] + C[j][0]
        SI costo_total < optimo:
            optimo <- costo_total
            ultimo_nodo <- j

    // Reconstrucción hacia atrás
    INICIALIZAR tour como lista
    curr_mascara <- mascara_completa
    curr_nodo <- ultimo_nodo
    MIENTRAS curr_nodo != -1:
        INSERTAR curr_nodo AL INICIO DE tour
        prev_nodo <- padre[curr_mascara][curr_nodo]
        curr_mascara <- curr_mascara SIN EL BIT DE curr_nodo
        curr_nodo <- prev_nodo
    INSERTAR 0 AL INICIO DE tour
    AGREGAR 0 AL FINAL DE tour

    RETORNAR (optimo, tour)
```

* **Complejidad:**
  * **Tiempo:** Hay $\binom{n-1}{k}$ subconjuntos de tamaño $k$. Para cada par $(S, j)$, hay $k$ transiciones posibles. El tiempo total es:
    $$\sum_{k=1}^{n-1} k \binom{n-1}{k} (n-1) = O(n^2 2^n)$$
  * **Espacio:** $O(n \cdot 2^n)$ para almacenar los estados de la tabla DP.
  * **Comparativa con Fuerza Bruta:** Para $n = 20$:
    * $n! = 20! \approx 2.43 \times 10^{18}$ operaciones (imposible en milenios).
    * $n^2 2^n = 20^2 \cdot 2^{20} \approx 4.19 \times 10^8$ operaciones (corre en **menos de 1 segundo** en una PC moderna).

---

#### 3. Paradigma Greedy y Heurísticas de Aproximación

##### A. Heurística Voraz del Vecino más Cercano (Nearest Neighbor)
* **Regla:** Comenzar en una ciudad inicial y en cada paso viajar a la **ciudad no visitada más cercana**. Al visitar las $n$ ciudades, regresar al inicio.
* **Complejidad:** $O(n^2)$ en tiempo y $O(n)$ en espacio.
* **Contraejemplo de Falla Catastrófica (No es óptimo ni acotado en general):**
  * Consideremos 4 ciudades en línea: $A, B, C, D$ con distancias: $\text{dist}(A, B) = 1$, $\text{dist}(B, C) = 2$, $\text{dist}(C, D) = 4$, y $\text{dist}(A, D) = 100$.
  * Iniciando en $B$:
    * El vecino más cercano es $A$ (costo 1).
    * Desde $A$, las no visitadas son $C$ y $D$. La más cercana es $C$ (costo $\text{dist}(A, C) = 3$).
    * Desde $C$, la única no visitada es $D$ (costo 4).
    * Finalmente, desde $D$ debe regresar a $B$ (costo $\text{dist}(D, B) = 6$ o arista de retorno forzosa).
    * Si la última arista de retorno cuesta $M = 10.000$, la voracidad inicial queda atrapada en un costo astronómico.
  * *Conclusión:* En grafos generales, ninguna heurística voraz puede garantizar una cota de aproximación constante a menos que $P = NP$.

---

##### B. Algoritmo 2-Aproximado para TSP Métrico (con Desigualdad Triangular)
Cuando las distancias cumplen la **desigualdad triangular** ($c_{uw} \le c_{uv} + c_{vw}$ para todo $u, v, w$), existe un algoritmo polinomial que garantiza que el costo del tour es a lo sumo **el doble del óptimo ($\text{Tour} \le 2 \cdot OPT$)**.

* **Pasos del Algoritmo:**
  1. **Árbol Generador Mínimo (MST):** Construir un MST del grafo completo usando Kruskal o Prim en $O(n^2)$.
  2. **Duplicación de Aristas:** Duplicar cada arista del MST. El grafo resultante es euleriano (todos los vértices tienen grado par).
  3. **Recorrido en Preorden con Atajos (*Shortcuts*):** Realizar un recorrido DFS en preorden sobre el MST. Si un nodo ya fue visitado previamente, **se saltea tomando un atajo directo** hacia la siguiente ciudad no visitada, regresando finalmente al origen.

**Pseudocódigo del Algoritmo 2-Aproximado**

```text
FUNCION TSP_Metrico2Aproximado(grafo_completo_con_pesos, n):
    // 1. Árbol Generador Mínimo con Prim en O(n^2)
    mst <- PrimMST(grafo_completo_con_pesos, nodo_origen=0)

    // 2. Recorrido DFS en preorden para generar el tour con atajos
    INICIALIZAR visitado como arreglo booleano de tamaño n en FALSO
    INICIALIZAR tour como lista vacía

    DFS_Preorden(mst, 0, visitado, tour)

    // 3. Cerrar el tour regresando al nodo inicial
    AGREGAR 0 AL FINAL DE tour
    RETORNAR tour

PROCEDIMIENTO DFS_Preorden(mst, u, visitado, tour):
    visitado[u] <- VERDADERO
    AGREGAR u AL FINAL DE tour
    PARA CADA v EN VecinosEnMST(mst, u):
        SI NO visitado[v]:
            DFS_Preorden(mst, v, visitado, tour)
```

**Demostración Directa de la Garantía de Aproximación 2:**
1. **El MST cuesta menos que el tour óptimo (`Costo(MST) <= OPT`):** Si al tour óptimo de TSP le borramos una arista cualquiera, nos queda un árbol que conecta todas las ciudades. Como el Árbol Generador Mínimo (MST) es el más barato de todos los árboles posibles, seguro cuesta menos o igual que el tour óptimo.
2. **Ida y vuelta por el MST cuesta el doble (`2 * Costo(MST) <= 2 * OPT`):** Recorrer el árbol con DFS pasando dos veces por cada arista (una de ida y otra de vuelta) cuesta exactamente `2 * Costo(MST)`.
3. **Los atajos no encarecen el recorrido:** Cuando el DFS está por repetir una ciudad ya visitada y toma el atajo directo a la siguiente ciudad nueva, por desigualdad triangular ir directo cuesta menos o igual que dar el rodeo. Por lo tanto, el tour final cuesta **`<= 2 * OPT`**.

---

#### 4. Paradigma Programación Lineal Entera (PLI) — Formulación MTZ

Para formular TSP en PLI, no basta con exigir que cada nodo tenga grado de entrada 1 y grado de salida 1 (eso admitiría **subtours desconectados**, por ejemplo dos triángulos aislados de 3 nodos en vez de un ciclo de 6). Se utiliza la **formulación de Miller-Tucker-Zemlin (MTZ)**:

* **Variables de Decisión:**
  * $x_{ij} \in \{0, 1\}$ para todo $i, j \in \{1, \dots, n\}$ con $i \neq j$ (1 si se viaja directamente de la ciudad $i$ a la $j$, 0 si no).
  * $u_i \in \mathbb{R}$ para $i \in \{2, \dots, n\}$: variable continua auxiliar que representa el **orden de visita** de la ciudad $i$ a lo largo del tour.
* **Función Objetivo:**
  $$\text{MINIMIZAR } Z = \sum_{i=1}^n \sum_{j=1, j \neq i}^n c_{ij} \cdot x_{ij}$$
* **Restricciones de Grado (Asignación):**
  1. Salir exactamente una vez de cada ciudad:
     $$\sum_{j=1, j \neq i}^n x_{ij} = 1 \quad \forall i \in \{1, \dots, n\}$$
  2. Llegar exactamente una vez a cada ciudad:
     $$\sum_{i=1, i \neq j}^n x_{ij} = 1 \quad \forall j \in \{1, \dots, n\}$$
* **Restricciones de Eliminación de Subtours (MTZ):**
  Para cada par de ciudades $i, j \in \{2, \dots, n\}$ con $i \neq j$:
  $$u_i - u_j + n \cdot x_{ij} \le n - 1$$
* **Por qué MTZ elimina los subtours (Explicación directa):**
  * Cada vez que viajamos de `i` a `j` (`x_{ij} = 1`), la restricción obliga a que el número de orden suba (`u_j >= u_i + 1`).
  * Si hubiera un ciclo cerrado aparte que no pasa por la ciudad inicial `1`, los números de orden `u` tendrían que subir en cada paso alrededor del ciclo hasta que una ciudad tendría que tener un orden mayor a sí misma (imposible). Así solo puede existir un único tour conectado que sale y vuelve a la ciudad `1`.
* **Recuento Riguroso para Examen:**
  * **Variables:** $n(n - 1)$ variables binarias $x_{ij} + (n - 1)$ variables continuas $u_i$. Total: $n^2 - 1$ variables.
  * **Restricciones:** $n$ de salida $+ n$ de entrada $+ (n - 1)(n - 2)$ restricciones MTZ. Total: $2n + n^2 - 3n + 2 = n^2 - n + 2$ restricciones (orden $O(n^2)$, frente a las $O(2^n)$ de la formulación DFJ).

---

#### 5. Reducciones Polinomiales y Complejidad NP-Completa

* **Problema de Decisión de TSP:**
  Dado un grafo ponderado $G = (V, E)$, matriz de costos $C = [c_{uv}]$ y un entero $K$, ¿existe un tour cerrado que visite cada ciudad exactamente una vez con costo total $\le K$?
* **Paso 1: TSP está en NP:**
  * Si nos dan una lista ordenada de ciudades como certificado, chequeamos en `O(n)` que estén todas las ciudades sin repetir y que la suma de los costos de las aristas sea `<= K`. Como verifica en tiempo polinomial, **TSP pertenece a NP**.
* **Paso 2 y 3: Reducción desde Ciclo Hamiltoniano (`HC <=p TSP`):**
  Dado un grafo `G = (V, E)` de Ciclo Hamiltoniano:
  1. Creamos un grafo completo `G'` con las mismas ciudades.
  2. Le ponemos **peso `1`** a las aristas que existían en `G` y **peso `2`** a las que no existían.
  3. Fijamos el costo máximo en **`K = |V|`**. Construir `G'` tarda `O(V^2)` (polinomial).
* **Paso 4: Equivalencia (Ida y Vuelta):**
  * **($\implies$) Ida:** Si `G` tiene un Ciclo Hamiltoniano, usa `|V|` aristas originales (todas de peso `1`), por lo que en `G'` forma un tour de TSP de costo `|V| * 1 = |V| <= K`.
  * **($\impliedby$) Vuelta:** Si `G'` tiene un tour de TSP de costo `<= |V|`, como el tour tiene `|V|` aristas y ninguna cuesta menos de `1`, no pudo haber usado ninguna arista de peso `2` (si usara una de peso `2`, costaría al menos `|V| + 1`). Por lo tanto, todas sus aristas son de peso `1`, existen en `G` y forman un Ciclo Hamiltoniano.
* **Conclusión:** TSP es **NP-Completo**.

---

#### 6. Tabla Comparativa Maestra: El Viajante de Comercio en los 5 Paradigmas

| Paradigma | Enfoque / Algoritmo | Complejidad Temporal | Complejidad Espacial | ¿Garantiza Óptimo? | Cuándo Usarlo en Parcial |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Backtracking (B&B)**| Búsqueda con cota MST | **$O(n!)$** peor caso | **$O(n)$** | ✅ **SÍ (Exacto)** | Cuando $n \le 20$ y piden algoritmo exacto combinatorio con poda de árbol. |
| **Prog. Dinámica** | Bellman-Held-Karp | **$O(n^2 \cdot 2^n)$** | **$O(n \cdot 2^n)$** | ✅ **SÍ (Exacto)** | Cuando $n \le 23$ y se exige el óptimo reduciendo factorial a exponencial. |
| **Greedy Heurístico** | Vecino más Cercano | **$O(n^2)$** | **$O(n)$** | ❌ Sin garantía general | Para mostrar por qué una decisión voraz miope puede ser catastrófica. |
| **Algoritmo Aprox** | 2-Aproximación por MST | **$O(n^2)$** | **$O(n)$** | ❌ Cota: $\text{Tour} \le 2 \cdot OPT$ | En grafos métricos (con desigualdad triangular) para tiempo polinomial. |
| **Prog. Lineal (PLI)**| Formulación MTZ | Exponencial (peor caso) | $O(n^2)$ variables | ✅ **SÍ (Exacto)** | Para solvers de optimización matemática con eliminación de subtours. |
| **Reducciones NP-C** | De Ciclo Hamiltoniano | Reducción en **$O(V^2)$** | $O(V^2)$ | Demostración formal | Cuando piden probar que TSP de decisión es NP-Completo. |
"""
