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
2. **El Esquema Canónico de 4 Pasos Obligatorios para Demostrar que un Problema B es NP-Completo:**
   En las correcciones de FIUBA, no hace falta usar notación matemática pesada, pero sí cumplir estos 4 pasos claros en lenguaje directo:
   * **Paso 1: Demostrar que B está en NP (`Verificador`).**  
     Explicar qué es el **certificado** (una solución candidata que nos dan armada) y cómo un algoritmo verificador chequea en **tiempo polinomial** si cumple las condiciones del problema.
   * **Paso 2: Elegir el problema conocido A que ya sabemos que es NP-Completo.**  
     Elegir un problema visto en clase (3-SAT, Vertex Cover, Ciclo Hamiltoniano, Independent Set, Subset Sum, k-Coloring).  
     **DIRECCIÓN SAGRADA:** Siempre reducir **DESDE** el problema conocido **HACIA** el problema nuevo (`Conocido <=p Nuevo`). Reducir al revés anula el ejercicio.
   * **Paso 3: Transformación Polinomial (`Transformar`).**  
     Explicar paso a paso cómo convertir cualquier entrada del problema conocido A en una entrada del problema nuevo B en **tiempo polinomial** (sin resolver el problema).
   * **Paso 4: Equivalencia ("Ida y Vuelta" con palabras):**  
     * **Ida ($\implies$):** Explicar por qué si A tiene solución, entonces la instancia transformada de B también tiene solución.
     * **Vuelta ($\impliedby$):** Explicar por qué si la instancia transformada de B tiene solución, de ahí podemos recuperar una solución válida para A.

---

### Patrón de Ejercicio 7.1: Reducciones sobre Grafos con Gadgets de Aristas

Aparece de forma reiterada en los parciales de FIUBA (2024 y 2025). Requiere transformar cobertura de aristas en dominancia de vértices mediante *gadgets*.

---

### Ejercicio 71 — Demostración de NP-Completitud de Dominating Set (desde Vertex Cover)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Parcial 2024-2-2 (Ej 5) y Parcial 2024-2-3 (Ej 5) / Guía 07 Ejercicio 2 y 14  
**Qué evalúa la cátedra:** Protocolo de 4 pasos completo, diseño del triángulo auxiliar por arista, verificación polinomial y justificación de ida y vuelta en lenguaje claro.

**Enunciado**  
Un conjunto dominante (*Dominating Set*) en un grafo no dirigido $G = (V, E)$ es un subconjunto de vértices $D \subseteq V$ tal que todo vértice $v \in V$ pertenece a $D$ o es adyacente a al menos un vértice en $D$.  
El problema de decisión de Dominating Set plantea: dado un grafo $G = (V, E)$ y un entero positivo $k \le |V|$, ¿existe un conjunto dominante $D$ tal que $|D| \le k$?  
Demostrar formalmente que **Dominating Set es NP-Completo**, reduciendo desde **Vertex Cover**.

#### 1. Idea y Justificación en Lenguaje Natural (Los 4 Pasos para la Hoja del Parcial)

1. **Paso 1 (Pertenece a NP — Verificador):**
   * **Certificado:** Un subconjunto de vértices $D \subseteq V$ propuesto como solución.
   * **Verificación en tiempo polinomial:** Chequeamos primero que $|D| \le k$ en $\mathcal{O}(1)$. Luego recorremos cada vértice $u \in D$ y marcamos como "dominados" a $u$ y a todos sus vecinos directos en $G$. Al finalizar, verificamos si quedaron marcados los $|V|$ vértices del grafo. Como recorremos vértices y aristas una sola vez, el verificador tarda **$\mathcal{O}(|V| + |E|)$** (polinomial) $\implies \text{Dominating Set} \in \text{NP}$.
2. **Paso 2 y 3 (Reducción desde problema conocido $\text{Vertex Cover} \le_P \text{Dominating Set}$):**
   * Partimos de una instancia $(G = (V, E), k)$ de **Vertex Cover** (sabemos que es NP-Completo: ¿existen $\le k$ vértices que toquen todas las aristas de $G$?).
   * **Transformación en lenguaje natural:**
     1. Eliminamos de $G$ los vértices aislados (sin aristas), ya que en Vertex Cover no cubren ninguna arista y en Dominating Set obligarían a gastar vértices extra.
     2. Copiamos todos los vértices y aristas restantes de $G$ a un nuevo grafo $G'$.
     3. **Por cada arista $(u, v) \in E$, creamos un vértice nuevo $w_{uv}$ y lo conectamos a $u$ y a $v$** (armando un triángulo entre $u$, $v$ y $w_{uv}$).
     4. Mantenemos el mismo límite **$k' = k$**.
   * **Cuánto tarda:** Agregamos $|E|$ vértices nuevos y $2|E|$ aristas en tiempo **$\mathcal{O}(|V| + |E|)$** (polinomial).
3. **Paso 4 (Ida y Vuelta $\iff$):**
   * **($\implies$) Ida (Si hay Vertex Cover de tamaño $\le k$ en $G \implies$ hay Dominating Set de tamaño $\le k$ en $G'$):**
     Tomamos el mismo conjunto $D$ del Vertex Cover. Como cubría todas las aristas $(u, v)$ de $G$, al menos uno entre $u$ y $v$ está en $D$: ese vértice domina al nodo nuevo $w_{uv}$ y también a los extremos de la arista (como no hay vértices aislados, todo vértice original tiene al menos una arista cubierta y queda dominado). Así, $D$ domina todo $G'$ con $|D| \le k$.
   * **($\impliedby$) Vuelta (Si hay Dominating Set de tamaño $\le k$ en $G' \implies$ hay Vertex Cover de tamaño $\le k$ en $G$):**
     Si el conjunto dominante $D$ de $G'$ eligió algún vértice auxiliar $w_{uv}$, **lo reemplazamos por $u$** (o por $v$). Esto no aumenta el tamaño de $D$ ni pierde dominancia (porque $w_{uv}$ solo tocaba a $u$ y $v$, y $u$ también los cubre). Ahora $D$ solo tiene vértices originales de $G$, y como cada $w_{uv}$ está dominado sin pertenecer a $D$, sí o sí al menos uno de sus dos únicos vecinos ($u$ o $v$) está en $D$, cubriendo todas las aristas de $G$.
   * **Conclusión:** $\text{Dominating Set} \in \text{NP-Completo}$.

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

#### 2. Semi-Pseudocódigo Simplificado del Verificador y la Transformación

```text
FUNCION VerificadorDominatingSet(G = (V, E), k, certificado_D):
    SI tamaño(certificado_D) > k:
        RETORNAR FALSO

    dominados <- conjunto_vacio()
    PARA CADA u EN certificado_D:
        agregar u a dominados
        PARA CADA v EN Vecinos(G, u):
            agregar v a dominados

    RETORNAR (tamaño(dominados) == tamaño(V)) // Tiempo O(|V| + |E|)

FUNCION TransformarVCaDominatingSet(G = (V, E), k):
    G_sin_aislados <- eliminar vértices de grado 0 en G
    G' <- copiar(G_sin_aislados)

    PARA CADA arista (u, v) EN Aristas(G_sin_aislados):
        crear vértice nuevo w_uv en G'
        agregar_arista(G', u, w_uv)
        agregar_arista(G', v, w_uv)

    RETORNAR (G', k' = k) // Transformación en O(|V| + |E|)
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Reducir al revés ($DominatingSet \le_P VertexCover$):</strong> Reducir el problema nuevo al problema conocido demuestra que el nuevo es fácil, pero <strong>no prueba que sea NP-Hard</strong>. La reducción debe partir obligatoriamente desde el problema conocido.</li>
    <li><strong>Olvidar reemplazar los vértices auxiliares en la vuelta:</strong> Si un conjunto dominante contiene $w_{uv}$, no es un subconjunto de los vértices originales. Es obligatorio explicar por qué $w_{uv}$ puede sustituirse por $u$ sin aumentar el tamaño ni perder dominancia.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 7.2: Reducciones de Caminos y Ciclos (El Dilema de Marco el Cadete)

Reducción polinomial estricta desde Ciclo Hamiltoniano hacia el Problema del Viajante de Comercio (TSP) en grafos ponderados completos.

---

### Ejercicio 72 — El Dilema de Marco el Cadete: Reducción de Ciclo Hamiltoniano a TSP

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Parcial 2025-1-1 (27 de mayo de 2025), Ejercicio 5  
**Qué evalúa la cátedra:** Reducción entre problemas NP-Completos de grafos, diseño de matrices de costo con penalización asimétrica (gadget métrico), y prueba bidireccional.

**Enunciado**  
Marco, el cadete administrativo de una empresa de logística, compró un costoso paquete de software para resolver el **Problema del Viajante de Comercio** (TSP en su versión de decisión), cuando la gerencia le había solicitado explícitamente un módulo para resolver **Ciclo Hamiltoniano**. El vendedor del software le aseguró a Marco:  
*"Si puedes resolver TSP de decisión en un grafo completo ponderado, puedes resolver exactamente Ciclo Hamiltoniano en cualquier grafo en el mismo orden de tiempo"*.  
Definiciones formales:
- **Ciclo Hamiltoniano (HC):** Dado un grafo no dirigido $G = (V, E)$, determinar si existe un ciclo simple que visite todos los vértices de $V$ exactamente una vez y retorne al origen.
- **TSP (Decisión):** Dado un grafo completo $G' = (V', E')$ con pesos enteros $w(e) \ge 0$ en las aristas y un entero $k$, determinar si existe un tour cerrado que visite cada vértice una única vez con costo total $\le k$.
Determinar con fundamento formal si el vendedor tiene razón o si hay que despedir a Marco. Desarrollar la reducción polinomial completa con demostración de equivalencia.

#### 1. Idea y Justificación en Lenguaje Natural (Los 4 Pasos para la Hoja del Parcial)

**Veredicto inicial:** **El vendedor tiene razón y no hay que despedir a Marco**, porque podemos reducir **$\text{Ciclo Hamiltoniano} \le_P \text{TSP (Decisión)}$** en tiempo polinomial.

1. **Paso 1 (Pertenece a NP — Verificador de TSP):**
   * **Certificado:** Una secuencia ordenada de vértices $(v_1, v_2, \dots, v_n, v_1)$ propuesta como tour.
   * **Verificación en tiempo polinomial:** Revisamos en $\mathcal{O}(n)$ que aparezcan las $n = |V|$ ciudades sin repetidos, que empiece y termine en la misma ciudad y que la suma de los pesos de las $n$ aristas consecutivas sea $\le k$. Como tarda **$\mathcal{O}(n)$**, $\text{TSP} \in \text{NP}$.
2. **Paso 2 y 3 (Reducción desde problema conocido $\text{Ciclo Hamiltoniano} \le_P \text{TSP}$):**
   * Dada una instancia $G = (V, E)$ de **Ciclo Hamiltoniano** con $n = |V|$ vértices:
   * **Transformación en lenguaje natural:**
     1. Creamos un **grafo completo $G'$** con las mismas $n$ ciudades (conectamos todos los pares de vértices entre sí).
     2. Asignamos el peso de cada arista $(u, v)$ en $G'$ así:
        * **Peso $1$** si la arista $(u, v)$ **existía** en el grafo original $G$.
        * **Peso $2$** si la arista $(u, v)$ **no existía** en $G$ (arista agregada con penalización).
     3. Fijamos el presupuesto máximo del tour en **$k = n$**.
   * **Cuánto tarda:** Armar la matriz de costos de $n \times n$ consultando las aristas de $G$ toma tiempo **$\mathcal{O}(n^2)$** (polinomial).
3. **Paso 4 (Ida y Vuelta $\iff$):**
   * **($\implies$) Ida (Si $G$ tiene Ciclo Hamiltoniano $\implies G'$ tiene tour TSP de costo $\le n$):**
     El Ciclo Hamiltoniano recorre los $n$ vértices y vuelve al origen usando exactamente $n$ aristas originales de $G$. En $G'$ todas esas aristas pesan $1$, por lo que ese mismo ciclo es un tour válido de TSP con costo total $n \times 1 = n \le k$.
   * **($\impliedby$) Vuelta (Si $G'$ tiene tour TSP de costo $\le n \implies G$ tiene Ciclo Hamiltoniano):**
     Cualquier tour cerrado que visite las $n$ ciudades usa exactamente $n$ aristas, y cada arista en $G'$ cuesta al menos $1$. Si el tour hubiera usado aunque sea **una sola arista de peso $2$**, su costo total sería como mínimo $2 + (n - 1) \times 1 = n + 1 > n$, lo cual es imposible. Por lo tanto, las $n$ aristas del tour tienen **todas peso $1$**, existen en $G$ y forman un Ciclo Hamiltoniano.

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

#### 2. Semi-Pseudocódigo Simplificado del Verificador y la Transformación

```text
FUNCION VerificadorTSP(G', k, certificado_tour):
    SI tamaño(certificado_tour) != tamaño(V(G')) O tiene vértices repetidos:
        RETORNAR FALSO
    costo_total <- 0
    PARA i <- 0 HASTA n - 1:
        u <- certificado_tour[i]
        v <- certificado_tour[(i + 1) mod n]
        costo_total <- costo_total + peso(G', u, v)
    RETORNAR (costo_total <= k) // Tiempo O(n)

FUNCION TransformarCicloHamiltonianoATSP(G = (V, E)):
    n <- tamaño(V)
    Crear grafo completo G' con los mismos n vértices de V

    PARA CADA par (u, v) EN V x V con u != v:
        SI (u, v) PERTENECE A E:
            peso(G', u, v) <- 1   // Arista real de G
        SINO:
            peso(G', u, v) <- 2   // Arista ficticia penalizada

    k <- n
    RETORNAR OraculoTSP(G', k) // Transformación en O(n^2)
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Asignar peso 0 a las aristas existentes y 1 a las inexistentes:</strong> Si se pone peso 0 a las aristas existentes y cota $k = 0$, matemáticamente es válido, pero muchos docentes exigen pesos estrictamente positivos ($w(e) > 0$). Con pesos $\{1, 2\}$ y cota $k = n$, se respeta la formulación clásica de TSP métrico.</li>
    <li><strong>No explicar por qué no puede haber aristas de peso 2 en la vuelta:</strong> Hay que mencionar explícitamente que si usara una sola arista de peso 2, el tour de $n$ aristas costaría al menos $n + 1 > n$.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 7.3: Reducciones Numéricas (Cambio de Monedas a Subset Sum)

Demostración de que la versión de decisión del problema de cambio de monedas no es más difícil que Subset Sum y análisis de equivalencia en la clase NP-Completo.

---

### Ejercicio 73 — Reducción de Cambio de Monedas a Subset Sum

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Parcial 2024-2-1 (5 de noviembre de 2024), Ejercicio 5  
**Qué evalúa la cátedra:** Concepto de orden de dificultad entre problemas en NP, transformación con copias de monedas y comprensión de que dos problemas NP-Completos se reducen mutuamente.

**Enunciado**  
Demostrar formalmente que el problema del **Cambio de Monedas** (en su versión de decisión: dadas denominaciones enteras $D = \{d_1, \dots, d_m\}$, un entero objetivo $V$ y una cota $k$, ¿es posible dar cambio de valor exacto $V$ utilizando a lo sumo $k$ monedas?) **no es más difícil** que el problema de la **Suma de Subconjuntos (Subset Sum)**.  
¿Es posible demostrar la reducción en sentido inverso? Fundamentar en base a las clases de complejidad teóricas.

#### 1. Idea y Justificación en Lenguaje Natural (Los 4 Pasos para la Hoja del Parcial)

**Qué significa "no es más difícil":** Significa probar que **$\text{Cambio de Monedas} \le_P \text{Subset Sum}$**.

1. **Paso 1 (Pertenece a NP — Verificador):**
   * **Certificado:** Una lista de monedas elegidas (o un subconjunto de números en Subset Sum).
   * **Verificación en tiempo polinomial:** Chequeamos que la cantidad de monedas sea $\le k$, que cada moneda pertenezca al conjunto $D$ y que la suma de sus valores sea exactamente $V$. Sumar lleva tiempo lineal en la cantidad de elementos y bits $\implies$ ambos pertenecen a **NP**.
2. **Paso 2 y 3 (Reducción $\text{Cambio de Monedas} \le_P \text{Subset Sum}$):**
   * En *Cambio de Monedas* podemos repetir denominaciones y usar a lo sumo $k$ monedas en total; en *Subset Sum* cada elemento de la lista se puede usar a lo sumo $1$ vez y no hay tope de cantidad de elementos.
   * **Transformación en lenguaje natural:**
     1. Como en total se usan a lo sumo $k$ monedas, creamos una lista $L$ **repitiendo $k$ veces cada denominación $d_i$** (obtenemos $m \cdot k$ elementos).
     2. Para obligar a que *Subset Sum* elija exactamente $k' \le k$ monedas que sumen $V$, codificamos cada moneda en base $M = k + 1$: reemplazamos cada copia de $d_i$ por el número **$e_i = d_i \cdot (k + 1) + 1$** (el $+1$ cuenta cuántas monedas se usan sin generar acarreo porque $k' < k + 1$).
     3. Consultamos si existe un subconjunto de $L$ que sume **$W = V \cdot (k + 1) + k'$** (para algún $k' \in \{1, \dots, k\}$, o agregando $k$ elementos comodín de valor $1$ y pidiendo suma exacta $W = V \cdot (k + 1) + k$).
   * **Cuánto tarda:** Generar los $m \cdot k$ elementos de la lista $L$ toma tiempo **$\mathcal{O}(m \cdot k)$**.
3. **Paso 4 (Ida y Vuelta $\iff$ y Reducción Inversa):**
   * **($\implies$) Ida:** Si existen $k' \le k$ monedas que suman $V$, tomamos esas $k'$ copias en $L$ (más $k - k'$ comodines de valor $1$); su suma en la parte alta da $V \cdot (k + 1)$ y en las unidades da $k' + (k - k') = k$, sumando exactamente $W$.
   * **($\impliedby$) Vuelta:** Si un subconjunto de $L$ suma $W = V \cdot (k + 1) + k$, como la suma de los $+1$ no puede superar $k < k + 1$ (no hay acarreo hacia el múltiplo de $k + 1$), obligatoriamente se eligieron a lo sumo $k$ monedas cuyos valores originales suman exactamente $V$.
   * **¿Se puede reducir en sentido inverso ($\text{Subset Sum} \le_P \text{Cambio de Monedas}$)? SÍ:** Porque *Subset Sum* pertenece a **NP** y *Cambio de Monedas* (con valores en binario) es **NP-Completo**; por definición, todo problema en NP se reduce polinomialmente a cualquier problema NP-Completo.

```mermaid
flowchart LR
    I["Instancia Cambio de Monedas:<br/>D = {d₁..dₘ}, monto V, cota k"]:::src --> R["Expansión en k copias:<br/>L tiene m · k elementos"]:::step
    R --> G["Gadget Base M = k + 1:<br/>eᵢ = dᵢ · (k+1) + 1<br/>+ k comodines de valor 1"]:::step
    G --> SS(["Oráculo Subset Sum:<br/>¿Suma exacta W = V·(k+1) + k?"]):::opt
    classDef src fill:#1e40af,stroke:#1e3a8a,stroke-width:2px,color:#fff
    classDef step fill:#334155,stroke:#1e293b,stroke-width:1px,color:#fff
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 2. Semi-Pseudocódigo Simplificado del Verificador y la Transformación

```text
FUNCION VerificadorCambioMonedas(D, V, k, certificado_monedas):
    SI tamaño(certificado_monedas) > k:
        RETORNAR FALSO
    suma <- 0
    PARA CADA m EN certificado_monedas:
        SI m NO PERTENECE A D:
            RETORNAR FALSO
        suma <- suma + m
    RETORNAR (suma == V)

FUNCION TransformarCambioMonedasASubsetSum(D, V, k):
    M <- k + 1
    L <- lista_vacia()

    // 1. Agregar k copias de cada moneda desplazadas en base M = k + 1
    PARA CADA d_i EN D:
        PARA r <- 1 HASTA k:
            agregar (d_i * M + 1) a L

    // 2. Agregar k elementos comodín de valor 1 (para completar exactamente k unidades)
    PARA r <- 1 HASTA k:
        agregar 1 a L

    W_objetivo <- V * M + k
    RETORNAR OraculoSubsetSum(L, W_objetivo)
```

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

### Ejercicio 74 — Reducción Dual: Independent Set a Vertex Cover

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Guía de Ejercicios 07, Ejercicio 3  
**Qué evalúa la cátedra:** Comprensión de la dualidad entre Independent Set y Vertex Cover por complemento en tiempo `O(1)`.

**Enunciado**  
Dados los problemas de decisión de **Independent Set** (¿existe un subconjunto de vértices $I \subseteq V$ de tamaño $|I| \ge k$ tal que no existan aristas entre vértices de $I$?) y **Vertex Cover** (¿existe un subconjunto $S \subseteq V$ de tamaño $|S| \le k'$ que cubra todas las aristas de $E$?):
1. Diseñar una reducción polinomial formal de **Independent Set a Vertex Cover**.
2. Demostrar rigurosamente la equivalencia lógica fundamentando el teorema del complemento en teoría de grafos.

#### 1. Idea y Justificación en Lenguaje Natural (Los 4 Pasos para la Hoja del Parcial)

1. **Paso 1 (Pertenece a NP — Verificador de Vertex Cover):**
   * **Certificado:** Un subconjunto de vértices $S \subseteq V$.
   * **Verificación en tiempo polinomial:** Chequeamos que $|S| \le k'$ y recorremos todas las aristas $(u, v) \in E$ verificando que para cada una se cumpla $u \in S$ o $v \in S$. Esto tarda **$\mathcal{O}(|V| + |E|)$** (polinomial) $\implies \text{Vertex Cover} \in \text{NP}$.
2. **Paso 2 y 3 (Reducción desde problema conocido $\text{Independent Set} \le_P \text{Vertex Cover}$):**
   * Dada una instancia $(G = (V, E), k)$ de **Independent Set** (sabemos que es NP-Completo):
   * **Transformación en lenguaje natural:**
     1. Mantenemos **exactamente el mismo grafo $G' = G$**.
     2. Fijamos la cota máxima del Vertex Cover como **$k' = |V| - k$**.
   * **Cuánto tarda:** Es una simple resta aritmética sobre el mismo grafo, por lo que tarda **$\mathcal{O}(1)$** (o $\mathcal{O}(|V| + |E|)$ si se copia el grafo).
3. **Paso 4 (Ida y Vuelta $\iff$ por el Teorema del Complemento):**
   * **Propiedad clave:** Un conjunto $I \subseteq V$ es un *Independent Set* en $G$ si y solo si su complemento $S = V \setminus I$ es un *Vertex Cover* en $G$.
   * **($\implies$) Ida (Si $G$ tiene Independent Set $I$ de tamaño $\ge k \implies G'$ tiene Vertex Cover de tamaño $\le |V| - k$):**
     Tomamos $S = V \setminus I$. Su tamaño es $|S| = |V| - |I| \le |V| - k = k'$. Además, para cualquier arista $(u, v) \in E$, como $I$ es independiente no pueden estar $u$ y $v$ ambos en $I$; por lo tanto, al menos uno de los dos está afuera de $I$, es decir, pertenece a $S = V \setminus I$. Así, $S$ cubre todas las aristas.
   * **($\impliedby$) Vuelta (Si $G'$ tiene Vertex Cover $S$ de tamaño $\le k' = |V| - k \implies G$ tiene Independent Set de tamaño $\ge k$):**
     Tomamos $I = V \setminus S$. Su tamaño es $|I| = |V| - |S| \ge |V| - (|V| - k) = k$. Como toda arista $(u, v) \in E$ tiene al menos un extremo en $S$, ninguna arista puede tener sus dos extremos en $V \setminus S = I$. Por ende, $I$ es un conjunto independiente válido de tamaño $\ge k$.

```mermaid
flowchart LR
    IS["Independent Set I: tamaño |I| ≥ k"] ---|Complemento Exacto S = V \ I| VC["Vertex Cover S: tamaño |S| ≤ |V| - k"]
```

#### 2. Semi-Pseudocódigo Simplificado del Verificador y la Transformación

```text
FUNCION VerificadorVertexCover(G = (V, E), k_prima, certificado_S):
    SI tamaño(certificado_S) > k_prima:
        RETORNAR FALSO
    PARA CADA arista (u, v) EN E:
        SI u NO PERTENECE A certificado_S Y v NO PERTENECE A certificado_S:
            RETORNAR FALSO
    RETORNAR VERDADERO // Tiempo O(|V| + |E|)

FUNCION TransformarISaVertexCover(G = (V, E), k):
    G_prima <- G
    k_prima <- tamaño(V) - k
    RETORNAR (G_prima, k_prima) // Transformación en O(1)
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Invertir el sentido de las desigualdades:</strong> Olvidar que Independent Set es un problema de <strong>maximización</strong> ($|I| \ge k$) mientras que Vertex Cover es de <strong>minimización</strong> ($|S| \le k'$). Al restar del total $|V|$, la desigualdad se invierte automáticamente ($|I| \ge k \iff |V| - |I| \le |V| - k$).</li>
  </ul>
</div>

---

### Errores Fatales en Exámenes sobre Reducciones NP

1. **Reducir en la dirección equivocada ($B \le_P A$ en lugar de $A \le_P B$):** Es el error más grave de toda la materia. Si se pide probar que $B \in \text{NPC}$, la reducción DEBE partir del problema conocido $A$ y llegar al nuevo problema $B$. Reducir al revés tiene calificación automática de 0 puntos en la pregunta.
2. **Omitir el Paso 1 ($B \in \text{NP}$):** No definir el certificado o no justificar la verificación polinomial impide calificar el problema como NP-Completo (solo quedaría como NP-Hard).
3. **Probar únicamente la implicación de ida ($\implies$):** Demostrar que si $I_A \in \text{YES} \implies I_B \in \text{YES}$ no es suficiente. Debe demostrarse rigurosamente la vuelta ($\impliedby$) para asegurar que instancias $\text{NO}$ de $A$ no produzcan falsos positivos en $B$.
4. **Usar algoritmos exponenciales en la transformación:** La función de mapeo $f(I_A)$ debe ejecutarse en tiempo estrictamente polinomial $O(n^c)$. Si la reducción requiere calcular algo NP-Hard antes de armar la instancia, la reducción queda invalidada.
"""
