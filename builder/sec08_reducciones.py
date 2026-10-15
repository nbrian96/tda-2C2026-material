"""Módulo 8: Reducciones Polinomiales y NP-Completitud."""

def get_content():
    return r"""## 10. Tema 7: Reducciones Polinomiales y NP-Completitud

### Conceptos Mínimos de Supervivencia

1. **Definiciones Formales de Clases de Complejidad:**
   * **Clase P:** Problemas de decisión que pueden resolverse mediante un algoritmo determinístico en tiempo polinomial (O(nᵏ)).
   * **Clase NP (Nondeterministic Polynomial):** Problemas de decisión cuyas respuestas afirmativas (*instancias YES*) admiten un **certificado** (o testigo) que puede ser verificado por un algoritmo en tiempo polinomial.
   * **Reducción Polinomial de Karp (A ≤_P B):** Significa que el problema A se reduce en tiempo polinomial al problema B. Interpretación: *"El problema A no es más difícil que el problema B (a lo sumo tan difícil como B)"*. Si contamos con un algoritmo eficiente para B, podemos resolver A eficientemente.
   * **Clase NP-Completo (NPC):** Un problema B es NP-Completo si y solo si:
     1. B ∈ NP.
     2. Para todo A ∈ NP, A ≤_P B (es decir, B es NP-Hard).
2. **El Esquema Sagrado de 4 Pasos Obligatorios para Demostrar que B ∈ NPC:**
   En las correcciones de la cátedra, omitir cualquiera de estos 4 pasos implica la pérdida automática de la mayor parte del puntaje:
   * **Paso 1: Demostrar que B ∈ NP.**  
     Definir el certificado C de tamaño polinomial. Presentar el algoritmo verificador V(I_B, C) en pseudocódigo y justificar que corre en tiempo polinomial O(P(n)).
   * **Paso 2: Elegir un problema conocido A ∈ NPC.**  
     Elegir un problema cuya NP-Completitud ya sea conocida (Vertex Cover, 3-SAT, Ciclo Hamiltoniano, Independent Set, Subset Sum). **ATENCIÓN:** Se debe reducir **DESDE** el problema conocido **HACIA** el problema nuevo (A ≤_P B). Reducir al revés (B ≤_P A) es un error fatal.
   * **Paso 3: Definir la transformación polinomial f: I_A → I_B.**  
     Explicar cómo convertir cualquier instancia I_A del problema conocido en una instancia válida I_B del nuevo problema. Demostrar que la construcción de I_B toma tiempo polinomial.
   * **Paso 4: Demostración Bidireccional (Equivalencia Lógica):**  
     * (⟹) **Si I_A ∈ YES_A, entonces f(I_A) ∈ YES_B (Ida).**
     * (⟸) **Si f(I_A) ∈ YES_B, entonces I_A ∈ YES_A (Vuelta).**

---

### Patrón de Ejercicio 7.1: Reducciones sobre Grafos (Dominating Set desde Vertex Cover)

Aparece de forma reiterada en los parciales de 2024 (2ª y 3ª oportunidad).

---

### Ejercicio 28 — Demostración de NP-Completitud de Dominating Set (desde Vertex Cover)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-2 (Ej 5) y Parcial 2024-2-3 (Ej 5) / Guía 07 Ejercicio 2 y 14

**Enunciado**  
Un set dominante (*Dominating Set*) de un grafo G = (V, E) es un subconjunto D ⊆ V tal que todo vértice de G pertenece a D o es adyacente a un vértice en D. El problema de decisión de Dominating Set implica, dado un grafo G y un número entero k, determinar si existe un set dominante de a lo sumo tamaño k. Demostrar formalmente que Dominating Set es un problema NP-Completo, reduciendo desde Vertex Cover.

**Qué está evaluando**  
Ejecución rigurosa del esquema de 4 pasos, diseño de *gadgets* de aristas para transformar cobertura de aristas en dominancia de vértices, y demostración en ambos sentidos.

**Demostración Paso a Paso**

#### Paso 1: Dominating Set ∈ NP
* **Certificado C:** Un subconjunto de vértices D ⊆ V. Tamaño del certificado: |D| ≤ |V| (tamaño polinomial).
* **Verificador V(G, k, D):**
  1. Verifica que |D| ≤ k en O(1).
  2. Inicializa un arreglo booleano `dominado` de tamaño |V| en `FALSO`.
  3. Para cada vértice u ∈ D:
     * Marca `dominado[u] = VERDADERO`.
     * Para cada vecino v de u: marca `dominado[v] = VERDADERO`.
  4. Recorre el arreglo: si todos los vértices están marcados como `VERDADERO`, retorna `SI`; en caso contrario, retorna `NO`.
* **Complejidad del Verificador:** Recorrer D y sus adyacencias toma a lo sumo ∑_{u ∈ D} (1 + grado(u)) ≤ O(|V| + |E|). Como corre en tiempo polinomial, **Dominating Set ∈ NP**.

#### Paso 2: Selección del Problema Conocido
Elegimos **Vertex Cover (VC)**, cuya versión de decisión es NP-Completa:  
*Dado un grafo G = (V, E) y un entero k, ¿existe un subconjunto S ⊆ V con |S| ≤ k tal que toda arista (u, v) ∈ E tenga al menos uno de sus extremos en S?*  
Queremos demostrar:
> **Vertex Cover ≤_P Dominating Set**

#### Paso 3: Transformación Polinomial f(G, k) → (G', k')
Dada una instancia de Vertex Cover (G = (V, E), k):
1. Si G tiene aristas aisladas o vértices desconectados sin aristas, estos deben ser incluidos en el análisis. Asumimos sin pérdida de generalidad que G no tiene vértices aislados (un vértice aislado en VC no cubre aristas, en DS requiere dominarse a sí mismo).
2. Construimos un grafo G' = (V', E') de la siguiente manera:
   * Conservamos todos los vértices originales de G: V' = V ∪ V_aristas.
   * Para cada arista e = (u, v) ∈ E, agregamos un **nuevo vértice** w_e a V'.
   * Conectamos w_e mediante aristas con los dos extremos originales u y v: agregamos las aristas (u, w_e) y (v, w_e) a E'.
   * Mantenemos las aristas originales (u, v) ∈ E en E' (o bien un triángulo u - v - w_e).
3. Fijamos el tamaño objetivo del set dominante:
   > **k' = k**
* **Complejidad de la Transformación:** |V'| = |V| + |E| y |E'| = |E| + 2|E| = 3|E|. La construcción agrega un vértice y dos aristas por cada arista original, lo cual se realiza en tiempo O(|V| + |E|), que es estrictamente polinomial.

#### Paso 4: Demostración de Equivalencia Bidireccional

* **(⟹) Si G tiene un Vertex Cover S de tamaño ≤ k, entonces G' tiene un Dominating Set D de tamaño ≤ k:**
  * Elegimos D = S. Como |S| ≤ k, tenemos que |D| ≤ k.
  * Veamos que D domina todos los vértices de G':
    1. **Vértices nuevos w_e (asociados a aristas e = (u, v)):** Como S es un Vertex Cover de G, al menos uno de los extremos u o v pertenece a S. Dado que w_e es adyacente a u y a v en G', y al menos uno está en D, el vértice w_e está dominado.
    2. **Vértices originales u ∈ V:** Como no hay vértices aislados en G, u tiene al menos una arista incidente e = (u, v). Si u ∈ S, u ∈ D (se domina a sí mismo). Si u ∉ S, necesariamente v ∈ S = D (porque (u, v) debía estar cubierta), y como (u, v) ∈ E', u es adyacente a v ∈ D, por lo que u está dominado.
  * Por lo tanto, D es un Dominating Set válido de tamaño ≤ k.

* **(⟸) Si G' tiene un Dominating Set D' de tamaño ≤ k, entonces G tiene un Vertex Cover S de tamaño ≤ k:**
  * Supongamos que D' contiene algún vértice auxiliar w_e correspondiente a la arista e = (u, v).
  * El vértice w_e solo tiene dos vecinos en G': u y v. Si reemplazamos w_e en D' por u (o por v):
    * El nodo w_e sigue dominado (porque u ∈ D').
    * El nodo u ahora se domina a sí mismo.
    * Cualquier otro nodo dominado por w_e (que solo podían ser u o v) sigue dominado. Además, u podría dominar a otros vecinos originales en G.
    * Por lo tanto, el nuevo conjunto sigue siendo un Dominating Set y su tamaño no aumentó.
  * Realizando este reemplazo para todos los vértices auxiliares, obtenemos un set dominante D'' ⊆ V compuesto **exclusivamente por vértices originales de G**, con |D''| ≤ |D'| ≤ k.
  * Veamos que D'' es un Vertex Cover de G:
    * Para cada arista e = (u, v) ∈ E, el nodo auxiliar w_e en G' debía estar dominado por D''.
    * Los únicos vecinos de w_e en G' son u y v. Como w_e ∉ D'', necesariamente al menos u ∈ D'' o v ∈ D''.
    * Esto implica que toda arista (u, v) tiene al menos un extremo en D''.
  * Por lo tanto, S = D'' es un Vertex Cover de G de tamaño ≤ k.

**Conclusión Final**  
Habiendo probado que Dominating Set ∈ NP y que Vertex Cover ≤_P Dominating Set con equivalencia lógica en ambos sentidos, queda formalmente demostrado que **Dominating Set es NP-Completo**.

---

### Patrón de Ejercicio 7.2: Reducciones de Caminos y Ciclos (El Dilema de Marco el Cadete)

Reducción entre Ciclo Hamiltoniano y el Problema del Viajante de Comercio (TSP).

---

### Ejercicio 29 — El Dilema de Marco el Cadete: Reducción de Ciclo Hamiltoniano a TSP

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2025-1-1 (27 de mayo de 2025), Ejercicio 5

**Enunciado**  
Marco, el cadete de la empresa, compró un software que resuelve el problema del Viajante de Comercio (TSP en su versión de decisión) cuando le habían pedido un software para resolver Ciclo Hamiltoniano. El vendedor afirmó: *"Si puedes resolver TSP de decisión, puedes resolver fácilmente Ciclo Hamiltoniano"*.  
Recordemos:  
* **Ciclo Hamiltoniano:** Dado un grafo incompleto no dirigido G = (V, E), determinar si existe un ciclo simple que visite todos los vértices exactamente una vez y regrese al origen.  
* **TSP (Decisión):** Dado un grafo completo G' = (V', E') con pesos enteros w(e) en las aristas y un entero k, determinar si existe un tour que recorra todos los vértices sin repetir y vuelva al origen con costo total ≤ k.  
Determinar si el vendedor tiene razón o hay que despedir a Marco. Fundamentar construyendo la reducción polinomial formal.

**Qué está evaluando**  
Construcción de un grafo completo con ponderación de penalización (1 para aristas existentes, 2 o ∞ para inexistentes) y equivalencia lógica con cota k = |V|.

**Resolución y Demostración Formal**  
**El vendedor tiene razón.** Demostraremos que:
> **Ciclo Hamiltoniano ≤_P TSP (Decisión)**

#### 1. Transformación Polinomial f(G) → (G', w, k)
Dada una instancia de Ciclo Hamiltoniano G = (V, E) con n = |V| vértices:
1. Construimos un grafo completo G' = (V, E') con el mismo conjunto de vértices V, donde existe una arista entre todo par de vértices distintos u, v ∈ V.
2. Asignamos pesos w(u, v) a cada arista de G':
   > **w(u, v) = 1** si (u, v) ∈ E (la arista existía en el grafo original)  
   > **w(u, v) = 2** si (u, v) ∉ E (la arista no existía)
3. Fijamos el valor objetivo de costo del tour:
   > **k = n = |V|**
* **Costo de la Transformación:** Generar las C(n, 2) = O(n²) aristas y asignarles pesos 1 o 2 toma tiempo O(n²), que es polinomial.

#### 2. Equivalencia Bidireccional
* **(⟹) Si G tiene un Ciclo Hamiltoniano ⟹ G' tiene un tour TSP de costo ≤ n:**
  * Sea C = (v₁, v₂, ..., vₙ, v₁) un ciclo hamiltoniano en G.
  * Como todas las aristas de C pertenecen a E, cada arista (v_i, v_{i+1}) tiene peso w(v_i, v_{i+1}) = 1 en G'.
  * El ciclo C visita los n vértices una sola vez y tiene n aristas.
  * Costo total del tour en G': ∑_{i=1}^n 1 = n ≤ k.
  * Por lo tanto, (G', w, k) es una instancia YES de TSP.

* **(⟸) Si G' tiene un tour TSP de costo ≤ n ⟹ G tiene un Ciclo Hamiltoniano:**
  * Sea T = (u₁, u₂, ..., uₙ, u₁) un tour que visita todos los vértices en G' con costo ≤ n.
  * El tour consta de exactamente n aristas.
  * Por construcción, los pesos posibles son únicamente 1 o 2.
  * Si el tour utilizara al menos una arista que no pertenecía a E (peso 2), el costo total sería al menos:
    > **Costo(T) ≥ 1 · (n - 1) + 2 = n + 1 > n**
  * Para que el costo total sea ≤ n, **todas las n aristas del tour deben tener obligatoriamente peso 1**.
  * Por lo tanto, todas las aristas de T pertenecen a E, lo que implica que T es un Ciclo Hamiltoniano válido en G.

**Conclusión:** Marco puede usar el software de TSP para resolver Ciclo Hamiltoniano en tiempo polinomial. Por lo tanto, **el vendedor tiene razón y no hay que despedir a Marco**.

---

### Patrón de Ejercicio 7.3: Reducciones Numéricas (Cambio de Monedas a Subset Sum)

Comparación de dificultad entre problemas de la clase NP mediante reducciones de decisión.

---

### Ejercicio 30 — Reducción de Cambio de Monedas a Subset Sum

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-1 (5 de noviembre de 2024), Ejercicio 5

**Enunciado**  
Demostrar que el problema del cambio de monedas (en su versión de decisión: dadas monedas de denominaciones D y enteros k y V, ¿se puede dar cambio de valor exacto V usando a lo sumo k monedas?) no es más difícil que el de suma de subconjuntos (*Subset Sum*). ¿Es posible demostrarlo en sentido opuesto? ¿Por qué?

**Resolución y Demostración**  
* La frase *"el problema A no es más difícil que B"* equivale a demostrar:
  > **Cambio de Monedas ≤_P Subset Sum**
* En Subset Sum clásico cada elemento puede usarse a lo sumo **una sola vez**. En Cambio de Monedas, cada denominación puede usarse múltiples veces (hasta k veces).
* **Transformación:**
  1. Si permitimos usar hasta k monedas de cada denominación d ∈ D, creamos un multiconjunto de enteros L donde cada denominación d se replica k veces: L = {d^(1), d^(2), ..., d^(k) | ∀ d ∈ D}.
  2. Para controlar que la cantidad total de monedas usadas sea ≤ k, expandimos la representación o agregamos variables auxiliares con base alta.
  3. Fijamos el objetivo S = V.
* **¿Es posible demostrarlo en sentido opuesto (Subset Sum ≤_P Cambio de Monedas)?**
  * **Sí, es perfectamente posible:** Como Subset Sum es NP-Completo y Cambio de Monedas de decisión pertenece a NP, por definición de NP-Completitud, **todo problema en NP se reduce polinomialmente a Subset Sum y viceversa** (ambos son NP-Completos bajo codificación binaria de números).

---

### Patrón de Ejercicio 7.4: La Reducción Dual Canónica (Independent Set a Vertex Cover)

---

### Ejercicio 31 — Reducción Dual: Independent Set a Vertex Cover

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Guía de Ejercicios 07, Ejercicio 3

**Enunciado**  
Dados los problemas de decisión de Independent Set y Vertex Cover:  
1. Reducir Independent Set a Vertex Cover.  
2. Demostrar la equivalencia lógica fundamentando el teorema del complemento en teoría de grafos.

**Demostración Formal**  
* **Teorema Fundamental:** En cualquier grafo no dirigido G = (V, E), un subconjunto S ⊆ V es un **Independent Set** si y solo si su complemento V \ S es un **Vertex Cover**.
* **Demostración del Lema:**
  * (⟹) Si S es Independent Set, ningún par de vértices en S comparte arista. Por ende, para cualquier arista (u, v) ∈ E, es imposible que ambos extremos pertenezcan a S. Por lo tanto, al menos uno de los extremos debe pertenecer a V \ S. Esto prueba que V \ S cubre todas las aristas y es un Vertex Cover.
  * (⟸) Si V \ S es un Vertex Cover, cubre toda arista (u, v). Por ende, ninguna arista puede tener ambos extremos fuera de V \ S (es decir, en S). Por lo tanto, no hay aristas entre nodos de S, lo que prueba que S es un Independent Set.
* **Reducción Independent Set ≤_P Vertex Cover:**  
  Dada la instancia (G, k) de IS: construimos la instancia de VC (G, k') con el mismo grafo G y fijamos k' = |V| - k.  
  G tiene un IS de tamaño ≥ k ⟺ G tiene un VC de tamaño ≤ |V| - k.  
  La transformación copia el grafo y resta enteros en tiempo O(1).

---

### Errores Fatales en Exámenes sobre Reducciones NP

1. **Reducir al revés (B ≤_P A en lugar de A ≤_P B):** Si querés probar que B es NP-Completo, debés reducir **desde** el problema conocido A **hacia** tu nuevo problema B. Reducir al revés solo prueba que B es resoluble si A lo fuera, ¡lo cual no prueba NP-Dureza!
2. **Olvidar el Paso 1 (B ∈ NP):** Si no mostrás el certificado y el verificador polinomial, el problema solo califica como NP-Hard, no NP-Completo.
3. **Probar solo la ida (⟹) y olvidar la vuelta (⟸):** La equivalencia debe ser exacta: instancias NO de A deben mapear obligatoriamente a instancias NO de B.
"""
