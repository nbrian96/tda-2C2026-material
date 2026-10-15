"""Módulo 7: Redes de Flujo (Flujo Máximo y Corte Mínimo)."""

def get_content():
    return r"""## 9. Tema 6: Redes de Flujo (Flujo Máximo y Corte Mínimo)

### Conceptos Mínimos de Supervivencia

1. **Definiciones y Leyes Fundamentales:**
   * **Red de Transporte:** Grafo dirigido G = (V, E) con un nodo fuente s, un nodo sumidero t, y capacidades no negativas c(u, v) ≥ 0 en cada arista.
   * **Restricción de Capacidad:** Para toda arista (u, v) ∈ E: 0 ≤ f(u, v) ≤ c(u, v).
   * **Conservación de Flujo:** Para todo vértice intermedio u ∈ V \ {s, t}:
     > **∑_{v ∈ V} f(v, u) = ∑_{w ∈ V} f(u, w)** (lo que entra es igual a lo que sale)
2. **Red Residual (G_f) y Aristas Hacia Atrás:**
   La red residual modela la capacidad disponible para empujar más flujo o para **deshacer** flujo previamente enviado:
   * Arista hacia adelante (forward): capacidad residual c_f(u, v) = c(u, v) - f(u, v).
   * Arista hacia atrás (backward): capacidad residual c_f(v, u) = f(u, v) (permite reencaminar flujo cancelando compromisos previos).
3. **Algoritmos de Resolución:**
   * **Ford-Fulkerson:** Busca caminos de aumento arbitrarios en G_f. Complejidad O(E · |f*|) (pseudo-polinomial con capacidades enteras).
   * **Edmonds-Karp:** Elige caminos de aumento de **menor cantidad de aristas** mediante búsqueda en anchura (BFS). Complejidad polinomial estricta: O(V · E²).
4. **Teorema Flujo Máximo = Corte Mínimo (Max-Flow Min-Cut):**
   * Un corte (A, B) es una partición de V tal que s ∈ A y t ∈ B.
   * La **capacidad del corte** es la suma de las capacidades de las aristas que van estrictamente de A a B: C(A, B) = ∑_{u ∈ A, v ∈ B} c(u, v).
   * **Teorema:** El valor del flujo máximo de s a t es exactamente igual a la capacidad del corte mínimo que separa s de t.
   * **Obtención del Corte Mínimo:** Una vez saturada la red (sin caminos de aumento), el conjunto A está formado por todos los nodos alcanzables desde s en la red residual final G_f, y B = V \ A.

---

### Patrón de Ejercicio 6.1: Matching Bipartito y Asignación con Restricciones

Problemas de asignación de personas a turnos, médicos a pacientes, estudiantes a materias o tareas a máquinas.

---

### Ejercicio 24 — Asignación de Turnos Médicos y Pacientes (Matching Bipartito Máximo)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-2 (26 de noviembre de 2024), Ejercicio 4 / Guía 06 Ejercicio 15

**Enunciado**  
En un hospital se tiene un conjunto de M médicos y un conjunto de P pacientes. Cada médico m dispone de un conjunto de franjas horarias libres H_m para citas médicas. Cada paciente p necesita a lo sumo una cita y tiene un listado de médicos y franjas horarias en las cuales puede ser atendido. Nuestro objetivo es emparejar médicos con pacientes de manera que se maximice el número total de citas médicas programadas, asegurando que ningún médico atienda a más de un paciente en una misma franja horaria y ningún paciente tenga más de una cita.  
1. Implementar un algoritmo que resuelva dicho problema de manera eficiente mediante redes de flujo.  
2. Detallar la construcción formal de la red (nodos, aristas, fuentes, sumideros y capacidades).  
3. Indicar y justificar la complejidad del algoritmo implementado.

**Qué está evaluando**  
Modelado de asignación con capacidades unitarias mediante Redes de Flujo, creación de capas intermedias para franjas horarias, y aplicación del Teorema de Integralidad.

**Idea de resolución**  
* Construimos un grafo dirigido con 4 capas de nodos:
  1. Nodo super-fuente s.
  2. Capa de pacientes: un nodo p por cada paciente p ∈ P.
  3. Capa de turnos específicos: un nodo (m, h) por cada médico m y franja horaria disponible h ∈ H_m.
  4. Nodo super-sumidero t.
* **Aristas y Capacidades:**
  * Desde s a cada paciente p: capacidad c(s, p) = 1 (cada paciente recibe a lo sumo 1 cita).
  * Desde cada paciente p al turno (m, h) si el paciente es compatible con ese médico y horario: capacidad c(p, (m, h)) = 1.
  * Desde cada turno (m, h) al sumidero t: capacidad c((m, h), t) = 1 (un médico solo atiende a un paciente en esa franja horaria).
* Corremos Edmonds-Karp o Ford-Fulkerson para hallar el flujo máximo de s a t. Por el Teorema de Integralidad, cada arista tendrá flujo 0 o 1, definiendo el emparejamiento óptimo sin conflictos.

**Pseudocódigo**

```text
FUNCION AsignarCitasMedicas(pacientes, medicos_horarios, compatibilidades):
    // 1. Construcción de la Red de Flujo G
    INICIALIZAR Red como grafo dirigido con capacidades
    s <- "SUPER_FUENTE"
    t <- "SUPER_SUMIDERO"

    // Aristas de fuente a pacientes
    PARA CADA p EN pacientes:
        AgregarArista(Red, s, p, capacidad=1)

    // Aristas de compatibilidad entre pacientes y turnos
    PARA CADA (p, m, h) EN compatibilidades:
        turno_id <- Concatenar(m, "_", h)
        AgregarArista(Red, p, turno_id, capacidad=1)

    // Aristas de turnos al sumidero
    PARA CADA (m, h) EN medicos_horarios:
        turno_id <- Concatenar(m, "_", h)
        AgregarArista(Red, turno_id, t, capacidad=1)

    // 2. Ejecución de Ford-Fulkerson / Edmonds-Karp
    (flujo_max, flujo_aristas) <- EdmondsKarp(Red, s, t)

    // 3. Extracción del emparejamiento óptimo
    INICIALIZAR asignaciones como lista vacía
    PARA CADA (p, m, h) EN compatibilidades:
        turno_id <- Concatenar(m, "_", h)
        SI flujo_aristas[(p, turno_id)] = 1:
            INSERTAR (paciente=p, medico=m, horario=h) EN asignaciones

    RETORNAR (flujo_max, asignaciones)
```

**Explicación del algoritmo**  
La red fuerza a que cada paciente consuma a lo sumo 1 unidad de flujo desde s, y que cada turno de médico expulse a lo sumo 1 unidad hacia t. La conservación de flujo en los nodos intermedios asegura que un paciente solo se vincule con un médico en un horario compatible. Al ser todas las capacidades enteras, el flujo máximo equivale al matching máximo.

**Complejidad**  
* La cantidad total de nodos es |V| = 2 + |P| + ∑ |H_m| = O(|P| + |Turnos|).
* El flujo máximo está acotado superiormente por el número de pacientes: |f*| ≤ |P|.
* Cada camino de aumento encontrado por BFS toma O(E).
* Complejidad total con Ford-Fulkerson: **O(|P| · |E|)**, lo cual es estrictamente polinomial y muy eficiente para capacidades unitarias.

**Puntos donde puedo equivocarme**  
* Conectar al médico directamente con capacidad infinita en lugar de separar por franja horaria (m, h), lo que permitiría que un médico atienda a varios pacientes a la misma hora.
* Olvidar justificar por qué la solución es entera (debe citarse el **Teorema de Integralidad de Flujo**).

---

### Patrón de Ejercicio 6.2: Redes de Demanda y Suministro con Super-Nodos

Sistemas de transporte o energía con múltiples fuentes de generación y múltiples centros de consumo, requiriendo super-fuente y super-sumidero para balancear el sistema.

---

### Ejercicio 25 — Red de Distribución Energética con Super-Fuente y Super-Sumidero (Ford-Fulkerson)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2025-1-1 (27 de mayo de 2025), Ejercicio 1

**Enunciado**  
El sistema energético argentino está dividido en 9 regiones. Para cada región se conoce su Generación prevista G_i y su Demanda esperada D_i. Desde cualquier región i se puede enviar energía a la región j con una capacidad máxima de transporte de CAP_ij MWh por día. Realizar un algoritmo que, mediante Ford-Fulkerson, determine cuánta energía transportar entre cada par de zonas para cubrir las demandas. Detallar todos los pasos de la construcción de la red y del algoritmo de flujo.

**Qué está evaluando**  
Modelado de problemas con múltiples fuentes y múltiples sumideros mediante la técnica de super-fuente (s) y super-sumidero (t), y ejecución paso a paso de Ford-Fulkerson.

**Idea de resolución**  
1. **Construcción de la Red:**
   * Nodos: las 9 regiones más un super-nodo fuente S y un super-nodo sumidero T.
   * Para cada región i con generación G_i > 0: agregamos una arista dirigida S → i con capacidad c(S, i) = G_i.
   * Para cada región j con demanda D_j > 0: agregamos una arista dirigida j → T con capacidad c(j, T) = D_j.
   * Para cada par de regiones con línea de transmisión: arista i → j con capacidad CAP_ij.
2. **Determinación de Factibilidad:**
   * La demanda total requerida es D_total = ∑_j D_j.
   * Calculamos el flujo máximo de S a T.
   * Si FlujoMax = D_total, la demanda de todas las regiones queda completamente satisfecha y los flujos en las aristas i → j indican la energía a transportar. Si es menor, el sistema tiene un déficit insalvable por cuello de botella de transmisión o falta de generación.

**Pseudocódigo del Algoritmo de Ford-Fulkerson**

```text
FUNCION ResolverFlujoEnergetico(regiones, G, D, CAP):
    // 1. Construir red con super-fuente S y super-sumidero T
    INICIALIZAR Red con nodos S, T y todas las regiones
    PARA CADA r EN regiones:
        SI G[r] > 0:
            AgregarArista(Red, S, r, G[r])
        SI D[r] > 0:
            AgregarArista(Red, r, T, D[r])

    PARA CADA (u, v) EN lineas:
        AgregarArista(Red, u, v, CAP[u][v])

    // 2. Inicializar flujo f en 0 para todas las aristas
    INICIALIZAR flujo como diccionario con 0 para cada arista
    INICIALIZAR RedResidual como copia de Red con capacidades originales

    // 3. Bucle principal de Ford-Fulkerson
    camino <- BuscarCaminoAumento(RedResidual, S, T) // Vía BFS o DFS

    MIENTRAS camino != NULO:
        // Cuello de botella: mínima capacidad residual en el camino
        cuello_botella <- INFINITO
        PARA CADA arista (u, v) EN camino:
            SI RedResidual[u][v] < cuello_botella:
                cuello_botella <- RedResidual[u][v]

        // Aumentar flujo y actualizar red residual
        PARA CADA arista (u, v) EN camino:
            flujo[u][v] <- flujo[u][v] + cuello_botella
            // Arista hacia adelante disminuye
            RedResidual[u][v] <- RedResidual[u][v] - cuello_botella
            // Arista hacia atrás (antiparalela) aumenta
            RedResidual[v][u] <- RedResidual[v][u] + cuello_botella

        camino <- BuscarCaminoAumento(RedResidual, S, T)

    // 4. Calcular valor del flujo máximo
    flujo_total <- 0
    PARA CADA r EN regiones:
        flujo_total <- flujo_total + flujo[S][r]

    RETORNAR (flujo_total, flujo)
```

**Complejidad**  
* Si usamos Edmonds-Karp (BFS para el camino de aumento), la complejidad es estrictamente polinomial: O(V · E²). Con 9 regiones, |V| = 11 y |E| ≤ 90, corriendo en menos de 1 milisegundo.

---

### Patrón de Ejercicio 6.3: Análisis Teórico y Propiedades de Cortes Mínimos

Preguntas conceptuales de Verdadero/Falso con justificación formal o construcción de contraejemplos minimales sobre perturbaciones en las capacidades de las aristas.

---

### Ejercicio 26 — Análisis Teórico: Aumento Uniforme de Capacidades y Corte Mínimo

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-3 (10 de diciembre de 2024), Ejercicio 1

**Enunciado**  
Indicar si la siguiente afirmación es verdadera o falsa. Si es verdadera, indicar por qué. Si es falsa, dar un contraejemplo riguroso:  
*“Sea G una red de flujo arbitraria, con una fuente s y un sumidero t y una capacidad entera positiva c_e en cada arista e. Sea A-B un corte mínimo s-t con respecto a esas capacidades. Si sumamos 1 a la capacidad de cada arista, el corte A-B sigue siendo mínimo con respecto a las nuevas capacidades.”*

**Qué está evaluando**  
Comprensión de la definición matemática de la capacidad de un corte: C(A, B) = ∑_{e ∈ δ⁺(A)} c_e. Si un corte tiene más aristas cruzando de A a B que otro corte competidor, sumarle 1 a cada arista penalizará en mayor medida al corte con más aristas.

**Respuesta y Demostración**  
**La afirmación es FALSA.**

**Contraejemplo Formal Minimal**  
Consideremos la siguiente red con 4 vértices: V = {s, v, u, t}.
* Aristas y capacidades originales:
  * Arista (s, v) con capacidad c(s, v) = 10.
  * Arista (v, t) con capacidad c(v, t) = 10.
  * Aristas paralelas o por caminos alternativos:
    * Arista (s, u) con capacidad c(s, u) = 3.
    * Arista (u, t) con capacidad c(u, t) = 3.
* Para hacerlo aún más simple y canónico:
  Sea un grafo con fuente s, sumidero t y dos nodos intermedios a, b:
  * Corte 1 (Corte₁): Formado por una **única arista** de capacidad 10 (C₁ = 10).
  * Corte 2 (Corte₂): Formado por **tres aristas distintas** de capacidad 4 cada una (C₂ = 4 + 4 + 4 = 12).
  * Inicialmente: C₁ = 10 < C₂ = 12, por lo que Corte₁ es el **corte mínimo**.
* **Perturbación (+1 en cada arista):**
  * Nueva capacidad de la arista de Corte₁: 10 + 1 = 11. Como tiene 1 arista, la nueva capacidad del corte es: **C'₁ = 11**.
  * Nuevas capacidades de las aristas de Corte₂: cada una pasa de 4 a 5. Como Corte₂ tiene 3 aristas, su nueva capacidad de corte es: **C'₂ = (4 + 1) + (4 + 1) + (4 + 1) = 5 + 5 + 5 = 15**.
  * *Para que el corte mínimo cambie, invertimos la desigualdad original:*  
    Supongamos que originalmente:
    * Corte_A tiene **5 aristas** de capacidad 2 cada una: **C(A) = 2 + 2 + 2 + 2 + 2 = 10**.
    * Corte_B tiene **1 sola arista** de capacidad 11: **C(B) = 11**.
    * Como 10 < 11, el corte mínimo original es Corte_A.
  * **Ahora sumamos 1 a cada arista:**
    * Para Corte_A, al tener 5 aristas, cada una aumenta en 1: **C'(A) = (2 + 1) · 5 = 3 · 5 = 15**.
    * Para Corte_B, al tener 1 arista, aumenta en 1: **C'(B) = 11 + 1 = 12**.
  * **Conclusión:** Bajo las nuevas capacidades, C'(B) = 12 < 15 = C'(A). El corte mínimo pasa a ser Corte_B, dejando de serlo Corte_A. **Queda refutada la afirmación.**

---

### Patrón de Ejercicio 6.4: Actualización Dinámica de Flujo Máximo

Se dispone del flujo máximo ya calculado y se incrementa la capacidad de una única arista en 1 unidad. Se pide recalcular el nuevo flujo máximo en tiempo lineal O(V + E).

---

### Ejercicio 27 — Actualización de Flujo Máximo ante Aumento de Capacidad Unitaria en O(V + E)

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Guía de Ejercicios 06, Ejercicio 5

**Enunciado**  
Dado el flujo máximo de una red y su red residual asociada, implementar un algoritmo que, si se le aumenta en una unidad la capacidad a una arista (u, v) (de c pasa a c + 1), permita obtener el nuevo flujo máximo en tiempo O(V + E).

**Idea de resolución**  
* Al aumentar la capacidad de (u, v) en 1, en la red residual G_f la capacidad residual de (u, v) aumenta exactamente en 1 unidad.
* Por el Teorema de Flujo Máximo, el flujo máximo de la red o bien **se mantiene igual**, o bien **aumenta a lo sumo en 1 unidad**.
* Por lo tanto, alcanza con buscar **un único camino de aumento** desde s hasta t en la nueva red residual G_f' mediante una búsqueda en anchura (BFS) o profundidad (DFS):
  * Si existe un camino de aumento, aumentamos 1 unidad de flujo a lo largo de dicho camino en O(V). El nuevo flujo máximo es f* + 1.
  * Si no existe ningún camino de aumento, el flujo máximo original sigue siendo óptimo: el nuevo flujo máximo es f*.
* Un único BFS/DFS sobre la red toma O(V + E).

**Pseudocódigo**

```text
FUNCION ActualizarFlujoCapacidadMasUno(RedResidual, s, t, u, v, flujo_actual):
    // 1. Aumentar en 1 la capacidad residual de la arista modificada
    RedResidual[u][v] <- RedResidual[u][v] + 1

    // 2. Buscar si existe un camino de aumento desde s hasta t en O(V + E)
    camino <- BFS_CaminoAumento(RedResidual, s, t)

    SI camino != NULO:
        // Aumentar 1 unidad a lo largo del camino
        PARA CADA arista (x, y) EN camino:
            flujo_actual[x][y] <- flujo_actual[x][y] + 1
            RedResidual[x][y] <- RedResidual[x][y] - 1
            RedResidual[y][x] <- RedResidual[y][x] + 1
        RETORNAR (flujo_actual + 1, "Flujo aumentado en 1")
    SINO:
        RETORNAR (flujo_actual, "El flujo maximo no cambio")
```

**Complejidad**  
* **Tiempo:** O(V + E) por una única ejecución de BFS.
* **Espacio:** O(V) para la cola y vector de visitados del BFS.

---

### Errores Frecuentes en Exámenes sobre Redes de Flujo

1. **Olvidar las aristas hacia atrás en la red residual:** No permitir deshacer flujo imposibilita que Ford-Fulkerson corrija decisiones subóptimas tempranas.
2. **Confundir la capacidad de un corte:** Sumar aristas que van de B hacia A en lugar de sumar únicamente las aristas que van de A hacia B.
3. **Afirmar que Ford-Fulkerson siempre es polinomial:** Ford-Fulkerson es pseudo-polinomial (O(E · |f*|)). El algoritmo que garantiza tiempo polinomial estricto independiente de los valores de capacidad es **Edmonds-Karp** (O(V · E²)).
"""
