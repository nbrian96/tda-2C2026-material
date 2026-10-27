"""Módulo 7: Redes de Flujo (Flujo Máximo y Corte Mínimo)."""

def get_content():
    return r"""## 9. Tema 6: Redes de Flujo (Flujo Máximo y Corte Mínimo)

### Conceptos Mínimos de Supervivencia

1. **Definiciones y Leyes Fundamentales:**
   * **Red de Transporte:** Grafo dirigido $G = (V, E)$ con un nodo fuente $s$, un nodo sumidero $t$, y capacidades no negativas $c(u, v) \ge 0$ en cada arista. Si $(u, v) \notin E$, $c(u, v) = 0$.
   * **Restricción de Capacidad:** Para toda arista $(u, v) \in E$: $0 \le f(u, v) \le c(u, v)$.
   * **Conservación de Flujo:** Para todo vértice intermedio $u \in V \setminus \{s, t\}$:
     $$\sum_{v \in V} f(v, u) = \sum_{w \in V} f(u, w)$$
     *(El caudal entrante es idéntico al caudal saliente).*
2. **Red Residual ($G_f$) y Aristas Hacia Atrás:**
   La red residual modela la capacidad disponible para empujar más flujo o para **deshacer / reencaminar** flujo previamente enviado:
   * **Arista hacia adelante (*forward*):** Para cada $(u, v) \in E$, si $f(u, v) < c(u, v)$, existe arista $(u, v)$ en $G_f$ con capacidad residual:
     $$c_f(u, v) = c(u, v) - f(u, v)$$
   * **Arista hacia atrás (*backward*):** Para cada $(u, v) \in E$, si $f(u, v) > 0$, existe arista reversa $(v, u)$ en $G_f$ con capacidad residual:
     $$c_f(v, u) = f(u, v)$$
   *Sin aristas backward, el algoritmo queda atrapado en óptimos locales subóptimos.*
3. **Algoritmos y Complejidades:**
   * **Ford-Fulkerson:** Busca caminos de aumento arbitrarios en $G_f$ (vía DFS o BFS). Complejidad $O(E \cdot |f^*|)$ (pseudo-polinomial con capacidades enteras).
   * **Edmonds-Karp:** Elige caminos de aumento de **menor cantidad de aristas** mediante BFS estricto. Complejidad estrictamente polinomial: $O(V \cdot E^2)$.
   * **Dinic:** Construye grafos por niveles y bloquea flujos. Complejidad $O(V^2 E)$, y en redes unitarias $O(E \sqrt{V})$.
4. **Teorema Fundamental Max-Flow Min-Cut:**
   * Un corte $(A, B)$ es una partición de $V$ tal que $s \in A$ y $t \in B$ con $B = V \setminus A$.
   * La **capacidad del corte** es la suma de las capacidades de las aristas orientadas estrictamente de $A$ hacia $B$:
     $$C(A, B) = \sum_{u \in A, v \in B} c(u, v)$$
   * **Teorema de Ford-Fulkerson:** En toda red de flujo, el valor del flujo máximo es exactamente igual a la capacidad del corte mínimo que separa $s$ de $t$.
   * **Recuperación del Corte Mínimo:** Al finalizar el algoritmo (cuando no hay más caminos de aumento de $s$ a $t$ en $G_f$), el conjunto $A$ está formado por todos los nodos alcanzables desde $s$ en $G_f$, y $B = V \setminus A$.

---

### Patrón de Ejercicio 6.1: Matching Bipartito y Asignación con Restricciones

Problemas de emparejamiento de entidades disjuntas (médicos-turnos, tareas-máquinas, estudiantes-proyectos) bajo cotas de compatibilidad y unicidad.

---

### Ejercicio 24 — Asignación de Turnos Médicos y Pacientes (Matching Bipartito Máximo)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-2 (26 de noviembre de 2024), Ejercicio 4 / Guía 06 Ejercicio 15  
**Qué evalúa la cátedra:** Modelado de matching con capacidades unitarias y franjas horarias mediante Redes de Flujo, creación de nodos compuestos para evitar colisiones de agenda, demostración mediante Teorema de Integralidad y análisis de complejidad.

#### 1. Enunciado Completo
En un centro médico de alta complejidad se dispone de un conjunto de $M$ profesionales médicos y un conjunto de $P$ pacientes. Cada médico $m \in M$ dispone de un listado de franjas horarias libres $H_m$ para consultas. Cada paciente $p \in P$ requiere a lo sumo una cita médica y ha declarado un listado de tuplas compatibles $(m, h)$ donde puede y desea ser atendido. Se desea diseñar un algoritmo eficiente basado en redes de flujo que determine la asignación que maximice la cantidad total de citas médicas efectivas, garantizando que:
- Ningún médico atienda a más de un paciente en una misma franja horaria.
- Ningún paciente reciba más de un turno médico.
Detallar la topología formal de la red, capacidades, algoritmo empleado, demostración de correctitud y complejidad asintótica.

#### 2. Los 5 Pasos Metodológicos de Modelado en Redes de Flujo

1. **Diseño de la Topología en Capas Nodal:**
   Para desacoplar médicos de franjas horarias y evitar que un médico atienda a dos pacientes a la misma hora, construimos una red dirigida en 4 niveles de nodos:
   - Nivel 0: Super-fuente $s$.
   - Nivel 1: Capa de pacientes: un nodo $p$ por cada paciente $p \in P$.
   - Nivel 2: Capa de citas específicas: un nodo compuesto $(m, h)$ por cada médico $m$ y cada franja horaria disponible $h \in H_m$.
   - Nivel 3: Super-sumidero $t$.
2. **Definición de Aristas y Asignación de Capacidades:**
   - **Fuente a Pacientes:** Aristas dirigidas $(s, p)$ con capacidad $c(s, p) = 1$ para todo $p \in P$. *Significado:* Cada paciente puede recibir a lo sumo 1 consulta en todo el sistema.
   - **Pacientes a Turnos Disponibles:** Aristas dirigidas $(p, (m, h))$ con capacidad $c(p, (m, h)) = 1$ para cada compatibilidad declarada por el paciente $p$. *Significado:* El paciente puede optar por dicho horario.
   - **Turnos a Sumidero:** Aristas dirigidas $((m, h), t)$ con capacidad $c((m, h), t) = 1$ para cada franja médica $(m, h)$. *Significado:* Cada médico solo puede atender a un único paciente en esa franja temporal.
3. **Conservación de Flujo e Invariantes:**
   En cada nodo intermedio $p$ y $(m, h)$, el flujo entrante coincide con el saliente: un paciente solo transmite su unidad de flujo hacia una única cita compatible, y esa cita la transmite a $t$.
4. **Algoritmo de Resolución:**
   Ejecutar **Edmonds-Karp** (Ford-Fulkerson con BFS) desde $s$ hasta $t$ en la red construida.
5. **Decodificación del Matching:**
   Toda arista $(p, (m, h))$ con flujo residual saturado $f(p, (m, h)) = 1$ representa una cita médica confirmada entre el paciente $p$, el médico $m$ y el horario $h$.

#### 3. Demostración Teórica de Correctitud e Integralidad

**Teorema de Integralidad de Flujo (Dantzig-Fulkerson):**  
Si todas las capacidades de la red son números enteros, entonces existe un flujo máximo en el cual el flujo en cada arista es un número entero.
1. **Flujo Binario:** Dado que $c(e) = 1$ para todas las aristas de la red, en el flujo máximo calculado se cumple que $f(e) \in \{0, 1\}$ para toda arista $e \in E$.
2. **Unicidad de Paciente:** Para cada paciente $p$, la arista de entrada tiene capacidad $c(s, p) = 1$. Por conservación:
   $$\sum_{(m, h)} f(p, (m, h)) = f(s, p) \le 1$$
   Por lo tanto, ningún paciente puede ser asignado a más de un turno simultáneo.
3. **Unicidad de Médico en Horario:** Para cada turno $(m, h)$, la arista de salida hacia $t$ tiene $c((m, h), t) = 1$. Por conservación:
   $$\sum_{p} f(p, (m, h)) = f((m, h), t) \le 1$$
   Por lo tanto, ningún médico puede recibir más de un paciente en la franja $h$.
4. **Biyección con el Matching Máximo:** Todo flujo entero factible de valor $k$ corresponde biyectivamente a un emparejamiento válido de cardinalidad $k$. Maximizar el flujo maximiza rigurosamente la cantidad de citas.

#### 4. Diagrama Visual de la Red en 4 Capas

```mermaid
flowchart LR
    S_SRC["Nodo Fuente s"] -->|1| P1["Paciente 1"]
    S_SRC -->|1| P2["Paciente 2"]
    S_SRC -->|1| P3["Paciente 3"]
    P1 -->|1| T1["Dr. Perez 09h"]
    P1 -->|1| T2["Dr. Perez 10h"]
    P2 -->|1| T2
    P2 -->|1| T3["Dra. Gomez 09h"]
    P3 -->|1| T3
    T1 -->|1| T_SNK["Nodo Sumidero t"]
    T2 -->|1| T_SNK
    T3 -->|1| T_SNK
```

#### 5. Ejemplo Numérico y Traza de Aumento

Consideremos 3 pacientes y 3 turnos:
- Pacientes: $P_1, P_2, P_3$.
- Turnos: $T_1 = (\text{Perez}, 9), T_2 = (\text{Perez}, 10), T_3 = (\text{Gomez}, 9)$.
- Compatibilidades: $P_1 \to \{T_1, T_2\}$; $P_2 \to \{T_2, T_3\}$; $P_3 \to \{T_3\}$.

| Iteración | Camino de Aumento en $G_f$ | Cuello de Botella | Flujo Acumulado | Asignación Provisional |
| :---: | :--- | :---: | :---: | :--- |
| **1** | $s \to P_1 \to T_1 \to t$ | $1$ | $1$ | $P_1 \to T_1$ |
| **2** | $s \to P_2 \to T_2 \to t$ | $1$ | $2$ | $P_1 \to T_1, P_2 \to T_2$ |
| **3** | $s \to P_3 \to T_3 \to t$ | $1$ | $3$ | $P_1 \to T_1, P_2 \to T_2, P_3 \to T_3$ |
| **Fin** | No hay más caminos alcanzables hacia $t$ | - | **$3$ citas** | Citas óptimas = 3 |

*Si en la iteración 1 se hubiera elegido $s \to P_1 \to T_2 \to t$, en la siguiente iteración el camino de aumento residual usaría la arista backward $T_2 \to P_1$ para redirigir a $P_1$ hacia $T_1$ y liberar $T_2$ para $P_2$, alcanzando igualmente el óptimo de 3.*

#### 6. Análisis de Complejidad Asintótica

- **Cantidad de Nodos:** $|V| = 2 + |P| + \sum_{m \in M} |H_m| = O(|P| + |Turnos|)$.
- **Cantidad de Aristas:** $|E| = |P| + |Compatibilidades| + |Turnos| = O(|Compatibilidades|)$.
- **Cota del Flujo Máximo:** $|f^*| \le \min(|P|, |Turnos|) \le |P|$.
- Como cada camino de aumento se halla en $O(|E|)$ y se requieren a lo sumo $|P|$ aumentos unitarios:
  $$\text{Complejidad Temporal:} \quad O(|P| \cdot |E|)$$
  lo cual es estrictamente polinomial y óptimo para redes unitarias.

#### 7. Pseudocódigo del Algoritmo (Estilo Examen Presencial)

```text
Algoritmo AsignarTurnosMedicos(Medicos, Pacientes, HorariosPorMedico, Compatibilidades):
    Construir Red de Flujo G = (V, E) con super-fuente s y super-sumidero t:

    // 1. Nivel 0 -> Nivel 1: Arcos desde la fuente s a cada paciente p (capacidad 1)
    para cada p in Pacientes:
        agregar_arco(G, s, p, capacidad = 1)

    // 2. Nivel 1 -> Nivel 2: Arcos desde el paciente p a sus turnos compatibles (m, h)
    para cada p in Pacientes:
        para cada tupla (m, h) in Compatibilidades[p]:
            agregar_arco(G, p, (m, h), capacidad = 1)

    // 3. Nivel 2 -> Nivel 3: Arcos desde cada turno (m, h) al sumidero t (capacidad 1)
    // (Nota: si el enunciado agregara un tope diario C_m por médico, se intercala un nodo m
    //  con arcos (m, h) -> m de cap 1 y m -> t de cap C_m)
    para cada m in Medicos:
        para cada h in HorariosPorMedico[m]:
            agregar_arco(G, (m, h), t, capacidad = 1)

    // 4. Ejecución de flujo máximo mediante algoritmo polinomial estándar:
    flujo_maximo = EdmondsKarp(G, s, t)

    // 5. Decodificar asignaciones (aristas intermedias p -> (m, h) con flujo f == 1)
    citas_confirmadas = []
    para cada arco (p, (m, h)) con flujo(p, (m, h)) == 1:
        agregar (p, m, h) a citas_confirmadas

    devolver (flujo_maximo, citas_confirmadas)
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Conectar pacientes directamente a los médicos:</strong> Si se crea un nodo por médico con capacidad igual a la cantidad de horarios, se pierde el control de concurrencia: el algoritmo podría asignarle 3 pacientes al Dr. Pérez a las 09:00 hs. Es **obligatorio crear un nodo por cada par (médico, horario)**.</li>
    <li><strong>Olvidar justificar el Teorema de Integralidad:</strong> Si no se menciona que las capacidades enteras garantizan flujo $0$ o $1$, la cátedra descuenta puntos al asumir que las soluciones podrían ser fraccionarias (ej. paciente atendido $0.5$ por un médico y $0.5$ por otro).</li>
  </ul>
</div>

---

### Patrón de Ejercicio 6.2: Redes de Demanda y Suministro con Super-Nodos

Sistemas de transporte, logística o energía con múltiples fuentes de generación y múltiples centros de consumo, requiriendo super-fuente y super-sumidero para balancear el sistema.

---

### Ejercicio 25 — Red de Distribución Energética con Super-Fuente y Super-Sumidero (Ford-Fulkerson)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2025-1-1 (27 de mayo de 2025), Ejercicio 1  
**Qué evalúa la cátedra:** Modelado de múltiples fuentes y sumideros con cotas heterogéneas, construcción de la red residual, ejecución de Ford-Fulkerson y análisis de corte mínimo para diagnóstico de cuellos de botella energéticos.

#### 1. Enunciado Completo
El sistema interconectado energético nacional está constituido por 9 regiones geográficas ($R_1, \dots, R_9$). Para cada región $i$ se conoce su capacidad de generación prevista $G_i \ge 0$ (MWh) y su demanda requerida $D_i \ge 0$ (MWh). Entre pares de regiones existen líneas de transmisión de alta tensión con capacidad máxima $CAP_{ij}$ MWh/día. Se desea diseñar un algoritmo basado en redes de flujo que determine si es factible abastecer la demanda total de todas las regiones y, en caso afirmativo, cuánta energía transportar por cada línea. Si la demanda no puede cubrirse, el algoritmo debe identificar el conjunto crítico de líneas que causan el cuello de botella.

#### 2. Los 5 Pasos Metodológicos de Modelado con Super-Nodos

1. **Creación de Super-Fuente ($S$) y Super-Sumidero ($T$):**
   Dado que existen múltiples puntos generadores y múltiples centros de consumo, introducimos dos vértices ficticios:
   - Super-fuente $S$: inyecta toda la generación del país a la red.
   - Super-sumidero $T$: absorbe toda la demanda del país desde la red.
2. **Definición de Aristas y Capacidades:**
   - **Alimentación desde Generadores:** Para cada región $i$ con $G_i > 0$, creamos arista dirigida $(S, R_i)$ con capacidad $c(S, R_i) = G_i$.
   - **Extracción hacia Consumidores:** Para cada región $j$ con $D_j > 0$, creamos arista dirigida $(R_j, T)$ con capacidad $c(R_j, T) = D_j$.
   - **Líneas de Red:** Para cada línea de transmisión entre $i$ y $j$, arista $(R_i, R_j)$ con capacidad $c(R_i, R_j) = CAP_{ij}$.
3. **Criterio de Factibilidad Global:**
   Sea $D_{total} = \sum_{j=1}^9 D_j$ la demanda acumulada.
   - Si $\text{FlujoMax}(S, T) = D_{total}$: El sistema es **factible**. Todas las aristas $(R_j, T)$ están saturadas al $100\%$.
   - Si $\text{FlujoMax}(S, T) < D_{total}$: El sistema tiene un **déficit energético insalvable**.
4. **Diagnóstico del Cuello de Botella vía Corte Mínimo:**
   Si hay déficit, hallamos el corte mínimo $(A, B)$ alcanzable desde $S$ en la red residual final $G_f$. Las aristas que cruzan de $A$ a $B$ están totalmente saturadas y constituyen el cuello de botella físico de la red.
5. **Determinación del Transporte Interregional:**
   Para cada línea $(R_i, R_j)$, el valor $f(R_i, R_j)$ representa exactamente la energía a transmitir en MWh/día.

#### 3. Demostración Teórica de Conservación y Despacho

**Teorema de Conservación Nodal en Regiones:**  
Para cualquier región $i \in \{R_1, \dots, R_9\}$, la ecuación de conservación de flujo impone:
$$\sum_{\text{entradas}} f(u, R_i) = \sum_{\text{salidas}} f(R_i, v)$$
Desglosando las conexiones con los super-nodos:
$$f(S, R_i) + \sum_{k \ne i} f(R_k, R_i) = f(R_i, T) + \sum_{j \ne i} f(R_i, R_j)$$
Dado que $f(S, R_i) \le G_i$ y si el sistema es factible $f(R_i, T) = D_i$:
$$(\text{Generación utilizada}) + (\text{Importación}) = (\text{Demanda cubierta}) + (\text{Exportación})$$
lo que coincide de manera idéntica con la primera ley de Kirchhoff y el balance termodinámico del sistema eléctrico.

#### 4. Diagrama Visual de la Red con Super-Fuente y Super-Sumidero

```mermaid
graph LR
    S((Super-Fuente S)) -->|G1| R1["R1 (Generadora)"]
    S -->|G2| R2["R2 (Generadora)"]
    R1 -->|CAP_13| R3["R3 (Intermedia)"]
    R2 -->|CAP_23| R3
    R1 -->|CAP_14| R4["R4 (Consumidora)"]
    R3 -->|CAP_34| R4
    R4 -->|D4| T((Super-Sumidero T))
    R3 -->|D3| T
```

#### 5. Ejemplo Numérico y Traza

- Regiones:
  - $R_1$: $G_1 = 50, D_1 = 0$.
  - $R_2$: $G_2 = 40, D_2 = 0$.
  - $R_3$: $G_3 = 0, D_3 = 60$.
  - $R_4$: $G_4 = 0, D_4 = 30$.
- Demanda total requerida: $60 + 30 = 90$ MWh. Generación total: $50 + 40 = 90$ MWh.
- Capacidades de línea:
  - $(R_1, R_3) = 35$, $(R_1, R_4) = 15$.
  - $(R_2, R_3) = 25$, $(R_2, R_4) = 15$.
- Despacho:
  - $R_1$ envía $35$ a $R_3$ y $15$ a $R_4$ (total $50$, satura $S \to R_1$).
  - $R_2$ envía $25$ a $R_3$ y $15$ a $R_4$ (total $40$, satura $S \to R_2$).
  - $R_3$ recibe $35 + 25 = 60$ y los envía a $T$ (cubre su demanda de $60$).
  - $R_4$ recibe $15 + 15 = 30$ y los envía a $T$ (cubre su demanda de $30$).
- Flujo Máximo $= 90 = D_{total}$. Sistema **100% Factible**.

#### 6. Análisis de Complejidad

- Número de nodos: $|V| = 9 + 2 = 11$.
- Número de aristas: $|E| \le 9 (\text{fuente}) + 9 (\text{sumidero}) + 72 (\text{líneas}) = 90$.
- Complejidad con Edmonds-Karp: $O(|V| \cdot |E|^2) \approx 11 \cdot 90^2 \approx 89.100$ operaciones elementales, ejecutándose en menos de $0.5$ milisegundos.

#### 7. Pseudocódigo del Algoritmo y Diagnóstico de Corte (Estilo Examen Presencial)

```text
Algoritmo DiagnosticarRedEnergetica(Generacion, Demanda, Lineas):
    Construir Red de Flujo G con superfuente S y supersumidero T:
    demanda_total = sumatoria(Demanda[r] para cada r)

    // 1. Conectar superfuente S a regiones generadoras
    para cada r in Generacion donde Generacion[r] > 0:
        agregar_arco(G, S, r, capacidad = Generacion[r])

    // 2. Conectar regiones demandantes a supersumidero T
    para cada r in Demanda donde Demanda[r] > 0:
        agregar_arco(G, r, T, capacidad = Demanda[r])

    // 3. Arcos dirigidos de transporte interzonal
    para cada (u, v, cap) in Lineas:
        agregar_arco(G, u, v, capacidad = cap)

    // Flujo máximo con algoritmo polinomial
    flujo_obtenido = EdmondsKarp(G, S, T)

    si flujo_obtenido == demanda_total:
        devolver (Verdadero, flujo_obtenido, "Demanda satisfecha al 100%")
    sino:
        // Hallar corte mínimo (A, B) por BFS en red residual G_f desde S
        A_alcanzables = NodosAlcanzablesDesde(G_f, S)
        cuellos_botella = [ (u, v) para (u, v) en Lineas si u in A_alcanzables y v no in A_alcanzables ]
        devolver (Falso, flujo_obtenido, cuellos_botella)
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Crear aristas bidireccionales sumando flujos netos erróneamente:</strong> En una línea de transmisión se debe modelar con dos aristas dirigidas opuestas independientes $(u, v)$ y $(v, u)$, cada una con su capacidad $CAP$.</li>
    <li><strong>No distinguir capacidad de generación de capacidad de transporte:</strong> Asumir que toda la energía generada llega si $\sum G_i \ge \sum D_i$. El examen evalúa precisamente el cuello de botella en las líneas intermedias.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 6.3: Análisis Teórico y Propiedades de Cortes Mínimos

Preguntas conceptuales de demostración formal o refutación mediante contraejemplos matemáticos mínimos ante perturbaciones uniformes en las capacidades de las aristas.

---

### Ejercicio 26 — Análisis Teórico: Aumento Uniforme de Capacidades y Corte Mínimo

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-3 (10 de diciembre de 2024), Ejercicio 1  
**Qué evalúa la cátedra:** Comprensión matemática rigurosa de la definición de capacidad de un corte, sensibilidad ante perturbaciones uniformes $+1$, y construcción de contraejemplos matemáticos minimales irrebatibles.

#### 1. Enunciado Completo
Indicar si la siguiente afirmación es verdadera o falsa. Si es verdadera, proveer una demostración formal rigurosa. Si es falsa, construir un contraejemplo explícito indicando nodos, aristas, capacidades originales, corte original, nuevas capacidades y el nuevo corte mínimo:  
*“Sea $G = (V, E)$ una red de flujo arbitraria con fuente $s$, sumidero $t$ y capacidades enteras positivas $c(e)$ en cada arista $e \in E$. Sea $(A, B)$ un corte mínimo $s-t$ con respecto a las capacidades $c$. Si se suma $1$ a la capacidad de cada arista de la red ($c'(e) = c(e) + 1$), el corte $(A, B)$ sigue siendo obligatoriamente un corte mínimo respecto a las nuevas capacidades $c'$.”*

#### 2. Demostración de Falsedad mediante Análisis Analítico

**La afirmación es FALSA.**

**Análisis de Sensibilidad de la Capacidad de un Corte:**  
Sea $(A, B)$ un corte $s-t$ cualquiera. Su capacidad bajo la función original $c$ es:
$$C(A, B) = \sum_{e \in \delta^+(A)} c(e)$$
donde $\delta^+(A) = \{(u, v) \in E : u \in A, v \in B\}$ es el conjunto de aristas que cruzan el corte.  
Al aplicar la perturbación $c'(e) = c(e) + 1$, la nueva capacidad es:
$$C'(A, B) = \sum_{e \in \delta^+(A)} (c(e) + 1) = \sum_{e \in \delta^+(A)} c(e) + \sum_{e \in \delta^+(A)} 1 = C(A, B) + |\delta^+(A)|$$
**Conclusión Analítica:** La nueva capacidad del corte **depende linealmente de la cantidad de aristas que lo componen ($|\delta^+(A)|$)**.  
Un corte con muchas aristas sufrirá un incremento mucho mayor que un corte compuesto por pocas aristas. Si dos cortes tenían capacidades originales cercanas, la perturbación penalizará al corte con más aristas, pudiendo invertir el orden de minimalidad.

#### 3. Contraejemplo Formal Minimal (4 Nodos)

Construyamos la red más simple posible con $V = \{s, u_1, u_2, u_3, u_4, u_5, v, t\}$ donde compiten dos cortes:
- **Corte 1 ($A_1 = \{s\}, B_1 = V \setminus \{s\}$):** Contiene **5 aristas** saliendo de $s$ hacia $u_1 \dots u_5$, cada una de capacidad $c = 2$:
  $$C(A_1, B_1) = 2 + 2 + 2 + 2 + 2 = 10, \qquad |\delta^+(A_1)| = 5$$
- **Corte 2 ($A_2 = V \setminus \{t\}, B_2 = \{t\}$):** Contiene **1 única arista** $(v, t)$ entrando a $t$, con capacidad $c = 11$:
  $$C(A_2, B_2) = 11, \qquad |\delta^+(A_2)| = 1$$
- **Evaluación Inicial:**
  - $C(A_1, B_1) = 10 < 11 = C(A_2, B_2)$.
  - El **corte mínimo original es $(A_1, B_1)$** con capacidad $10$.
- **Evaluación tras la Perturbación ($c'(e) = c(e) + 1$):**
  - Para el Corte 1 (5 aristas):
    $$C'(A_1, B_1) = (2 + 1) \times 5 = 3 \times 5 = 15$$
  - Para el Corte 2 (1 arista):
    $$C'(A_2, B_2) = 11 + 1 = 12$$
- **Comparación Final:**
  $$C'(A_2, B_2) = 12 < 15 = C'(A_1, B_1)$$
  Bajo las nuevas capacidades, el corte mínimo es ahora $(A_2, B_2)$ y **ha dejado de serlo $(A_1, B_1)$**.
- **Queda formalmente refutada la afirmación.**

#### 4. Diagrama Visual del Contraejemplo

```mermaid
flowchart LR
    S_SRC["Fuente s"] -->|c=2 → c'=3| u1["u1"]
    S_SRC -->|c=2 → c'=3| u2["u2"]
    S_SRC -->|c=2 → c'=3| u3["u3"]
    S_SRC -->|c=2 → c'=3| u4["u4"]
    S_SRC -->|c=2 → c'=3| u5["u5"]
    u1 -->|c=10| v["Hub v"]
    u2 -->|c=10| v
    u3 -->|c=10| v
    u4 -->|c=10| v
    u5 -->|c=10| v
    v -->|c=11 → c'=12| T_SNK["Sumidero t"]
```

#### 5. Tabla Comparativa de Capacidades de Corte

| Corte | Composición de Aristas | Capacidad Original $C$ | Aristas $|\delta^+|$ | Nueva Capacidad $C'$ | ¿Es Mínimo? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Corte 1 ($A_1=\{s\}$)** | 5 aristas de capacidad 2 | **$10$** | $5$ | $10 + 5 = \mathbf{15}$ | **NO** (Pierde minimalidad) |
| **Corte 2 ($B_2=\{t\}$)** | 1 arista de capacidad 11 | $11$ | $1$ | $11 + 1 = \mathbf{12}$ | **SÍ (Nuevo Corte Mínimo)** |

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Decir que es Verdadera asumiendo que "sumar una constante no cambia el mínimo":</strong> En optimización lineal, sumar una constante a la función objetivo no cambia el óptimo. Pero aquí **no se suma una constante al corte**, se suma 1 a cada arista, por lo que a cada corte se le suma una constante distinta proporcional a su cantidad de aristas ($C' = C + k$).</li>
    <li><strong>Dar un contraejemplo sin valores numéricos explícitos:</strong> Un contraejemplo debe incluir el grafo completo, los conjuntos de vértices $A$ y $B$, y la cuenta aritmética explícita de antes y después.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 6.4: Actualización Dinámica de Flujo Máximo

Se dispone del flujo máximo y red residual calculados y se incrementa la capacidad de una única arista en 1 unidad. Se pide actualizar el flujo en tiempo lineal $O(V + E)$ sin reejecutar el algoritmo desde cero.

---

### Ejercicio 27 — Actualización de Flujo Máximo ante Aumento de Capacidad Unitaria en O(V + E)

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Guía de Ejercicios 06, Ejercicio 5  
**Qué evalúa la cátedra:** Comprensión profunda de la red residual, explotación del estado previo para actualización incremental (*dynamic max-flow*) y cota estricta de caminos de aumento en $O(V + E)$.

#### 1. Enunciado Completo
Dada una red de flujo $G = (V, E)$ con capacidades enteras positivas, se ha calculado previamente un flujo máximo $f^*$ de $s$ a $t$ y se dispone de su red residual asociada $G_f$. Supongamos que se incrementa en una unidad la capacidad de una arista arbitraria $(u, v) \in E$ (de $c(u, v)$ pasa a $c(u, v) + 1$). Diseñar un algoritmo que recalcule el nuevo flujo máximo en tiempo estrictamente acotado por $O(V + E)$. Justificar la correctitud y la cota temporal.

#### 2. Los 5 Pasos Metodológicos de Actualización Incremental

1. **Impacto Local en la Red Residual:**
   Al modificarse únicamente la arista $(u, v)$, en la red residual $G_f$ la capacidad residual de esa arista pasa de $c_f(u, v) = c(u, v) - f^*(u, v)$ a:
   $$c_f'(u, v) = c(u, v) + 1 - f^*(u, v) = c_f(u, v) + 1$$
   Todas las demás capacidades residuales de la red permanecen inalteradas.
2. **Propiedad de Acotamiento del Incremento:**
   Por el Teorema Max-Flow Min-Cut, la capacidad de cualquier corte que contenga a $(u, v)$ aumenta a lo sumo en $1$, y los cortes que no la contienen mantienen su capacidad idéntica. Por lo tanto, el nuevo flujo máximo $f_{nuevo}^*$ satisface estrictamente:
   $$|f^*| \le |f_{nuevo}^*| \le |f^*| + 1$$
3. **Búsqueda de Camino de Aumento Único:**
   Dado que las capacidades son enteras y el incremento es a lo sumo 1, alcanza con buscar **a lo sumo un camino de aumento** desde $s$ hasta $t$ en la red residual actualizada $G_f'$ mediante BFS o DFS.
4. **Actualización de Flujos:**
   - Si se encuentra un camino de aumento $P$ de $s$ a $t$: su cuello de botella es necesariamente $\ge 1$ (al ser capacidades enteras). Se empuja exactamente 1 unidad de flujo a lo largo de $P$, actualizando las aristas forward y backward. El nuevo flujo máximo es $|f^*| + 1$.
   - Si no existe ningún camino de aumento en $G_f'$: $t$ sigue siendo inalcanzable desde $s$. El flujo máximo se mantiene en $|f^*|$.
5. **Cómputo en Tiempo Lineal:**
   Un único recorrido BFS/DFS sobre la red residual toma $O(|V| + |E|)$.

#### 3. Demostración Rigurosa de Correctitud

1. **Caso 1 (Arista no saturada originalmente):** Si antes del cambio $f^*(u, v) < c(u, v)$, la arista no era un cuello de botella activo del corte mínimo. El flujo máximo previo ya era el óptimo y al no existir camino de aumento, el algoritmo termina inmediatamente en $O(V + E)$ con $|f_{nuevo}^*| = |f^*|$.
2. **Caso 2 (Arista saturada que habilita aumento):** Si $f^*(u, v) = c(u, v)$, su capacidad residual previa era $0$ y ahora pasa a $1$. Si dicha arista permite conectar las componentes $s$ y $t$ en $G_f'$, existirá un camino simple $P$. Dado que todas las capacidades en $G_f$ son enteras y positivas a lo largo de $P$, la capacidad residual mínima es $\Delta \ge 1$.
3. Al aumentar $1$ unidad de flujo, la capacidad residual de $(u, v)$ vuelve a $0$, restaurando el estado sin caminos de aumento a través de ella.
4. Por el Teorema de Ford-Fulkerson, una red residual sin caminos de aumento certifica que el flujo resultante es estrictamente el flujo máximo.

#### 4. Diagrama Visual del Proceso de Actualización

```mermaid
flowchart LR
    A["c'(u,v) = c(u,v) + 1"] --> B["c'_f(u,v) = c_f(u,v) + 1"]
    B --> C{"¿BFS en G'_f halla<br/>camino s → t?"}
    C -->|Sí| D["Empujar Δ = 1 por P"]:::opt
    D --> E(["Nuevo Flujo = |f*| + 1"]):::opt
    C -->|No| F(["Flujo se mantiene en |f*|"]):::same
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    classDef same fill:#1e40af,stroke:#1e3a8a,stroke-width:2px,color:#fff
```

#### 5. Ejemplo Numérico y Traza

Sea una red con $s \to u \to v \to t$:
- Capacidades: $c(s, u) = 5$, $c(u, v) = 3$, $c(v, t) = 5$.
- Flujo máximo previo: $f^* = 3$ (cuello de botella en $(u, v)$).
- Red residual inicial $G_f$: $c_f(u, v) = 3 - 3 = 0$. No hay camino de $s$ a $t$.
- Se aumenta la capacidad de $(u, v)$ de 3 a 4:
  - $c_f'(u, v) = 0 + 1 = 1$.
  - BFS halla el camino $s \to u \to v \to t$ con capacidades residuales $(2, 1, 2)$.
  - Cuello de botella del camino: $\min(2, 1, 2) = 1$.
  - Se empuja 1 unidad: $f(s, u) = 4, f(u, v) = 4, f(v, t) = 4$.
  - Nuevo flujo máximo: $3 + 1 = 4$.

#### 6. Pseudocódigo del Algoritmo en O(V + E) (Estilo Examen Presencial)

```text
Algoritmo ActualizarFlujoAumentoUnitario(G_f, f, s, t, u, v):
    // 1. Incrementar en 1 unidad la capacidad residual de la arista modificada
    c_f(u, v) = c_f(u, v) + 1

    // 2. Realizar un único BFS desde s en G_f para buscar camino de aumento en O(V + E)
    camino = BFS_BuscarCamino(G_f, s, t)

    // 3. Actualizar flujo si se encontró camino
    si camino != nulo:
        // Como las capacidades son enteras, el cuello de botella es exactamente Delta = 1
        para cada arista (x, y) en camino:
            f(x, y) = f(x, y) + 1
            c_f(x, y) = c_f(x, y) - 1
            c_f(y, x) = c_f(y, x) + 1
        devolver (|f| + 1, f)
    sino:
        // Si no hay camino de aumento, el flujo previo sigue siendo el óptimo
        devolver (|f|, f)
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Ejecutar Edmonds-Karp completo desde cero:</strong> Si se reinicia el algoritmo desde flujo 0, la complejidad vuelve a ser $O(V E^2)$, violando la cota obligatoria de $O(V + E)$ exigida en el enunciado.</li>
    <li><strong>Buscar más de un camino de aumento:</strong> Como la capacidad de una sola arista aumentó en 1, el flujo máximo no puede crecer en más de 1 unidad. Ejecutar un bucle `while` buscando caminos adicionales es conceptualmente redundante.</li>
  </ul>
</div>

---

### Errores Frecuentes en Exámenes sobre Redes de Flujo

1. **Omitir las aristas hacia atrás en la red residual:** No graficar o no considerar las capacidades $c_f(v, u) = f(u, v)$ impide deshacer decisiones subóptimas y es motivo de anulación del algoritmo.
2. **Confundir la capacidad del corte:** Sumar erróneamente aristas dirigidas que van desde el conjunto de destino $B$ hacia el conjunto de origen $A$. La definición matemática solo suma aristas orientadas de $A \to B$.
3. **Ignorar el Teorema de Integralidad:** Asumir que se pueden obtener flujos fraccionarios en redes con capacidades enteras, o no citar este teorema al modelar problemas combinatorios discretos.
4. **Afirmar que Ford-Fulkerson es polinomial:** Ford-Fulkerson depende del valor del flujo $|f^*|$ ($O(E \cdot |f^*|)$), lo que lo hace pseudo-polinomial. El algoritmo polinomial estándar evaluado es **Edmonds-Karp** ($O(V E^2)$).
"""
