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

#### 1. Enunciado Completo
Un conjunto dominante (*Dominating Set*) en un grafo no dirigido $G = (V, E)$ es un subconjunto de vértices $D \subseteq V$ tal que todo vértice $v \in V$ pertenece a $D$ o es adyacente a al menos un vértice en $D$.  
El problema de decisión de Dominating Set plantea: dado un grafo $G = (V, E)$ y un entero positivo $k \le |V|$, ¿existe un conjunto dominante $D$ tal que $|D| \le k$?  
Demostrar formalmente que **Dominating Set es NP-Completo**, reduciendo desde **Vertex Cover**.

#### 2. Demostración Directa (Lista para Hoja de Examen)

##### Paso 1: Dominating Set está en NP
Si alguien nos entrega un subconjunto de vértices `certificado_D` como posible solución, podemos verificar si es válido en tiempo polinomial:
1. Chequeamos que `certificado_D` tenga a lo sumo `k` vértices.
2. Recorremos cada vértice de `certificado_D` y marcamos como "dominados" a él mismo y a todos sus vecinos directos.
3. Al terminar, nos fijamos si la cantidad de vértices marcados es igual al total de vértices del grafo.

Como solo recorremos los vértices y sus aristas una vez, el verificador tarda `O(V + E)` (polinomial). Por lo tanto, **Dominating Set pertenece a NP**.

##### Paso 2 y 3: Reducción Polinomial desde Vertex Cover (`Vertex Cover <=p Dominating Set`)
Sabemos que **Vertex Cover (VC)** es NP-Completo (¿existen a lo sumo `k` vértices que toquen todas las aristas de `G`?).  
Dada una instancia `(G, k)` de Vertex Cover:
1. **Vértices aislados:** Asumimos sin pérdida de generalidad que `G` no tiene vértices aislados (sin aristas), ya que en Vertex Cover no sirven para cubrir ninguna arista y se pueden eliminar antes de empezar en `O(V)`.
2. **Construcción del grafo `G'`:**
   - Copiamos todos los vértices y aristas originales de `G`.
   - **Por cada arista `(u, v)` de `G`, agregamos un vértice auxiliar nuevo `w_uv` y lo conectamos tanto a `u` como a `v`** (formando un triángulo entre `u`, `v` y `w_uv`).
3. **Cota:** Mantenemos el mismo límite **`k' = k`**.

*Complejidad de la transformación:* Solo agregamos un vértice y dos aristas por cada arista original, lo que toma tiempo `O(V + E)` (polinomial).

#### 3. Demostración de Equivalencia (Ida y Vuelta)

##### ($\implies$) Ida: Si `G` tiene un Vertex Cover de tamaño `<= k`, entonces `G'` tiene un Dominating Set de tamaño `<= k`
Elegimos exactamente los mismos vértices del Vertex Cover como nuestro conjunto dominante `D` en `G'`.
- **Los vértices nuevos `w_uv` quedan dominados:** Como el Vertex Cover cubría todas las aristas de `G`, para cada arista `(u, v)` al menos uno de sus extremos (`u` o `v`) está en `D`. Como `w_uv` es vecino de ambos, queda dominado.
- **Los vértices originales de `G` quedan dominados:** Como no hay vértices aislados, todo vértice `u` tiene al menos una arista `(u, v)`. Si `u` fue elegido en `D`, se domina a sí mismo; si no fue elegido, obligatoriamente su vecino `v` está en `D` (para cubrir esa arista) y lo domina.
Por lo tanto, `D` domina todo `G'` usando a lo sumo `k` vértices.

##### ($\impliedby$) Vuelta: Si `G'` tiene un Dominating Set de tamaño `<= k`, entonces `G` tiene un Vertex Cover de tamaño `<= k`
Tomamos el conjunto dominante de `G'`.
- **Reemplazo de vértices nuevos:** Si el conjunto dominante incluye algún vértice auxiliar `w_uv`, lo cambiamos por `u` (o por `v`). Hacer este cambio **no aumenta la cantidad de vértices** y no pierde cobertura, porque `w_uv` solo tenía como vecinos a `u` y `v` (y `u` también los cubre a ambos, además de cubrir a otros posibles vecinos).
- Tras reemplazar todos los vértices auxiliares, nos queda un conjunto de a lo sumo `k` vértices formado **únicamente por vértices originales de `G`**.
- **Por qué es un Vertex Cover:** Para cada arista `(u, v)` de `G`, su vértice auxiliar `w_uv` está dominado. Como ningún `w_uv` quedó dentro del conjunto elegido, sí o sí tiene que estar elegido al menos uno de sus únicos dos vecinos (`u` o `v`). Esto garantiza que toda arista `(u, v)` de `G` tiene al menos un extremo elegido.

**Conclusión Final:** Como Dominating Set está en NP y transformamos Vertex Cover en Dominating Set en tiempo polinomial probando la equivalencia de ida y vuelta, **Dominating Set es NP-Completo**.

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

#### 6. Pseudocódigo del Verificador y Reducción (Estilo Examen Presencial)

```text
Algoritmo VerificadorDominatingSet(G = (V, E), k, certificado_D):
    // 1. Verificar tamaño de la cota en O(1)
    si tamaño(certificado_D) > k:
        devolver Falso

    // 2. Construir conjunto de vértices dominados en O(V + E)
    dominados = conjunto_vacío()
    para cada u in certificado_D:
        agregar u a dominados             // Se domina a sí mismo
        para cada vecino v in G.adyacentes(u):
            agregar v a dominados         // Domina a sus vecinos

    // 3. Verificar cobertura total
    si tamaño(dominados) == cantidad(V):
        devolver Verdadero  // Certificado válido en tiempo polinomial O(V + E)
    sino:
        devolver Falso

Algoritmo TransformarVCaDominatingSet(G = (V, E), k):
    // Construir G' = (V', E') en tiempo O(V + E)
    V' = copiar(V)
    E' = copiar(E)

    para cada arista e = (u, v) in E:
        crear nuevo vértice auxiliar w_e
        agregar w_e a V'
        agregar aristas (u, w_e) y (v, w_e) a E'

    k' = k
    devolver (G', k')
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

### Ejercicio 72 — El Dilema de Marco el Cadete: Reducción de Ciclo Hamiltoniano a TSP

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★★☆ (4/5)  
**Origen:** Parcial 2025-1-1 (27 de mayo de 2025), Ejercicio 5  
**Qué evalúa la cátedra:** Reducción entre problemas NP-Completos de grafos, diseño de matrices de costo con penalización asimétrica (gadget métrico), y prueba bidireccional.

#### 1. Enunciado Completo
Marco, el cadete administrativo de una empresa de logística, compró un costoso paquete de software para resolver el **Problema del Viajante de Comercio** (TSP en su versión de decisión), cuando la gerencia le había solicitado explícitamente un módulo para resolver **Ciclo Hamiltoniano**. El vendedor del software le aseguró a Marco:  
*"Si puedes resolver TSP de decisión en un grafo completo ponderado, puedes resolver exactamente Ciclo Hamiltoniano en cualquier grafo en el mismo orden de tiempo"*.  
Definiciones formales:
- **Ciclo Hamiltoniano (HC):** Dado un grafo no dirigido $G = (V, E)$, determinar si existe un ciclo simple que visite todos los vértices de $V$ exactamente una vez y retorne al origen.
- **TSP (Decisión):** Dado un grafo completo $G' = (V', E')$ con pesos enteros $w(e) \ge 0$ en las aristas y un entero $k$, determinar si existe un tour cerrado que visite cada vértice una única vez con costo total $\le k$.
Determinar con fundamento formal si el vendedor tiene razón o si hay que despedir a Marco. Desarrollar la reducción polinomial completa con demostración de equivalencia.

#### 2. Demostración Directa (Lista para Hoja de Examen)

**El vendedor tiene razón.** Demostraremos que podemos transformar cualquier problema de **Ciclo Hamiltoniano** en uno de **TSP (Decisión)** en tiempo polinomial (`Ciclo Hamiltoniano <=p TSP`), por lo que el software de TSP sirve para resolver Ciclo Hamiltoniano.

##### 1. Transformación Polinomial (`O(V^2)`)
Dado el grafo `G` de Ciclo Hamiltoniano con `n` vértices:
1. Creamos un **grafo completo `G'`** con las mismas `n` ciudades (conectamos todos contra todos).
2. Asignamos los pesos de las aristas en `G'` con esta regla simple:
   - **Peso `1`** si la arista **existía** en el grafo original `G`.
   - **Peso `2`** si la arista **no existía** en `G` (arista agregada con penalización).
3. Fijamos el límite de costo máximo del tour en **`k = n`**.

*Complejidad:* Armar la matriz de `n x n` consultando si cada arista existía o no en `G` toma tiempo `O(n^2)` (polinomial).

##### 2. Demostración de Equivalencia (Ida y Vuelta)

- **($\implies$) Ida: Si `G` tiene un Ciclo Hamiltoniano $\to$ `G'` tiene un tour TSP de costo `<= n`:**
  - El Ciclo Hamiltoniano pasa por las `n` ciudades y vuelve al inicio usando exactamente `n` aristas que sí existen en `G`.
  - En `G'`, todas esas aristas tienen peso `1`.
  - Por lo tanto, ese mismo recorrido es un tour válido de TSP con costo total `n * 1 = n <= k`.

- **($\impliedby$) Vuelta: Si `G'` tiene un tour TSP de costo `<= n` $\to$ `G` tiene un Ciclo Hamiltoniano:**
  - Todo tour de TSP que recorre las `n` ciudades y vuelve al origen usa exactamente `n` aristas.
  - Como todas las aristas de `G'` cuestan `1` o `2`, **es imposible que el tour haya usado siquiera una arista de peso `2`**: si usara aunque sea una de peso `2`, como las otras `n - 1` cuestan al menos `1`, el costo total sería como mínimo `2 + (n - 1) = n + 1`, superando el límite `n`.
  - Entonces, las `n` aristas usadas tienen sí o sí **peso `1`**, lo que significa que todas existían en el grafo original `G` y forman un Ciclo Hamiltoniano válido.

**Conclusión:** Marco puede cargar la matriz con pesos `1` y `2` y tope `k = n` en el software de TSP. Si el software responde que sí existe tour, hay Ciclo Hamiltoniano; si responde que no, no existe. **El vendedor tenía razón y Marco conserva su empleo.**

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

#### 4. Pseudocódigo de la Reducción Polinomial (Estilo Examen Presencial)

```text
Algoritmo ReducirCicloHamiltonianoATSP(G = (V, E)):
    n = cantidad(V)
    Crear grafo completo G' = (V, E') con pesos en aristas:

    para cada par de vértices u, v in V con u != v:
        si (u, v) in E:
            peso(u, v) = 1    // Arista original presente
        sino:
            peso(u, v) = 2    // Arista penalizada inexistente en G

    cota_k = n  // Cota de costo del tour

    // Se entrega la instancia (G', cota_k) al resolvedor de decisión de TSP
    devolver (G', cota_k)
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

#### 1. Enunciado Completo
Demostrar formalmente que el problema del **Cambio de Monedas** (en su versión de decisión: dadas denominaciones enteras $D = \{d_1, \dots, d_m\}$, un entero objetivo $V$ y una cota $k$, ¿es posible dar cambio de valor exacto $V$ utilizando a lo sumo $k$ monedas?) **no es más difícil** que el problema de la **Suma de Subconjuntos (Subset Sum)**.  
¿Es posible demostrar la reducción en sentido inverso? Fundamentar en base a las clases de complejidad teóricas.

#### 2. Demostración Directa (Lista para Hoja de Examen)

**¿Qué significa "no es más difícil"?**  
Decir que *Cambio de Monedas* no es más difícil que *Subset Sum* significa que podemos reducir `Cambio de Monedas <=p Subset Sum` en tiempo polinomial.

##### 1. Transformación Polinomial (`O(m * k)`)
La diferencia entre ambos problemas es que en *Cambio de Monedas* podemos repetir una misma denominación y tenemos un tope de `k` monedas, mientras que en *Subset Sum* cada número de la lista se puede elegir una sola vez.
1. **Expandir en copias:** Como en total se usan a lo sumo `k` monedas, ninguna denominación puede usarse más de `k` veces. Creamos una lista `L` repitiendo `k` veces cada denominación disponible (total: `m * k` números).
2. **Controlar el límite de `k` monedas:** Para que Subset Sum controle al mismo tiempo que el valor sume `V` y que no se elijan más de `k` elementos, desplazamos los números multiplicando por `M = k + 1` y sumando `1`:
   - Cada moneda de valor `d` pasa a valer **`d * (k + 1) + 1`** (el `+1` final actúa como contador de monedas).
   - Buscamos si existe un subconjunto que sume **`W = V * (k + 1) + k'`** (para alguna cantidad `k'` de `1` a `k` monedas).
- *Complejidad:* Generar los `m * k` números toma tiempo `O(m * k)` (polinomial respecto a `m` y `k`).

##### 2. Equivalencia (Ida y Vuelta)
- **($\implies$) Ida:** Si se puede formar el monto `V` usando `k'` monedas (`k' <= k`), eligiendo esas mismas `k'` copias en la lista `L` la parte alta suma `V * (k + 1)` y los `+1` suman `k'`, alcanzando exactamente `W`.
- **($\impliedby$) Vuelta:** Si un subconjunto de la lista `L` suma `W`, como cada elemento elegido aporta `+1` y `k' < k + 1` no puede producir acarreo hacia el monto, obligatoriamente se eligieron `k' <= k` monedas cuyos valores suman exactamente `V`.

##### 3. ¿Se puede demostrar al revés (`Subset Sum <=p Cambio de Monedas`)?
**SÍ, totalmente.**  
- *Justificación directa:* *Subset Sum* está en **NP** y la versión de decisión de *Cambio de Monedas* (con valores en binario) es **NP-Completa**. Por definición de NP-Completitud, **cualquier problema de la clase NP se puede reducir en tiempo polinomial a un problema NP-Completo**, por lo que ambos problemas tienen la misma dificultad teórica.

#### 3. Diagrama Visual del Gadget de Réplicas y Base $M = k + 1$

```mermaid
flowchart LR
    I["Instancia Cambio de Monedas:<br/>D = {d₁..dₘ}, monto V, cota k"]:::src --> R["Expansión en k copias:<br/>L tiene m · k elementos"]:::step
    R --> G["Gadget Base M = k + 1:<br/>eᵢ⁽ʳ⁾ = dᵢ · M + 1<br/>Objetivo W = V · M + k'"]:::step
    G --> SS(["Oráculo Subset Sum:<br/>¿Existe subconjunto que sume W?"]):::opt
    classDef src fill:#1e40af,stroke:#1e3a8a,stroke-width:2px,color:#fff
    classDef step fill:#334155,stroke:#1e293b,stroke-width:1px,color:#fff
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
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

#### 1. Enunciado Completo
Dados los problemas de decisión de **Independent Set** (¿existe un subconjunto de vértices $I \subseteq V$ de tamaño $|I| \ge k$ tal que no existan aristas entre vértices de $I$?) y **Vertex Cover** (¿existe un subconjunto $S \subseteq V$ de tamaño $|S| \le k'$ que cubra todas las aristas de $E$?):
1. Diseñar una reducción polinomial formal de **Independent Set a Vertex Cover**.
2. Demostrar rigurosamente la equivalencia lógica fundamentando el teorema del complemento en teoría de grafos.

#### 2. Demostración Directa de la Propiedad del Complemento

**Propiedad Clave:**  
En cualquier grafo `G`, un grupo de vértices `S` es un **Independent Set** (ninguna arista une dos vértices de `S`) si y solo si los vértices restantes **`V - S`** forman un **Vertex Cover** (toda arista toca al menos un vértice de `V - S`).

- **($\implies$) Si `S` es un Independent Set $\to$ el resto `V - S` es un Vertex Cover:**
  - Tomemos cualquier arista `(u, v)` del grafo.
  - Como en `S` no puede haber dos vértices conectados entre sí, es imposible que tanto `u` como `v` estén ambos dentro de `S`.
  - Por lo tanto, al menos uno de los dos (`u` o `v`) quedó afuera de `S`, es decir, está en `V - S`.
  - Como esto pasa para todas las aristas, `V - S` cubre todas las aristas del grafo.

- **($\impliedby$) Si `V - S` es un Vertex Cover $\to$ `S` es un Independent Set:**
  - Como `V - S` cubre todas las aristas del grafo, toda arista tiene al menos un extremo en `V - S`.
  - Eso significa que ninguna arista puede tener sus dos extremos dentro de `S`.
  - Por lo tanto, no hay aristas entre vértices de `S`, así que `S` es un conjunto independiente válido.

#### 3. Transformación Polinomial (`O(1)`)

Dada una instancia `(G, k)` de Independent Set:
1. Dejamos exactamente el mismo grafo: **`G' = G`**.
2. Fijamos el límite de tamaño para Vertex Cover como **`k' = |V| - k`**.
- *Complejidad:* Solo hacemos una resta en tiempo `O(1)` (polinomial).

#### 4. Equivalencia (Ida y Vuelta)
- **Ida:** Si `G` tiene un Independent Set `S` de tamaño **al menos `k`**, entonces los vértices restantes `V - S` son un Vertex Cover de tamaño **a lo sumo `|V| - k = k'`**.
- **Vuelta:** Si `G` tiene un Vertex Cover `C` de tamaño **a lo sumo `k' = |V| - k`**, entonces los vértices restantes `V - C` son un Independent Set de tamaño **al menos `|V| - (|V| - k) = k`**.

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
