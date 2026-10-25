"""Módulo 8: Reducciones Polinomiales y NP-Completitud."""

def get_content():
    return r"""## 10. Tema 7: Reducciones Polinomiales y NP-Completitud

### Conceptos Mínimos de Supervivencia

1. **Definiciones Formales de Clases de Complejidad:**
   * **Clase P:** Problemas de decisión que pueden resolverse mediante un algoritmo determinístico en tiempo polinomial ($O(n^k)$).
   * **Clase NP (Nondeterministic Polynomial):** Problemas de decisión cuyas instancias afirmativas (*instancias YES*) admiten un **certificado polinomial** (o testigo $C$) que puede ser verificado por un algoritmo determinístico en tiempo polinomial $O(P(n))$.
   * **Reducción Polinomial de Karp ($A \le_P B$):** Significa que el problema $A$ se reduce en tiempo polinomial al problema $B$.
     $$\text{Interpretación:} \quad \text{"El problema } A \text{ no es más difícil que el problema } B \text{ (a lo sumo tan difícil como } B\text{)"}$$
     Si contamos con una subrutina polinomial para resolver $B$, podemos resolver $A$ en tiempo polinomial.
   * **Clase NP-Completo (NPC):** Un problema $B$ es NP-Completo si y solo si:
     1. $B \in \text{NP}$.
     2. Para todo $A \in \text{NP}$, $A \le_P B$ (es decir, $B$ es **NP-Hard**).
2. **El Esquema Canónico de 4 Pasos Obligatorios para Demostrar $B \in \text{NPC}$:**
   En las correcciones de FIUBA, omitir cualquiera de estos 4 pasos implica la pérdida automática de más del $50\%$ del puntaje de la pregunta:
   * **Paso 1: Demostrar que $B \in \text{NP}$.**  
     Definir formalmente el certificado $C$, su tamaño polinomial en función de la entrada, escribir el algoritmo verificador $V(I_B, C)$ en pseudocódigo y justificar su complejidad temporal $O(P(n))$.
   * **Paso 2: Selección del problema conocido $A \in \text{NPC}$.**  
     Elegir un problema cuya NP-Completitud ya fue demostrada en clase (3-SAT, Vertex Cover, Ciclo Hamiltoniano, Independent Set, Subset Sum).  
     **DIRECCIÓN SAGRADA:** Reducir **DESDE** el problema conocido **HACIA** el nuevo problema:
     $$A \le_P B$$
     *(Reducir al revés, $B \le_P A$, es un error fatal que anula por completo la demostración).*
   * **Paso 3: Definir la transformación de instancias $f: I_A \to I_B$.**  
     Construir una función determinística que transforme cualquier instancia arbitraria $I_A$ en una instancia válida $I_B$. Demostrar analíticamente que la construcción toma tiempo polinomial $O(P(n))$.
   * **Paso 4: Demostración Bidireccional de Equivalencia Lógica:**  
     * ($\implies$) **Ida:** Si $I_A$ es una instancia positiva de $A$ ($I_A \in \text{YES}_A$), entonces $f(I_A)$ es una instancia positiva de $B$ ($f(I_A) \in \text{YES}_B$).
     * ($\impliedby$) **Vuelta:** Si $f(I_A)$ es una instancia positiva de $B$ ($f(I_A) \in \text{YES}_B$), entonces $I_A$ es una instancia positiva de $A$ ($I_A \in \text{YES}_A$). *(O demostrar el contra-recíproco: si $I_A \in \text{NO}_A \implies f(I_A) \in \text{NO}_B$).*

---

### Patrón de Ejercicio 7.1: Reducciones sobre Grafos con Gadgets de Aristas

Aparece de forma reiterada en los parciales de FIUBA (2024 y 2025). Requiere transformar cobertura de aristas en dominancia de vértices mediante *gadgets*.

---

### Ejercicio 28 — Demostración de NP-Completitud de Dominating Set (desde Vertex Cover)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-2 (Ej 5) y Parcial 2024-2-3 (Ej 5) / Guía 07 Ejercicio 2 y 14  
**Qué evalúa la cátedra:** Protocolo estricto de 4 pasos, diseño de *gadgets* de subdivisión triangular de aristas, verificación polinomial, y demostración bidireccional exhaustiva.

#### 1. Enunciado Completo
Un conjunto dominante (*Dominating Set*) en un grafo no dirigido $G = (V, E)$ es un subconjunto de vértices $D \subseteq V$ tal que todo vértice $v \in V$ pertenece a $D$ o es adyacente a al menos un vértice en $D$.  
El problema de decisión de Dominating Set plantea: dado un grafo $G = (V, E)$ y un entero positivo $k \le |V|$, ¿existe un conjunto dominante $D$ tal que $|D| \le k$?  
Demostrar formalmente que **Dominating Set es NP-Completo**, reduciendo desde **Vertex Cover**.

#### 2. Los 5 Pasos Metodológicos de la Demostración

##### Paso 1: Pertenencia a la Clase NP ($DominatingSet \in \text{NP}$)
- **Certificado Candidato ($C$):** Un subconjunto de vértices propuesto $D \subseteq V$.  
  - *Tamaño del certificado:* $|D| \le |V|$ vértices. Dado que cada vértice se codifica en $O(\log |V|)$ bits, el tamaño total del certificado es $O(|V| \log |V|)$, estrictamente polinomial respecto a la entrada.
- **Algoritmo Verificador Polinomial $V(G, k, D)$:**
  1. Verificar que $|D| \le k$. Si no, retornar $\text{FALSO}$.
  2. Inicializar un arreglo booleano `cubierto` de tamaño $|V|$ inicializado en $\text{FALSO}$.
  3. Para cada vértice $u \in D$:
     - Marcar `cubierto[u] = VERDADERO`.
     - Para cada vecino $v$ adyacente a $u$ en $G$:
       - Marcar `cubierto[v] = VERDADERO`.
  4. Recorrer el arreglo: si existe algún vértice con `cubierto[x] == FALSO`, retornar $\text{FALSO}$; si todos están cubiertos, retornar $\text{VERDADERO}$.
- **Complejidad del Verificador:** Marcar a cada $u \in D$ y a sus vecinos toma $\sum_{u \in D} (1 + \text{grado}(u)) \le |V| + 2|E| = O(|V| + |E|)$ operaciones elementales. Como el verificador corre en tiempo lineal-polinomial, **Dominating Set $\in$ NP**.

##### Paso 2: Selección del Problema Conocido
Seleccionamos el problema **Vertex Cover (VC)**, cuya versión de decisión es conocida como NP-Completa (Karp, 1972):  
*Dado un grafo no dirigido $G = (V, E)$ y un entero $k$, ¿existe un subconjunto $S \subseteq V$ con $|S| \le k$ tal que toda arista $(u, v) \in E$ tenga al menos uno de sus extremos en $S$?*  
Objetivo: Demostrar que:
$$\text{Vertex Cover} \le_P \text{Dominating Set}$$

##### Paso 3: Transformación Polinomial $f(G, k) \to (G', k')$ (Diseño del Gadget)
Sea $(G = (V, E), k)$ una instancia arbitraria de Vertex Cover.
1. Asumimos sin pérdida de generalidad que $G$ no posee vértices aislados (un vértice aislado no cubre aristas en VC y puede ser eliminado de la instancia de forma trivial en $O(|V|)$).
2. Construimos el grafo transformado $G' = (V', E')$ mediante el siguiente gadget de aristas:
   - **Vértices:** Conservamos todos los vértices originales de $V$ y agregamos un **nuevo vértice auxiliar $w_e$ por cada arista $e \in E$**:
     $$V' = V \cup \{w_e : e \in E\}$$
     Por lo tanto, $|V'| = |V| + |E|$.
   - **Aristas:** Para cada arista $e = (u, v) \in E$:
     - Mantenemos la arista original $(u, v) \in E'$.
     - Agregamos aristas entre el vértice auxiliar $w_e$ y ambos extremos originales $u$ y $v$: $(u, w_e)$ y $(v, w_e)$.
     $$E' = E \cup \{(u, w_e), (v, w_e) : e = (u, v) \in E\}$$
     Por lo tanto, $|E'| = |E| + 2|E| = 3|E|$. Cada arista original forma un triángulo $\{u, v, w_e\}$.
3. Fijamos la cota del conjunto dominante:
   $$k' = k$$
- **Complejidad Temporal de la Construcción:** Duplicar nodos y aristas toma tiempo $O(|V| + |E|)$, que es estrictamente polinomial.

#### 3. Demostración Rigurosa de Equivalencia Bidireccional

##### ($\implies$) Si $G$ tiene un Vertex Cover $S$ con $|S| \le k$, entonces $G'$ tiene un Dominating Set $D$ con $|D| \le k$:
- Proponemos el conjunto dominante $D = S$. Como $|S| \le k$, tenemos inmediatamente que $|D| \le k$.
- Verifiquemos que $D$ domina a todos los vértices de $V'$:
  1. **Vértices auxiliares $w_e \in V' \setminus V$:** Cada $w_e$ corresponde a una arista original $e = (u, v) \in E$. Dado que $S$ es un Vertex Cover de $G$, al menos uno de los extremos pertenece a $S$ (es decir, $u \in S$ o $v \in S$). Dado que en $G'$ existen las aristas $(u, w_e)$ y $(v, w_e)$, $w_e$ es adyacente a al menos un vértice en $D = S$. Por lo tanto, todo $w_e$ queda dominado.
  2. **Vértices originales $u \in V$:** Como $G$ no tiene vértices aislados, $u$ pertenece a al menos una arista $e = (u, v) \in E$. Si $u \in S$, entonces $u \in D$ y se domina a sí mismo. Si $u \notin S$, por ser $S$ un Vertex Cover, necesariamente el otro extremo $v$ pertenece a $S = D$. Como $(u, v) \in E'$, $u$ es adyacente a $v \in D$. Por lo tanto, $u$ está dominado.
- En conclusión, $D$ es un conjunto dominante válido de $G'$ de tamaño $\le k$.

##### ($\impliedby$) Si $G'$ tiene un Dominating Set $D'$ con $|D'| \le k$, entonces $G$ tiene un Vertex Cover $S$ con $|S| \le k$:
- Supongamos que $D'$ contiene vértices auxiliares $w_e$ correspondientes a aristas $e = (u, v)$.
- En $G'$, el vértice $w_e$ solo tiene dos vecinos: $u$ y $v$.
- Si reemplazamos en $D'$ al vértice auxiliar $w_e$ por el vértice original $u$ (o $v$):
  - El propio $w_e$ sigue dominado porque es vecino de $u$.
  - El vértice $u$ ahora se domina a sí mismo.
  - Cualquier vecino original de $w_e$ (que solo podían ser $u$ y $v$) sigue dominado. Además, $u$ puede dominar a otros vecinos en $G$.
  - El tamaño del conjunto no se incrementa: $|(D' \setminus \{w_e\}) \cup \{u\}| \le |D'| \le k$.
- Aplicando esta sustitución a todo vértice auxiliar en $D'$, obtenemos un nuevo conjunto dominante $D'' \subseteq V$ compuesto **exclusivamente por vértices originales de $G$**, con $|D''| \le |D'| \le k$.
- Demostremos que $D''$ es un Vertex Cover en $G$:
  - Consideremos cualquier arista $e = (u, v) \in E$. En $G'$, el vértice auxiliar $w_e$ debe estar dominado por $D''$.
  - Como $w_e \notin D''$ (porque $D'' \subseteq V$), $w_e$ debe ser adyacente a algún vértice en $D''$.
  - Pero los únicos vecinos de $w_e$ en $G'$ son $u$ y $v$. Por lo tanto, necesariamente:
    $$u \in D'' \quad \lor \quad v \in D''$$
  - Esto significa que toda arista $(u, v) \in E$ tiene al menos un extremo en $D''$.
- Por lo tanto, $S = D''$ es un Vertex Cover válido de $G$ con $|S| \le k$.

**Conclusión Final:** Habiendo demostrado que Dominating Set $\in$ NP y que Vertex Cover $\le_P$ Dominating Set en ambas direcciones en tiempo polinomial, queda rigurosamente demostrado que **Dominating Set es NP-Completo**.

#### 4. Diagrama Visual del Gadget Triangular

```mermaid
flowchart LR
    subgraph AristaG [Arista uv en G]
        u1["Vertice u"] --- v1["Vertice v"]
    end
    subgraph GadgetGPrime [Gadget Triangular en G prima]
        u2["Vertice u"] --- v2["Vertice v"]
        u2 --- we["Vertice Auxiliar we"]
        v2 --- we
    end
```

#### 5. Ejemplo Numérico y Traza

Consideremos un grafo simple $G$ con 3 vértices en línea: $1 - 2 - 3$.
- Aristas: $e_1 = (1, 2)$ y $e_2 = (2, 3)$.
- Vertex Cover óptimo en $G$: $S = \{2\}$ de tamaño $k = 1$ (el nodo 2 cubre ambas aristas).
- Construcción de $G'$:
  - Vértices: $V' = \{1, 2, 3, w_{e1}, w_{e2}\}$.
  - Aristas de $w_{e1}$: $(1, w_{e1})$ y $(2, w_{e1})$.
  - Aristas de $w_{e2}$: $(2, w_{e2})$ y $(3, w_{e2})$.
  - Aristas originales: $(1, 2)$ y $(2, 3)$.
- Evaluemos $D = \{2\}$ en $G'$ ($k'=1$):
  - Nodo 2 se domina a sí mismo.
  - Nodos 1 y 3 son adyacentes a 2 $\implies$ dominados.
  - Nodos $w_{e1}$ y $w_{e2}$ son adyacentes a 2 $\implies$ dominados.
- ¡Todos los 5 vértices de $G'$ quedan dominados con un único nodo $D = \{2\}$!

#### 6. Implementación en Python con Verificador Polinomial

```python
from typing import Dict, List, Set, Tuple

def verificador_dominating_set(
    vertices: List[int],
    adyacencia: Dict[int, List[int]],
    k: int,
    certificado_D: Set[int]
) -> bool:
    # 1. Verificar tamano cota
    if len(certificado_D) > k:
        return False

    # 2. Verificar que D este contenido en V
    set_v = set(vertices)
    if not certificado_D.issubset(set_v):
        return False

    # 3. Conjunto de dominados en O(V + E)
    dominados = set(certificado_D)
    for u in certificado_D:
        for vecino in adyacencia.get(u, []):
            dominados.add(vecino)

    # 4. Todos los vertices deben estar dominados
    return len(dominados) == len(vertices)

def transformar_vc_a_dominating_set(
    vertices: List[int],
    aristas: List[Tuple[int, int]],
    k: int
) -> Tuple[List[int], List[Tuple[int, int]], int]:
    # Gadget: V' = V U {w_e}, E' = E U {(u, w_e), (v, w_e)}
    nuevos_vertices = list(vertices)
    nuevas_aristas = list(aristas)
    next_id = max(vertices) + 1 if vertices else 1

    for u, v in aristas:
        w_e = next_id
        next_id += 1
        nuevos_vertices.append(w_e)
        nuevas_aristas.append((u, w_e))
        nuevas_aristas.append((v, w_e))

    return nuevos_vertices, nuevas_aristas, k
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Reducir al revés ($DominatingSet \le_P VertexCover$):</strong> Reducir el problema nuevo al problema conocido demuestra que el nuevo es fácil, pero **no prueba que sea NP-Hard**. La reducción debe partir obligatoriamente desde el problema conocido.</li>
    <li><strong>Olvidar reemplazar los vértices auxiliares en la vuelta:</strong> Si un conjunto dominante contiene $w_e$, no es un subconjunto de los vértices originales. Es obligatorio explicar por qué $w_e$ puede sustituirse por $u$ sin aumentar el tamaño ni perder dominancia.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 7.2: Reducciones de Caminos y Ciclos (El Dilema de Marco el Cadete)

Reducción polinomial estricta desde Ciclo Hamiltoniano hacia el Problema del Viajante de Comercio (TSP) en grafos ponderados completos.

---

### Ejercicio 29 — El Dilema de Marco el Cadete: Reducción de Ciclo Hamiltoniano a TSP

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2025-1-1 (27 de mayo de 2025), Ejercicio 5  
**Qué evalúa la cátedra:** Reducción entre problemas NP-Completos de grafos, diseño de matrices de costo con penalización asimétrica (gadget métrico), y prueba bidireccional.

#### 1. Enunciado Completo
Marco, el cadete administrativo de una empresa de logística, compró un costoso paquete de software para resolver el **Problema del Viajante de Comercio** (TSP en su versión de decisión), cuando la gerencia le había solicitado explícitamente un módulo para resolver **Ciclo Hamiltoniano**. El vendedor del software le aseguró a Marco:  
*"Si puedes resolver TSP de decisión en un grafo completo ponderado, puedes resolver exactamente Ciclo Hamiltoniano en cualquier grafo en el mismo orden de tiempo"*.  
Definiciones formales:
- **Ciclo Hamiltoniano (HC):** Dado un grafo no dirigido $G = (V, E)$, determinar si existe un ciclo simple que visite todos los vértices de $V$ exactamente una vez y retorne al origen.
- **TSP (Decisión):** Dado un grafo completo $G' = (V', E')$ con pesos enteros $w(e) \ge 0$ en las aristas y un entero $k$, determinar si existe un tour cerrado que visite cada vértice una única vez con costo total $\le k$.
Determinar con fundamento formal si el vendedor tiene razón o si hay que despedir a Marco. Desarrollar la reducción polinomial completa con demostración de equivalencia.

#### 2. Resolución y Demostración Formal

**El vendedor tiene razón.** Demostraremos que:
$$\text{Ciclo Hamiltoniano} \le_P \text{TSP (Decisión)}$$
lo que significa que una subrutina que resuelve TSP permite resolver Ciclo Hamiltoniano de manera directa.

##### 1. Transformación Polinomial $f(G) \to (G', w, k)$
Dada una instancia arbitraria de Ciclo Hamiltoniano $G = (V, E)$ con $n = |V|$ vértices:
1. Construimos un grafo completo $G' = (V, E')$ con el mismo conjunto de vértices $V$. Como es completo, para todo par de vértices distintos $u, v \in V$, existe la arista $(u, v) \in E'$.
2. Definimos la función de ponderación $w: E' \to \mathbb{Z}^+$ según pertenezcan o no al grafo original:
   $$w(u, v) = \begin{cases} 1 & \text{si } (u, v) \in E \text{ (la arista existía en el grafo original)} \\ 2 & \text{si } (u, v) \notin E \text{ (arista artificial de penalización)} \end{cases}$$
3. Fijamos el umbral de costo del tour TSP:
   $$k = n = |V|$$
- **Complejidad de la Transformación:** El grafo $G'$ contiene $\binom{n}{2} = \frac{n(n-1)}{2} = O(n^2)$ aristas. Asignar los pesos 1 o 2 consultando la matriz de adyacencia de $G$ toma tiempo $O(n^2)$, estrictamente polinomial.

##### 2. Demostración de Equivalencia Bidireccional

- **($\implies$) Si $G$ tiene un Ciclo Hamiltoniano, entonces $G'$ tiene un tour TSP de costo $\le n$:**
  - Sea $C = (v_1, v_2, \dots, v_n, v_1)$ un ciclo hamiltoniano en $G$.
  - Como $C$ es un ciclo en $G$, todas sus $n$ aristas $(v_i, v_{i+1})$ y $(v_n, v_1)$ pertenecen a $E$.
  - Por la regla de construcción, cada una de estas aristas tiene peso $w = 1$ en $G'$.
  - El ciclo $C$ visita los $n$ vértices sin repetir y regresa al origen, constituyendo un tour válido de TSP en $G'$.
  - El costo acumulado del tour es:
    $$\text{Costo}(C) = \sum_{i=1}^n w(v_i, v_{i+1}) = \sum_{i=1}^n 1 = n \le k$$
  - Por lo tanto, $(G', w, k)$ es una instancia $\text{YES}$ de TSP.

- **($\impliedby$) Si $G'$ tiene un tour TSP de costo $\le n$, entonces $G$ tiene un Ciclo Hamiltoniano:**
  - Sea $T = (u_1, u_2, \dots, u_n, u_1)$ un tour cerrado en $G'$ que visita los $n$ vértices con costo total $\le n$.
  - El tour consta de exactamente $n$ aristas.
  - Por construcción de $G'$, todas las aristas tienen peso $w \in \{1, 2\}$.
  - Supongamos por contradicción que al menos una arista del tour $T$, digamos $(u_j, u_{j+1})$, no pertenecía a $E$ ($w=2$).
  - Dado que las restantes $n-1$ aristas tienen peso como mínimo $1$, el costo total del tour sería:
    $$\text{Costo}(T) \ge 2 + \sum_{i \ne j} 1 = 2 + (n - 1) = n + 1 > n$$
    lo cual contradice la hipótesis de que $\text{Costo}(T) \le n$.
  - Por consiguiente, **ninguna arista del tour puede tener peso 2**. Todas las $n$ aristas de $T$ deben tener obligatoriamente peso $w = 1$.
  - Que tengan peso 1 significa que todas las aristas de $T$ existen en $E$.
  - Por lo tanto, $T$ es un ciclo simple en $G$ que visita los $n$ vértices sin repetir y retorna al origen: **$T$ es un Ciclo Hamiltoniano en $G$**.

**Conclusión:** Marco puede cargar la matriz con pesos 1 y 2 en el software de TSP. Si el software responde que existe un tour de costo $\le n$, Marco sabe que existe un ciclo hamiltoniano. Si responde que no, no existe. **El vendedor tenía razón y Marco conserva su empleo.**

#### 3. Diagrama Visual del Gadget de Penalización

```mermaid
graph LR
    subgraph GrafoOriginalG [Grafo G con 4 vertices]
        A["Nodo A"] -->|Existe en E| B["Nodo B"]
        B -->|Existe en E| C["Nodo C"]
        C -->|Existe en E| D["Nodo D"]
        D -->|Existe en E| A
    end
    subgraph GrafoCompletoGPrime [Grafo Completo Ponderado]
        A2["Nodo A"] -->|peso 1| B2["Nodo B"]
        B2 -->|peso 1| C2["Nodo C"]
        C2 -->|peso 1| D2["Nodo D"]
        D2 -->|peso 1| A2
        A2 -. Penalizacion peso 2 .-> C2
        B2 -. Penalizacion peso 2 .-> D2
    end
```

#### 4. Código Python de la Reducción

```python
from typing import List, Tuple
import numpy as np

def reducir_ciclo_hamiltoniano_a_tsp(
    n_vertices: int,
    aristas_g: List[Tuple[int, int]]
) -> Tuple[np.ndarray, int]:
    # Matriz completa con penalizacion 1 y 2
    matriz_pesos = np.full((n_vertices, n_vertices), 2, dtype=int)
    for i in range(n_vertices):
        matriz_pesos[i, i] = 0 # Sin bucles

    for u, v in aristas_g:
        matriz_pesos[u, v] = 1
        matriz_pesos[v, u] = 1

    cota_k = n_vertices
    return matriz_pesos, cota_k
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Asignar peso 0 a las aristas existentes y 1 a las inexistentes:</strong> Si se pone peso 0 a las aristas existentes y cota $k = 0$, matemáticamente es válido, pero muchos docentes exigen pesos estrictamente positivos ($w(e) > 0$). Con pesos $\{1, 2\}$ y cota $k = n$, se respeta la formulación clásica de TSP métrico.</li>
    <li><strong>No demostrar la cota $n+1 > n$ en la vuelta:</strong> Omitir la desigualdad aritmética que prueba por qué una sola arista de peso 2 hace imposible alcanzar el costo $n$.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 7.3: Reducciones Numéricas (Cambio de Monedas a Subset Sum)

Demostración de que la versión de decisión del problema de cambio de monedas no es más difícil que Subset Sum y análisis de equivalencia en la clase NP-Completo.

---

### Ejercicio 30 — Reducción de Cambio de Monedas a Subset Sum

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-1 (5 de noviembre de 2024), Ejercicio 5  
**Qué evalúa la cátedra:** Concepto de orden de dificultad entre problemas en NP, manipulación de multiconjuntos con réplicas y comprensión del Teorema de Cook-Levin.

#### 1. Enunciado Completo
Demostrar formalmente que el problema del **Cambio de Monedas** (en su versión de decisión: dadas denominaciones enteras $D = \{d_1, \dots, d_m\}$, un entero objetivo $V$ y una cota $k$, ¿es posible dar cambio de valor exacto $V$ utilizando a lo sumo $k$ monedas?) **no es más difícil** que el problema de la **Suma de Subconjuntos (Subset Sum)**.  
¿Es posible demostrar la reducción en sentido inverso? Fundamentar en base a las clases de complejidad teóricas.

#### 2. Demostración Formal

**Interpretación de la Consigna:**  
La afirmación "el problema $A$ no es más difícil que el problema $B$" equivale rigurosamente a la relación de reducción polinomial:
$$\text{Cambio de Monedas} \le_P \text{Subset Sum}$$

##### 1. Transformación Polinomial
En Subset Sum clásico, cada elemento de un conjunto $S$ puede seleccionarse a lo sumo **una única vez** para sumar un objetivo $W$. En Cambio de Monedas, cada denominación $d_i \in D$ puede utilizarse múltiples veces, pero en total no pueden emplearse más de $k$ monedas.
1. Como a lo sumo se usarán $k$ monedas en total, ninguna moneda individual puede usarse más de $k$ veces.
2. Construimos una lista de enteros $L$ creando $k$ copias independientes de cada denominación $d_i \in D$:
   $$L = \{d_{i}^{(1)}, d_{i}^{(2)}, \dots, d_{i}^{(k)} : \forall d_i \in D\}$$
   El conjunto $L$ contiene exactamente $m \cdot k$ enteros.
3. Para controlar simultáneamente el valor monetario $V$ y que la cantidad de monedas no exceda $k$, empleamos la técnica de **desplazamiento de base (gadget decimal/binario)**:
   - Sea $M = k + 1$ (un número estrictamente mayor que la cota de monedas).
   - Para cada elemento $d_i^{(r)} \in L$, definimos un nuevo entero de dos campos:
     $$e_i^{(r)} = d_i \cdot M + 1$$
   - Fijamos el objetivo de Subset Sum:
     $$W = V \cdot M + k' \quad \text{probando para cada } k' \in \{1, \dots, k\}$$
   - *Alternativa directa estándar:* Dado que la versión de decisión de Cambio de Monedas con $k$ libre admite réplicas de elementos, se reduce directamente a Subset Sum con réplicas en tiempo $O(m \cdot k)$.
- **Complejidad:** Generar los $m \cdot k$ elementos toma tiempo polinomial $O(m \cdot k)$.

##### 2. Equivalencia Lógica
- ($\implies$) Si existe una combinación de $\le k$ monedas que suma $V$, esa combinación utiliza a lo sumo $k$ copias de las denominaciones, las cuales están presentes en $L$. Por lo tanto, existe un subconjunto de $L$ cuya suma es exactamente $V$.
- ($\impliedby$) Todo subconjunto de $L$ que sume $V$ y contenga a lo sumo $k$ elementos corresponde a una combinación válida de monedas con las denominaciones disponibles.

##### 3. ¿Es posible demostrarlo en sentido opuesto (Subset Sum $\le_P$ Cambio de Monedas)?
**SÍ, es totalmente posible y válido.**  
- **Fundamentación Teórica:** Dado que Subset Sum es un problema conocido de la clase **NP-Completo** y la versión de decisión general de Cambio de Monedas pertenece a la clase **NP**:
  - Por la definición canónica de NP-Completitud (Cook-Levin / Karp), **todo problema en la clase NP se reduce polinomialmente a cualquier problema NP-Completo**.
  - Si la versión de decisión del problema de monedas es NP-Completa (bajo representación binaria de denominaciones), ambos problemas son computacionalmente equivalentes bajo reducciones polinomiales de Karp:
    $$\text{Cambio de Monedas} \equiv_P \text{Subset Sum}$$

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Confundir tiempo pseudo-polinomial con polinomial:</strong> Afirmar que como ambos se resuelven con programación dinámica en $O(n V)$ están en P. No están en P bajo codificación binaria porque el tamaño de la entrada es $O(\log V)$, haciendo que $O(V)$ sea exponencial respecto a la longitud en bits.</li>
    <li><strong>Decir que no se puede reducir en sentido inverso:</strong> Creer erróneamente que porque uno parece más general no puede reducirse al otro. Dos problemas NP-Completos cualesquiera siempre admiten reducción mutua bidireccional.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 7.4: La Reducción Dual Canónica (Independent Set a Vertex Cover)

Reducción estructural basada en el Teorema del Complemento de Gallai en grafos no dirigidos.

---

### Ejercicio 31 — Reducción Dual: Independent Set a Vertex Cover

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Guía de Ejercicios 07, Ejercicio 3  
**Qué evalúa la cátedra:** Comprensión de la dualidad estructural de grafos, demostración del Teorema de Gallai ($|IS| + |VC| = |V|$) y reducción formal de Karp en tiempo $O(1)$.

#### 1. Enunciado Completo
Dados los problemas de decisión de **Independent Set** (¿existe un subconjunto de vértices $I \subseteq V$ de tamaño $|I| \ge k$ tal que no existan aristas entre vértices de $I$?) y **Vertex Cover** (¿existe un subconjunto $S \subseteq V$ de tamaño $|S| \le k'$ que cubra todas las aristas de $E$?):
1. Diseñar una reducción polinomial formal de **Independent Set a Vertex Cover**.
2. Demostrar rigurosamente la equivalencia lógica fundamentando el teorema del complemento en teoría de grafos.

#### 2. Demostración del Teorema del Complemento (Lema de Gallai)

**Teorema Fundamental:**  
En cualquier grafo no dirigido $G = (V, E)$, un subconjunto de vértices $S \subseteq V$ es un **Independent Set** si y solo si su complemento $V \setminus S$ es un **Vertex Cover**.

**Demostración:**
- **($\implies$) Si $S$ es un Independent Set, entonces $V \setminus S$ es un Vertex Cover:**
  - Supongamos por contradicción que $V \setminus S$ no es un Vertex Cover.
  - Esto significa que existe al menos una arista $e = (u, v) \in E$ que no está cubierta por $V \setminus S$.
  - Para que $(u, v)$ no esté cubierta, ninguno de sus extremos puede pertenecer a $V \setminus S$.
  - Por lo tanto, necesariamente $u \in S$ y $v \in S$.
  - Pero si $u, v \in S$ y existe la arista $(u, v) \in E$, entonces $S$ contiene dos vértices adyacentes, lo cual contradice directamente la hipótesis de que $S$ es un conjunto independiente.
  - La contradicción prueba que toda arista tiene al menos un extremo en $V \setminus S$, por lo que $V \setminus S$ es un Vertex Cover válido.
- **($\impliedby$) Si $V \setminus S$ es un Vertex Cover, entonces $S$ es un Independent Set:**
  - Supongamos por contradicción que $S$ no es un Independent Set.
  - Esto implica que existen dos vértices $u, v \in S$ tales que $(u, v) \in E$.
  - Pero si $(u, v) \in E$, por ser $V \setminus S$ un Vertex Cover, al menos uno de los extremos debe pertenecer a $V \setminus S$.
  - Sin embargo, ambos extremos pertenecen a $S$, lo que significa que ninguno pertenece a $V \setminus S$.
  - Esto contradice que $V \setminus S$ cubra la arista $(u, v)$.
  - Por lo tanto, no pueden existir aristas entre vértices de $S$, concluyendo que $S$ es un Independent Set.

#### 3. Construcción de la Reducción Polinomial

Dada una instancia $(G = (V, E), k)$ de Independent Set:
1. El grafo transformado es idéntico: $G' = G$.
2. Fijamos la cota de Vertex Cover:
   $$k' = |V| - k$$
- **Complejidad:** La transformación simplemente lee la cantidad de vértices y efectúa una resta entera en tiempo $O(1)$.

#### 4. Equivalencia Lógica
$$G \text{ tiene un Independent Set de tamaño } \ge k \iff G \text{ tiene un Vertex Cover de tamaño } \le |V| - k$$
- Si existe $S$ independiente con $|S| \ge k$, su complemento $V \setminus S$ es un Vertex Cover con tamaño:
  $$|V \setminus S| = |V| - |S| \le |V| - k = k'$$
- Si existe un Vertex Cover $C$ con $|C| \le k'$, su complemento $V \setminus C$ es un Independent Set con tamaño:
  $$|V \setminus C| = |V| - |C| \ge |V| - k' = |V| - (|V| - k) = k$$

#### 5. Diagrama Visual de la Dualidad

```mermaid
flowchart LR
    IS["Independent Set S: tamano al menos k"] ---|Complemento Exacto en V| VC["Vertex Cover: V sin S, tamano a lo sumo V-k"]
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Invertir el sentido de las desigualdades:</strong> Olvidar que Independent Set es un problema de **maximización** ($|S| \ge k$) mientras que Vertex Cover es de **minimización** ($|C| \le k'$). Al restar del total $|V|$, la desigualdad se invierte automáticamente ($|S| \ge k \iff |V| - |S| \le |V| - k$).</li>
  </ul>
</div>

---

### Errores Fatales en Exámenes sobre Reducciones NP

1. **Reducir en la dirección equivocada ($B \le_P A$ en lugar de $A \le_P B$):** Es el error más grave de toda la materia. Si se pide probar que $B \in \text{NPC}$, la reducción DEBE partir del problema conocido $A$ y llegar al nuevo problema $B$. Reducir al revés tiene calificación automática de 0 puntos en la pregunta.
2. **Omitir el Paso 1 ($B \in \text{NP}$):** No definir el certificado o no justificar la verificación polinomial impide calificar el problema como NP-Completo (solo quedaría como NP-Hard).
3. **Probar únicamente la implicación de ida ($\implies$):** Demostrar que si $I_A \in \text{YES} \implies I_B \in \text{YES}$ no es suficiente. Debe demostrarse rigurosamente la vuelta ($\impliedby$) para asegurar que instancias $\text{NO}$ de $A$ no produzcan falsos positivos en $B$.
4. **Usar algoritmos exponenciales en la transformación:** La función de mapeo $f(I_A)$ debe ejecutarse en tiempo estrictamente polinomial $O(n^c)$. Si la reducción requiere calcular algo NP-Hard antes de armar la instancia, la reducción queda invalidada.
"""
