"""Módulo 3: Algoritmos Greedy (Voraces) — Fundamentos y Ejercicios de Parcial (13 al 18)."""

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

### Ejercicio 13 — Concesión de Permisos a Mafias en la Ruta Costera (Arnook)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Parcial 2024-2-2 (26 de noviembre de 2024), Ejercicio 3 / Guía 02 Ejercicio 12

**Enunciado**  
Trabajamos para el mafioso Arnook, quien organiza los pedidos de pequeñas mafias locales por el control de diferentes kilómetros de la ruta costera de Ciudad República. Cada mafia le pide control sobre un rango de kilómetros $[s_i, f_i]$ (por ejemplo, del kilómetro 1 al 5, del 3 al 8, etc.). Si una mafia toma control de un kilómetro, ninguna otra puede ocupar ese mismo tramo (no pueden solaparse). Arnook cobra una tarifa fija por otorgar el permiso, independientemente de los kilómetros pedidos, por lo que su objetivo es maximizar la cantidad total de permisos otorgados sin conflictos de territorio.  
1. Implementar un algoritmo Greedy que determine a qué mafias otorgar el permiso.  
2. Indicar y justificar la complejidad temporal y espacial.  
3. Justificar por qué el algoritmo planteado es Greedy.  
4. ¿El algoritmo da la solución óptima siempre? Demostrarlo formalmente.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Regla Voraz:** Ordenamos todos los pedidos de las mafias de menor a mayor según su **kilómetro de finalización ($f_i$)**. Luego los recorremos en ese orden y le otorgamos el permiso a una mafia siempre que su kilómetro de inicio no se pise con el último permiso entregado (`inicio >= ultimo_fin`).
* **¿Por qué es un algoritmo Greedy?** Porque una vez ordenados los pedidos, en cada paso aplica una regla local fija (elegir el que termina antes para liberar la ruta lo más rápido posible) y toma una decisión irrevocable sin volver atrás.
* **¿Da siempre la solución óptima? SÍ. Demostración ("El Voraz se Mantiene Adelante"):**
  - Comparemos paso a paso los permisos que elige nuestro algoritmo Greedy ($g_1, g_2, \dots, g_k$) contra los de cualquier solución óptima ($o_1, o_2, \dots, o_m$), ambos ordenados de izquierda a derecha en la ruta.
  - **En el 1er permiso ($r = 1$):** Como Greedy elige el pedido que termina en el kilómetro más chico de todos, seguro termina antes o igual que el primero de la solución óptima (`fin(g_1) <= fin(o_1)`).
  - **En cualquier permiso siguiente ($r$):** Como el permiso anterior de Greedy terminó antes o igual que el del óptimo (`fin(g_{r-1}) <= fin(o_{r-1})`), a Greedy le queda libre la ruta desde antes. Por lo tanto, el pedido $o_r$ que eligió el óptimo también está disponible sin solaparse para Greedy; y como Greedy siempre agarra el que termina primero, se cumple que `fin(g_r) <= fin(o_r)`.
  - **Por qué tienen la misma cantidad de permisos ($k = m$):** Si la solución óptima tuviera un permiso más ($o_{k+1}$), como empieza después de `fin(o_k)` y sabemos que `fin(g_k) <= fin(o_k)`, ese pedido tampoco se chocaría con $g_k$ y Greedy lo habría agregado antes de frenar. Por lo tanto, **Greedy siempre es óptimo**.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo ConcederPermisosMafias(pedidos):
    si pedidos está vacío:
        devolver []

    // 1. Regla voraz: ordenar por kilómetro de fin creciente
    ordenar pedidos por p.fin de menor a mayor

    seleccionados = [ pedidos[0] ]
    ultimo_fin = pedidos[0].fin

    // 2. Recorrer y aceptar cada pedido que no se solape con el último aceptado
    para cada p en pedidos desde el segundo en adelante:
        si p.inicio >= ultimo_fin:
            agregar p a seleccionados
            ultimo_fin = p.fin

    devolver seleccionados
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* **Complejidad Temporal:** Ordenar los $n$ pedidos por su kilómetro de fin cuesta **$O(n \log n)$**, y luego recorrer la lista una sola vez haciendo una comparación en $O(1)$ por pedido cuesta **$O(n)$**. Total temporal: **$O(n \log n)$**.
* **Complejidad Espacial:** **$O(n)$** para guardar la lista de permisos otorgados.

```mermaid
flowchart LR
    subgraph Ruta [Secuencia de Evaluación Voraz por Fin más Temprano]
        A["1º: Mafia A [1, 4]<br/>ACEPTADO (f_ult = 4)"]:::opt -->|s_B = 3 &lt; 4| B["2º: Mafia B [3, 5]<br/>RECHAZADO (Solapa)"]:::bad
        B -->|s_C = 0 &lt; 4| C["3º: Mafia C [0, 6]<br/>RECHAZADO (Solapa)"]:::bad
        C -->|s_D = 4 &ge; 4| D["4º: Mafia D [4, 7]<br/>ACEPTADO (f_ult = 7)"]:::opt
        D -->|s_E = 6 &lt; 7| E["5º: Mafia E [6, 9]<br/>RECHAZADO (Solapa)"]:::bad
    end
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    classDef bad fill:#991b1b,stroke:#7f1d1d,stroke-width:1px,color:#fff
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Confundir Interval Scheduling con Interval Scheduling Ponderado:</strong> Si las mafias ofrecieran dinero diferente por cada permiso ($v_i$), la regla voraz por fin más temprano <strong>deja de ser óptima</strong> y se debe usar Programación Dinámica.</li>
    <li><strong>Ordenar por menor duración ($f_i - s_i$) o por inicio más temprano ($s_i$):</strong> Ambos fallan; un intervalo corto en el medio puede bloquear a dos intervalos a sus costados, y uno que empieza muy temprano puede ser larguísimo y bloquear toda la ruta.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 2.2: Mochila Fraccionaria vs 0-1 con Garantía de Calidad 1/2

En las evaluaciones teóricas y en los TPs de la cátedra se examina la relación entre la solución fraccionaria (óptima con greedy) y la versión entera 0-1, demostrando cómo una regla greedy corregida otorga una cota de aproximación constante.

---

### Ejercicio 14 — Mochila 0-1 con Garantía de Aproximación 1/2

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía de Ejercicios 02, Ejercicio 8 / Diapositivas Explicativas de Cátedra

**Enunciado**  
Se tiene una mochila de capacidad de peso $W$ y $n$ objetos indivisibles (0-1), donde cada objeto $i$ tiene peso $w_i$ y valor $v_i$.  
1. Explicar por qué la regla voraz estándar basada en ordenar por densidad de valor ($v_i / w_i$) puede fallar de forma arbitraria en la mochila 0-1.  
2. Diseñar un algoritmo greedy modificado que garantice una calidad de al menos $1/2$ respecto a la solución óptima global ($V_{\text{aprox}} \ge \frac{1}{2} OPT$).  
3. Demostrar formalmente que $V_{\text{aprox}} / OPT > 1/2$.  
4. Indicar la complejidad temporal del algoritmo.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **1. ¿Por qué falla el Greedy común por densidad ($v_i / w_i$)? (Contraejemplo corto):**
  - Sea una mochila de capacidad $W = 100$ con dos objetos: el objeto A ($w_A = 1, v_A = 2$, densidad $2$) y el objeto B ($w_B = 100, v_B = 100$, densidad $1$).
  - El Greedy común elige primero a A por tener mayor densidad, ocupando $1$ de peso, y luego ya no entra B. Gana apenas **$2$**, mientras que el óptimo era llevar B solo y ganar **$100$**.
* **2. Algoritmo Greedy Modificado (Garantía $1/2$):**
  - Descartamos de entrada los objetos con $w_i > W$ (que no entran ni solos).
  - Ordenamos los restantes de mayor a menor por densidad $v_i / w_i$ y los vamos metiendo en la mochila hasta toparnos con el **primer objeto que no entra por falta de espacio** (llamado **elemento crítico $k$**, de valor $v_k$).
  - Devolvemos **el que tenga mayor valor entre dos opciones**: quedarnos con la bolsa voraz acumulada ($V_{\text{greedy}}$) o vaciar la mochila y llevar **solamente el elemento crítico $k$ solo** ($v_k$). Es decir: $V_{\text{aprox}} = \max(V_{\text{greedy}}, v_k)$.
* **3. Demostración de que $V_{\text{aprox}} > OPT / 2$:**
  - Si pudiéramos partir los objetos (mochila fraccionaria), el valor obtenido $OPT_{\text{frac}}$ sería mayor o igual al mejor valor posible sin partir objetos ($OPT \le OPT_{\text{frac}}$).
  - La mochila fraccionaria mete exactamente los mismos objetos enteros que metió nuestro Greedy ($V_{\text{greedy}}$) más una fracción (menor al 100%) del objeto crítico $k$ (de valor $v_k$).
  - Por lo tanto, la suma de ambos supera al óptimo entero: $V_{\text{greedy}} + v_k > OPT_{\text{frac}} \ge OPT$.
  - Como dos números ($V_{\text{greedy}}$ y $v_k$) suman más que $OPT$, **el mayor de los dos vale sí o sí más de la mitad de $OPT$**: $V_{\text{aprox}} = \max(V_{\text{greedy}}, v_k) > OPT / 2$.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo MochilaAproxMedio(items, W):
    // 1. Filtrar los objetos que caben por sí solos y ordenar por v_i / w_i decreciente
    candidatos = [ it en items tal que it.peso <= W ]
    ordenar candidatos por (it.valor / it.peso) de mayor a menor

    v_greedy = 0, w_actual = 0
    sol_greedy = []
    critico = nulo

    // 2. Meter objetos vorazmente hasta el primero que no entra (elemento crítico)
    para cada it en candidatos:
        si w_actual + it.peso <= W:
            agregar it a sol_greedy
            w_actual = w_actual + it.peso
            v_greedy = v_greedy + it.valor
        sino:
            critico = it
            romper bucle

    // 3. Devolver el mejor entre lo acumulado y el elemento crítico solo
    si critico != nulo y critico.valor > v_greedy:
        devolver [ critico ]
    devolver sol_greedy
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* Filtrar los objetos cuesta $O(n)$, ordenarlos por densidad $v_i / w_i$ cuesta **$O(n \log n)$** y recorrerlos linealmente cuesta $O(n)$. Por lo tanto, la complejidad temporal es **$O(n \log n)$** y espacial **$O(n)$**.

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

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Olvidar el filtrado inicial $w_i \le W$:</strong> Si un objeto pesa 150 y la mochila es de 100, jamás puede ser candidato ni elemento crítico.</li>
    <li><strong>No nombrar la mochila fraccionaria en la demostración:</strong> Para justificar $OPT < V_{\text{greedy}} + v_k$ es obligatorio mencionar que proviene de que $OPT \le OPT_{\text{frac}}$.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 2.3: Minimización de Latencia y Deadlines (EDF)

Se tienen tareas con tiempos de procesamiento y fechas límite de entrega (deadlines). El objetivo es ordenar las tareas para minimizar la latencia máxima que experimenta cualquier tarea.

---

### Ejercicio 15 — Minimización de Latencia Máxima (Earliest Deadline First)

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía de Ejercicios 02, Ejercicio 9 / Práctica

**Enunciado**  
Se tienen $n$ tareas que deben procesarse secuencialmente en una única máquina que comienza en el tiempo $t = 0$. Cada tarea $i$ tiene una duración $t_i$ y una fecha límite de entrega (deadline) $d_i$. Si una tarea comienza en el tiempo $s_i$, finaliza en $f_i = s_i + t_i$. La latencia de la tarea $i$ se define como $L_i = \max(0, f_i - d_i)$. Diseñar un algoritmo greedy que programe las tareas minimizando la latencia máxima $L_{\max} = \max_i L_i$. Demostrar formalmente su optimalidad.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Regla Voraz (Earliest Deadline First — EDF):** Ordenamos las tareas de menor a mayor según su **fecha límite de entrega ($d_i$)** y las ejecutamos de corrido una tras otra sin pausas.
* **Demostración de Optimalidad (Argumento de Intercambio):**
  - Decimos que un orden de tareas tiene una **"inversión"** si hay dos tareas vecinas $i$ y $j$ donde $i$ se hace justo antes que $j$, pero $j$ vencía antes ($d_i > d_j$). Nuestro algoritmo Greedy ordena por vencimiento, así que **no tiene ninguna inversión**.
  - Supongamos que una solución óptima tiene un par de tareas vecinas invertidas $(i, j)$ con $d_i > d_j$, y **las cambiamos de lugar** (hacemos primero $j$ y después $i$):
    1. **El resto de las tareas no se entera:** Todas las tareas anteriores a $i$ y posteriores a $j$ terminan exactamente a la misma hora que antes.
    2. **La tarea $j$ mejora:** Como pasa adelante, termina antes y su retraso baja (o sigue en 0).
    3. **La tarea $i$ no supera el retraso que antes tenía $j$:** Al pasar atrás, la tarea $i$ termina exactamente a la hora en que antes terminaba $j$ ($T$). Pero como el vencimiento de $i$ es menos urgente que el de $j$ ($d_i > d_j$), el retraso nuevo de $i$ ($T - d_i$) es **menor o igual al retraso que ya sufría antes $j$** ($T - d_j$).
  - **Conclusión:** Desarmar cualquier inversión entre dos tareas vecinas nunca empeora la latencia máxima. Repitiendo estos cambios hasta eliminar todas las inversiones, transformamos el óptimo en la solución Greedy sin empeorar el resultado. **Por lo tanto, Greedy es óptimo.**

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo MinimizarLatenciaEDF(tareas):
    // 1. Regla voraz: ordenar por fecha de entrega (deadline d_i) de menor a mayor
    ordenar tareas por t.d ascendente

    tiempo_actual = 0
    latencia_max = 0
    cronograma = []

    // 2. Ejecutar de corrido sin tiempo ocioso
    para cada t en tareas:
        inicio = tiempo_actual
        fin = tiempo_actual + t.duracion
        latencia = max(0, fin - t.d)
        latencia_max = max(latencia_max, latencia)

        agregar (t, inicio, fin) a cronograma
        tiempo_actual = fin

    devolver (latencia_max, cronograma)
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* Ordenar las $n$ tareas por su deadline $d_i$ toma **$O(n \log n)$**, y asignar los horarios en un único recorrido lineal toma **$O(n)$**. Complejidad temporal total: **$O(n \log n)$** y espacial **$O(n)$**.

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

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Definición de Latencia vs Retraso negativo:</strong> La latencia nunca es negativa ($L_i = \max(0, f_i - d_i)$). Entregar temprano da latencia $0$, no compensa retrasos de otras tareas.</li>
    <li><strong>Ordenar por menor duración ($t_i$) o menor holgura ($d_i - t_i$):</strong> Ambos fallan en minimizar la latencia máxima; la única regla óptima es ordenar por $d_i$.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 2.4: Heurísticas Voraces de Cobertura (Set Cover Greedy)

Aparece cuando el problema exacto es NP-Hard (como Set Cover o Dominating Set) y el enunciado solicita explícitamente: *"Diseñar un algoritmo greedy de costo/beneficio marginal..."*.

---

### Ejercicio 16 — Ubicación Voraz de Antenas Celulares con Costo por Vecindario

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2024-2-3 (10 de diciembre de 2024), Ejercicio 4

**Enunciado**  
Una empresa de telefonía celular desea colocar antenas en una grilla de celdas para brindar cobertura a un conjunto de vecindarios distribuidos en la zona. Cada antena colocada en una celda $(i, j)$ da cobertura a esa celda y a las 8 que la rodean (un bloque de $3 \times 3$). El costo de instalar una antena en la celda $(i, j)$ es de $CTO_{ij}$ pesos. Se desea cubrir todos los vecindarios minimizando el costo total. Diseñar un algoritmo Greedy que determine en qué celdas colocar antenas. Justificar la regla de elección voraz, la cota de aproximación y la complejidad del algoritmo.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Regla Voraz (Menor costo por cada nuevo vecindario cubierto):**
  Mientras queden vecindarios sin cubrir, para cada celda candidata $c = (i, j)$ contamos cuántos vecindarios **que todavía no tienen cobertura** ($\text{nuevos}(c)$) entrarían dentro de su bloque de $3 \times 3$, y calculamos su costo marginal por vecindario nuevo:
  $$\text{Ratio}(c) = \frac{CTO_{ij}}{\text{nuevos}(c)}$$
  En cada paso instalamos la antena que tenga el **menor ratio** (la más barata por cada nuevo vecindario que suma), marcamos esos vecindarios como cubiertos y repetimos hasta cubrir todos.
* **¿Es óptimo? NO (Garantía de Aproximación):**
  Este problema es un caso de *Weighted Set Cover* (Cobertura de Conjuntos con Costos), que es **NP-Completo**. Por lo tanto, el algoritmo Greedy **no garantiza la solución óptima**, sino que actúa como una heurística de aproximación que garantiza un costo total de a lo sumo $(\ln V + 1) \cdot OPT$ (aproximación logarítmica, donde $V$ es la cantidad de vecindarios).

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo AntenasSetCoverGreedy(vecindarios, antenas):
    no_cubiertos = copiar(vecindarios)
    elegidas = []

    mientras no_cubiertos no esté vacío:
        mejor_antena = nulo
        mejor_ratio = infinito

        // Buscar la antena con menor costo por cada vecindario NUEVO cubierto
        para cada A en antenas:
            nuevos = cantidad(A.cobertura_3x3 intersección no_cubiertos)
            si nuevos > 0:
                ratio = A.costo / nuevos
                si ratio < mejor_ratio:
                    mejor_ratio = ratio
                    mejor_antena = A

        agregar mejor_antena a elegidas
        no_cubiertos = no_cubiertos - mejor_antena.cobertura_3x3

    devolver elegidas
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* Llamando $V$ a la cantidad de vecindarios y $M$ a la cantidad de celdas candidatas para antenas: en cada vuelta del ciclo `mientras` revisamos las $M$ antenas y miramos sus 9 casillas del bloque $3 \times 3$ en tiempo constante $O(1)$, tardando $O(M)$ por iteración.
* Como en cada paso cubrimos al menos 1 vecindario nuevo, el ciclo se ejecuta a lo sumo $V$ veces. Complejidad temporal total: **$O(V \cdot M)$** y espacial **$O(V + M)$**.

```mermaid
graph TD
    U["Vecindarios No Cubiertos: {v1, v2, v3, v4}"] --> A1["Instalar A1: Cubre {v1, v2} a $5/vecino"]:::opt
    A1 --> U2["Vecindarios Restantes: {v3, v4}"]
    U2 --> A3["Instalar A3: Cubre {v3, v4} a $6/vecino"]:::opt
    A3 --> FIN(["Cobertura 100% Completada por $22"]):::done
    classDef opt fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#fff
    classDef done fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Dividir por la cobertura total fija en vez de los vecindarios <em>nuevos</em>:</strong> El denominador del ratio debe ser únicamente los vecindarios que <em>todavía no están cubiertos</em>. Si divides siempre por la cantidad fija inicial, elegirás antenas redundantes sobre zonas ya cubiertas.</li>
    <li><strong>Afirmar que este Greedy es óptimo:</strong> Set Cover es NP-Completo; decir que da siempre el óptimo invalida la respuesta teórica.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 2.5: Greedy en Caminos y Etapas (Demostración de No-Optimalidad)

Aparece cuando se plantea un problema de etapas secuenciales y se pide evaluar si un enfoque voraz local alcanza el óptimo global.

---

### Ejercicio 17 — Traslado Crítico INVAP: Enfoque Voraz y Contraejemplo Formal

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Parcial 2025-1-2 (17 de junio de 2025), Ejercicio 3

**Enunciado**  
Para el traslado de una carga peligrosa del INVAP de Ezeiza a Bariloche a través de etapas diarias (con alternativas de ciudades intermedias y costos de seguro asociados a cada tramo):  
1. Diseñar un algoritmo Greedy que decida el itinerario.  
2. Indicar si la solución obtenida será óptima o no. Fundamentar con un contraejemplo riguroso con datos numéricos explícitos.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Regla Voraz:** Empezando en Ezeiza ($E$), en cada etapa miramos únicamente las ciudades vecinas de la etapa siguiente y **elegimos avanzar hacia la ciudad conectada que tenga el menor costo de seguro inmediato** en ese tramo, repitiendo hasta llegar a Bariloche ($B$).
* **¿Asegura la solución óptima? NO.** Porque ahorrar un poco en el tramo de hoy puede meternos en una ciudad cuyas únicas rutas de salida hacia Bariloche sean carísimas.
* **Contraejemplo numérico concreto (listo para escribir en la hoja):**
  - Supongamos 2 etapas desde Ezeiza ($E$) hasta Bariloche ($B$) con dos ciudades intermedias $V_1$ y $V_2$:
    * Tramos desde el origen: $E \to V_1$ cuesta **$\$10$** y $E \to V_2$ cuesta **$\$20$**.
    * Tramos hacia el destino: $V_1 \to B$ cuesta **$\$100$** y $V_2 \to B$ cuesta **$\$5$**.
  - **Qué hace Greedy:** Parado en $E$, compara $\$10$ contra $\$20$ y elige ir a $V_1$ ($\$10$). Una vez en $V_1$, su única salida a $B$ cuesta $\$100$. **Costo total Greedy = $10 + 100 = \$110$**.
  - **Solución Óptima:** Ir por $E \to V_2 \to B$ pagando **$20 + 5 = \$25$**.
  - Como $\$110 > \$25$, queda demostrado que el algoritmo Greedy **no garantiza la solución óptima** *(para obtener siempre el óptimo habría que usar Programación Dinámica o Dijkstra)*.

```mermaid
graph LR
    E(["E (Ezeiza)"]) -->|Costo: 10| V1["V1"]
    E -->|Costo: 20| V2["V2"]
    V1 -->|Costo: 100| B(["B (Bariloche)"])
    V2 -->|Costo: 5| B
```

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo TrasladoINVAPGreedy(G, origen, destino):
    actual = origen
    camino = [ actual ]
    costo_total = 0

    mientras actual != destino:
        // Regla voraz miope: elegir el vecino de la etapa siguiente con menor costo inmediato
        (mejor_vecino, menor_costo) = vecino saliente de menor costo desde actual
        agregar mejor_vecino a camino
        costo_total = costo_total + menor_costo
        actual = mejor_vecino

    devolver (costo_total, camino)
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* En cada etapa el algoritmo solo inspecciona las aristas salientes de la ciudad actual (sin retroceder ni visitar las demás ciudades de esa misma etapa). Por lo tanto, recorre a lo sumo una fracción de las aristas en tiempo **$O(V + E)$** y espacio **$O(V)$**.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Contraejemplos sin números:</strong> Explicar en el aire <em>"puede ser que después venga un camino más caro"</em> sin dar los nodos y costos concretos ($10+100=110$ vs $20+5=25$) no suma el puntaje del contraejemplo.</li>
  </ul>
</div>

---

### Ejercicio 18 — Ruta de Transporte con Estaciones (Greedy + Instancia Óptima y No Óptima)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Parcial 2026-2-1 (Enunciados), Ejercicio 4

**Enunciado**  
Un transporte debe recorrer una ruta hasta su objetivo final pasando por $N$ estaciones intermedias con tarifas fijas $T[1 \dots N]$ por detenerse. Desde cada estación puede ir a la siguiente, o saltear una o dos estaciones (no puede saltear más de dos estaciones consecutivas). Diseñar un algoritmo greedy que permita resolver el problema. Si el algoritmo no asegura la solución óptima, indicar una instancia donde la solución obtenida sea la óptima y una instancia donde la solución obtenida no sea la óptima.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Regla Voraz:** Estando parados en la posición actual $i$ (empezando en el origen $i = 0$), miramos hasta 3 pasos adelante ($i+1, i+2, i+3$). Si el destino final ($N+1$) ya está a nuestro alcance ($i + 3 \ge N + 1$), saltamos directo al destino sin pagar nada más. Si no, **elegimos parar entre las estaciones alcanzables $\{i+1, i+2, i+3\}$ en aquella que tenga la menor tarifa inmediata** (y ante empate, en la más lejana).
* **¿Asegura la solución óptima? NO.** Porque elegir una estación apenas más barata hoy puede dejarnos cortos de alcance y obligarnos a pisar estaciones carísimas más adelante.
* **Instancia donde SÍ obtiene la solución óptima:**
  - Tarifas de 3 estaciones: `T = [10, 20, 5]`.
  - Desde el inicio (0) alcanza las estaciones 1 (\$10), 2 (\$20) y 3 (\$5). Elige la más barata: **estación 3** (costo \$5), y desde la 3 llega directo al destino (4). Costo Greedy = **\$5**, que coincide con el óptimo global.
* **Instancia donde NO obtiene la solución óptima (Contraejemplo):**
  - Tarifas de 4 estaciones: `T = [5, 6, 100, 100]`.
  - Desde el inicio (0) las alcanzables son 1 (\$5), 2 (\$6) y 3 (\$100). Greedy elige la más barata: **estación 1** (\$5).
  - Pero desde la estación 1 solo alcanza hasta la 4 (estaciones 2, 3 y 4, con costos \$6, \$100 y \$100), viéndose obligado a parar de nuevo en la **estación 2** (\$6) para recién de ahí llegar al destino (5). **Costo Greedy = \$5 + \$6 = \$11**.
  - **Solución Óptima:** Saltar directo del inicio a la **estación 2** (\$6) y de la estación 2 directo al destino (5) salteando la 3 y la 4. **Costo Óptimo = \$6 < \$11**.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo TransporteGreedy(T, N):
    actual = 0   // 0 es el origen, N+1 es el destino final
    paradas = []
    costo_total = 0

    mientras actual + 3 < N + 1:
        // Entre las 3 estaciones alcanzables (actual+1, actual+2, actual+3),
        // elegir la de menor tarifa (en empate, la más lejana)
        mejor_est = actual + 1
        para k desde actual + 2 hasta actual + 3:
            si T[k] <= T[mejor_est]:
                mejor_est = k

        agregar mejor_est a paradas
        costo_total = costo_total + T[mejor_est]
        actual = mejor_est

    devolver (costo_total, paradas)
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* En cada iteración avanzamos al menos 1 estación y miramos solo 3 opciones hacia adelante en $O(1)$. Por lo tanto, la complejidad temporal es **$O(N)$** y espacial **$O(N)$**.
"""
