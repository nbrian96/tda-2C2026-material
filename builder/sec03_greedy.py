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
   * **Greedy Stays Ahead ("El voraz se mantiene adelante"):** Se define una métrica de progreso m(i). Se demuestra por inducción que en cada paso k, la solución voraz aventaja o iguala a cualquier solución óptima OPT (m(G_k) ≤ m(OPT_k) o m(G_k) ≥ m(OPT_k)), garantizando que al finalizar no puede ser superada.
   * **Argumento de Intercambio (Exchange Argument):** Se toma una solución óptima hipotética OPT que difiere de la solución greedy G. Se identifica la primera inversión o discrepancia y se demuestra que al intercambiar el elemento de OPT por el elemento elegido por G, la calidad de la solución no empeora. Repitiendo el proceso, OPT se transforma en G sin perder valor, probando que G también es óptima.
4. **Cómo Probar que una Idea Greedy es Incorrecta (El Contraejemplo):**
   Si en un examen te preguntan *"¿El algoritmo greedy propuesto es óptimo siempre? Indicar si es óptimo o dar un contraejemplo"*, **NUNCA** respondas con explicaciones vagas. Debes presentar un contraejemplo concreto:
   1. Definir una instancia pequeña con datos numéricos explícitos.
   2. Mostrar paso a paso qué elige el algoritmo greedy y cuál es su costo/beneficio obtenido.
   3. Mostrar una solución alternativa factible y su costo/beneficio estrictamente superior.
   4. Concluir formalmente: *Como Valor(Alternativa) > Valor(Greedy), el algoritmo no garantiza la solución óptima.*

---

### Patrón de Ejercicio 2.1: Interval Scheduling (Planificación de Intervalos No Solapados)

Aparece con diferentes metáforas narrativas: charlas en un aula, pedidos de mafias locales para controlar kilómetros de una ruta, franjas horarias de satélites o turnos de guardias. El objetivo es maximizar la cantidad de pedidos aceptados sin solapamiento.

---

### Ejercicio 4 — Concesión de Permisos a Mafias en la Ruta Costera (Arnook)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-2 (26 de noviembre de 2024), Ejercicio 3 / Guía 02 Ejercicio 12

**Enunciado**  
Trabajamos para el mafioso Arnook, quien organiza los pedidos de pequeñas mafias locales por el control de diferentes kilómetros de la ruta costera de Ciudad República. Cada mafia le pide control sobre un rango de kilómetros [s_i, f_i] (por ejemplo, del kilómetro 1 al 5, del 3 al 8, etc.). Si una mafia toma control de un kilómetro, ninguna otra puede ocupar ese mismo tramo (no pueden solaparse). Arnook cobra una tarifa fija por otorgar el permiso, independientemente de los kilómetros pedidos, por lo que su objetivo es maximizar la cantidad total de permisos otorgados sin conflictos de territorio.  
1. Implementar un algoritmo Greedy que determine a qué mafias otorgar el permiso.  
2. Indicar y justificar la complejidad temporal y espacial.  
3. Justificar por qué el algoritmo planteado es Greedy.  
4. ¿El algoritmo da la solución óptima siempre? Demostrarlo formalmente.

**Qué está evaluando**  
Comprensión del arquetipo de *Interval Scheduling*, diseño del criterio voraz correcto (ordenamiento por punto final más temprano), y la demostración formal de optimalidad vía *Greedy Stays Ahead*.

**Idea de resolución**  
* ¿Por qué descartar otros criterios?
  * *Ordenar por inicio más temprano (s_i):* Falla si un pedido empieza muy temprano y ocupa toda la ruta ([1, 100] vs [2, 3] y [4, 5]).
  * *Ordenar por menor longitud (f_i - s_i):* Falla si un pedido corto bloquea a dos pedidos compatibles a sus costados ([10, 20], [19, 21], [20, 30]).
* *Criterio óptimo:* Ordenar las solicitudes por su **kilómetro de finalización más temprano (f_i)**. Esto deja libre la mayor cantidad de ruta posible hacia adelante para futuras mafias.
* Seleccionamos el primer pedido que termine más temprano. Luego, iteramos seleccionando el próximo pedido cuyo inicio s_j sea mayor o igual al fin del último pedido aceptado (s_j ≥ f_ultimo).

**Pseudocódigo**

```text
FUNCION ConcederPermisosMafias(pedidos):
    SI longitud(pedidos) = 0:
        RETORNAR lista vacía

    // 1. Ordenar por fin ascendente: pedidos[i].fin
    ORDENAR pedidos POR fin ASCENDENTE

    INICIALIZAR seleccionados como lista vacía
    INSERTAR pedidos[0] EN seleccionados
    ultimo_fin <- pedidos[0].fin

    // 2. Selección voraz de intervalos compatibles
    PARA i <- 1 HASTA longitud(pedidos) - 1:
        SI pedidos[i].inicio >= ultimo_fin:
            INSERTAR pedidos[i] EN seleccionados
            ultimo_fin <- pedidos[i].fin

    RETORNAR seleccionados
```

**Explicación del algoritmo**  
El algoritmo clasifica las solicitudes de menor a mayor según el kilómetro en el que terminan. Al aceptar siempre la que termina antes y es compatible con las ya otorgadas, se minimiza el territorio retenido en cada decisión.

**Complejidad**  
* **Tiempo:** Ordenar n solicitudes requiere O(n log n) mediante Mergesort o Heapsort. El recorrido lineal posterior realiza una comparación O(1) por elemento en O(n). Por lo tanto, la complejidad temporal total es:
  > **O(n log n)**
* **Espacio:** O(n) para almacenar los pedidos seleccionados (o memoria auxiliar de ordenamiento).

**Justificación de por qué es Greedy**  
Es un algoritmo voraz porque:
1. En cada paso toma una decisión basada en una regla miope de optimización local (elegir el intervalo compatible que termine antes).
2. La decisión es **irrevocable**: una vez que un permiso es otorgado, nunca se retira ni se reconsidera a la luz de los pedidos futuros.

**Demostración de Optimalidad (Greedy Stays Ahead)**  
* Sean G = {g_1, g_2, ..., g_k} los intervalos seleccionados por el algoritmo voraz ordenados por fin, y OPT = {o_1, o_2, ..., o_m} los intervalos de una solución óptima arbitraria también ordenados por fin, con m ≥ k.
* **Proposición inductiva:** Para todo r ≤ k, el tiempo de fin del r-ésimo elemento voraz es menor o igual al del r-ésimo elemento óptimo:
  > **f(g_r) ≤ f(o_r)**
* **Caso Base (r = 1):** El algoritmo voraz elige el intervalo con el menor tiempo de fin absoluto en todo el conjunto. Por lo tanto, f(g_1) ≤ f(o_1).
* **Paso Inductivo:** Asumimos f(g_{r-1}) ≤ f(o_{r-1}). Como o_r es compatible con o_{r-1}, sabemos que s(o_r) ≥ f(o_{r-1}). Por hipótesis inductiva:
  > s(o_r) ≥ f(o_{r-1}) ≥ f(g_{r-1})
  
  Esto prueba que o_r era una opción válida y compatible para el algoritmo voraz al buscar su r-ésimo elemento. Dado que el algoritmo voraz selecciona el que tiene el menor tiempo de fin entre todos los compatibles disponibles, necesariamente:
  > f(g_r) ≤ f(o_r)
* **Conclusión:** Si la solución óptima tuviera más elementos que el voraz (m > k), existiría un elemento o_{k+1} en OPT. Por la propiedad anterior, s(o_{k+1}) ≥ f(o_k) ≥ f(g_k), lo cual significa que o_{k+1} era compatible con g_k. Pero el algoritmo voraz terminó en g_k porque ya no quedaba ningún intervalo compatible. Contradicción. Por lo tanto, k = m y la solución voraz es **óptima**.

**Puntos donde puedo equivocarme**  
* Permitir solapamiento estricto si dos intervalos comparten un borde (chequear si el enunciado dice s_j ≥ f_i o s_j > f_i).
* Ordenar por tiempo de inicio o por duración, los cuales no son óptimos.

**Variación típica de parcial**  
* *Interval Scheduling Ponderado:* Cada intervalo tiene un valor o peso v_i. En este caso, **Greedy NO funciona** y se debe resolver con Programación Dinámica (ver Ejercicio 18).
* *Interval Partitioning:* Se pide determinar la cantidad mínima de salas/recursos necesarios para programar todas las charlas sin solapamiento (se resuelve ordenando por inicio y usando una cola de prioridad).

---

### Patrón de Ejercicio 2.2: Mochila Fraccionaria vs 0-1 con Garantía de Calidad 1/2

En las evaluaciones teóricas y en los TPs de la cátedra se examina la relación entre la solución fraccionaria (óptima con greedy) y la versión entera 0-1, demostrando cómo una regla greedy corregida otorga una cota de aproximación constante.

---

### Ejercicio 5 — Mochila 0-1 con Garantía de Aproximación 1/2

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Guía de Ejercicios 02, Ejercicio 8 / Diapositivas Explicativas de Cátedra

**Enunciado**  
Se tiene una mochila de capacidad de peso W y n objetos indivisibles (0-1), donde cada objeto i tiene peso w_i y valor v_i.  
1. Explicar por qué la regla voraz estándar basada en ordenar por densidad de valor (v_i / w_i) puede fallar de forma arbitraria en la mochila 0-1.  
2. Diseñar un algoritmo greedy modificado que garantice una calidad de al menos 1/2 respecto a la solución óptima global.  
3. Demostrar formalmente que Sol / OPT > 1/2.  
4. Indicar la complejidad temporal del algoritmo.

**Qué está evaluando**  
Capacidad de analizar por qué un algoritmo voraz falla, cómo corregirlo mediante la detección del *elemento crítico*, y el cálculo de factores de aproximación comparando contra la relajación continua.

**Idea de resolución**  
1. Descartamos elementos que individualmente pesen más que W.
2. Ordenamos por ratio r_i = v_i / w_i descendente.
3. Llenamos vorazmente. El primer objeto que no entra lo denominamos **Elemento Crítico (c)** con peso w_c y valor v_c.
4. La solución voraz acumulada tiene valor P_1.
5. Comparamos P_1 contra el elemento crítico en solitario v_c. Devolvemos max(P_1, v_c).

**Pseudocódigo**

```text
FUNCION MochilaGreedyConGarantia(objetos, W):
    INICIALIZAR candidatos como lista vacía

    // 1. Filtrar objetos que no entran por sí solos
    PARA CADA obj EN objetos:
        SI obj.peso <= W:
            INSERTAR obj EN candidatos

    SI longitud(candidatos) = 0:
        RETORNAR (0, lista vacía)

    // 2. Ordenar por densidad valor/peso descendente
    ORDENAR candidatos POR (valor / peso) DESCENDENTE

    INICIALIZAR solucion_greedy como lista vacía
    peso_acumulado <- 0
    valor_acumulado <- 0
    elemento_critico <- NULO

    // 3. Llenado voraz e identificación del elemento crítico
    PARA CADA obj EN candidatos:
        SI peso_acumulado + obj.peso <= W:
            INSERTAR obj EN solucion_greedy
            peso_acumulado <- peso_acumulado + obj.peso
            valor_acumulado <- valor_acumulado + obj.valor
        SINO:
            SI elemento_critico = NULO:
                elemento_critico <- obj

    // 4. Aplicación de la cota 1/2
    SI elemento_critico != NULO Y elemento_critico.valor > valor_acumulado:
        INICIALIZAR sol_critica como lista con elemento_critico
        RETORNAR (elemento_critico.valor, sol_critica)

    RETORNAR (valor_acumulado, solucion_greedy)
```

**Explicación del algoritmo**  
La debilidad de la densidad v_i / w_i es que puede tomar objetos muy densos pero diminutos, dejando capacidad insuficiente para un objeto pesado que vale mucho más. Al comparar la solución greedy acumulada contra el valor del primer objeto rechazado (v_c), nos cubrimos de ese peor caso.

**Demostración Formal de la Cota 1/2**  
1. Sea OPT el valor de la solución óptima del problema entero 0-1.
2. Sea OPT_frac el valor de la solución óptima fraccionaria. Es inmediato que OPT ≤ OPT_frac.
3. La solución fraccionaria óptima toma exactamente los elementos de la solución greedy entera (P_1) más una fracción α ∈ [0, 1) del elemento crítico c:
   > OPT_frac = P_1 + α · v_c < P_1 + v_c
4. Por transitividad: OPT < P_1 + v_c.
5. Nuestro algoritmo devuelve Sol = max(P_1, v_c). Por propiedad del promedio aritmético:
   > max(P_1, v_c) ≥ (P_1 + v_c) / 2
6. Sustituyendo la cota de OPT:
   > Sol ≥ (P_1 + v_c) / 2 > OPT / 2  ⟹  Sol / OPT > 1/2

**Complejidad**  
* **Tiempo:** Filtrado en O(n), ordenamiento de n elementos en O(n log n), recorrido voraz en O(n). Total: O(n log n).
* **Espacio adicional:** O(n) para almacenar la lista de candidatos y la solución seleccionada.

**Puntos donde puedo equivocarme**  
* No descartar previamente los elementos con w_i > W. Si el elemento crítico pesa más que W, no puede incluirse en solitario.

**Variación típica de parcial**  
Preguntar por qué la mochila fraccionaria sí es óptima con greedy y la 0-1 requiere Programación Dinámica (subestructura óptima con superposición vs subproblemas fraccionarios independientes).

---

### Patrón de Ejercicio 2.3: Minimización de Latencia y Deadlines (EDF)

Se tienen tareas con tiempos de procesamiento y fechas límite de entrega (deadlines). El objetivo es ordenar las tareas para minimizar la latencia máxima que experimenta cualquier tarea.

---

### Ejercicio 6 — Minimización de Latencia Máxima (Earliest Deadline First)

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Guía de Ejercicios 02, Ejercicio 9 / Práctica

**Enunciado**  
Se tienen n tareas que deben procesarse secuencialmente en una única máquina. Cada tarea i tiene una duración t_i y una fecha límite de entrega d_i. Si una tarea comienza en el tiempo s_i, finaliza en f_i = s_i + t_i. La latencia de la tarea i se define como L_i = max(0, f_i - d_i). Diseñar un algoritmo greedy que programe las tareas minimizando la latencia máxima L_max = max_i L_i. Demostrar su optimalidad.

**Qué está evaluando**  
Técnica de ordenamiento por fecha de vencimiento más temprana (*Earliest Deadline First*) y demostración por argumento de intercambio de inversiones adyacentes.

**Idea de resolución**  
* ¿Por qué otros criterios fallan?
  * *Menor duración primero (t_i):* Ignora fechas límites urgentes.
  * *Menor holgura (d_i - t_i):* Falla si una tarea corta tiene menor holgura pero fecha límite lejana y bloquea una urgente.
* *Criterio óptimo (EDF):* Ordenar las tareas en orden creciente de sus fechas límites: d_1 ≤ d_2 ≤ ... ≤ d_n.
* No dejar tiempo ocioso en la máquina entre tareas consecutivas.

**Pseudocódigo**

```text
FUNCION MinimizarLatenciaMaxima(tareas):
    // Cada tarea tiene id, duracion, deadline
    ORDENAR tareas POR deadline ASCENDENTE

    tiempo_actual <- 0
    latencia_maxima <- 0
    INICIALIZAR programacion como lista vacía

    PARA CADA tarea EN tareas:
        inicio <- tiempo_actual
        fin <- tiempo_actual + tarea.duracion
        latencia <- maximo(0, fin - tarea.deadline)

        SI latencia > latencia_maxima:
            latencia_maxima <- latencia

        INSERTAR (tarea.id, inicio, fin, latencia) EN programacion
        tiempo_actual <- fin

    RETORNAR (latencia_maxima, programacion)
```

**Explicación del algoritmo**  
Al atender siempre la tarea cuyo vencimiento está más próximo, se previene que las fechas límites inminentes acumulen retrasos catastróficos causados por tareas menos urgentes.

**Demostración de Optimalidad (Argumento de Intercambio)**  
1. Decimos que una programación tiene una **inversión** si existe un par de tareas adyacentes i seguida inmediatamente por j tal que d_i > d_j (la tarea i vence más tarde que j, pero se ejecuta antes).
2. La solución greedy por definición no tiene inversiones.
3. Sea OPT una solución óptima sin tiempo ocioso con la menor cantidad de inversiones. Si OPT tiene cero inversiones, coincide con la programación greedy.
4. Si OPT tiene al menos una inversión, deben existir dos tareas contiguas invertidas i y j con d_i > d_j.
5. Al intercambiar i y j en el cronograma:
   * Las tareas distintas de i y j no modifican sus tiempos de inicio ni fin, por lo que sus latencias no cambian.
   * La tarea j se adelanta, por lo que su latencia estrictamente no aumenta.
   * La nueva latencia de i finaliza en el mismo tiempo que antes finalizaba j. Como d_i > d_j, su latencia nueva es menor que la latencia previa que tenía j.
6. Por lo tanto, la latencia máxima tras el intercambio no aumentó. Esto reduce la cantidad de inversiones sin empeorar la solución óptima. Repitiendo el proceso se llega a la solución greedy, probando que es **óptima**.

**Complejidad**  
* **Tiempo:** O(n log n) por el ordenamiento inicial y O(n) en el barrido temporal. Total: O(n log n).
* **Espacio adicional:** O(n) para almacenar el cronograma resultante.

**Puntos donde puedo equivocarme**  
* Dejar huecos ociosos entre tareas. Una programación con tiempo ocioso siempre puede comprimirse hacia la izquierda sin aumentar la latencia.

**Variación típica de parcial**  
Considerar que las tareas tienen tiempos de arribo r_i diferentes. En este caso el problema se vuelve NP-Duro y EDF simple no garantiza el óptimo.

---

### Patrón de Ejercicio 2.4: Heurísticas Voraces de Cobertura (Set Cover Greedy)

Aparece cuando el problema exacto es NP-Hard (como Set Cover o Dominating Set) y el enunciado solicita explícitamente: *"El personal no conoce programación lineal, diseñar un algoritmo greedy..."*.

---

### Ejercicio 7 — Ubicación Voraz de Antenas Celulares con Costo por Vecindario

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-3 (10 de diciembre de 2024), Ejercicio 4

**Enunciado**  
Una empresa de telefonía celular desea colocar antenas en una grilla de celdas para brindar cobertura a un conjunto de vecindarios distribuidos en la zona. Cada antena colocada en una celda (i, j) da cobertura a esa celda y a las 8 que la rodean (un bloque de 3 × 3). El costo de instalar una antena en la celda (i, j) es de CTO_ij pesos. Se desea cubrir todos los vecindarios (o un porcentaje requerido) minimizando el costo total. Diseñar un algoritmo Greedy que determine en qué celdas colocar antenas. Justificar la regla de elección voraz y la complejidad del algoritmo.

**Qué está evaluando**  
Modelado del problema de *Weighted Set Cover* mediante una heurística voraz de costo/beneficio marginal.

**Idea de resolución**  
* En cada paso, evaluamos todas las celdas candidatas donde aún no hay antena.
* Para cada celda candidata (i, j), calculamos cuántos **nuevos vecindarios no cubiertos previamente** aportaría instalar una antena allí: NuevosCobertura(i, j).
* Definimos el ratio de costo por beneficio marginal:
  > **Ratio(i, j) = CTO_ij / NuevosCobertura(i, j)**
* Elegimos vorazmente la celda que tenga el **menor ratio de costo por vecindario nuevo cubierto**.
* Marcamos los vecindarios como cubiertos y repetimos hasta que todos los vecindarios estén cubiertos.

**Pseudocódigo**

```text
FUNCION ColocarAntenasGreedy(grilla, vecindarios, CTO):
    INICIALIZAR no_cubiertos como conjunto con todos los vecindarios
    INICIALIZAR antenas_elegidas como lista vacía

    MIENTRAS longitud(no_cubiertos) > 0:
        mejor_celda <- NULO
        mejor_ratio <- INFINITO

        // Evaluar todas las celdas posibles de la grilla
        PARA CADA celda (i, j) EN grilla:
            vecinos_nuevos <- 0
            PARA CADA v EN Cobertura(i, j):
                SI v PERTENECE A no_cubiertos:
                    vecinos_nuevos <- vecinos_nuevos + 1

            // Solo consideramos celdas que aportan cobertura nueva
            SI vecinos_nuevos > 0:
                ratio <- CTO[i][j] / vecinos_nuevos
                SI ratio < mejor_ratio:
                    mejor_ratio <- ratio
                    mejor_celda <- (i, j)

        // Si no encontramos celda que cubra los restantes, es infactible
        SI mejor_celda = NULO:
            ROMPER // No se pueden cubrir todos los vecindarios restantes

        INSERTAR mejor_celda EN antenas_elegidas
        // Actualizar vecindarios cubiertos
        PARA CADA v EN Cobertura(mejor_celda):
            ELIMINAR v DE no_cubiertos

    RETORNAR antenas_elegidas
```

**Explicación del algoritmo**  
El algoritmo aplica la regla clásica de Chvátal para Set Cover. En cada iteración maximiza la eficiencia económica por cada elemento nuevo incorporado al universo cubierto.

**Complejidad**  
* Si la grilla tiene M celdas y hay V vecindarios, en el peor caso se seleccionan hasta V antenas. En cada paso se evalúan las M celdas inspeccionando las 9 celdas cubiertas (O(1)).
* Tiempo total: O(V · M).
* Espacio adicional: O(V) para mantener el conjunto de vecindarios no cubiertos.

**Puntos donde puedo equivocarme**  
* Elegir la celda con menor costo absoluto CTO_ij (podría no cubrir ningún vecindario o muy pocos).
* Elegir la celda que cubre más vecindarios sin considerar el costo (podría ser extremadamente cara).
* El cociente debe ser siempre costo / nuevos vecindarios, no sobre el total histórico de celdas que abarca.

**Variación típica de parcial**  
Preguntar si este algoritmo garantiza la solución óptima. **Respuesta:** No, porque Set Cover es NP-Duro. Este algoritmo voraz es una aproximación con factor de garantía ln |V| + 1.

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
2. Indicar si la solución obtenida será óptima o no. Fundamentar con un contraejemplo riguroso.

**Qué está evaluando**  
Construcción de heurísticas paso a paso y formulación de contraejemplos matemáticos claros para refutar la optimalidad de algoritmos voraces en grafos de decisión multietapa.

**Idea de resolución**  
* *Regla voraz:* Estando en la ciudad actual, elegir como siguiente parada aquella ciudad accesible en la etapa que tenga el **menor costo de seguro inmediato**.
* *Optimalidad:* **NO es óptimo**. Un tramo inicial barato puede forzar a tomar en la siguiente etapa rutas con costos astronómicos o sin salida barata.

**Pseudocódigo**

```text
FUNCION TrasladoInvapGreedy(origen, destino, grafo_etapas):
    ciudad_actual <- origen
    costo_total <- 0
    INICIALIZAR camino como lista con origen

    MIENTRAS ciudad_actual != destino:
        siguientes_opciones <- ObtenerVecinos(grafo_etapas, ciudad_actual)
        SI longitud(siguientes_opciones) = 0:
            RETORNAR ("Error: camino bloqueado", INFINITO)

        // Elección voraz: mínimo costo en el tramo inmediato
        mejor_siguiente <- NULO
        menor_costo_tramo <- INFINITO

        PARA CADA (ciudad_sig, costo_seguro) EN siguientes_opciones:
            SI costo_seguro < menor_costo_tramo:
                menor_costo_tramo <- costo_seguro
                mejor_siguiente <- ciudad_sig

        INSERTAR mejor_siguiente EN camino
        costo_total <- costo_total + menor_costo_tramo
        ciudad_actual <- mejor_siguiente

    RETORNAR (camino, costo_total)
```

**Contraejemplo Formal de No-Optimalidad**  
Consideremos el siguiente grafo de etapas desde el origen E (Ezeiza) hasta el destino B (Bariloche):
* Etapa 1 desde E:
  * Tramo E → V1 con costo de seguro de 10 pesos.
  * Tramo E → V2 con costo de seguro de 20 pesos.
* Etapa 2 hacia el destino B:
  * Desde V1 → B con costo de seguro de 100 pesos.
  * Desde V2 → B con costo de seguro de 5 pesos.

* **Ejecución del algoritmo Greedy:**
  * En E, compara las opciones inmediatas: 10 pesos (a V1) vs 20 pesos (a V2).
  * Elige vorazmente E → V1 por costar 10 pesos.
  * En V1, la única opción hacia el destino es V1 → B con costo de 100 pesos.
  * **Costo total obtenido por Greedy:** 10 + 100 = 110 pesos.
* **Solución alternativa factible:**
  * Ruta E → V2 → B.
  * Costo total: 20 + 5 = 25 pesos.
* **Conclusión:** Como 110 > 25, el algoritmo voraz no encuentra la solución óptima. Los problemas de caminos mínimos en grafos por etapas requieren **Programación Dinámica** (ver Ejercicio 32).

**Complejidad**  
* **Tiempo:** O(V + E) en el peor caso si recorre las aristas de las etapas.
* **Espacio:** O(V) para la lista de ciudades del camino.

---

### Errores Frecuentes en Exámenes sobre Greedy

1. **Afirmar que Greedy es óptimo sin demostrarlo:** Poner "es óptimo porque siempre elijo lo mejor" es causal de pérdida total de puntos. Se debe presentar *Greedy Stays Ahead* o *Argumento de Intercambio*.
2. **Dar un contraejemplo sin números:** Decir "podría pasar que después sea más caro" no es un contraejemplo. Un contraejemplo exige nodos, aristas y costos numéricos explícitos.
3. **No justificar por qué el algoritmo es voraz:** Se debe explicitar que la decisión es local, miope e irrevocable.
4. **Confundir Interval Scheduling con Interval Scheduling Ponderado:** Si las tareas tienen valores o beneficios distintos, ordenar por tiempo de fin no es óptimo.
"""
