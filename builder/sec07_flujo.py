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

### Ejercicio 66 — Asignación de Turnos Médicos y Pacientes (Matching Bipartito Máximo)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2024-2-2 (26 de noviembre de 2024), Ejercicio 4 / Guía 06 Ejercicio 15  
**Qué evalúa la cátedra:** Modelado de matching con capacidades unitarias y franjas horarias mediante Redes de Flujo, creación de nodos compuestos para evitar colisiones de agenda, demostración mediante Teorema de Integralidad y análisis de complejidad.

**Enunciado**  
En un centro médico de alta complejidad se dispone de un conjunto de $M$ profesionales médicos y un conjunto de $P$ pacientes. Cada médico $m \in M$ dispone de un listado de franjas horarias libres $H_m$ para consultas. Cada paciente $p \in P$ requiere a lo sumo una cita médica y ha declarado un listado de tuplas compatibles $(m, h)$ donde puede y desea ser atendido. Se desea diseñar un algoritmo eficiente basado en redes de flujo que determine la asignación que maximice la cantidad total de citas médicas efectivas, garantizando que:
- Ningún médico atienda a más de un paciente en una misma franja horaria.
- Ningún paciente reciba más de un turno médico.
Detallar la topología formal de la red, capacidades, algoritmo empleado, demostración de correctitud y complejidad asintótica.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Cómo armamos los nodos (Red en 4 capas):**
  Para evitar que un mismo médico atienda a dos pacientes en el mismo horario, **no conectamos pacientes directo a médicos**, sino que creamos un nodo compuesto $(m, h)$ por cada par `(médico, horario disponible)`:
  1. **Super-fuente $s$** y **Super-sumidero $t$**.
  2. **Capa de Pacientes:** Un nodo $p$ por cada paciente $p \in P$.
  3. **Capa de Turnos:** Un nodo $(m, h)$ por cada médico $m \in M$ y cada franja libre $h \in H_m$.
* **Qué capacidades ponemos en las aristas:**
  * **De $s$ a cada paciente $p$:** Arista dirigida $(s \to p)$ con **capacidad $1$** (garantiza que cada paciente reciba a lo sumo $1$ turno en total).
  * **De cada paciente $p$ a sus turnos compatibles $(m, h)$:** Arista dirigida $(p \to (m, h))$ con **capacidad $1$** por cada tupla compatible declarada por $p$.
  * **De cada turno $(m, h)$ al sumidero $t$:** Arista dirigida $((m, h) \to t)$ con **capacidad $1$** (garantiza que ese médico en ese horario atienda a lo sumo a $1$ paciente).
* **Por qué funciona (Teorema de Integralidad y Optimalidad):**
  1. **Sin medios turnos (Teorema de Integralidad):** Como todas las capacidades son enteras ($1$), Ford-Fulkerson / Edmonds-Karp garantiza que el flujo óptimo en cada arista será entero ($0$ o $1$). Ningún paciente queda partido entre dos turnos.
  2. **Conservación y validez:** Por conservación de flujo en los nodos intermedios, cada unidad de flujo que sale de $s$ y llega a $t$ pasa por un único paciente $p$ y un único turno $(m, h)$.
  3. **Maximización:** El valor del flujo máximo $|f^*|$ de $s$ a $t$ coincide exactamente con la cantidad máxima posible de citas médicas válidas, y las aristas $(p \to (m, h))$ con flujo $f = 1$ indican qué turno se asignó a cada paciente.

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

#### 2. Semi-Pseudocódigo Simplificado

```text
FUNCION AsignarTurnosMedicos(Medicos, Pacientes, HorariosPorMedico, Compatibilidades):
    Crear red de flujo dirigida G con super-fuente s y super-sumidero t

    // 1. Fuente s -> cada paciente p (capacidad 1: a lo sumo 1 turno por paciente)
    PARA CADA p EN Pacientes:
        agregar_arista(G, s, p, cap = 1)

    // 2. Paciente p -> cada turno compatible (m, h) (capacidad 1)
    PARA CADA p EN Pacientes:
        PARA CADA (m, h) EN Compatibilidades[p]:
            agregar_arista(G, p, (m, h), cap = 1)

    // 3. Turno (m, h) -> sumidero t (capacidad 1: a lo sumo 1 paciente por médico y hora)
    PARA CADA m EN Medicos:
        PARA CADA h EN HorariosPorMedico[m]:
            agregar_arista(G, (m, h), t, cap = 1)

    // 4. Correr flujo máximo con Edmonds-Karp (Ford-Fulkerson con BFS)
    flujo <- EdmondsKarp(G, s, t)

    // 5. Recuperar las citas asignadas (aristas con flujo == 1)
    citas_confirmadas <- []
    PARA CADA arista (p -> (m, h)) EN G:
        SI flujo(p, (m, h)) == 1:
            agregar (p, m, h) a citas_confirmadas

    RETORNAR citas_confirmadas
```

#### 3. Justificación de Complejidad

* **Tamaño de la red:**
  * Nodos: $|V| = 2 + |P| + |T|$, donde $|T| = \sum_{m \in M} |H_m|$ es el total de turnos ofrecidos.
  * Aristas: $|E| = |P| + |C| + |T| = \mathcal{O}(|P| + |C| + |T|)$, donde $|C|$ es el total de compatibilidades declaradas.
* **Costo de armar la red:** Recorrer pacientes, turnos y compatibilidades toma tiempo y espacio lineal **$\mathcal{O}(|V| + |E|)$**.
* **Costo de correr Ford-Fulkerson / Edmonds-Karp:** Como todas las aristas de $s$ a los pacientes tienen capacidad $1$, el flujo máximo está acotado por $|f^*| \le \min(|P|, |T|) \le |P|$. Cada búsqueda de camino de aumento por BFS/DFS cuesta $\mathcal{O}(|E|)$ y aumenta el flujo en al menos $1$ unidad, por lo que ocurren a lo sumo $|P|$ iteraciones. La complejidad temporal total es **$\mathcal{O}(|P| \cdot |E|)$** (estrictamente polinomial), y la complejidad espacial es **$\mathcal{O}(|V| + |E|)$**.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Conectar pacientes directamente a los médicos:</strong> Si se crea un nodo por médico con capacidad igual a la cantidad de horarios, se pierde el control de concurrencia: el algoritmo podría asignarle 3 pacientes al Dr. Pérez a las 09:00 hs. Es <strong>obligatorio crear un nodo por cada par (médico, horario)</strong>.</li>
    <li><strong>Olvidar justificar el Teorema de Integralidad:</strong> Si no se menciona que las capacidades enteras garantizan flujo $0$ o $1$, la cátedra descuenta puntos al asumir que las soluciones podrían ser fraccionarias (ej. paciente atendido $0.5$ por un médico y $0.5$ por otro).</li>
  </ul>
</div>

---

### Patrón de Ejercicio 6.2: Redes de Demanda y Suministro con Super-Nodos

Sistemas de transporte, logística o energía con múltiples fuentes de generación y múltiples centros de consumo, requiriendo super-fuente y super-sumidero para balancear el sistema.

---

### Ejercicio 67 — Red de Distribución Energética con Super-Fuente y Super-Sumidero (Ford-Fulkerson)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2025-1-1 (27 de mayo de 2025), Ejercicio 1  
**Qué evalúa la cátedra:** Modelado de múltiples fuentes y sumideros con cotas heterogéneas, construcción de la red residual, ejecución de Ford-Fulkerson y análisis de corte mínimo para diagnóstico de cuellos de botella energéticos.

**Enunciado**  
El sistema interconectado energético nacional está constituido por 9 regiones geográficas ($R_1, \dots, R_9$). Para cada región $i$ se conoce su capacidad de generación prevista $G_i \ge 0$ (MWh) y su demanda requerida $D_i \ge 0$ (MWh). Entre pares de regiones existen líneas de transmisión de alta tensión con capacidad máxima $CAP_{ij}$ MWh/día. Se desea diseñar un algoritmo basado en redes de flujo que determine si es factible abastecer la demanda total de todas las regiones y, en caso afirmativo, cuánta energía transportar por cada línea. Si la demanda no puede cubrirse, el algoritmo debe identificar el conjunto crítico de líneas que causan el cuello de botella.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Cómo armamos los nodos (Super-Fuente $S$ y Super-Sumidero $T$):**
  Como tenemos múltiples regiones que generan energía y múltiples regiones que consumen, creamos una **Super-Fuente $S$** (que inyecta toda la generación disponible del país) y un **Super-Sumidero $T$** (que absorbe toda la demanda requerida), además de los $9$ nodos de las regiones $R_1, \dots, R_9$.
* **Qué capacidades ponemos en las aristas:**
  * **De la Super-Fuente $S$ a cada región generadora $R_i$ ($G_i > 0$):** Arista dirigida $(S \to R_i)$ con **capacidad $G_i$** (máxima energía que puede aportar esa región).
  * **De cada región consumidora $R_j$ ($D_j > 0$) al Super-Sumidero $T$:** Arista dirigida $(R_j \to T)$ con **capacidad $D_j$** (demanda que necesita cubrir esa región).
  * **Entre regiones conectadas $(R_i, R_j)$:** Arista dirigida $(R_i \to R_j)$ con **capacidad $CAP_{ij}$** (límite físico de la línea de alta tensión).
* **Por qué funciona (Conservación de Flujo y Corte Mínimo):**
  1. **Condición de factibilidad total:** Sea $D_{\text{total}} = \sum_{j=1}^9 D_j$ la demanda nacional. Por conservación de flujo en cada región, todo lo que entra (generación local desde $S$ $+$ importación) es igual a todo lo que sale (consumo local hacia $T$ $+$ exportación). Como las aristas que llegan a $T$ suman capacidad $D_{\text{total}}$, el flujo máximo de $S$ a $T$ es a lo sumo $D_{\text{total}}$.
  2. **Si $\text{FlujoMax}(S, T) == D_{\text{total}}$:** Todas las aristas $(R_j \to T)$ se saturaron al $100\%$, por lo que **es factible cubrir toda la demanda** y el flujo $f(R_i, R_j)$ da los MWh a enviar por cada línea.
  3. **Diagnóstico de cuellos de botella (Teorema Max-Flow Min-Cut):** Si $\text{FlujoMax}(S, T) < D_{\text{total}}$, la demanda no se puede abastecer. Corremos un BFS desde $S$ en la red residual final $G_f$ para obtener el conjunto $A$ de nodos alcanzables y $B = V \setminus A$. Las líneas originales $(R_i \to R_j)$ que cruzan de $A$ hacia $B$ están saturadas al $100\%$ y forman el **corte mínimo (cuello de botella físico)** que impide llegar a $D_{\text{total}}$.

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

#### 2. Semi-Pseudocódigo Simplificado

```text
FUNCION AbastecerRedEnergetica(Regiones, Generacion, Demanda, Lineas):
    Crear red de flujo G con Super-Fuente S y Super-Sumidero T
    D_total <- 0

    // 1. Conectar Super-Fuente S a regiones con generación y regiones con demanda a T
    PARA CADA r EN Regiones:
        SI Generacion[r] > 0:
            agregar_arista(G, S, r, cap = Generacion[r])
        SI Demanda[r] > 0:
            agregar_arista(G, r, T, cap = Demanda[r])
            D_total <- D_total + Demanda[r]

    // 2. Agregar líneas de transmisión entre regiones
    PARA CADA (u, v, CAP_uv) EN Lineas:
        agregar_arista(G, u, v, cap = CAP_uv)

    // 3. Ejecutar Edmonds-Karp (Ford-Fulkerson con BFS)
    (flujo_max, f, G_f) <- EdmondsKarp(G, S, T)

    // 4. Verificar si se cubrió el 100% de la demanda o hallar el Corte Mínimo
    SI flujo_max == D_total:
        RETORNAR ("FACTIBLE", f)
    SINO:
        A <- NodosAlcanzablesConBFS(G_f, S)
        cuellos_de_botella <- []
        PARA CADA (u, v, CAP_uv) EN Lineas:
            SI u PERTENECE A A Y v NO PERTENECE A A:
                agregar (u, v) a cuellos_de_botella
        RETORNAR ("INFACTIBLE - Cuellos de botella:", cuellos_de_botella)
```

#### 3. Justificación de Complejidad

* **Tamaño de la red:** Para $R$ regiones ($R = 9$ en el enunciado), la red tiene $|V| = R + 2$ nodos y $|E| \le 2R + |\text{Líneas}|$ aristas (a lo sumo $9 + 9 + 72 = 90$ aristas).
* **Costo de armar la red y hallar el corte:** Construir la red y hacer el BFS final sobre $G_f$ cuesta **$\mathcal{O}(|V| + |E|)$**.
* **Costo de correr Edmonds-Karp:** La complejidad temporal es estrictamente polinomial **$\mathcal{O}(|V| \cdot |E|^2)$** (con $R = 9$ es $\mathcal{O}(1)$ en la práctica, apenas $\sim 11 \times 90^2 \approx 89.100$ operaciones). Si se usa Ford-Fulkerson con DFS, es pseudo-polinomial $\mathcal{O}(|E| \cdot D_{\text{total}})$. Complejidad espacial: **$\mathcal{O}(|V| + |E|)$**.

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

### Ejercicio 68 — Análisis Teórico: Aumento Uniforme de Capacidades y Corte Mínimo

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2024-2-3 (10 de diciembre de 2024), Ejercicio 1  
**Qué evalúa la cátedra:** Comprensión matemática rigurosa de la definición de capacidad de un corte, sensibilidad ante perturbaciones uniformes $+1$, y construcción de contraejemplos matemáticos minimales irrebatibles.

**Enunciado**  
Indicar si la siguiente afirmación es verdadera o falsa. Si es verdadera, proveer una demostración formal rigurosa. Si es falsa, construir un contraejemplo explícito indicando nodos, aristas, capacidades originales, corte original, nuevas capacidades y el nuevo corte mínimo:  
*“Sea $G = (V, E)$ una red de flujo arbitraria con fuente $s$, sumidero $t$ y capacidades enteras positivas $c(e)$ en cada arista $e \in E$. Sea $(A, B)$ un corte mínimo $s-t$ con respecto a las capacidades $c$. Si se suma $1$ a la capacidad de cada arista de la red ($c'(e) = c(e) + 1$), el corte $(A, B)$ sigue siendo obligatoriamente un corte mínimo respecto a las nuevas capacidades $c'$.”*

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Respuesta directa:** **La afirmación es FALSA.**
* **Por qué falla (Justificación en un renglón):** Cuando sumamos $+1$ a la capacidad de **cada arista**, la capacidad de un corte $(A, B)$ **no aumenta en $+1$**, sino que aumenta en **$+1$ por cada arista que cruza el corte**:
  $$C'(A, B) = \sum_{e \in \delta^+(A)} (c(e) + 1) = C(A, B) + |\delta^+(A)|$$
  Por lo tanto, un corte que era mínimo pero tenía **muchas aristas chicas** sube mucho más que otro corte que tenía **una sola arista grande**, dejando de ser el corte mínimo.
* **Contraejemplo de un renglón para la hoja:**
  * Armamos una red donde el **Corte 1** ($A_1 = \{s\}$) tiene **$5$ aristas en paralelo** de capacidad $2$ saliendo de $s$ hacia un nodo intermedio $v$ (capacidad original $C_1 = 5 \times 2 = \mathbf{10}$), y el **Corte 2** ($A_2 = V \setminus \{t\}$) tiene **$1$ sola arista** desde $v$ hacia $t$ de capacidad $\mathbf{11}$ ($C_2 = 11$).
  * **Antes de sumar $+1$:** El corte mínimo único es el **Corte 1** porque $10 < 11$.
  * **Después de sumar $+1$ a cada arista:** Las $5$ aristas del Corte 1 pasan a capacidad $3$ y su corte sube a $C'_1 = 5 \times 3 = \mathbf{15}$, mientras que la única arista del Corte 2 pasa de $11$ a $C'_2 = \mathbf{12}$. Como ahora $12 < 15$, el Corte 1 **dejó de ser mínimo** y el nuevo corte mínimo es el Corte 2.

| Corte Evaluado | Aristas que cruzan de $A$ a $B$ | Capacidad Original $C$ | Cantidad de Aristas $|\delta^+|$ | Nueva Capacidad $C' = C + |\delta^+|$ | ¿Es Corte Mínimo? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Corte 1 ($A_1=\{s\}$)** | $5$ aristas de capacidad $2$ | **$10$** | $5$ | $10 + 5 = \mathbf{15}$ | **Antes SÍ ($10 < 11$) / Después NO** |
| **Corte 2 ($B_2=\{t\}$)** | $1$ arista de capacidad $11$ | $11$ | $1$ | $11 + 1 = \mathbf{12}$ | **Antes NO / Después SÍ ($12 < 15$)** |

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

#### 2. Semi-Pseudocódigo Simplificado

```text
// Construcción y verificación formal del contraejemplo en papel:
PROCEDIMIENTO ContraejemploCorteMinimoMasUno():
    // Grafo con fuente s, nodos intermedios u1..u5, v y sumidero t
    // Corte 1: A1 = {s}, B1 = {u1..u5, v, t} -> corta las 5 aristas (s, u_i) de cap 2
    C_original_Corte1 <- 5 * 2   // = 10 (Corte Mínimo Original)

    // Corte 2: A2 = {s, u1..u5, v}, B2 = {t} -> corta la única arista (v, t) de cap 11
    C_original_Corte2 <- 1 * 11  // = 11

    // Al sumar +1 a toda arista e de la red, cada corte suma su cantidad de aristas:
    C_nuevo_Corte1 <- C_original_Corte1 + 5  // 10 + 5 = 15
    C_nuevo_Corte2 <- C_original_Corte2 + 1  // 11 + 1 = 12

    // Como C_nuevo_Corte2 (12) < C_nuevo_Corte1 (15), A1 dejó de ser corte mínimo
    RETORNAR FALSO
```

#### 3. Justificación de Complejidad

* **Verificación del contraejemplo:** El grafo construido tiene $|V| = 8$ nodos y $|E| = 11$ aristas; calcular la capacidad de ambos cortes antes y después de la perturbación toma tiempo constante **$\mathcal{O}(1)$** (y en un grafo general de $|E|$ aristas, evaluar la capacidad de un corte dado $(A, B)$ cuesta **$\mathcal{O}(|E|)$** recorriendo las aristas que van de $A$ hacia $B$).

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Decir que es Verdadera asumiendo que "sumar una constante no cambia el mínimo":</strong> En optimización lineal, sumar una constante a la función objetivo no cambia el óptimo. Pero aquí <strong>no se suma una constante al corte</strong>, se suma 1 a cada arista, por lo que a cada corte se le suma una constante distinta proporcional a su cantidad de aristas ($C' = C + k$).</li>
    <li><strong>Dar un contraejemplo sin valores numéricos explícitos:</strong> Un contraejemplo debe incluir el grafo completo, los conjuntos de vértices $A$ y $B$, y la cuenta aritmética explícita de antes y después.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 6.4: Actualización Dinámica de Flujo Máximo

Se dispone del flujo máximo y red residual calculados y se incrementa la capacidad de una única arista en 1 unidad. Se pide actualizar el flujo en tiempo lineal $O(V + E)$ sin reejecutar el algoritmo desde cero.

---

### Ejercicio 69 — Actualización de Flujo Máximo ante Aumento de Capacidad Unitaria en O(V + E)

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía de Ejercicios 06, Ejercicio 5  
**Qué evalúa la cátedra:** Comprensión profunda de la red residual, explotación del estado previo para actualización incremental (*dynamic max-flow*) y cota estricta de caminos de aumento en $O(V + E)$.

**Enunciado**  
Dada una red de flujo $G = (V, E)$ con capacidades enteras positivas, se ha calculado previamente un flujo máximo $f^*$ de $s$ a $t$ y se dispone de su red residual asociada $G_f$. Supongamos que se incrementa en una unidad la capacidad de una arista arbitraria $(u, v) \in E$ (de $c(u, v)$ pasa a $c(u, v) + 1$). Diseñar un algoritmo que recalcule el nuevo flujo máximo en tiempo estrictamente acotado por $O(V + E)$. Justificar la correctitud y la cota temporal.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Cómo actualizamos la red residual:**
  No debemos reiniciar Ford-Fulkerson desde cero (eso tardaría $\mathcal{O}(V E^2)$). Aprovechamos la red residual $G_f$ que ya tenemos calculada y simplemente **sumamos $+1$ a la capacidad residual directa de la arista modificada**:
  $$c'_f(u, v) = c_f(u, v) + 1$$
* **Por qué el flujo máximo solo puede subir en $0$ o en $1$ (Teorema de Corte Mínimo e Integralidad):**
  1. Como solo aumentamos en $+1$ la capacidad de una única arista $(u, v)$, la capacidad del corte mínimo de la red puede aumentar **a lo sumo en $1$ unidad** (sube en $1$ si $(u, v)$ era parte de todos los cortes mínimos, o en $0$ si existe otro cuello de botella).
  2. Como todas las capacidades son enteras, por el **Teorema de Integralidad** el nuevo flujo máximo solo puede valer $|f^*|$ o $|f^*| + 1$.
* **Cómo hallamos el nuevo flujo óptimo en un solo paso:**
  Corremos **un único BFS (o DFS)** desde la fuente $s$ hasta el sumidero $t$ sobre la red residual actualizada $G'_f$:
  * **Si el BFS encuentra un camino de aumento $P$ de $s$ a $t$:** Como las capacidades residuales son enteras positivas, el cuello de botella es al menos $1$. Empujamos $\Delta = 1$ unidad de flujo por $P$, actualizamos $G'_f$ y devolvemos $|f^*| + 1$ (que ya es máximo porque no puede subir más de $1$).
  * **Si el BFS no llega a $t$:** No existe camino de aumento en $G'_f$, por lo que el flujo máximo sigue siendo exactamente $f^*$ con valor $|f^*|$.

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

#### 2. Semi-Pseudocódigo Simplificado

```text
FUNCION ActualizarFlujoMasUno(G_f, f, valor_flujo, s, t, u, v):
    // 1. Actualizar en O(1) la capacidad residual de la única arista modificada
    c_f(u, v) <- c_f(u, v) + 1

    // 2. Buscar UN único camino de aumento de s a t en G_f usando BFS
    camino_P <- BuscarCaminoBFS(G_f, s, t)

    // 3. Si existe camino, empujar exactamente 1 unidad de flujo
    SI camino_P != NULO:
        PARA CADA arista (x, y) EN camino_P:
            SI (x, y) es arista original:
                f(x, y) <- f(x, y) + 1
            SINO:
                f(y, x) <- f(y, x) - 1
            c_f(x, y) <- c_f(x, y) - 1
            c_f(y, x) <- c_f(y, x) + 1

        RETORNAR (valor_flujo + 1, f)

    // Si no hay camino a t, el flujo máximo no cambió
    RETORNAR (valor_flujo, f)
```

#### 3. Justificación de Complejidad

* **Actualización de la arista $(u, v)$:** Incrementar $c_f(u, v)$ en $1$ cuesta **$\mathcal{O}(1)$**.
* **Búsqueda y aumento en la red residual:** Ejecutamos **una sola vez** el recorrido BFS desde $s$ hasta $t$ sobre $G'_f$, lo cual visita cada nodo y arista a lo sumo una vez en tiempo **$\mathcal{O}(|V| + |E|)$**. Si halla el camino simple $P$ (de longitud a lo sumo $|V|$ aristas), actualizar el flujo a lo largo de $P$ cuesta $\mathcal{O}(|V|)$.
* **Complejidad Total:** Tiempo **$\mathcal{O}(|V| + |E|)$** y espacio adicional **$\mathcal{O}(|V|)$** para la cola y el arreglo de visitados/padres del BFS.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Ejecutar Edmonds-Karp completo desde cero:</strong> Si se reinicia el algoritmo desde flujo 0, la complejidad vuelve a ser $O(V E^2)$, violando la cota obligatoria de $O(V + E)$ exigida en el enunciado.</li>
    <li><strong>Buscar más de un camino de aumento:</strong> Como la capacidad de una sola arista aumentó en 1, el flujo máximo no puede crecer en más de 1 unidad. Ejecutar un bucle <code>while</code> buscando caminos adicionales es conceptualmente redundante.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 6.5: Transporte Multipunto hacia un Sumidero Central

Problemas logísticos donde existen $N$ nodos de origen independientes que envían caudal a través de una red de postas o nodos intermedios hacia un único nodo destino final, resueltos mediante la introducción de una Super-Fuente $s$.

---

### Ejercicio 70 — Transporte de Urnas Electorales al Centro Nacional de Estadísticas

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2026-2-1 (Enunciados), Ejercicio 6

**Enunciado**  
Luego de las elecciones del domingo, en cierto país limítrofe, se deben llevar las urnas desde los $N$ centros de votación ($C_1, C_2, \dots, C_N$) hasta el Centro Nacional de Estadísticas ($CNE$) para proceder al escrutinio definitivo. Desde los centros de votación hay caminos que pasan por diversos puntos intermedios (como $A$ y $B$ en el grafo de referencia). Para cada camino se sabe la cantidad máxima de urnas por minuto que se pueden transportar. Diseñar un algoritmo que mediante Ford-Fulkerson (FF) calcule la cantidad de urnas a transportar por cada ruta para maximizar la cantidad de urnas transportadas por minuto. Indicar la complejidad del algoritmo desarrollado.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* El algoritmo de **Ford-Fulkerson** requiere una red de transporte con **una única fuente $s$** y **un único sumidero $t$**. En este problema ya contamos con un único sumidero natural, que es el **Centro Nacional de Estadísticas ($t = CNE$)**, pero tenemos múltiples orígenes ($C_1, C_2, \dots, C_N$).
* **Reducción a fuente única:** Creamos un nodo ficticio llamado **Super-Fuente $s$** y agregamos una arista dirigida desde $s$ hacia cada uno de los $N$ centros de votación $(s \to C_i)$ con **capacidad $\infty$** (o bien, con capacidad igual a la suma de las capacidades de todos los caminos que salen de $C_i$, ya que el enunciado no impone un tope de emisión en el centro sino en las rutas).
* **Conservación en puntos intermedios y maximización:** Los puntos de paso intermedios (como $A, B, \dots$) actúan como nodos internos donde rige la ley de conservación de flujo ($\text{urnas que entran por minuto} = \text{urnas que salen por minuto}$), y cada tramo vial dirigido $(u, v)$ conserva su capacidad máxima de urnas por minuto $c(u, v)$. Al ejecutar **Ford-Fulkerson** (implementado mediante **Edmonds-Karp** usando BFS para elegir siempre el camino de aumento más corto en cantidad de aristas) desde $s$ hasta $CNE$, el flujo final $f(u, v)$ en cada arista indica exactamente cuántas urnas por minuto deben enviarse por cada camino para alcanzar el máximo caudal posible hacia el $CNE$.

```mermaid
flowchart LR
    s(("Super-Fuente s")) -->|"cap = ∞"| C1(("C1"))
    s -->|"cap = ∞"| C2(("C2"))
    s -->|"cap = ∞"| C3(("C3"))

    C1 -->|"c(C1, A)"| A(("A"))
    C1 -->|"c(C1, CNE)"| CNE(("CNE (Sumidero t)"))
    C2 -->|"c(C2, A)"| A
    C2 -->|"c(C2, B)"| B(("B"))
    C3 -->|"c(C3, B)"| B
    C3 -->|"c(C3, CNE)"| CNE

    A -->|"c(A, B)"| B
    A -->|"c(A, CNE)"| CNE
    B -->|"c(B, CNE)"| CNE

    classDef src fill:#1d4ed8,stroke:#1e40af,stroke-width:2px,color:#fff
    classDef snk fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    class s src
    class CNE snk
```

#### 2. Semi-Pseudocódigo Simplificado

```text
FUNCION MaximizarTransporteUrnasFF(Centros, NodosIntermedios, Caminos, CNE):
    // 1. Construir la red de flujo G = (V, E) y la red residual G_f
    Crear grafo dirigido G y grafo residual G_f
    Crear nodo ficticio SuperFuente s
    Sumidero t <- CNE

    // Conectar la Super-Fuente s a cada centro de votación C_i
    PARA CADA C_i EN Centros:
        agregar_arista(G, s, C_i, capacidad = INFINITO)
        c_f(s, C_i) <- INFINITO
        c_f(C_i, s) <- 0

    // Cargar todos los caminos viales (u -> v) con su capacidad máxima de urnas/minuto
    PARA CADA (u, v, max_urnas_min) EN Caminos:
        agregar_arista(G, u, v, capacidad = max_urnas_min)
        f(u, v) <- 0
        c_f(u, v) <- max_urnas_min
        c_f(v, u) <- 0

    flujo_total_urnas <- 0

    // 2. Ciclo principal de Ford-Fulkerson (Edmonds-Karp con BFS)
    MIENTRAS exista un camino P desde s hasta t en G_f con c_f > 0 (hallado con BFS):
        // Cuello de botella del camino de aumento P
        delta <- MINIMO { c_f(u, v) para toda arista (u, v) en P }

        // Actualizar flujos y capacidades residuales (directas y reversas)
        PARA CADA arista (u, v) EN P:
            SI (u, v) es arista original de G:
                f(u, v) <- f(u, v) + delta
            SINO:
                // Se usó una arista backward (reversa): deshacemos flujo previo
                f(v, u) <- f(v, u) - delta

            c_f(u, v) <- c_f(u, v) - delta
            c_f(v, u) <- c_f(v, u) + delta

        flujo_total_urnas <- flujo_total_urnas + delta

    // 3. Devolver el máximo de urnas/minuto y el detalle por cada camino original
    RETORNAR (flujo_total_urnas, f)
```

#### 3. Justificación de Complejidad

* **Con Ford-Fulkerson clásico (búsqueda de camino arbitrario con DFS):** En cada iteración se busca un camino de aumento en la red residual en tiempo $\mathcal{O}(|E|)$ (dado que $|V| \le |E| + 1$) y, al ser las capacidades enteras (urnas por minuto), el flujo aumenta al menos en $1$ unidad por iteración. Por lo tanto, la complejidad temporal es **$\mathcal{O}(|E| \cdot |f^*|)$** (pseudo-polinomial), donde $|f^*|$ es el flujo máximo total de urnas por minuto que llegan al $CNE$.
* **Con Edmonds-Karp (implementación de Ford-Fulkerson usando BFS para elegir el camino más corto en cantidad de aristas):** Se garantiza que ocurren a lo sumo $\mathcal{O}(|V| \cdot |E|)$ aumentos de flujo, y cada BFS toma $\mathcal{O}(|E|)$. Por lo tanto, la complejidad temporal es estrictamente polinomial **$\mathcal{O}(|V| \cdot |E|^2)$**, donde $|V| = N + |\text{NodosIntermedios}| + 2$ y $|E| = N + |\text{Caminos}|$.
* **Complejidad Espacial:** **$\mathcal{O}(|V| + |E|)$** para almacenar la red de flujo, la red residual $G_f$ y la cola del BFS.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Ejecutar $N$ veces Ford-Fulkerson por separado desde cada centro $C_i$:</strong> Correr flujo máximo desde $C_1$ a $CNE$, luego desde $C_2$, etc., es incorrecto o subóptimo si no se mantiene una única red residual compartida. La forma limpia y estándar es unificar todos los orígenes con una única <strong>Super-Fuente $s$</strong> antes de iniciar el algoritmo.</li>
    <li><strong>Omitir las aristas reversas (backward) $c_f(v, u)$ en la red residual:</strong> En el grafo del parcial existen enlaces cruzados entre nodos intermedios ($A \to B$). Sin aristas reversas, Ford-Fulkerson no puede reencaminar flujo y puede devolver un valor menor al óptimo.</li>
  </ul>
</div>

---

### Errores Frecuentes en Exámenes sobre Redes de Flujo

1. **Omitir las aristas hacia atrás en la red residual:** No graficar o no considerar las capacidades $c_f(v, u) = f(u, v)$ impide deshacer decisiones subóptimas y es motivo de anulación del algoritmo.
2. **Confundir la capacidad del corte:** Sumar erróneamente aristas dirigidas que van desde el conjunto de destino $B$ hacia el conjunto de origen $A$. La definición matemática solo suma aristas orientadas de $A \to B$.
3. **Ignorar el Teorema de Integralidad:** Asumir que se pueden obtener flujos fraccionarios en redes con capacidades enteras, o no citar este teorema al modelar problemas combinatorios discretos.
4. **Afirmar que Ford-Fulkerson es polinomial:** Ford-Fulkerson depende del valor del flujo $|f^*|$ ($O(E \cdot |f^*|)$), lo que lo hace pseudo-polinomial. El algoritmo polinomial estándar evaluado es **Edmonds-Karp** ($O(V E^2)$).
"""
