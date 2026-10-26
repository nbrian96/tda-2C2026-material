"""Módulo 3: Algoritmos Greedy (Voraces)."""

def get_content():
    return r"""## 5. Tema 2: Algoritmos Greedy (Voraces)

### Conceptos Mínimos de Supervivencia

1. **Naturaleza de un Algoritmo Greedy:**
   En cada paso, toma la decisión que parece mejor en ese momento específico (óptimo local) bajo una regla de selección fija, sin mirar atrás ni reconsiderar elecciones previas (elección irrevocable).

2. **Propiedad de la Elección Voraz y Subestructura Óptima:**
   Para que un algoritmo greedy sea **óptimo**, debe cumplirse que:
   * Una elección voraz inicial conduce a una solución globalmente óptima (propiedad de elección voraz).
   * La solución óptima del problema global contiene dentro de sí soluciones óptimas a los subproblemas resultantes (subestructura óptima).

3. **Las Dos Técnicas Canónicas de Demostración de Optimalidad:**
   * **Greedy Stays Ahead ("El voraz se mantiene adelante"):** Se define una métrica de progreso $m(i)$. Se demuestra por inducción que en cada paso $k$, la solución voraz aventaja o iguala a cualquier solución óptima $OPT$ ($m(G_k) \le m(OPT_k)$ o $m(G_k) \ge m(OPT_k)$), garantizando que al finalizar no puede ser superada.
   * **Argumento de Intercambio (Exchange Argument):** Se toma una solución óptima hipotética $OPT$ que difiere de la solución greedy $G$. Se identifica la primera inversión o discrepancia y se demuestra que al intercambiar el elemento de $OPT$ por el elemento elegido por $G$, la calidad de la solución no empeora. Repitiendo el proceso, $OPT$ se transforma en $G$ sin perder valor, probando que $G$ también es óptima.

4. **Cómo Probar que una Idea Greedy es Incorrecta (El Contraejemplo):**
   Si en un examen te preguntan *"¿El algoritmo greedy propuesto es óptimo siempre? Indicar si es óptimo o dar un contraejemplo"*, **NUNCA** respondas con explicaciones vagas. Debes presentar un contraejemplo concreto:
   1. Definir una instancia pequeña con datos numéricos explícitos.
   2. Mostrar paso a paso qué elige el algoritmo greedy y cuál es su costo/beneficio obtenido.
   3. Mostrar una solución alternativa factible y su costo/beneficio estrictamente superior.
   4. Concluir formalmente: *Como $\text{Valor}(\text{Alternativa}) > \text{Valor}(\text{Greedy})$, el algoritmo no garantiza la solución óptima.*

---

### Patrón de Ejercicio 2.1: Interval Scheduling (Planificación de Intervalos No Solapados)

Aparece con diferentes metáforas narrativas: charlas en un aula, pedidos de mafias locales por el control de kilómetros de una ruta, franjas horarias de satélites o turnos de guardias. El objetivo es maximizar la cantidad total de pedidos aceptados sin solapamiento.

---

### Ejercicio 4 — Concesión de Permisos a Mafias en la Ruta Costera (Arnook)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-2 (26 de noviembre de 2024), Ejercicio 3 / Guía 02 Ejercicio 12

**Enunciado**  
Trabajamos para el mafioso Arnook, quien organiza los pedidos de pequeñas mafias locales por el control de diferentes kilómetros de la ruta costera de Ciudad República. Cada mafia le pide control sobre un rango de kilómetros $[s_i, f_i]$ (por ejemplo, del kilómetro 1 al 5, del 3 al 8, etc.). Si una mafia toma control de un kilómetro, ninguna otra puede ocupar ese mismo tramo (no pueden solaparse). Arnook cobra una tarifa fija por otorgar el permiso, independientemente de los kilómetros pedidos, por lo que su objetivo es maximizar la cantidad total de permisos otorgados sin conflictos de territorio.  
1. Implementar un algoritmo Greedy que determine a qué mafias otorgar el permiso.  
2. Indicar y justificar la complejidad temporal y espacial.  
3. Justificar por qué el algoritmo planteado es Greedy.  
4. ¿El algoritmo da la solución óptima siempre? Demostrarlo formalmente.

**Qué está evaluando la cátedra**  
Comprensión del arquetipo de *Interval Scheduling*, diseño del criterio voraz correcto (ordenamiento por punto final más temprano), y la demostración formal de optimalidad vía *Greedy Stays Ahead*.

#### 1. Deducción Metodológica Formal (Los 5 Pasos de Greedy)

1. **Paso 1: Análisis de Reglas Candidatas y Descarte de Erróneas:**
   * *Criterio erróneo 1 (Inicio más temprano $s_i$):* Falla si un pedido empieza muy temprano y ocupa toda la ruta ($[1, 100]$ bloquea a $[2, 3]$ y $[4, 5]$).
   * *Criterio erróneo 2 (Menor longitud $f_i - s_i$):* Falla si un intervalo corto bloquea a dos largos compatibles a sus extremos ($[10, 20]$ y $[20, 30]$ vs $[19, 21]$).
   * *Criterio Óptimo:* Ordenar las solicitudes por su **kilómetro de finalización más temprano ($f_i$)**. Al terminar lo antes posible, se libera el recurso de la ruta lo más temprano posible para futuras mafias.
2. **Paso 2: Criterio de Ordenamiento:**
   Se ordenan los $n$ intervalos de modo que $f_1 \le f_2 \le \dots \le f_n$. Esto insume tiempo $O(n \log n)$.
3. **Paso 3: Verificación de Factibilidad:**
   Un intervalo candidato $j$ es factible si y solo si su punto de inicio es mayor o igual al fin del último intervalo aceptado:
   $$s_j \ge f_{\text{último}}$$
4. **Paso 4: Invocación Irrevocable:**
   Se acepta el intervalo compatible y se actualiza $f_{\text{último}} = f_j$. Esta decisión es definitiva: nunca se desasigna un permiso otorgado.
5. **Paso 5: Complejidad:**
   * **Tiempo:** $O(n \log n)$ por el ordenamiento inicial y $O(n)$ en el barrido secuencial. Total: $\Theta(n \log n)$.
   * **Espacio:** $O(n)$ para la lista de permisos seleccionados.

#### 2. Demostración Formal de Optimalidad (Greedy Stays Ahead)

* **Definición de Soluciones:**
  Sea $G = \{g_1, g_2, \dots, g_k\}$ el conjunto de intervalos elegidos por el algoritmo Greedy, ordenados cronológicamente por tiempo de fin.
  Sea $OPT = \{o_1, o_2, \dots, o_m\}$ el conjunto de intervalos de una solución óptima arbitraria, también ordenados por tiempo de fin, con $m \ge k$.
* **Lema Inductivo:** Para todo $r \le k$, el tiempo de fin del $r$-ésimo elemento voraz es menor o igual al del $r$-ésimo elemento óptimo:
  $$f(g_r) \le f(o_r)$$
* **Caso Base ($r = 1$):** El algoritmo voraz selecciona como primer elemento aquel con el menor tiempo de fin absoluto en todo el conjunto de entrada. Por ende, $f(g_1) \le f(o_1)$ por definición.
* **Hipótesis Inductiva:** Asumimos que para un $r - 1 < k$ se cumple $f(g_{r-1}) \le f(o_{r-1})$.
* **Paso Inductivo ($r$):**
  Como $OPT$ es una solución factible, el intervalo $o_r$ no se solapa con $o_{r-1}$, lo que implica $s(o_r) \ge f(o_{r-1})$.
  Aplicando la hipótesis inductiva:
  $$s(o_r) \ge f(o_{r-1}) \ge f(g_{r-1})$$
  Esto demuestra que cuando el algoritmo voraz buscaba su $r$-ésimo elemento tras haber seleccionado $g_{r-1}$, el intervalo $o_r$ era una alternativa perfectamente **factible y compatible**.
  Dado que el algoritmo voraz selecciona el intervalo compatible con el menor tiempo de fin disponible, su elección $g_r$ debe satisfacer:
  $$f(g_r) \le f(o_r)$$
* **Conclusión de Optimalidad ($k = m$):**
  Supongamos por contradicción que $m > k$, lo que significa que la solución óptima tiene al menos un intervalo adicional $o_{k+1}$.
  Por el lema anterior aplicado a $r = k$:
  $$s(o_{k+1}) \ge f(o_k) \ge f(g_k)$$
  Esto significa que $o_{k+1}$ es compatible con el último elemento voraz $g_k$. Pero el algoritmo voraz terminó en $g_k$ precisamente porque no existía ningún intervalo compatible remanente en el conjunto. Contradicción. Por ende, $k = m$ y la solución voraz es **estrictamente óptima**. $\blacksquare$

#### 3. Ejemplo Concreto y Tabla de Traza Paso a Paso

Sean los siguientes 5 pedidos de mafias sobre la ruta costera:

| ID | Mafia | Kilómetros $[s_i, f_i]$ | Longitud | ¿Fin más temprano? |
| :---: | :---: | :---: | :---: | :---: |
| **A** | Los del Puerto | $[1, 4]$ | $3$ | 1º en terminar ($f=4$) |
| **B** | Banda del Centro | $[3, 5]$ | $2$ | 2º en terminar ($f=5$) |
| **C** | Costanera Sur | $[0, 6]$ | $6$ | 3º en terminar ($f=6$) |
| **D** | Zona Norte | $[4, 7]$ | $3$ | 4º en terminar ($f=7$) |
| **E** | Pescadores | $[6, 9]$ | $3$ | 5º en terminar ($f=9$) |

*Traza del Algoritmo Voraz (Ordenados por $f_i$ ascendente: A, B, C, D, E):*

| Paso | Pedido Evaluado | $[s_i, f_i]$ | $f_{\text{último}}$ | Condición $s_i \ge f_{\text{último}}$ | Decisión | Permisos Otorgados |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | **A** | $[1, 4]$ | $0$ (inicial) | $1 \ge 0$ (Sí) | **ACEPTAR A** | $\{A\}$, $f_{\text{último}} = 4$ |
| **2** | **B** | $[3, 5]$ | $4$ | $3 \ge 4$ (No) | **RECHAZAR** (conflicto) | $\{A\}$ |
| **3** | **C** | $[0, 6]$ | $4$ | $0 \ge 4$ (No) | **RECHAZAR** (conflicto) | $\{A\}$ |
| **4** | **D** | $[4, 7]$ | $4$ | $4 \ge 4$ (Sí) | **ACEPTAR D** | $\{A, D\}$, $f_{\text{último}} = 7$ |
| **5** | **E** | $[6, 9]$ | $7$ | $6 \ge 7$ (No) | **RECHAZAR** (conflicto) | $\{A, D\}$ |

*Total de permisos máximos otorgados:* 2 mafias ($\{A, D\}$).

#### 4. Diagrama Visual de Intervalos

```mermaid
graph LR
    subgraph Ruta [Ocupación en Ruta Costera]
        A["[1, 4] Mafia A (ACEPTADO)"]:::opt
        B["[3, 5] Mafia B (RECHAZADO)"]:::bad
        C["[0, 6] Mafia C (RECHAZADO)"]:::bad
        D["[4, 7] Mafia D (ACEPTADO)"]:::opt
        E["[6, 9] Mafia E (RECHAZADO)"]:::bad
    end
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    classDef bad fill:#991b1b,stroke:#7f1d1d,stroke-width:1px,color:#fff
```

#### 5. Implementación en Python (Tipada y Ejecutable)

```python
def conceder_permisos_mafias(pedidos: list[tuple[str, int, int]]) -> list[tuple[str, int, int]]:
    # pedidos: lista de (nombre, inicio, fin)
    if not pedidos:
        return []

    # 1. Ordenar vorazmente por punto final ascendente
    pedidos_ordenados = sorted(pedidos, key=lambda x: x[2])

    seleccionados = [pedidos_ordenados[0]]
    ultimo_fin = pedidos_ordenados[0][2]

    # 2. Selección voraz de intervalos compatibles
    for pedido in pedidos_ordenados[1:]:
        nombre, inicio, fin = pedido
        if inicio >= ultimo_fin:
            seleccionados.append(pedido)
            ultimo_fin = fin

    return seleccionados
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Confundir Interval Scheduling con Interval Scheduling Ponderado:</strong> Si las mafias ofrecieran dinero diferente por cada permiso ($v_i$), la regla voraz por fin más temprano **deja de ser óptima**. Se debe resolver obligatoriamente mediante Programación Dinámica con búsqueda binaria en $O(n \log n)$ (ver Ejercicio 18).</li>
    <li><strong>Solapamiento en extremos ($s_j == f_i$):</strong> Prestar atención a si el enunciado indica si compartir el kilómetro exacto está permitido o no ($s_j \ge f_i$ vs $s_j > f_i$). En la ruta costera, la frontera compartida es admisible ($s_j \ge f_{\text{último}}$).</li>
    <li><strong>Ordenar por duración ($f_i - s_i$):</strong> Es el error intuitivo más frecuente en parciales. Recuerde que un intervalo de duración 2 puede arruinar a dos intervalos adyacentes de duración 3, obteniendo 1 en lugar de 2.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 2.2: Mochila Fraccionaria vs 0-1 con Garantía de Calidad 1/2

En las evaluaciones teóricas y en los TPs de la cátedra se examina la relación entre la solución fraccionaria (óptima con greedy) y la versión entera 0-1, demostrando cómo una regla greedy corregida otorga una cota de aproximación constante.

---

### Ejercicio 5 — Mochila 0-1 con Garantía de Aproximación 1/2

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Guía de Ejercicios 02, Ejercicio 8 / Diapositivas Explicativas de Cátedra

**Enunciado**  
Se tiene una mochila de capacidad de peso $W$ y $n$ objetos indivisibles (0-1), donde cada objeto $i$ tiene peso $w_i$ y valor $v_i$.  
1. Explicar por qué la regla voraz estándar basada en ordenar por densidad de valor ($v_i / w_i$) puede fallar de forma arbitraria en la mochila 0-1.  
2. Diseñar un algoritmo greedy modificado que garantice una calidad de al menos $1/2$ respecto a la solución óptima global ($V_{\text{aprox}} \ge \frac{1}{2} OPT$).  
3. Demostrar formalmente que $V_{\text{aprox}} / OPT > 1/2$.  
4. Indicar la complejidad temporal del algoritmo.

**Qué está evaluando la cátedra**  
Capacidad de analizar por qué un algoritmo voraz falla en problemas NP-Hard, diseño de heurísticas con garantías formales de aproximación y uso de la relajación continua como cota superior de optimalidad.

#### 1. Deducción Metodológica Formal (Los 5 Pasos)

1. **Paso 1: Análisis del Fallo de la Densidad Voraz Pura:**
   Consideremos $W = 100$, un objeto 1 con $w_1 = 1, v_1 = 2$ (densidad $2$) y un objeto 2 con $w_2 = 100, v_2 = 100$ (densidad $1$). La regla voraz elige el objeto 1 y llena la mochila hasta $w=1$, impidiendo que entre el objeto 2. Obtiene valor 2 en vez del óptimo 100 (eficiencia tan mala como $2/100 \to 0$).
2. **Paso 2: Filtrado Previo de Factibilidad:**
   Se descartan de inmediato todos los ítems cuyo peso individual sea mayor a la capacidad ($w_i > W$).
3. **Paso 3: Identificación del Elemento Crítico:**
   Se ordenan los elementos restantes por ratio de densidad decreciente:
   $$\frac{v_1}{w_1} \ge \frac{v_2}{w_2} \ge \dots \ge \frac{v_n}{w_n}$$
   Se introducen ítems vorazmente hasta que el primer elemento no entra por exceso de peso. A este ítem lo llamamos **Elemento Crítico ($k$)** con valor $v_k$ y peso $w_k$.
4. **Paso 4: Corrección de Cota Dual:**
   Sea $V_{\text{greedy}}$ el valor acumulado antes de topar con el elemento crítico. Se define la solución aproximada como el máximo entre la solución voraz y el elemento crítico en solitario:
   $$V_{\text{aprox}} = \max(V_{\text{greedy}}, \; v_k)$$
5. **Paso 5: Complejidad:**
   * Filtrado inicial en $O(n)$.
   * Ordenamiento por densidad en $O(n \log n)$.
   * Barrido voraz en $O(n)$.
   * Complejidad total: $\Theta(n \log n)$ en tiempo y $O(n)$ en espacio auxiliar.

#### 2. Demostración Formal de la Garantía de Aproximación 1/2

* **Paso A (Cota Superior por Relajación Continua):**
  Sea $OPT$ el valor de la solución óptima del problema entero 0-1, y sea $OPT_{\text{frac}}$ el valor de la solución óptima del problema de la mochila fraccionaria (donde se permiten fracciones de ítems).
  Como toda solución entera es una solución fraccionaria factible, se cumple:
  $$OPT \le OPT_{\text{frac}}$$
* **Paso B (Composición de la Solución Fraccionaria):**
  La solución fraccionaria óptima coincide exactamente con los primeros $k-1$ elementos enteros tomados por el greedy ($V_{\text{greedy}}$) más una fracción estricta $\alpha \in [0, 1)$ del elemento crítico $k$:
  $$OPT_{\text{frac}} = V_{\text{greedy}} + \alpha \cdot v_k < V_{\text{greedy}} + v_k$$
* **Paso C (Desigualdad Fundamental):**
  Por transitividad de las cotas anteriores:
  $$OPT < V_{\text{greedy}} + v_k$$
* **Paso D (Cota del Máximo):**
  Dado que $V_{\text{aprox}} = \max(V_{\text{greedy}}, v_k)$, es inmediato que:
  $$V_{\text{greedy}} \le V_{\text{aprox}} \quad \text{y} \quad v_k \le V_{\text{aprox}}$$
  Sumando ambas desigualdades:
  $$V_{\text{greedy}} + v_k \le 2 \cdot V_{\text{aprox}}$$
* **Paso E (Conclusión de la Garantía 1/2):**
  Sustituyendo en la cota de $OPT$:
  $$OPT < 2 \cdot V_{\text{aprox}} \implies \frac{V_{\text{aprox}}}{OPT} > \frac{1}{2}$$
  El algoritmo garantiza estrictamente más del $50\%$ del valor óptimo global en tiempo $O(n \log n)$. $\blacksquare$

#### 3. Ejemplo Concreto y Tabla de Traza Paso a Paso

Capacidad $W = 50$. Tres elementos candidatos:

| Ítem | Peso ($w_i$) | Valor ($v_i$) | Densidad ($v_i / w_i$) | ¿Entra en Greedy? |
| :---: | :---: | :---: | :---: | :--- |
| **1** | $10$ | $60$ | $6.0$ | Sí (Peso acumulado: $10$, Valor: $60$) |
| **2** | $20$ | $100$ | $5.0$ | Sí (Peso acumulado: $30$, Valor: $160$) |
| **3** | $30$ | $120$ | $4.0$ | No cabe ($30 + 30 = 60 > 50$). **¡ELEMENTO CRÍTICO!** |

*Comparación:*
* $V_{\text{greedy}} = 60 + 100 = 160$ (elementos $\{1, 2\}$, peso 30).
* Elemento Crítico en solitario: Ítem 3 ($v_3 = 120$, peso $30 \le 50$).
* $V_{\text{aprox}} = \max(160, 120) = 160$.
* *Óptimo entero real (DP):* Ítems $\{2, 3\}$ con peso $20 + 30 = 50$, valor $100 + 120 = 220$.
* *Ratio obtenido:* $160 / 220 \approx 72.7\% > 50\%$ (satisface holgadamente la cota $\ge 1/2$).

#### 4. Diagrama del Proceso de Selección

```mermaid
graph TD
    A["Ordenar ítems por densidad v_i / w_i"] --> B["Llenado voraz hasta agotar capacidad"]
    B --> C["¿Quedó capacidad para el siguiente ítem?"]
    C -- No --> D["Identificar Elemento Crítico k"]
    D --> E{"¿v_k es mayor que V_greedy?"}
    E -- Sí --> F["Solución = {Elemento Crítico k}"]:::opt
    E -- No --> G["Solución = Conjunto Voraz"]:::opt
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 5. Implementación en Python (Tipada y Ejecutable)

```python
def mochila_aprox_medio(items: list[tuple[str, int, int]], w_max: int) -> tuple[int, list[tuple[str, int, int]]]:
    # items: lista de (nombre, peso, valor)
    # 1. Filtrar los que no caben por sí solos
    candidatos = [it for it in items if it[1] <= w_max]
    if not candidatos:
        return 0, []

    # 2. Ordenar por densidad decreciente
    candidatos.sort(key=lambda x: x[2] / x[1], reverse=True)

    v_greedy = 0
    w_greedy = 0
    sol_greedy = []
    elemento_critico = None

    # 3. Llenado voraz
    for it in candidatos:
        nombre, peso, valor = it
        if w_greedy + peso <= w_max:
            sol_greedy.append(it)
            w_greedy += peso
            v_greedy += valor
        elif elemento_critico is None:
            elemento_critico = it

    # 4. Cota dual max(V_greedy, v_critico)
    if elemento_critico is not None and elemento_critico[2] > v_greedy:
        return elemento_critico[2], [elemento_critico]

    return v_greedy, sol_greedy
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Olvidar el filtrado inicial $w_i \le W$:</strong> Si un objeto pesa 150 y la mochila es de 100, jamás puede ser candidato ni elemento crítico. Si lo seleccionas como solución única cometes una infracción de factibilidad.</li>
    <li><strong>No usar la relajación fraccionaria en la demostración:</strong> Decir que "el elemento que no entró más lo que entró supera al óptimo" exige justificar formalmente que $OPT \le OPT_{\text{frac}} = V_{\text{greedy}} + \alpha v_k$. Sin la relajación continua no hay demostración válida.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 2.3: Minimización de Latencia y Deadlines (EDF)

Se tienen tareas con tiempos de procesamiento y fechas límite de entrega (deadlines). El objetivo es ordenar las tareas para minimizar la latencia máxima que experimenta cualquier tarea.

---

### Ejercicio 6 — Minimización de Latencia Máxima (Earliest Deadline First)

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Guía de Ejercicios 02, Ejercicio 9 / Práctica

**Enunciado**  
Se tienen $n$ tareas que deben procesarse secuencialmente en una única máquina que comienza en el tiempo $t = 0$. Cada tarea $i$ tiene una duración $t_i$ y una fecha límite de entrega (deadline) $d_i$. Si una tarea comienza en el tiempo $s_i$, finaliza en $f_i = s_i + t_i$. La latencia de la tarea $i$ se define como $L_i = \max(0, f_i - d_i)$. Diseñar un algoritmo greedy que programe las tareas minimizando la latencia máxima $L_{\max} = \max_i L_i$. Demostrar formalmente su optimalidad.

**Qué está evaluando la cátedra**  
Técnica de ordenamiento por fecha de vencimiento más temprana (*Earliest Deadline First*) y demostración formal por argumento de intercambio de inversiones adyacentes (*Exchange Argument*).

#### 1. Deducción Metodológica Formal (Los 5 Pasos)

1. **Paso 1: Análisis de Reglas Voraces Alternativas y sus Fallas:**
   * *Menor duración primero ($t_i$):* Falla si una tarea corta tiene un deadline muy lejano y desplaza a una tarea larga con vencimiento inmediato.
   * *Menor holgura primero ($d_i - t_i$):* Falla si una tarea corta tiene holgura 1 pero vence en $t=100$, bloqueando a una con holgura 2 que vence en $t=2$.
   * *Criterio Óptimo (EDF):* Ordenar las tareas en orden creciente de sus fechas límites: $d_1 \le d_2 \le \dots \le d_n$.
2. **Paso 2: Ausencia de Tiempo Ocioso:**
   La máquina procesa las tareas de forma continua sin pausas entre tareas consecutivas. El tiempo de inicio de cada tarea es igual al tiempo de fin de la tarea previa.
3. **Paso 3: Algoritmo Voraz:**
   Ordenar por deadline $d_i$ ascendente en $O(n \log n)$ y asignar tiempos $s_i, f_i$ en un único recorrido de $O(n)$.
4. **Paso 4: Complejidad:**
   * **Tiempo:** $\Theta(n \log n)$ por el ordenamiento inicial.
   * **Espacio:** $O(n)$ para la lista del cronograma.

#### 2. Demostración Formal de Optimalidad (Argumento de Intercambio)

* **Definición de Inversión:** Decimos que un cronograma $S$ tiene una inversión si existen dos tareas $i$ y $j$ tales que $i$ se ejecuta antes que $j$, pero $d_i > d_j$ (la tarea que vence más tarde se ejecuta antes).
* **Propiedad de la Solución Voraz:** La solución voraz $S_{\text{greedy}}$ no tiene inversiones por definición (está ordenada por $d$ ascendente).
* **Existencia de Inversión Adyacente:** Si un cronograma tiene inversiones, necesariamente contiene al menos un par de tareas **adyacentes y consecutivas** $i$ y $j$ con $d_i > d_j$.
* **Efecto del Intercambio Adyacente:**
  Sea $S$ un cronograma óptimo con la menor cantidad de inversiones. Si $S$ tiene inversiones, tomamos un par adyacente $i, j$ tal que $i$ precede inmediatamente a $j$ con $d_i > d_j$. Intercambiamos el orden de ejecución de $i$ y $j$, obteniendo un nuevo cronograma $S'$.
  * Las tareas programadas antes de $i$ y después de $j$ no modifican sus tiempos de inicio ni fin. Sus latencias permanecen idénticas.
  * La tarea $j$ se ejecuta antes en $S'$ que en $S$: su tiempo de finalización se reduce de $f_j$ a $f'_j = f_j - t_i$. Por ende, su latencia $L'_j \le L_j$.
  * La tarea $i$ finaliza en $S'$ exactamente en el instante en que antes finalizaba $j$: $f'_i = f_j$.
    Calculamos su nueva latencia:
    $$L'_i = \max(0, f'_i - d_i) = \max(0, f_j - d_i)$$
    Como $d_i > d_j$, se cumple:
    $$f_j - d_i < f_j - d_j \le L_j$$
    Por lo tanto, $L'_i \le L_j$.
  * La nueva latencia máxima del par es:
    $$\max(L'_i, L'_j) \le \max(L_i, L_j)$$
  * Por consiguiente, la latencia máxima global del cronograma $S'$ **no aumentó**:
    $$L_{\max}(S') \le L_{\max}(S)$$
* **Conclusión:** Mediante intercambios de pares adyacentes invertidos, se puede transformar cualquier solución óptima $OPT$ en la solución voraz $S_{\text{greedy}}$ sin incrementar jamás la latencia máxima. Esto prueba que $S_{\text{greedy}}$ es **estrictamente óptima**. $\blacksquare$

#### 3. Ejemplo Concreto y Tabla de Traza Paso a Paso

Consideremos 4 tareas:

| Tarea ($i$) | Duración ($t_i$) | Deadline ($d_i$) |
| :---: | :---: | :---: |
| **A** | $3$ | $6$ |
| **B** | $2$ | $4$ |
| **C** | $1$ | $9$ |
| **D** | $4$ | $8$ |

*Paso 1: Ordenar por deadline ascendente (EDF):*
1. Tarea **B**: $d_B = 4$
2. Tarea **A**: $d_A = 6$
3. Tarea **D**: $d_D = 8$
4. Tarea **C**: $d_C = 9$

*Paso 2: Traza temporal continua:*

| Orden | Tarea | Duración ($t_i$) | Inicio ($s_i$) | Fin ($f_i$) | Deadline ($d_i$) | Retraso ($f_i - d_i$) | Latencia ($L_i$) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **B** | $2$ | $0$ | $2$ | $4$ | $2 - 4 = -2$ | **$0$** |
| **2** | **A** | $3$ | $2$ | $5$ | $6$ | $5 - 6 = -1$ | **$0$** |
| **3** | **D** | $4$ | $5$ | $9$ | $8$ | $9 - 8 = +1$ | **$1$** |
| **4** | **C** | $1$ | $9$ | $10$ | $9$ | $10 - 9 = +1$ | **$1$** |

*Latencia máxima alcanzada:* $L_{\max} = \max(0, 0, 1, 1) = 1$. Es imposible lograr latencia 0 porque el trabajo total acumulado supera los plazos.

#### 4. Diagrama Visual de Cronograma

```mermaid
flowchart LR
    B["Tarea B (0 a 2)<br/>d=4 | L=0 (A tiempo)"] -->|t=2| A["Tarea A (2 a 5)<br/>d=6 | L=0 (A tiempo)"]
    A -->|t=5| D["Tarea D (5 a 9)<br/>d=8 | L=1 (Retraso)"]
    D -->|t=9| C["Tarea C (9 a 10)<br/>d=9 | L=1 (Retraso)"]
    classDef ontime fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    classDef late fill:#b45309,stroke:#92400e,stroke-width:2px,color:#fff
    class B,A ontime
    class D,C late
```

#### 5. Implementación en Python (Tipada y Ejecutable)

```python
def minimizar_latencia_edf(tareas: list[tuple[str, int, int]]) -> tuple[int, list[tuple[str, int, int, int]]]:
    # tareas: lista de (nombre, duracion, deadline)
    if not tareas:
        return 0, []

    # 1. Ordenar vorazmente por deadline ascendente
    tareas_ordenadas = sorted(tareas, key=lambda x: x[2])

    tiempo_actual = 0
    latencia_maxima = 0
    cronograma = []

    for nombre, duracion, deadline in tareas_ordenadas:
        inicio = tiempo_actual
        fin = tiempo_actual + duracion
        latencia = max(0, fin - deadline)
        if latencia > latencia_maxima:
            latencia_maxima = latencia
        cronograma.append((nombre, inicio, fin, latencia))
        tiempo_actual = fin

    return latencia_maxima, cronograma
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Definición de Latencia vs Retraso negativo:</strong> La latencia nunca es negativa ($L_i = \max(0, f_i - d_i)$). Si entregas una tarea antes del deadline, su latencia es $0$, no un número negativo que compense a otras tareas.</li>
    <li><strong>Tiempos de arribo ($r_i$):</strong> Este algoritmo asume que todas las tareas están disponibles en $t = 0$. Si el enunciado incluye tiempos de llegada diferentes ($r_i \neq 0$), el problema se convierte en NP-Duro y EDF simple deja de ser óptimo.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 2.4: Heurísticas Voraces de Cobertura (Set Cover Greedy)

Aparece cuando el problema exacto es NP-Hard (como Set Cover o Dominating Set) y el enunciado solicita explícitamente: *"Diseñar un algoritmo greedy de costo/beneficio marginal..."*.

---

### Ejercicio 7 — Ubicación Voraz de Antenas Celulares con Costo por Vecindario

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-3 (10 de diciembre de 2024), Ejercicio 4

**Enunciado**  
Una empresa de telefonía celular desea colocar antenas en una grilla de celdas para brindar cobertura a un conjunto de vecindarios distribuidos en la zona. Cada antena colocada en una celda $(i, j)$ da cobertura a esa celda y a las 8 que la rodean (un bloque de $3 \times 3$). El costo de instalar una antena en la celda $(i, j)$ es de $CTO_{ij}$ pesos. Se desea cubrir todos los vecindarios minimizando el costo total. Diseñar un algoritmo Greedy que determine en qué celdas colocar antenas. Justificar la regla de elección voraz, la cota de aproximación y la complejidad del algoritmo.

**Qué está evaluando la cátedra**  
Modelado del problema canónico de *Weighted Set Cover* mediante una heurística voraz de costo/beneficio marginal, junto con el análisis de su factor de aproximación logarítmico de Chvátal.

#### 1. Deducción Metodológica Formal (Los 5 Pasos)

1. **Paso 1: Formulación como Weighted Set Cover:**
   Sea $U$ el universo de todos los vecindarios a cubrir ($|U| = V$). Cada celda candidata $c = (i, j)$ cubre un subconjunto $S_c \subseteq U$ de vecindarios y tiene costo $CTO_c$.
2. **Paso 2: Métrica de Selección Voraz (Costo Marginal por Elemento Nuevo):**
   En cada paso, sea $U_{\text{restantes}}$ el conjunto de vecindarios aún no cubiertos. Para cada celda candidata $c$, calculamos la ganancia marginal:
   $$\Delta(c) = |S_c \cap U_{\text{restantes}}|$$
   Definimos el ratio voraz:
   $$\text{Ratio}(c) = \frac{CTO_c}{\Delta(c)}$$
   Se selecciona vorazmente la celda $c^*$ que **minimiza el costo por cada nuevo vecindario cubierto**:
   $$c^* = \arg\min_{c: \Delta(c) > 0} \frac{CTO_c}{\Delta(c)}$$
3. **Paso 3: Actualización y Terminación:**
   Se incorpora $c^*$ a la solución y se actualiza $U_{\text{restantes}} = U_{\text{restantes}} \setminus S_{c^*}$. Se repite hasta que $U_{\text{restantes}} = \emptyset$.
4. **Paso 4: Factor de Garantía de Aproximación (Teorema de Chvátal):**
   Como Set Cover es NP-Duro, ningún algoritmo polinomial garantiza el óptimo global a menos que $P = NP$. El algoritmo voraz garantiza una cota de aproximación armónica:
   $$\text{Costo}(\text{Greedy}) \le H(d_{\max}) \cdot OPT \le (\ln |U| + 1) \cdot OPT$$
   donde $H(k) = \sum_{i=1}^k \frac{1}{i}$ es el $k$-ésimo número armónico.
5. **Paso 5: Complejidad:**
   * En cada iteración se evalúan a lo sumo $M$ celdas candidatas. La inspección de las 9 celdas vecinas toma $O(1)$.
   * Se realizan a lo sumo $V$ iteraciones (en cada una se cubre al menos 1 vecindario nuevo).
   * Complejidad temporal: $O(V \cdot M)$. Espacio: $O(V + M)$.

#### 2. Ejemplo Concreto y Traza Paso a Paso

Sean 4 vecindarios $\{v_1, v_2, v_3, v_4\}$ y 3 antenas candidatas:

| Antena | Cobertura ($S_c$) | Costo ($CTO$) |
| :---: | :---: | :---: |
| **A1** | $\{v_1, v_2\}$ | $\$10$ |
| **A2** | $\{v_2, v_3, v_4\}$ | $\$24$ |
| **A3** | $\{v_3, v_4\}$ | $\$12$ |

*Iteración 1 ($U_{\text{restantes}} = \{v_1, v_2, v_3, v_4\}$):*
* A1: cubre $2$ nuevos $\implies$ Ratio $= 10 / 2 = 5.0$.
* A2: cubre $3$ nuevos $\implies$ Ratio $= 24 / 3 = 8.0$.
* A3: cubre $2$ nuevos $\implies$ Ratio $= 12 / 2 = 6.0$.
* **Elección voraz:** Se instala **A1** (costo $\$10$). Quedan sin cubrir $\{v_3, v_4\}$.

*Iteración 2 ($U_{\text{restantes}} = \{v_3, v_4\}$):*
* A2: cubre $\{v_3, v_4\}$ ($2$ nuevos) $\implies$ Ratio $= 24 / 2 = 12.0$.
* A3: cubre $\{v_3, v_4\}$ ($2$ nuevos) $\implies$ Ratio $= 12 / 2 = 6.0$.
* **Elección voraz:** Se instala **A3** (costo $\$12$). Quedan sin cubrir $\emptyset$.

*Resultado Greedy:* Antenas $\{A1, A3\}$ con Costo Total $= 10 + 12 = \$22$. (En este caso coincide con el óptimo global).

#### 3. Diagrama Visual de Cobertura de Conjuntos

```mermaid
graph TD
    U["Vecindarios No Cubiertos: {v1, v2, v3, v4}"] --> A1["Instalar A1: Cubre {v1, v2} a $5/vecino"]:::opt
    A1 --> U2["Vecindarios Restantes: {v3, v4}"]
    U2 --> A3["Instalar A3: Cubre {v3, v4} a $6/vecino"]:::opt
    A3 --> FIN(["Cobertura 100% Completada por $22"]):::done
    classDef opt fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#fff
    classDef done fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 4. Implementación en Python (Tipada y Ejecutable)

```python
def set_cover_antenas_greedy(vecindarios: set[str], antenas: dict[str, tuple[int, set[str]]]) -> list[str]:
    # antenas: dict con nombre -> (costo, set_de_vecindarios_cubiertos)
    no_cubiertos = set(vecindarios)
    elegidas = []

    while no_cubiertos:
        mejor_antena = None
        mejor_ratio = float("inf")

        for nombre, (costo, cobertura) in antenas.items():
            nuevos = len(cobertura & no_cubiertos)
            if nuevos > 0:
                ratio = costo / nuevos
                if ratio < mejor_ratio:
                    mejor_ratio = ratio
                    mejor_antena = nombre

        if mejor_antena is None:
            break  # Infactible cubrir los restantes

        elegidas.append(mejor_antena)
        no_cubiertos -= antenas[mejor_antena][1]

    return elegidas
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Calcular el ratio sobre la cobertura total histórica:</strong> El denominador del ratio DEBE ser exclusivamente los vecindarios <em>no cubiertos hasta el momento</em> ($\Delta(c) = |S_c \cap U_{\text{restantes}}|$). Si divides por $|S_c|$ fijo, una antena que cubre celdas ya satisfechas parecerá falsamente rentable.</li>
    <li><strong>Afirmar que es óptimo:</strong> Set Cover es NP-Completo. Cualquier afirmación de que este greedy es siempre óptimo se califica con 0 puntos. Es una heurística con cota de aproximación armónica $\ln |U| + 1$.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 2.5: Greedy en Caminos y Etapas (Demostración de No-Optimalidad)

Aparece cuando se plantea un problema de etapas secuenciales y se pide evaluar si un enfoque voraz local alcanza el óptimo global.

---

### Ejercicio 8 — Traslado Crítico INVAP: Enfoque Voraz y Contraejemplo Formal

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2025-1-2 (17 de junio de 2025), Ejercicio 3

**Enunciado**  
Para el traslado de una carga peligrosa del INVAP de Ezeiza a Bariloche a través de etapas diarias (con alternativas de ciudades intermedias y costos de seguro asociados a cada tramo):  
1. Diseñar un algoritmo Greedy que decida el itinerario.  
2. Indicar si la solución obtenida será óptima o no. Fundamentar con un contraejemplo riguroso con datos numéricos explícitos.

**Qué está evaluando la cátedra**  
Construcción de heurísticas paso a paso y formulación de contraejemplos matemáticos claros para refutar la optimalidad de algoritmos voraces en grafos de decisión multietapa.

#### 1. Deducción Metodológica Formal

1. **Paso 1: Regla Voraz Local:**
   Estando en la ciudad actual en la etapa $t$, el algoritmo voraz selecciona como siguiente parada aquella ciudad conectada en la etapa $t+1$ que tenga el **menor costo de seguro inmediato**.
2. **Paso 2: Veredicto de Optimalidad:**
   **El algoritmo NO es óptimo**. Un ahorro mínimo en el tramo inicial puede forzar al convoy a quedar atrapado en una ciudad cuyas únicas salidas hacia el destino tengan costos astronómicos.
3. **Paso 3: Protocolo de Contraejemplo de Cátedra:**
   Para refutar formalmente un algoritmo voraz se deben definir:
   - Los nodos y aristas de una red pequeña pero completa.
   - La traza paso a paso de la decisión voraz y su costo total acumulado.
   - Una ruta alternativa factible con costo estrictamente inferior.
   - Conclusión formal matemática: $\text{Costo}(\text{Voraz}) > \text{Costo}(\text{Alternativa})$.

#### 2. Contraejemplo Formal Numérico

Sea el traslado desde **Origen $E$ (Ezeiza)** hasta **Destino $B$ (Bariloche)** a través de dos ciudades intermedias en la Etapa 1 ($V_1$ y $V_2$):

```mermaid
graph LR
    E(["E (Ezeiza)"]) -->|Costo: 10| V1["V1"]
    E -->|Costo: 20| V2["V2"]
    V1 -->|Costo: 100| B(["B (Bariloche)"])
    V2 -->|Costo: 5| B
```

* **Traza del Algoritmo Greedy:**
  1. En el nodo inicial $E$, evalúa las aristas salientes:
     * Tramo $E \to V_1$: costo $10$.
     * Tramo $E \to V_2$: costo $20$.
  2. Elige vorazmente el tramo de menor costo inmediato: $E \to V_1$ ($10$ pesos).
  3. Desde $V_1$, la única conexión hacia el destino es $V_1 \to B$ con costo $100$ pesos.
  4. **Costo total obtenido por Greedy:**
     $$\text{Costo}_{\text{greedy}} = 10 + 100 = 110 \text{ pesos}$$
* **Solución Alternativa Factible:**
  1. Tramo inicial $E \to V_2$ con costo $20$ pesos (rechazado por el voraz).
  2. Tramo final $V_2 \to B$ con costo $5$ pesos.
  3. **Costo total alternativo:**
     $$\text{Costo}_{\text{alternativo}} = 20 + 5 = 25 \text{ pesos}$$
* **Conclusión Formal:**
  $$\text{Costo}_{\text{greedy}} = 110 > 25 = \text{Costo}_{\text{alternativo}}$$
  Como la solución voraz es estrictamente peor que la alternativa factible, queda demostrado que **el enfoque greedy no garantiza la solución óptima**.
  *Paradigma adecuado:* Este problema exhibe subestructura óptima con superposición de subproblemas y debe modelarse mediante **Programación Dinámica** en tiempo $O(V + E)$ (ver Ejercicio 32). $\blacksquare$

#### 3. Implementación en Python del Greedy y Validación del Contraejemplo

```python
def traslado_invap_greedy(origen: str, destino: str, grafo: dict[str, list[tuple[str, int]]]) -> tuple[int, list[str]]:
    actual = origen
    camino = [actual]
    costo_total = 0

    while actual != destino:
        vecinos = grafo.get(actual, [])
        if not vecinos:
            return float("inf"), []

        # Elección voraz: mínimo costo en la arista inmediata
        mejor_sig, menor_costo = min(vecinos, key=lambda x: x[1])
        camino.append(mejor_sig)
        costo_total += menor_costo
        actual = mejor_sig

    return costo_total, camino

# Demostración del contraejemplo
grafo_invap = {
    "E": [("V1", 10), ("V2", 20)],
    "V1": [("B", 100)],
    "V2": [("B", 5)],
    "B": []
}

# Costo greedy = 110, Costo optimo = 25
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Contraejemplos sin valores numéricos:</strong> Escribir <em>"podría ser que después de la primera ciudad los caminos sean muy caros"</em> no es un contraejemplo válido para la cátedra y recibe 0 puntos. Se exige un grafo explícito con etiquetas de costos y sumatorias numéricas comparativas.</li>
    <li><strong>Afirmar que Dijkstra es greedy:</strong> Si bien Dijkstra utiliza una cola de prioridad voraz sobre la distancia acumulada, **no toma decisiones miopes por arista individual**. Evalúa la distancia total acumulada desde la fuente $d[u] + w(u, v)$, lo que pertenece conceptualmente a la programación dinámica sobre grafos dirigidos acíclicos.</li>
  </ul>
</div>

---

### Errores Frecuentes en Exámenes sobre Greedy

1. **Afirmar que Greedy es óptimo sin demostrarlo:** Poner *"es óptimo porque siempre elijo lo mejor en cada paso"* es causal de pérdida total de puntos. Se debe presentar *Greedy Stays Ahead* o *Argumento de Intercambio*.
2. **Dar un contraejemplo sin números:** Un contraejemplo exige nodos, aristas y costos numéricos explícitos.
3. **No justificar por qué el algoritmo es voraz:** Se debe explicitar que la decisión es local, miope e irrevocable.
4. **Confundir Interval Scheduling con Interval Scheduling Ponderado:** Si las tareas tienen valores o beneficios distintos, ordenar por tiempo de fin no es óptimo.
"""
