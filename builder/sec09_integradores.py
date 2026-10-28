"""Módulo 9: Ejercicios Integradores Multi-Paradigma."""

def get_content():
    return r"""## 11. Ejercicios Integradores Multi-Paradigma

En los parciales más exigentes, la cátedra suele plantear un mismo escenario del mundo real y exigir resolverlo o compararlo a través de múltiples paradigmas distintos (Greedy vs Programación Dinámica vs Programación Lineal vs Redes de Flujo). Esta sección entrena la capacidad de conectar y contrastar estos enfoques.

---

### Ejercicio 75 — El Dilema del Transporte en Etapas: Greedy vs Programación Dinámica vs Programación Lineal

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Integrador Parcial 2025-1-2 (Ejercicios 2, 3 y 5 combinados)

**Enunciado Integrador**  
El INVAP debe transportar una carga de alta seguridad desde Ezeiza hasta Bariloche a través de un grafo de etapas donde las ciudades intermedias están agrupadas en días de viaje (máximo $400\text{ km/día}$, sin viajar de noche). Para cada tramo dirigido $(u, v)$ entre paradas consecutivas se conoce el costo de seguro $C_{uv} > 0$.  
1. **Paradigma Greedy:** Formular un algoritmo voraz. Demostrar formalmente mediante un contraejemplo por qué **no garantiza** la solución óptima.  
2. **Paradigma Programación Dinámica:** Desarrollar la solución óptima definiendo el estado $OPT(v)$, la ecuación de recurrencia, el algoritmo en pseudocódigo y la complejidad temporal.  
3. **Paradigma Programación Lineal:** Formular un modelo de PL que encuentre la ruta de mínimo costo indicando variables, función objetivo, restricciones y recuento exacto de las mismas.

---

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

Para transportar la carga desde Ezeiza ($s$) hasta Bariloche ($t$) a través del grafo dirigido por etapas con costo $C_{uv} > 0$, comparamos las 3 alternativas solicitadas:

1. **Alternativa 1 — Greedy (Algoritmo Voraz):**
   * *Regla Voraz:* Estando en la ciudad actual $u$, elegir avanzar a la ciudad $v$ de la siguiente etapa que tenga el **mínimo costo de seguro inmediato $C_{uv}$**.
   * *Por qué NO es óptimo (Contraejemplo formal):*
     Sea Ezeiza ($E$) con dos ciudades posibles en la Etapa 1: Ciudad $A$ con $C_{EA} = 10$ y Ciudad $B$ con $C_{EB} = 20$. En la Etapa 2, de $A$ a Bariloche ($T$) el costo es $C_{AT} = 100$, mientras que de $B$ a $T$ es $C_{BT} = 5$.
     - **Greedy:** Elige $E \to A$ por ser más barato en el primer paso ($10 < 20$), quedando forzado a pagar $A \to T$ ($100$), con **costo total $= 110$**.
     - **Óptimo:** Toma la ruta $E \to B \to T$ con **costo total $= 20 + 5 = 25 < 110$**.
     - *Conclusión:* La decisión voraz miope no garantiza la solución óptima porque ignora los costos posteriores.

2. **Alternativa 2 — Programación Dinámica (Óptimo en DAG):**
   * *Subestructura Óptima y DAG:* Como los camiones avanzan etapa por etapa (días de viaje) sin retroceder, el grafo es un **Grafo Dirigido Acíclico (DAG)**. Cualquier subcamino de un camino de costo mínimo es a su vez un camino de costo mínimo hacia el nodo intermedio.
   * *Definición del Estado:* $OPT(v) =$ mínimo costo acumulado para viajar desde Ezeiza hasta la ciudad $v$.
   * *Ecuación de Recurrencia:*
     $$OPT(v) = \min_{u \in \text{Predecesores}(v)} \Big\{ OPT(u) + C_{uv} \Big\}$$
   * *Caso Base:* $OPT(\text{Ezeiza}) = 0$, y para todo otro nodo $OPT(v) = +\infty$.
   * *Orden de Llenado:* Por etapas en orden topológico estricto (Día 1, Día 2, $\dots$). **Garantiza optimalidad**.

3. **Alternativa 3 — Programación Lineal (PL Continua / Entera):**
   * *Idea:* Se formula como el envío de **$1$ unidad de flujo de costo mínimo** desde Ezeiza ($+1$) hacia Bariloche ($-1$), con balance $0$ en cada ciudad intermedia.
   * *Variables de Decisión:* $x_{uv} \in [0, 1]$ para cada tramo $(u, v) \in E$ ($1$ si se transita por el tramo, $0$ si no).
   * *Función Objetivo (Minimizar costo total):* $\min Z = \sum_{(u, v) \in E} C_{uv} \cdot x_{uv}$.
   * *Restricciones de Conservación (una por cada vértice $v \in V$):*
     $$\sum_{w: (v, w) \in E} x_{vw} - \sum_{u: (u, v) \in E} x_{uv} = \begin{cases} +1 & \text{si } v = \text{Ezeiza} \\ -1 & \text{si } v = \text{Bariloche} \\ 0 & \forall v \in V \setminus \{\text{Ezeiza}, \text{Bariloche}\} \end{cases}$$
   * *Garantía de Optimalidad:* Es **óptimo**. Por la propiedad de **Unimodularidad Total** de la matriz de incidencia de redes, resolver la relajación lineal continua produce automáticamente variables enteras $x_{uv} \in \{0, 1\}$ sin requerir Branch & Bound exponencial.

#### 2. Semi-Pseudocódigo Simplificado

```text
// 1. Programación Dinámica (Óptimo en DAG)
Algoritmo TransporteOptimoDP(etapas, ezeiza, bariloche):
    OPT = mapa con valor INFINITO para todo nodo; padre = mapa con NULO
    OPT[ezeiza] = 0

    para k desde 1 hasta total_etapas:
        para cada ciudad v en etapas[k]:
            para cada u en Predecesores(v):
                si OPT[u] + C[u][v] < OPT[v]:
                    OPT[v] = OPT[u] + C[u][v]
                    padre[v] = u

    // Reconstrucción del camino óptimo
    ruta = []; actual = bariloche
    mientras actual != NULO:
        insertar actual al inicio de ruta
        actual = padre[actual]
    devolver (OPT[bariloche], ruta)

// 2. Greedy (No óptimo): En cada etapa actual, siguiente = argmin_{v} { C[actual][v] }
// 3. Modelo PL: Min sum C_uv * x_uv  sujeto a sum x_vw - sum x_uv = balance(v)
```

#### 3. Justificación de Complejidad

* **Comparativa de Complejidades Temporales y Espaciales:**
  - **Greedy:** En cada una de las $K$ etapas solo inspecciona las aristas salientes del nodo elegido. Tiempo $\mathcal{O}(|V| + |E|)$ (o $\mathcal{O}(K \cdot \Delta)$), Espacio $\mathcal{O}(|V|)$. Es el más veloz pero **carece de garantía de optimalidad**.
  - **Programación Dinámica:** Al estar estructurado en etapas (DAG), recorre los vértices y cada arista entrante $(u, v)$ una única vez en orden topológico. Tiempo: **$\Theta(|V| + |E|)$**, Espacio: **$\Theta(|V|)$** para las tablas `OPT` y `padre`. **Garantiza la solución óptima** en tiempo lineal respecto al tamaño del grafo.
  - **Programación Lineal:** Formulación con $|E|$ variables y $|V|$ restricciones de conservación. Resuelto como flujo de costo mínimo con Simplex de redes en tiempo polinomial $\mathcal{O}(|V| \cdot |E|)$. **Garantiza la solución óptima**.
* **Elección en Examen:** Si se busca la ruta óptima en un grafo por etapas (DAG), **Programación Dinámica** es la solución óptima y más eficiente de implementar.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>En PD, no mencionar el orden topológico por etapas:</strong> La recurrencia $OPT(v) = \min(OPT(u) + C_{uv})$ solo es válida sin ciclos (DAG). En un grafo con ciclos requeriría Dijkstra o Bellman-Ford.</li>
    <li><strong>En PL, olvidar las restricciones de conservación en los nodos intermedios:</strong> Sin el balance $\sum_{\text{salen}} - \sum_{\text{entran}} = 0$ en cada ciudad intermedia, el solver dejaría el camino desconectado.</li>
  </ul>
</div>

---

### Ejercicio 76 — Asignación de Recursos con Restricción de Capacidad: Redes de Flujo vs PLI

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Integrador Sistemas de Distribución / Asignación

**Enunciado Integrador**  
Una empresa dispone de $N$ servidores y $M$ tareas. Cada tarea $j$ requiere una cantidad de memoria $R_j$, y cada servidor $i$ tiene una capacidad máxima $C_i$. Se sabe qué tareas pueden ejecutarse en qué servidores.  
1. Si todas las tareas tienen requerimiento unitario ($R_j = 1$), ¿qué paradigma conviene usar para maximizar tareas asignadas? Modelarlo.  
2. Si las tareas tienen requerimientos heterogéneos ($R_j$ arbitrarios), ¿por qué Redes de Flujo estándar ya no puede modelar el problema directamente y se debe recurrir a Programación Lineal Entera?

---

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **1. Caso Unitario ($R_j = 1$ para toda tarea $j$) — Redes de Flujo (Polinomial):**
  - Cuando cada tarea consume exactamente $1$ unidad de capacidad, el problema es un **Matching Bipartito con Capacidades** y se resuelve óptimamente con **Redes de Flujo**:
    1. Creamos una **Super-Fuente $s$** y un **Super-Sumidero $t$**.
    2. Aristas $s \to \text{Tarea } j$ con **capacidad $1$** (cada tarea se procesa a lo sumo una vez).
    3. Aristas $\text{Tarea } j \to \text{Servidor } i$ con **capacidad $1$** para cada par compatible.
    4. Aristas $\text{Servidor } i \to t$ con **capacidad $C_i$** (máximo de tareas unitarias que admite el servidor $i$).
  - Por el **Teorema de Integralidad de Ford-Fulkerson**, al ser todas las capacidades enteras, el flujo máximo calculado por Edmonds-Karp es estrictamente entero ($f(e) \in \{0, 1\}$ en las tareas), garantizando asignaciones completas en tiempo polinomial.
* **2. Caso Heterogéneo ($R_j$ arbitrarios indivisibles) — Por qué falla Flujo y Modelo PLI:**
  - **Por qué falla Redes de Flujo:** El flujo es un fluido continuo que satisface conservación escalar ($\sum f_{in} = \sum f_{out}$). Si una tarea $j$ requiere $R_j = 5$ GB y ponemos capacidad $5$ en $s \to j$, la red puede **bifurcar el caudal**: enviar $3$ GB al Servidor 1 y $2$ GB al Servidor 2. Flujo satura los $5$ GB requeridos, pero **la tarea se ejecutó partida en dos servidores**, violando la restricción física de indivisibilidad. El problema equivale al *Multiple Knapsack Problem*, que es NP-Hard.
  - **Modelo Formal en Programación Lineal Entera (PLI):**
    - **Variables de decisión:** $x_{ji} \in \{0, 1\}$ para cada tarea $j \in \{1, \dots, M\}$ y servidor compatible $i \in \{1, \dots, N\}$ ($1$ si la tarea $j$ se asigna completa al servidor $i$, $0$ si no).
    - **Función Objetivo (Maximizar tareas asignadas):**
      $$\max Z = \sum_{j=1}^M \sum_{i=1}^N x_{ji}$$
    - **Restricción 1 — A lo sumo 1 servidor por tarea ($M$ restricciones):**
      $$\sum_{i=1}^N x_{ji} \le 1 \qquad \forall j \in \{1, \dots, M\}$$
    - **Restricción 2 — Capacidad máxima de memoria por servidor ($N$ restricciones):**
      $$\sum_{j=1}^M R_j \cdot x_{ji} \le C_i \qquad \forall i \in \{1, \dots, N\}$$
    - **Conteo exacto:** $M \cdot N$ variables binarias y $M + N$ restricciones lineales.

#### 2. Semi-Pseudocódigo Simplificado

```text
// Caso Unitario (R_j = 1): Redes de Flujo con Edmonds-Karp
Algoritmo AsignarTareasUnitarias(Tareas, Servidores, Cap, Compatibles):
    G = crearRedFlujo(fuente=s, sumidero=t)
    para cada j en Tareas:
        agregarArista(G, s, j, cap=1)
        para cada i en Compatibles[j]:
            agregarArista(G, j, i, cap=1)
    para cada i en Servidores:
        agregarArista(G, i, t, cap=Cap[i])

    (max_tareas, flujo) = EdmondsKarp(G, s, t)
    asignaciones = [ (j, i) para cada (j, i) con flujo[j][i] == 1 ]
    devolver (max_tareas, asignaciones)

// Caso Heterogéneo (R_j arbitrario): Modelo PLI Indivisible
// Variables: x[j][i] in {0, 1} para j in 1..M, i in 1..N
// Maximizar: sum_{j, i} x[j][i]
// Sujeto a:  sum_i x[j][i] <= 1   (para todo j en 1..M)
//            sum_j R[j] * x[j][i] <= C[i]  (para todo i en 1..N)
```

#### 3. Justificación de Complejidad

* **Complejidad en Caso Unitario (Redes de Flujo):**
  - Tamaño de la red: $|V| = M + N + 2$ vértices, y $|E| \le M + M \cdot N + N$ aristas.
  - Con el algoritmo de Edmonds-Karp (caminos aumentantes por BFS), la complejidad temporal es **$\mathcal{O}(|V| \cdot |E|^2) = \mathcal{O}((M + N) \cdot (M \cdot N)^2)$**.
  - Complejidad espacial: $\mathcal{O}(|V| + |E|)$ para la red residual y listas de adyacencia. Es estrictamente **polinomial**.
* **Complejidad en Caso Heterogéneo (PLI):**
  - Al generalizar el problema de la mochila (*Multiple Knapsack*), es **NP-Hard**.
  - Complejidad temporal en peor caso: exponencial **$\mathcal{O}(2^{M \cdot N})$** mediante algoritmos exactos de *Branch & Cut*.
  - Complejidad espacial del modelo: $\mathcal{O}(M \cdot N)$ variables y $\mathcal{O}(M + N)$ restricciones (polinomial en representación matricial).

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Poner aristas de capacidad $R_j$ en Redes de Flujo para tareas indivisibles:</strong> Es un error clásico de parcial. Poner capacidad $R_j$ entre la tarea $j$ y cada servidor compatible permite que la tarea se parta en pedazos entre varios servidores.</li>
  </ul>
</div>

---

### Ejercicio 77 — Cobertura de Nodos en Redes: Vertex Cover por Backtracking, PLI y Aproximación 2

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Integrador Problemas NP-Hard (Vertex Cover)

**Enunciado Integrador**  
Para el problema de Vertex Cover Mínimo en un grafo $G = (V, E)$, comparar tres estrategias de abordaje:  
1. **Solución Exacta Combinatoria:** Backtracking con Branch and Bound.  
2. **Solución Exacta Matemática:** Formulación en Programación Lineal Entera.  
3. **Solución Heurística Polinomial:** Algoritmo de Aproximación con factor $2$ (basado en *Maximal Matching*).

---

#### 1. Idea y Comparativa en Lenguaje Natural (Qué escribir en la hoja)

| Dimensión | 1. Backtracking con B&B | 2. Programación Lineal Entera (PLI) | 3. Algoritmo Aproximado (2-Aprox) |
| :--- | :--- | :--- | :--- |
| **Garantía de Solución** | Óptima exacta | Óptima exacta | Aproximada: $|C| \le 2 \cdot OPT$ |
| **Complejidad Temporal** | $\mathcal{O}(2^{|V|})$ (o $\mathcal{O}(2^k \cdot |E|)$) | Exponencial en peor caso (*Branch & Cut*) | **$\mathcal{O}(|V| + |E|)$** (lineal) |
| **Idea Central para la Hoja** | Elegir una arista descubierta $(u, v)$ y ramificar probando incluir $u$ o incluir $v$, podando si $|C_{\text{actual}}| \ge |C_{\text{mejor}}|$. | Variable binaria $x_v \in \{0, 1\}$ por vértice; exigir $x_u + x_v \ge 1$ en cada arista $(u, v) \in E$ minimizando $\sum x_v$. | Tomar una arista no cubierta $(u, v)$ y **agregar ambos extremos $u$ y $v$** al conjunto $C$, tachando sus aristas incidentes. |

* **Justificación en Lenguaje Natural de por qué el 2-Aproximado garantiza $|C| \le 2 \cdot OPT$:**
  1. Las aristas que elige el algoritmo no comparten ningún vértice entre sí (forman un *Matching* $M$). Por lo tanto, **cualquier solución óptima está obligada a elegir al menos $1$ vértice distinto por cada arista de $M$**, de modo que $OPT \ge |M|$.
  2. Como nuestro algoritmo agrega **los $2$ extremos** ($u$ y $v$) por cada arista de $M$, en total elige $|C| = 2 \cdot |M|$ vértices.
  3. Juntando ambas desigualdades: $|C| = 2 \cdot |M| \le 2 \cdot OPT$. Nunca usa más del doble de vértices que el óptimo y corre en tiempo lineal $\mathcal{O}(|V| + |E|)$.

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

#### 2. Semi-Pseudocódigo Simplificado de los 3 Enfoques (Para la Hoja)

```text
// ENFOQUE 1: Backtracking con Branch & Bound (Exacto)
FUNCION VertexCoverBT(G, C_actual, MEJOR_C):
    // Poda por optimalidad (Branch & Bound)
    SI tamaño(C_actual) >= tamaño(MEJOR_C):
        RETORNAR MEJOR_C

    arista_descubierta <- buscar primera arista (u, v) de G con u no en C_actual y v no en C_actual
    SI arista_descubierta == NULO:
        RETORNAR copiar(C_actual) // Todas las aristas están cubiertas (nuevo récord)

    // Ramificar: para cubrir (u, v) sí o sí hay que incluir u o incluir v
    MEJOR_C <- VertexCoverBT(G, C_actual U {u}, MEJOR_C)
    MEJOR_C <- VertexCoverBT(G, C_actual U {v}, MEJOR_C)
    RETORNAR MEJOR_C

// ENFOQUE 2: Modelo de Programación Lineal Entera (PLI Exacto)
// Variables: x_v in {0, 1} para todo v en V (|V| variables)
// Minimizar: Z = sum_{v en V} x_v
// Sujeto a:  x_u + x_v >= 1   para toda arista (u, v) en E (|E| restricciones)

// ENFOQUE 3: Algoritmo 2-Aproximado en O(|V| + |E|)
FUNCION VertexCoverAproximado2(G = (V, E)):
    C <- conjunto_vacio()
    PARA CADA arista (u, v) EN E:
        SI u NO PERTENECE A C Y v NO PERTENECE A C:
            agregar u a C
            agregar v a C   // Obligatorio agregar AMBOS extremos
    RETORNAR C
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Elegir solo 1 extremo en lugar de ambos en el 2-Aproximado:</strong> Si al tomar una arista $(u, v)$ agregas solo $u$ (o el de mayor grado), el algoritmo pierde la garantía de factor 2 (el greedy por mayor grado tiene factor $O(\log |V|)$, no 2). Es obligatorio agregar <strong>ambos extremos</strong> $u$ y $v$.</li>
  </ul>
</div>

---

### Ejercicio 78 — El Problema Canónico de la Mochila (Knapsack) Resuelto en Todos los Paradigmas Algorítmicos

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★★ (5/5)  
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

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

El problema de la mochila dispone de $n$ elementos con pesos $w_i > 0$, valores $v_i > 0$ y una capacidad máxima $W$. Se resuelve en los 4 paradigmas principales según la variante:

1. **Paradigma Greedy (Mochila Fraccionaria vs Mochila 0-1):**
   * **Mochila Fraccionaria ($x_i \in [0, 1]$):** Se ordenan los elementos por densidad de valor decreciente $r_i = v_i / w_i$ tal que $r_1 \ge r_2 \ge \dots \ge r_n$. Se toman ítems completos con mayor $r_i$; el último ítem que excede la capacidad se fracciona tomando $x_k = \text{capacidad\_remanente} / w_k$. **Es estrictamente óptimo** en $\Theta(n \log n)$ (demostrable por técnica de intercambio: reemplazar masa de menor densidad por masa de mayor densidad nunca reduce el valor acumulado).
   * **Por qué falla en Mochila 0-1 (Indivisible):** Un ítem de alta densidad pero peso ineficiente puede bloquear la entrada de combinaciones de menor densidad pero mayor beneficio total. *Contraejemplo:* $W = 50$, Ítem 1 ($w=10, v=60, r=6$), Ítem 2 ($w=20, v=100, r=5$), Ítem 3 ($w=30, v=120, r=4$). Greedy toma ítems 1 y 2 (peso 30, valor 160). El óptimo toma ítems 2 y 3 (peso 50, valor $220 > 160$).

2. **Paradigma Programación Dinámica (Mochila 0-1 Indivisible):**
   * **Subestructura Óptima y Definición del Estado:** Para decidir si incluir o no el ítem $i$, solo importa cuánta capacidad remanente $w$ queda disponible. Definimos:
     $$OPT(i, w) = \text{máximo valor alcanzable considerando los primeros } i \text{ elementos con capacidad } w$$
   * **Ecuación de Recurrencia:**
     $$OPT(i, w) = \begin{cases} OPT(i-1, w) & \text{si } w_i > w \text{ (el ítem } i \text{ no cabe)} \\ \max\Big(OPT(i-1, w), \; OPT(i-1, w - w_i) + v_i\Big) & \text{si } w_i \le w \text{ (excluir vs incluir)} \end{cases}$$
   * **Casos Base:** $OPT(0, w) = 0$ para todo $w \in [0, W]$ y $OPT(i, 0) = 0$.
   * **Orden de Llenado:** Tabla $(n+1) \times (W+1)$ iterando $i$ de $1$ a $n$ y $w$ de $0$ a $W$. Puede optimizarse a un vector unidimensional de tamaño $W+1$ recorriendo $w$ en sentido descendente.

3. **Paradigma Backtracking y Branch & Bound (Mochila 0-1 con W Astronómico):**
   * **Árbol Binario de Decisiones:** Ordenamos previamente los ítems por $v_i / w_i$ decreciente. En cada nivel $i$, ramificamos en: (a) Incluir ítem $i$, (b) Excluir ítem $i$.
   * **Poda por Factibilidad:** Si $\text{peso\_actual} + w_i > W$, se descarta de inmediato la rama de inclusión.
   * **Poda por Optimalidad (Branch and Bound con Relajación Continua):** En el nodo $(i, \text{peso}, \text{valor})$, calculamos la cota superior del subárbol resolviendo la mochila fraccionaria con los ítems restantes $i \dots n$. Si $\text{valor} + \text{cota\_fraccionaria} \le \text{mejor\_valor}$, se poda todo el subárbol.

4. **Paradigma Programación Lineal Entera (PLI 0-1):**
   * **Variables de Decisión:** $x_i \in \{0, 1\}$ para $i \in \{1, \dots, n\}$ ($1$ si se empaca el ítem $i$, $0$ si no).
   * **Función Objetivo:** Maximizar el valor total: $\max Z = \sum_{i=1}^n v_i \cdot x_i$.
   * **Restricción de Capacidad (1 restricción):** $\sum_{i=1}^n w_i \cdot x_i \le W$.
   * **Relación con Relajación:** Relajar $x_i \in [0, 1]$ equivale a la Mochila Fraccionaria, cuya solución óptima es la cota superior utilizada por el solver en cada nodo del árbol de Branch & Cut.

#### 2. Semi-Pseudocódigo Simplificado

```text
// 1. Programación Dinámica (Mochila 0/1 con arreglo O(W))
Algoritmo Mochila01DP(pesos, valores, n, W):
    DP = arreglo de tamaño (W + 1) inicializado en 0
    para i desde 0 hasta n - 1:
        para w desde W bajando hasta pesos[i]:
            DP[w] = max(DP[w], DP[w - pesos[i]] + valores[i])
    devolver DP[W]

// 2. Backtracking con Branch & Bound (Cota Fraccionaria)
función MochilaBT(i, peso_act, val_act, ref mejor_val, pesos, valores, n, W):
    si val_act > mejor_val:
        mejor_val = val_act
    si i == n o peso_act == W:
        devolver

    // Poda Branch & Bound: cota superior fraccionaria con ítems restantes
    si val_act + CotaFraccionaria(i, W - peso_act, pesos, valores, n) <= mejor_val:
        devolver

    // Rama 1: Incluir ítem i (poda de factibilidad si no entra)
    si peso_act + pesos[i] <= W:
        MochilaBT(i + 1, peso_act + pesos[i], val_act + valores[i], mejor_val, pesos, valores, n, W)

    // Rama 2: Excluir ítem i
    MochilaBT(i + 1, peso_act, val_act, mejor_val, pesos, valores, n, W)
```

#### 3. Justificación de Complejidad

* **Análisis Comparativo de Complejidad:**
  - **Greedy Fraccionario:** Ordenamiento inicial en $\Theta(n \log n)$ y barrido voraz en $\Theta(n)$. Tiempo total: **$\Theta(n \log n)$**, Espacio auxiliar: $\mathcal{O}(1)$. Es óptimo para la versión continua; en 0-1 no garantiza solución óptima.
  - **Programación Dinámica 0-1:** Tiempo: **$\Theta(n \cdot W)$**. Espacio: $\Theta(W)$ (con vector optimizado) u $\Theta(n \cdot W)$ (con matriz para reconstrucción de ítems). Es una complejidad **pseudo-polinomial**: es polinomial respecto a la magnitud numérica de $W$, pero exponencial respecto a la cantidad de bits de la entrada $B = \log_2 W$ (dado que $W = 2^B$). Si $W$ es del orden de $10^{12}$, DP colapsa por memoria y tiempo.
  - **Backtracking con Branch & Bound:** Peor caso asintótico: **$O(2^n)$** tiempo, $\mathcal{O}(n)$ espacio en pila. Sin embargo, gracias a la cota fraccionaria estricta, las podas cortan grandes regiones del árbol. Es la estrategia superior cuando $W \gg 10^9$ pero $n$ es moderado ($n \le 40$).
  - **Programación Lineal Entera (PLI):** Problema NP-Hard en peor caso ($O(2^n)$), pero con solo $n$ variables binarias y 1 restricción lineal, resuelto eficazmente por solvers modernos con Branch & Cut.

| Paradigma | Variante | Complejidad Temporal | Complejidad Espacial | ¿Garantiza Óptimo? | Cuándo Usarlo en Parcial |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Greedy (Voraz)** | Fraccionaria | **$\Theta(n \log n)$** | **$\mathcal{O}(1)$** | ✅ **SÍ (Óptimo)** | Cuando los objetos admiten división continua (combustible, polvos). |
| **Prog. Dinámica** | 0-1 (Indivisible) | **$\Theta(n \cdot W)$** | **$\Theta(W)$** | ✅ **SÍ (Exacto)** | Cuando $W$ es moderado ($W \le 10^6$) y se exige el óptimo entero. |
| **Backtracking (B&B)**| 0-1 (Indivisible) | **$\mathcal{O}(2^n)$** peor caso | **$\mathcal{O}(n)$** | ✅ **SÍ (Exacto)** | Cuando $W$ es astronómico ($W > 10^9$) y $n \le 40$. |
| **Prog. Lineal (PLI)**| 0-1 (Indivisible) | Exponencial peor caso | $\mathcal{O}(n)$ variables | ✅ **SÍ (Exacto)** | Cuando hay múltiples recursos acoplados (peso, volumen, costo). |

---

### Ejercicio 79 — El Problema del Viajante de Comercio (TSP) Resuelto en Todos los Paradigmas Algorítmicos

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★★ (5/5)  
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

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

El problema del viajante (TSP) consiste en encontrar un circuito simple de costo mínimo que visite exactamente una vez las $n$ ciudades y regrese al punto de partida. Se sintetizan los 4 paradigmas fundamentales solicitados:

1. **Fuerza Bruta y Backtracking con Branch & Bound (Búsqueda Exacta):**
   * **Espacio de Búsqueda:** Fijamos la ciudad inicial en $1$ para romper la simetría cíclica, explorando las permutaciones de las restantes $n-1$ ciudades (espacio $(n-1)! / 2$).
   * **Poda por Factibilidad:** Si no existe arista entre la ciudad actual y la candidata ($c_{uv} = \infty$) o la candidata ya fue visitada en la ruta actual, se descarta.
   * **Poda por Cota Superior:** Si $\text{costo\_acumulado} \ge \text{mejor\_costo}$, se poda de inmediato la rama.
   * **Poda por Cota Inferior (Branch & Bound con MST / 1-Tree):** Para el conjunto de ciudades restantes no visitadas $V_{\text{no\_vis}}$, cualquier tour válido debe conectarlas formando al menos un árbol generador más 2 aristas de enlace. Cota inferior:
     $$\text{Cota} = \text{costo\_acum} + \text{CostoMST}(V_{\text{no\_vis}}) + \min_{r \in V_{\text{no\_vis}}} c_{\text{actual}, r} + \min_{r \in V_{\text{no\_vis}}} c_{r, 1}$$
     Si $\text{Cota} \ge \text{mejor\_costo}$, se poda el subárbol completo.

2. **Programación Dinámica (Algoritmo de Bellman-Held-Karp):**
   * **Subestructura Óptima:** Para continuar el recorrido desde la ciudad actual $j$, no importa el orden en que se visitaron las ciudades anteriores; solo importa **cuál es la ciudad actual $j$ y cuál es el subconjunto $S \subseteq \{2, \dots, n\}$ de ciudades ya visitadas**.
   * **Definición del Subproblema:** $C(S, j) =$ costo mínimo de un camino simple que inicia en 1, visita exactamente todas las ciudades de $S$ y finaliza en $j \in S$.
   * **Casos Base:** $C(\{j\}, j) = c_{1j}$ para todo $j \in \{2, \dots, n\}$.
   * **Ecuación de Recurrencia:**
     $$C(S, j) = \min_{k \in S \setminus \{j\}} \Big\{ C(S \setminus \{j\}, k) + c_{kj} \Big\}$$
   * **Cierre Óptimo:** $\min_{j \in \{2, \dots, n\}} \{ C(\{2, \dots, n\}, j) + c_{j1} \}$. Reduce la complejidad factorial a exponencial $\Theta(n^2 2^n)$.

3. **Programación Lineal Entera (PLI con Restricciones MTZ):**
   * **Variables:** $x_{ij} \in \{0, 1\}$ ($1$ si se viaja directo de $i$ a $j$) y variables continuas auxiliares $u_i \in \mathbb{R}$ para $i \in \{2, \dots, n\}$ que representan el orden de visita.
   * **Función Objetivo:** Minimizar $Z = \sum_{i \ne j} c_{ij} \cdot x_{ij}$.
   * **Restricciones de Asignación:** Salir exactamente una vez de cada ciudad ($\sum_{j} x_{ij} = 1$) y llegar exactamente una vez a cada una ($\sum_{i} x_{ij} = 1$).
   * **Restricciones de Eliminación de Subtours (Miller-Tucker-Zemlin / MTZ):**
     $$u_i - u_j + n \cdot x_{ij} \le n - 1 \qquad \forall i \ne j \in \{2, \dots, n\}$$
   * *Por qué MTZ elimina los subtours:* Si $x_{ij} = 1$, la desigualdad fuerza $u_j \ge u_i + 1$. Un subtour cerrado desconectado que no contenga al nodo $1$ exigiría que las variables de orden $u$ aumenten en cada paso a lo largo del ciclo, generando la contradicción $u_k > u_k$. Esto elimina subtours con solo $O(n^2)$ restricciones (evitando las $O(2^n)$ de la formulación DFJ).

4. **Heurística Greedy y Búsqueda Local (2-Opt / 2-Aprox):**
   * **Greedy (Vecino más Cercano):** Viajar iterativamente a la ciudad más cercana no visitada. No garantiza cota constante en grafos generales (una última arista de retorno forzada puede tener costo arbitrariamente alto).
   * **Búsqueda Local 2-Opt:** Partiendo de un tour factible, examina pares de aristas no consecutivas $(u, v)$ y $(w, z)$. Si eliminarlas y reconectar $(u, w)$ y $(v, z)$ revirtiendo el subcamino intermedio reduce el costo ($c_{uw} + c_{vz} < c_{uv} + c_{wz}$), se adopta el cambio. Se itera hasta alcanzar un óptimo local donde ninguna reconexión 2-opt mejore el recorrido.
   * *(Caso Métrico 2-Aproximado):* Si se cumple la desigualdad triangular, construir el MST, duplicar aristas y recorrer en preorden DFS con atajos garantiza $\text{Costo}(\text{Tour}) \le 2 \cdot OPT$ en $O(n^2)$.

#### 2. Semi-Pseudocódigo Simplificado

```text
// 1. Programación Dinámica (Held-Karp) en O(n^2 * 2^n)
Algoritmo TSP_HeldKarp(C, n):
    DP = tabla indexada por (mascara_S, ciudad_j) en INFINITO
    para j desde 1 hasta n - 1:
        DP[1 << (j - 1)][j] = C[0][j]  // Casos base desde origen 0

    para tam desde 2 hasta n - 1:
        para cada mascara de tamaño tam:
            para cada j en mascara:
                prev_mask = mascara sin bit j
                para cada k en prev_mask:
                    DP[mascara][j] = min(DP[mascara][j], DP[prev_mask][k] + C[k][j])

    // Cerrar tour retornando al origen 0
    full_mask = (1 << (n - 1)) - 1
    devolver min_{j} (DP[full_mask][j] + C[j][0])

// 2. Modelo PLI con Restricciones MTZ:
// Min sum c_ij * x_ij  sujeto a sum_j x_ij = 1, sum_i x_ij = 1
// y restricción de orden MTZ: u_i - u_j + n * x_ij <= n - 1 (para i != j >= 1)
```

#### 3. Justificación de Complejidad

* **Comparativa de Complejidades Temporales y Espaciales:**
  - **Fuerza Bruta / Backtracking con B&B:** Peor caso asintótico: **$O(n!)$** tiempo, $\mathcal{O}(n)$ espacio. Con cotas inferiores fuertes de MST resuelve instancias de hasta $n \approx 20-25$.
  - **Programación Dinámica (Held-Karp):** Hay $\binom{n-1}{k}$ subconjuntos de tamaño $k$, y para cada par $(S, j)$ se evalúan $k$ transiciones. Complejidad temporal: **$\Theta(n^2 2^n)$**, Espacio: $\Theta(n \cdot 2^n)$. Para $n = 20$, reduce de $20! \approx 2.43 \times 10^{18}$ operaciones a $20^2 \cdot 2^{20} \approx 4.19 \times 10^8$ operaciones (de milenios a menos de 1 segundo).
  - **Programación Lineal Entera (PLI con MTZ):** Peor caso exponencial $O(2^{n^2})$. El modelo utiliza $n^2 - 1$ variables y $n^2 - n + 2 = O(n^2)$ restricciones (polinomial en especificación).
  - **Greedy / 2-Opt:** Vecino más cercano corre en $\mathcal{O}(n^2)$. Cada pasada de 2-opt evalúa $\mathcal{O}(n^2)$ parejas de aristas en tiempo polinomial hacia un óptimo local.

| Paradigma | Enfoque / Algoritmo | Complejidad Temporal | Complejidad Espacial | ¿Garantiza Óptimo? | Cuándo Usarlo en Parcial |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **Backtracking (B&B)**| Búsqueda con cota MST | **$O(n!)$** peor caso | **$O(n)$** | ✅ **SÍ (Exacto)** | Cuando $n \le 20$ y piden algoritmo exacto combinatorio con poda de árbol. |
| **Prog. Dinámica** | Bellman-Held-Karp | **$O(n^2 \cdot 2^n)$** | **$O(n \cdot 2^n)$** | ✅ **SÍ (Exacto)** | Cuando $n \le 23$ y se exige el óptimo reduciendo factorial a exponencial. |
| **Greedy Heurístico** | Vecino más Cercano | **$O(n^2)$** | **$O(n)$** | ❌ Sin garantía general | Para mostrar por qué una decisión voraz miope puede ser catastrófica. |
| **Búsqueda Local** | Heurística 2-Opt | **$O(n^2)$** por pasada | **$O(n)$** | ❌ Óptimo Local | Para mejorar tours rápidamente en la práctica industrial. |
| **Prog. Lineal (PLI)**| Formulación MTZ | Exponencial (peor caso) | $O(n^2)$ variables | ✅ **SÍ (Exacto)** | Para solvers de optimización matemática con eliminación de subtours. |
"""
