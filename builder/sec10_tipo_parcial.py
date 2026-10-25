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
   Un dron $i$ es compatible con un puesto $j$ si y solo si:
   $$\text{Distancia}(i, j) \le \text{AlcanceMax}_i \quad \land \quad t_i^{ini} \le h_j^{min} \quad \land \quad h_j^{max} \le t_i^{fin}$$
   Sea $Comp(i, j) \in \{0, 1\}$ el indicador de dicha compatibilidad calculable en tiempo $O(D \cdot P)$.
2. **Topología en Capas Nodal:**
   - Super-fuente $s$.
   - Capa de drones: un nodo $d_i$ por cada dron $i \in \{1, \dots, D\}$.
   - Capa de puestos sanitarios: un nodo $p_j$ por cada puesto $j \in \{1, \dots, P\}$.
   - Super-sumidero $t$.
3. **Asignación de Aristas y Capacidades:**
   - **Aristas de Fuente a Drones:** $(s, d_i)$ con capacidad $c(s, d_i) = 2$ para todo $i$. *Justificación:* Modela directamente que cada dron puede efectuar a lo sumo 2 entregas.
   - **Aristas de Compatibilidad Dron-Puesto:** $(d_i, p_j)$ con capacidad $c(d_i, p_j) = 1$ para cada par compatible ($Comp(i, j) = 1$). *Justificación:* Un mismo dron realiza como máximo 1 viaje hacia un puesto determinado.
   - **Aristas de Puestos a Sumidero:** $(p_j, t)$ con capacidad $c(p_j, t) = 1$ para todo puesto $j$. *Justificación:* Cada puesto solo requiere y absorbe 1 entrega médica.
4. **Algoritmo de Resolución:**
   Ejecutar el algoritmo de **Edmonds-Karp** desde $s$ hasta $t$.
5. **Decodificación de la Solución:**
   Toda arista $(d_i, p_j)$ con flujo $f(d_i, p_j) = 1$ representa el despacho efectivo del dron $i$ hacia el puesto sanitario $j$.

#### 3. Demostración Teórica de Correctitud e Integralidad

**Lema de Flujo Entero y Validez:**
1. Como todas las capacidades de la red son números enteros ($c \in \{1, 2\}$), por el **Teorema de Integralidad de Flujo**, el flujo óptimo calculado por Edmonds-Karp asignará valores enteros a todas las aristas: $f(e) \in \{0, 1, 2\}$.
2. Para cada dron $i$, por conservación en el nodo $d_i$:
   $$\sum_{j} f(d_i, p_j) = f(s, d_i) \le c(s, d_i) = 2$$
   Ningún dron realizará más de dos entregas.
3. Para cada puesto $j$, por conservación en el nodo $p_j$:
   $$\sum_{i} f(d_i, p_j) = f(p_j, t) \le c(p_j, t) = 1$$
   Ningún puesto recibirá más de una entrega, y cada entrega provendrá de un único dron compatible con flujo $1$.
4. Al maximizar el flujo saliente de $s$, se maximiza la suma de puestos que reciben servicio $\sum_j f(p_j, t)$, garantizando la cobertura óptima del sistema.

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

#### 5. Implementación en Python con Tipado Estricto

```python
from collections import deque
from typing import Dict, List, Set, Tuple

def despachar_drones_emergencia(
    drones: List[str],
    puestos: List[str],
    compatibilidades: List[Tuple[str, str]] # (dron_id, puesto_id)
) -> Tuple[int, List[Tuple[str, str]]]:
    s = "SRC_S"
    t = "SNK_T"
    adyacencia: Dict[str, List[str]] = {}
    capacidad: Dict[Tuple[str, str], int] = {}
    flujo: Dict[Tuple[str, str], int] = {}

    def agregar_arco(u: str, v: str, c: int) -> None:
        if u not in adyacencia: adyacencia[u] = []
        if v not in adyacencia: adyacencia[v] = []
        adyacencia[u].append(v)
        adyacencia[v].append(u)
        capacidad[(u, v)] = c
        capacidad[(v, u)] = 0
        flujo[(u, v)] = 0
        flujo[(v, u)] = 0

    # 1. Fuente a drones con capacidad 2
    for d in drones:
        agregar_arco(s, d, 2)

    # 2. Puestos a sumidero con capacidad 1
    for p in puestos:
        agregar_arco(p, t, 1)

    # 3. Drones a puestos con capacidad 1
    for d, p in compatibilidades:
        agregar_arco(d, p, 1)

    # Edmonds-Karp BFS
    flujo_total = 0
    while True:
        padre: Dict[str, str] = {}
        visitados = {s}
        cola = deque([s])
        while cola:
            u = cola.popleft()
            if u == t: break
            for v in adyacencia.get(u, []):
                residual = capacidad.get((u, v), 0) - flujo.get((u, v), 0)
                if residual > 0 and v not in visitados:
                    visitados.add(v)
                    padre[v] = u
                    cola.append(v)

        if t not in padre: break

        # Cuello de botella
        cuello = float('inf')
        curr = t
        while curr != s:
            prev = padre[curr]
            cuello = min(cuello, capacidad[(prev, curr)] - flujo[(prev, curr)])
            curr = prev

        curr = t
        while curr != s:
            prev = padre[curr]
            flujo[(prev, curr)] += cuello
            flujo[(curr, prev)] -= cuello
            curr = prev

        flujo_total += cuello

    despachos = [(d, p) for d, p in compatibilidades if flujo.get((d, p), 0) == 1]
    return flujo_total, despachos
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

#### 3. Demostración de Optimalidad por Inducción Matemática

- **Base:** Para $i = 0$, $OPT(0, p) = 0$ es trivialmente óptimo pues no hay días.
- **Hipótesis Inductiva:** Supongamos que $OPT(k, p)$ calcula la conversión óptima para todo $k < i$ y todo $p \le P$.
- **Paso Inductivo:** En el día $i$, cualquier plan óptimo o bien pauta el día $i$ o no pauta el día $i$:
  - Si no pauta el día $i$, la solución óptima restringida a los primeros $i-1$ días con presupuesto $p$ es, por hipótesis inductiva, $OPT(i-1, p)$.
  - Si pauta el día $i$, consume $C[i]$ de presupuesto, quedando $p - C[i]$. Por la regla de enfriamiento de 2 días, no se pudo pautar ni en $i-1$ ni en $i-2$. Por ende, la subsolución previa óptima corresponde a los primeros $i-3$ días con presupuesto $p - C[i]$, que por hipótesis es $OPT(i-3, p - C[i])$.
  - Tomar el máximo entre ambas opciones cubre todo el espacio de decisiones factibles, garantizando que $OPT(i, p)$ es estrictamente óptimo.

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

#### 6. Implementación en Python con Tipado Estricto

```python
from typing import List, Tuple

def planificar_campana_publicidad(
    costos: List[int],
    beneficios: List[int],
    presupuesto_max: int
) -> Tuple[int, List[int]]:
    n = len(costos)
    dp = [[0] * (presupuesto_max + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        c_i = costos[i - 1]
        b_i = beneficios[i - 1]
        prev_dia = max(0, i - 3)

        for p in range(presupuesto_max + 1):
            val_sin = dp[i - 1][p]
            val_con = (dp[prev_dia][p - c_i] + b_i) if p >= c_i else -1
            dp[i][p] = max(val_sin, val_con)

    # Reconstruccion
    dias_elegidos = []
    curr_i = n
    curr_p = presupuesto_max

    while curr_i > 0 and curr_p > 0:
        c_i = costos[curr_i - 1]
        b_i = beneficios[curr_i - 1]
        prev_dia = max(0, curr_i - 3)

        if curr_p >= c_i and dp[curr_i][curr_p] == dp[prev_dia][curr_p - c_i] + b_i:
            dias_elegidos.append(curr_i) # 1-indexed
            curr_p -= c_i
            curr_i = prev_dia
        else:
            curr_i -= 1

    dias_elegidos.reverse()
    return dp[n][presupuesto_max], dias_elegidos
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

#### 2. Demostración en el Esquema Sagrado de 4 Pasos

##### Paso 1: Pertenencia a NP ($AF \in \text{NP}$)
- **Certificado Candidato ($C$):** Un vector de enteros $C \in \{1, \dots, k\}^A$ donde $C[a]$ representa el canal asignado a la antena $a$. Tamaño del certificado: $|A|$ enteros de tamaño $O(\log k)$ bits $\implies O(|A| \log k)$ bits (tamaño polinomial).
- **Algoritmo Verificador Polinomial $V(A, I, k, C)$:**
  1. Verificar que para cada antena $a \in A$, $1 \le C[a] \le k$.
  2. Para cada par de interferencia $(u, v) \in I$:
     - Si $C[u] == C[v]$, retornar $\text{FALSO}$ (colisión destructiva detectada).
  3. Retornar $\text{VERDADERO}$.
- **Complejidad del Verificador:** Recorrer las aristas de interferencia toma tiempo $O(|A| + |I|)$, estrictamente lineal-polinomial. Por lo tanto, **$AF \in \text{NP}$**.

##### Paso 2: Selección del Problema Conocido
Elegimos el problema **k-Coloring de Grafos** ($k \ge 3$), conocido NP-Completo (Karp, 1972):  
*Dado un grafo $G = (V, E)$ y un entero $k$, ¿es posible asignar un color de $\{1, \dots, k\}$ a cada vértice de modo que dos vértices adyacentes tengan colores distintos?*  
Objetivo: Demostrar que:
$$\text{k-Coloring} \le_P \text{Asignación de Frecuencias}$$

##### Paso 3: Transformación Polinomial $f(G, k) \to (A, I, k)$
Dada una instancia de k-Coloring con grafo $G = (V, E)$ y entero $k$:
1. Por cada vértice $v \in V$, creamos una antena de transmisión $v \in A$.
2. Por cada arista $(u, v) \in E$, declaramos un par de interferencia $(u, v) \in I$.
3. El número de canales disponibles es exactamente $k$.
- **Complejidad:** La transformación es la función identidad estructural $f(G, k) = (G, k)$ y se construye en tiempo $O(|V| + |E|)$, que es estrictamente polinomial.

##### Paso 4: Demostración Bidireccional de Equivalencia

- **($\implies$) Si $G$ es $k$-coloreable, entonces existe una asignación de frecuencias válida sin interferencias:**
  - Si $G$ admite un coloreo válido con $k$ colores, existe una función $col: V \to \{1, \dots, k\}$ tal que $(u, v) \in E \implies col(u) \ne col(v)$.
  - Asignamos al canal de la antena $v$ el color de su vértice: $\text{Canal}(v) = col(v)$.
  - Para todo par de interferencia $(u, v) \in I$, como $(u, v) \in E$, se tiene que $\text{Canal}(u) = col(u) \ne col(v) = \text{Canal}(v)$.
  - Por lo tanto, ninguna antena en interferencia comparte canal: es una asignación válida para AF.

- **($\impliedby$) Si existe una asignación válida de $k$ frecuencias, entonces $G$ es $k$-coloreable:**
  - Supongamos que existe una asignación de canales válida $F: A \to \{1, \dots, k\}$.
  - Definimos el coloreo de vértices asignando $col(v) = F(v)$ para cada $v \in V$.
  - Para toda arista $(u, v) \in E$, por la construcción existe el par de interferencia $(u, v) \in I$. Como la asignación es válida, necesariamente $F(u) \ne F(v)$, lo que implica que $col(u) \ne col(v)$.
  - Por lo tanto, ningún par de vértices vecinos tiene el mismo color, constituyendo un $k$-coloreo válido de $G$.

**Conclusión:** Habiendo demostrado que $AF \in \text{NP}$ y que $\text{k-Coloring} \le_P AF$ con equivalencia en ambos sentidos en tiempo polinomial, queda formalmente demostrado que **Asignación de Frecuencias es NP-Completo**.

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
    <li><strong>Creer que porque la reducción es la identidad estructural no requiere demostración:</strong> Aunque el mapeo sea $O(1)$, la cátedra exige escribir rigurosamente los 4 pasos, el certificado polinomial y la demostración de la ida y de la vuelta.</li>
    <li><strong>Reducir para $k=2$:</strong> 2-Coloring (bipartición) está en P (se resuelve con BFS en $O(V+E)$). Se debe especificar que la reducción es desde $k$-Coloring con $k \ge 3$, que es donde el problema es NP-Completo.</li>
  </ul>
</div>
"""
