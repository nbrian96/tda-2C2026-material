"""Módulo 10: Ejercicios Tipo Parcial Generados (Nuevos, Estilo Cátedra)."""

def get_content():
    return r"""## 12. Ejercicios Tipo Parcial Generados

Esta sección contiene ejercicios integrales creados específicamente siguiendo la estructura narrativa, nivel de dificultad, trampas de corrección y estilo de la cátedra de Teoría de Algoritmos de FIUBA.

---

### Ejercicio 37 — Despacho de Drones de Emergencia con Ventanas de Batería

**Tipo:** Ejercicio de Examen Integrador  
**Clasificación:** 🔴 IMPRESCINDIBLE  
**Paradigma:** Redes de Flujo (Matching Bipartito con Restricción de Recursos)  
**Qué evalúa la cátedra:** Modelado de capacidades heterogéneas ($c=2$ en fuentes intermedias), filtrado de compatibilidades temporales y espaciales previo al grafo, y demostración de integralidad.

#### 1. Enunciado Completo
El sistema de emergencias médicas de una provincia dispone de una flota de $D$ drones para transportar medicamentos críticos a $P$ puestos sanitarios aislados. Cada dron $i$ tiene una base de despegue y una autonomía de batería que le permite realizar vuelos únicamente dentro de un intervalo horario específico $[t_i^{ini}, t_i^{fin}]$. Además, por limitaciones de disipación térmica y recarga, cada dron puede realizar **a lo sumo 2 entregas** durante su turno de operación. Por su parte, cada puesto sanitario $j$ requiere **exactamente 1 entrega** y define una ventana horaria estricta $[h_j^{min}, h_j^{max}]$ en la cual su helipuerto está operativo. Se conoce la matriz de distancias y qué drones pueden alcanzar qué puestos.
1. Diseñar un algoritmo basado en Redes de Flujo que maximice la cantidad total de puestos sanitarios abastecidos.
2. Detallar la topología formal de la red (nodos, aristas, fuentes, sumideros y capacidades).
3. Demostrar la correctitud del modelo e indicar la complejidad temporal del algoritmo.

#### 2. Los 5 Pasos Metodológicos de Modelado

1. **Preprocesamiento de Compatibilidad:**
   Un dron $i$ es compatible con un puesto $j$ si y solo si está dentro de su alcance de vuelo y la ventana horaria del puesto entra dentro del horario de batería del dron (`Distancia(i, j) <= Alcance_i` y `t_ini_i <= h_min_j` y `h_max_j <= t_fin_i`). Esto se precalcula para todos los pares en `O(D * P)`.
2. **Topología en Capas Nodal:**
   - Super-fuente $s$.
   - Capa de drones: un nodo $d_i$ por cada dron $i \in \{1, \dots, D\}$.
   - Capa de puestos sanitarios: un nodo $p_j$ por cada puesto $j \in \{1, \dots, P\}$.
   - Super-sumidero $t$.
3. **Asignación de Aristas y Capacidades:**
   - **Aristas de Fuente a Drones:** $(s, d_i)$ con capacidad $c(s, d_i) = 2$ para todo $i$. *Justificación:* Modela directamente que cada dron puede efectuar a lo sumo 2 entregas.
   - **Aristas de Compatibilidad Dron-Puesto:** $(d_i, p_j)$ con capacidad $c(d_i, p_j) = 1$ para cada par compatible. *Justificación:* Un mismo dron realiza como máximo 1 viaje hacia un puesto determinado.
   - **Aristas de Puestos a Sumidero:** $(p_j, t)$ con capacidad $c(p_j, t) = 1$ para todo puesto $j$. *Justificación:* Cada puesto solo requiere y absorbe 1 entrega médica.
4. **Algoritmo de Resolución:**
   Ejecutar el algoritmo de **Edmonds-Karp** desde $s$ hasta $t$.
5. **Decodificación de la Solución:**
   Toda arista $(d_i, p_j)$ con flujo $f(d_i, p_j) = 1$ representa el despacho efectivo del dron $i$ hacia el puesto sanitario $j$.

#### 3. Justificación Directa de Correctitud e Integralidad (Lista para Examen)

1. **Entregas enteras (Teorema de Integralidad):** Como todas las capacidades de la red son enteras (`1` y `2`), Edmonds-Karp garantiza que el flujo por cada arista entre un dron y un puesto será `0` o `1` (nunca medio viaje).
2. **A lo sumo 2 viajes por dron:** Como la arista desde la fuente `s` hacia cada dron tiene capacidad `2`, por conservación de flujo ese dron solo puede enviar flujo hacia como máximo `2` puestos distintos.
3. **A lo sumo 1 entrega por puesto:** Como la arista desde cada puesto hacia el sumidero `t` tiene capacidad `1`, cada puesto recibe a lo sumo `1` dron.
4. **Maximización:** Cada unidad de flujo que llega a `t` representa un puesto sanitario abastecido, por lo que el flujo máximo encuentra la mayor cantidad posible de puestos cubiertos.

#### 4. Diagrama Visual de la Red de Flujo

```mermaid
graph LR
    s((Super-Fuente s)) -->|c=2| D1["Dron 1 (Max 2)"]
    s -->|c=2| D2["Dron 2 (Max 2)"]
    s -->|c=2| D3["Dron 3 (Max 2)"]
    D1 -->|c=1| P1["Puesto 1"]
    D1 -->|c=1| P2["Puesto 2"]
    D2 -->|c=1| P2
    D2 -->|c=1| P3["Puesto 3"]
    D3 -->|c=1| P3
    D3 -->|c=1| P4["Puesto 4"]
    P1 -->|c=1| t((Super-Sumidero t))
    P2 -->|c=1| t
    P3 -->|c=1| t
    P4 -->|c=1| t
```

#### 5. Pseudocódigo del Algoritmo (Estilo Examen Presencial)

```text
Algoritmo DespacharDronesEmergencia(Drones, Puestos, Compatibilidades):
    Construir Red de Flujo G = (V, E) con fuente s y sumidero t:

    // 1. Arcos desde s a cada dron d (capacidad 2 = cada dron realiza hasta 2 viajes)
    para cada d in Drones:
        agregar_arco(G, s, d, capacidad = 2)

    // 2. Arcos de compatibilidad entre dron d y puesto p (capacidad 1)
    para cada (d, p) in Compatibilidades:
        agregar_arco(G, d, p, capacidad = 1)

    // 3. Arcos desde cada puesto p a sumidero t (capacidad 1 = 1 dron por puesto)
    para cada p in Puestos:
        agregar_arco(G, p, t, capacidad = 1)

    // 4. Ejecución de flujo máximo en tiempo O(|Puestos| * |E|):
    flujo_maximo = EdmondsKarp(G, s, t)
    despachos = [ (d, p) para cada (d, p) en Compatibilidades si flujo_maximo(d, p) == 1 ]

    si cantidad(despachos) == cantidad(Puestos):
        devolver (cantidad(despachos), despachos)
    sino:
        devolver (cantidad(despachos), "Infactible: no es posible abastecer a todos los puestos")
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Duplicar los nodos de drones en lugar de asignar capacidad 2:</strong> Es válido crear nodos $d_{i,1}$ y $d_{i,2}$, pero innecesario y propenso a errores de índice. La forma canónica elegante es asignar directamente $c(s, d_i) = 2$.</li>
    <li><strong>Intentar modelar horarios con tiempos continuos en la red de flujo:</strong> Los filtros de horarios deben resolverse en el preprocesamiento de compatibilidad estática, no dentro de la red.</li>
  </ul>
</div>

---

### Ejercicio 38 — Plan de Publicidad Digital con Días de Enfriamiento y Presupuesto

**Tipo:** Ejercicio de Examen Integrador  
**Clasificación:** 🔴 IMPRESCINDIBLE  
**Paradigma:** Programación Dinámica (Exclusión Multidía con Restricción de Presupuesto)  
**Qué evalúa la cátedra:** Definición formal de subproblemas 2D, manejo riguroso de saltos de índice ($i - 3$) por cooldown y reconstrucción exacta de decisiones.

#### 1. Enunciado Completo
Una empresa de marketing digital planifica su campaña durante los próximos $n$ días. Para cada día $i \in \{1, \dots, n\}$ se dispone de una propuesta de pauta publicitaria que cuesta $C[i]$ pesos y genera una conversión estimada de $B[i]$ nuevos clientes ($C[i], B[i] > 0$). El presupuesto global disponible es de $P$ pesos. Por políticas de saturación de audiencia, si se pauta en el día $i$, **no se puede volver a pautar durante los siguientes 2 días** (es decir, los días $i+1$ e $i+2$ son de enfriamiento obligatorio; recién se podría volver a pautar el día $i+3$). Diseñar un algoritmo de Programación Dinámica que maximice las conversiones acumuladas sin exceder el presupuesto $P$.

#### 2. Los 5 Pasos Metodológicos de Programación Dinámica

1. **Definición Formal del Subproblema:**
   $$OPT(i, p): \text{Máxima conversión obtenible considerando el prefijo de días } \{1, \dots, i\} \text{ con un presupuesto disponible de } p \text{ pesos}$$
   donde $0 \le i \le n$ y $0 \le p \le P$.
2. **Casos Base:**
   - $OPT(0, p) = 0 \quad \forall p \in \{0, \dots, P\}$ (sin días disponibles no hay conversiones).
   - $OPT(i, 0) = 0 \quad \forall i \in \{0, \dots, n\}$ (sin dinero no es posible pautar, asumiendo $C[i] > 0$).
3. **Ecuación de Recurrencia de Bellman:**
   Para el día $i$, existen exactamente dos decisiones excluyentes:
   - **Opción A (No pautar el día $i$):** No consumimos presupuesto ni ganamos beneficio hoy. El valor es $OPT(i-1, p)$.
   - **Opción B (Pautar el día $i$):** Factible solo si $p \ge C[i]$. Ganamos $B[i]$ conversiones y el día publicitario previo pudo ser a lo sumo el día $i-3$ (por el enfriamiento obligatorio de 2 días). El valor es $OPT(\max(0, i-3), p - C[i]) + B[i]$.
   Combinando ambas alternativas:
   $$OPT(i, p) = \begin{cases} OPT(i-1, p) & \text{si } C[i] > p \\ \max \left( OPT(i-1, p), \; OPT(\max(0, i-3), p - C[i]) + B[i] \right) & \text{si } C[i] \le p \end{cases}$$
4. **Orden de Llenado de la Tabla:**
   Doble bucle anidado: fila por fila de $i = 1$ hasta $n$, y dentro de cada fila, columna por columna de presupuesto $p = 0$ hasta $P$.
5. **Reconstrucción del Plan Óptimo:**
   Comenzando desde $(n, P)$, si $OPT(i, p) = OPT(\max(0, i-3), p - C[i]) + B[i]$, se incluye el día $i$ y se transiciona a $(\max(0, i-3), p - C[i])$; si no, se transiciona a $(i-1, p)$.

#### 3. Justificación Directa de Optimalidad (Lista para Examen)

En cada día `i` con presupuesto `p`, solo hay dos opciones posibles:
1. **No pautar en el día `i`:** Nos queda intacto el presupuesto `p` para usar en los primeros `i - 1` días (`OPT(i - 1, p)`).
2. **Pautar en el día `i` (si `p >= C[i]`):** Ganamos `B[i]`, gastamos `C[i]` (nos queda `p - C[i]`) y, como hay 2 días obligatorios de enfriamiento, los días `i - 1` e `i - 2` quedan prohibidos, por lo que sumamos la mejor campaña posible hasta el día `i - 3` (`OPT(i - 3, p - C[i]) + B[i]`).

Como la tabla se llena desde el día `1` hasta `n` y desde presupuesto `0` hasta `P`, cuando calculamos `OPT(i, p)` tanto la fila `i - 1` como la `i - 3` ya fueron resueltas de forma óptima.

#### 4. Diagrama Visual de la Decisión con Cooldown

```mermaid
graph TD
    D_i["Decisión en Día i con Presupuesto p"] -->|NO Pautar| DP_prev["OPT(i-1, p)"]
    D_i -->|PAUTAR si p es suficiente| DP_jump["OPT(i-3, p - C(i)) + B(i)"]
    DP_jump -. Salta días i-1 e i-2 por enfriamiento .-> D_i
```

#### 5. Ejemplo Numérico y Traza

Consideremos $n = 4$ días, presupuesto $P = 10$:
- Día 1: Costo 5, Beneficio 10.
- Día 2: Costo 4, Beneficio 8.
- Día 3: Costo 6, Beneficio 14.
- Día 4: Costo 5, Beneficio 12.
- Si pautamos día 1 (costo 5, ben 10) $\implies$ enfriamiento días 2 y 3 $\implies$ podemos pautar día 4 (costo 5, ben 12).
- Costo total: $5 + 5 = 10 \le 10$. Beneficio total: $10 + 12 = 22$.
- Si pautáramos día 3 (costo 6, ben 14), no podríamos pautar día 1 ni 2 ni 4. Total = 14.
- El algoritmo devuelve $OPT(4, 10) = 22$ con días elegidos $\{1, 4\}$.

#### 6. Pseudocódigo del Algoritmo DP (Estilo Examen Presencial)

```text
Algoritmo PlanificarCampanaPublicidad(costos, beneficios, n, Presupuesto_Max):
    // 1. Matriz DP de dimensiones (n + 1) x (Presupuesto_Max + 1) en 0
    crear matriz DP[(n + 1)][(Presupuesto_Max + 1)] = 0

    // 2. Llenado Bottom-Up
    para i desde 1 hasta n:
        c_i = costos[i]
        b_i = beneficios[i]
        prev_dia = max(0, i - 3)  // Enfriamiento de 2 días: saltamos a i - 3

        para p desde 0 hasta Presupuesto_Max:
            val_sin = DP[i - 1][p]
            si p >= c_i:
                val_con = DP[prev_dia][p - c_i] + b_i
                DP[i][p] = max(val_sin, val_con)
            sino:
                DP[i][p] = val_sin

    // 3. Reconstrucción de los días de pauta óptimos
    dias_elegidos = []
    curr_i = n, curr_p = Presupuesto_Max

    mientras curr_i > 0 y curr_p > 0:
        c_i = costos[curr_i]
        b_i = beneficios[curr_i]
        prev_dia = max(0, curr_i - 3)

        si curr_p >= c_i y DP[curr_i][curr_p] == DP[prev_dia][curr_p - c_i] + b_i:
            agregar curr_i a dias_elegidos
            curr_p = curr_p - c_i
            curr_i = prev_dia
        sino:
            curr_i = curr_i - 1

    invertir(dias_elegidos)
    devolver (DP[n][Presupuesto_Max], dias_elegidos)
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Saltar a $i-2$ en lugar de $i-3$:</strong> Un error común es pensar que "2 días de enfriamiento" significa $i-2$. Si pautamos en el día 5 y hay 2 días de enfriamiento (días 6 y 7), la siguiente pauta recién puede ser en el día 8, por lo que el estado previo debe ser $i-3$.</li>
    <li><strong>Olvidar el parámetro de presupuesto en el estado:</strong> Definir el estado como $OPT(i)$ ignorando el dinero disponible convierte el problema en irresoluble. Es estrictamente una **DP 2D** ($i, p$).</li>
  </ul>
</div>

---

### Ejercicio 39 — Ubicación de Servidores Edge con Resiliencia del 80%

**Tipo:** Ejercicio de Examen Integrador  
**Clasificación:** 🔴 IMPRESCINDIBLE  
**Paradigma:** Programación Lineal Entera (Set Cover Ponderado con Umbral y Capacidad)  
**Qué evalúa la cátedra:** Modelado en PLI de vinculación de cobertura (*linking constraints* de capacidad de tráfico), activación de servidores e imposición de metas porcentuales.

#### 1. Enunciado Completo
Una compañía de infraestructura de telecomunicaciones debe instalar servidores de computación Edge en un conjunto de $S$ ubicaciones geográficas posibles para dar cobertura de ultrabaja latencia a $U$ clientes corporativos. Instalar un servidor en el sitio $i \in S$ tiene un costo de obra civil de $K_i > 0$ y ofrece una capacidad máxima de procesamiento de tráfico de $T_i > 0$ Gbps. Cada cliente $j \in U$ demanda $d_j > 0$ Gbps y define un conjunto $S_j \subseteq S$ de sitios candidatos cuya latencia de fibra óptica es $\le 5$ ms. La empresa exige brindar servicio a **por lo menos el 80% de los clientes corporativos** minimizando la inversión en infraestructura.
Plantear un modelo formal de Programación Lineal Entera indicando variables, dominios, función objetivo, restricciones y recuento exacto.

#### 2. Los 5 Pasos Metodológicos de Modelado en PLI

1. **Variables de Decisión:**
   - $y_i \in \{0, 1\} \quad \forall i \in S$: Vale 1 si se instala un servidor en la ubicación $i$, 0 si no.
   - $u_j \in \{0, 1\} \quad \forall j \in U$: Vale 1 si el cliente corporativo $j$ recibe servicio, 0 si no.
   - $x_{ji} \in \{0, 1\} \quad \forall j \in U, i \in S_j$: Vale 1 si el cliente $j$ es atendido específicamente por el servidor $i$, 0 si no.
2. **Función Objetivo:**
   Minimizar el gasto de inversión en infraestructura física:
   $$\min Z = \sum_{i \in S} K_i \cdot y_i$$
3. **Restricción de Umbral de Servicio (80%):**
   $$\sum_{j \in U} u_j \ge \lceil 0.80 \cdot |U| \rceil$$
4. **Restricciones de Asignación y Capacidad Operativa:**
   - **Unicidad de Asignación:** Todo cliente atendido ($u_j = 1$) debe ser abastecido por exactamente un servidor dentro de su rango de baja latencia $S_j$:
     $$\sum_{i \in S_j} x_{ji} = u_j \quad \forall j \in U$$
   - **Capacidad de Servidor con Activación (*Linking Constraint*):** El tráfico total asignado a un servidor no puede superar su capacidad $T_i$ si está activo ($y_i = 1$), y debe ser 0 si no fue instalado ($y_i = 0$):
     $$\sum_{j \in U : i \in S_j} d_j \cdot x_{ji} \le T_i \cdot y_i \quad \forall i \in S$$
5. **Dominios de las Variables:**
   $$y_i \in \{0, 1\} \quad \forall i \in S, \qquad u_j \in \{0, 1\} \quad \forall j \in U, \qquad x_{ji} \in \{0, 1\} \quad \forall j \in U, i \in S_j$$

#### 3. Conteo Formal de Variables y Restricciones

- **Variables de Decisión:**
   - $|S|$ variables de apertura de servidor $y_i$.
   - $|U|$ variables de cliente atendido $u_j$.
   - $\sum_{j \in U} |S_j|$ variables de asignación cliente-servidor $x_{ji}$.
   - **Total:** $|S| + |U| + \sum_{j \in U} |S_j|$ variables binarias.
- **Restricciones Lineales:**
   - 1 restricción de umbral mínimo del 80%.
   - $|U|$ restricciones de asignación exclusiva.
   - $|S|$ restricciones de capacidad de tráfico con enlace de activación.
   - **Total:** $1 + |U| + |S|$ restricciones funcionales.

#### 4. Diagrama Visual de Enlace Lógico Cliente-Servidor

```mermaid
graph TD
    subgraph Servidores [Servidores Edge y_i]
        S1["Servidor 1 (K1, T1)"]
        S2["Servidor 2 (K2, T2)"]
    end
    subgraph Clientes [Clientes Corporativos u_j]
        C1["Cliente 1 (d1)"]
        C2["Cliente 2 (d2)"]
        C3["Cliente 3 (d3)"]
    end
    C1 -->|x11| S1
    C2 -->|x21| S1
    C2 -->|x22| S2
    C3 -->|x32| S2
    S1 -. Demanda a lo sumo T1 .-> Cap1["Capacidad T1"]
    S2 -. Demanda a lo sumo T2 .-> Cap2["Capacidad T2"]
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Olvidar multiplicar la capacidad por $y_i$:</strong> Si se escribe $\sum d_j x_{ji} \le T_i$, el modelo asignará clientes a servidores no instalados ($y_i = 0$), teniendo costo 0 y violando la lógica física. La restricción debe ser estrictamente $\le T_i \cdot y_i$.</li>
    <li><strong>No imponer $x_{ji} = 0$ para servidores con latencia $> 5$ ms:</strong> Se debe indexar $x_{ji}$ únicamente sobre el subconjunto $S_j$ de baja latencia.</li>
  </ul>
</div>

---

### Ejercicio 40 — NP-Completitud del Problema de Asignación de Frecuencias

**Tipo:** Ejercicio de Examen Integrador  
**Clasificación:** 🔴 IMPRESCINDIBLE  
**Paradigma:** Reducciones Polinomiales (K-Coloring a Asignación de Frecuencias)  
**Qué evalúa la cátedra:** Protocolo riguroso de 4 pasos de NP-Completitud, reducción de K-Coloring y equivalencia de clases independientes.

#### 1. Enunciado Completo
Se define formalmente el problema de **Asignación de Frecuencias (AF)** de la siguiente manera:  
Dado un conjunto de $A$ antenas de transmisión y un conjunto $I$ de pares no ordenados de antenas que generan interferencia destructiva si operan en la misma frecuencia, junto con un número entero $k$ de canales de radiofrecuencia disponibles, determinar si es posible asignar un canal a cada antena de modo que ningún par de antenas con interferencia comparta canal.  
Demostrar formalmente que **Asignación de Frecuencias es NP-Completo** mediante una reducción polinomial desde **k-Coloring de Grafos**.

#### 2. Demostración Directa en 4 Pasos (Lista para Hoja de Examen)

##### Paso 1: Asignación de Frecuencias (AF) está en NP
Si nos dan una asignación candidata `C` que indica qué canal (de `1` a `k`) usa cada antena:
1. Chequeamos que todas las antenas tengan asignado un número de canal entre `1` y `k`.
2. Recorremos cada par de antenas con interferencia `(u, v)` y verificamos que sus canales sean distintos (`C[u] != C[v]`).
Como solo recorremos las antenas y los pares de interferencia una vez, el verificador tarda `O(A + I)` (polinomial). Luego, **AF pertenece a NP**.

##### Paso 2 y 3: Reducción Polinomial desde k-Coloring (`k-Coloring <=p AF`)
Sabemos que **k-Coloring** (para `k >= 3`) es NP-Completo: dado un grafo `G = (V, E)` y `k` colores, ¿se puede pintar cada vértice de modo que ningún par unido por una arista tenga el mismo color?  
Transformamos cualquier entrada `(G, k)` de k-Coloring en una entrada de Asignación de Frecuencias así:
1. **Antenas:** Por cada vértice de `V`, creamos una antena en `A`.
2. **Interferencias:** Por cada arista `(u, v)` de `E`, agregamos un par de interferencia `(u, v)` en `I`.
3. **Canales:** Usamos la misma cantidad `k` de canales que de colores.
- *Complejidad:* Copiar vértices y aristas toma tiempo `O(V + E)` (polinomial).

##### Paso 4: Equivalencia (Ida y Vuelta)
- **($\implies$) Ida: Si `G` se puede pintar con `k` colores $\to$ hay asignación válida de `k` frecuencias:**
  Le asignamos a cada antena el número del color que recibió su vértice. Como ningún par de vértices unidos por arista tiene el mismo color, ningún par de antenas con interferencia comparte el mismo canal.
- **($\impliedby$) Vuelta: Si hay una asignación válida de `k` frecuencias $\to$ `G` se puede pintar con `k` colores:**
  Pintamos cada vértice con el número de canal que recibió su antena. Como ningún par de antenas con interferencia tiene el mismo canal, ningún par de vértices vecinos queda con el mismo color.

**Conclusión:** Como AF está en NP y redujimos k-Coloring a AF en tiempo polinomial probando la equivalencia de ida y vuelta, **Asignación de Frecuencias es NP-Completo**.

#### 3. Diagrama Visual de la Reducción Identidad

```mermaid
graph LR
    subgraph KColoringG [Instancia k-Coloring G]
        V1((Vértice 1)) ---|Arista de Conflicto| V2((Vértice 2))
    end
    subgraph AsignacionFreq [Instancia AF]
        A1["Antena 1 (Canal c1)"] -. Par de Interferencia .-> A2["Antena 2 (Canal c2 != c1)"]
    end
    V1 ==>|Identidad O V+E| A1
    V2 ==>|Identidad O V+E| A2
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Creer que porque la reducción es la identidad estructural no requiere demostración:</strong> Aunque el mapeo sea directo, la cátedra exige escribir los 4 pasos completos: el verificador en NP, la transformación y la ida y vuelta.</li>
    <li><strong>Reducir para $k=2$:</strong> 2-Coloring (bipartición) está en P (se resuelve con BFS en $O(V+E)$). Se debe especificar que la reducción es desde $k$-Coloring con $k \ge 3$, que es donde el problema es NP-Completo.</li>
  </ul>
</div>
"""
