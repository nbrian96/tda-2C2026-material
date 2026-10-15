"""Módulo 9: Ejercicios Integradores Multi-Paradigma."""

def get_content():
    return r"""## 11. Ejercicios Integradores Multi-Paradigma

En los parciales más exigentes, la cátedra suele plantear un mismo escenario del mundo real y exigir resolverlo o compararlo a través de múltiples paradigmas distintos (Greedy vs Programación Dinámica vs Programación Lineal vs Redes de Flujo). Esta sección entrena la capacidad de conectar y contrastar estos enfoques.

---

### Ejercicio 32 — El Dilema del Transporte en Etapas: Greedy vs Programación Dinámica vs Programación Lineal

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Integrador Parcial 2025-1-2 (Ejercicios 2, 3 y 5 combinados)

**Enunciado Integrador**  
El INVAP debe transportar una carga de alta seguridad desde Ezeiza hasta Bariloche a través de un grafo de etapas donde las ciudades intermedias están agrupadas en días de viaje (máximo 400 km/día, sin viajar de noche). Para cada tramo dirigido (u, v) entre paradas consecutivas se conoce el costo de seguro C_uv > 0.  
1. **Paradigma Greedy:** Formular un algoritmo voraz. Demostrar formalmente mediante un contraejemplo por qué **no garantiza** la solución óptima.  
2. **Paradigma Programación Dinámica:** Desarrollar la solución óptima definiendo el estado OPT(v), la ecuación de recurrencia, el algoritmo en pseudocódigo y la complejidad temporal.  
3. **Paradigma Programación Lineal:** Formular un modelo de PL que encuentre la ruta de mínimo costo indicando variables, función objetivo, restricciones y recuento exacto de las mismas.

---

#### 1. Resolución por Algoritmo Greedy y Contraejemplo de No-Optimalidad
* **Regla Voraz:** Desde la ciudad actual u, avanzar hacia la ciudad siguiente v que tenga el menor costo de seguro inmediato C_uv.
* **Contraejemplo Minimal:**
  * Origen E (Ezeiza). Opciones etapa 1: Ciudad A (costo 10), Ciudad B (costo 20).
  * Desde A al destino Bariloche: costo 100.
  * Desde B al destino Bariloche: costo 5.
  * *Resultado Greedy:* Elige E → A (costo 10), luego A → Bariloche (costo 100). Costo Total = 110.
  * *Ruta Óptima:* E → B → Bariloche. Costo Total = 20 + 5 = 25.
  * Como 110 > 25, **Greedy falla**.

---

#### 2. Resolución Óptima por Programación Dinámica
* Como el grafo es por etapas (viajes de día sin ciclos), es un **DAG (Grafo Dirigido Acíclico)**.
* **Definición del Estado:**  
  OPT(v): Mínimo costo de seguro acumulado para llegar desde Ezeiza hasta la ciudad v.
* **Casos Base:**  
  OPT(Ezeiza) = 0.  
  OPT(v) = ∞ para todo v ≠ Ezeiza.
* **Ecuación de Recurrencia:**  
  Para cualquier ciudad v ∈ V:
  > **OPT(v) = min_{u ∈ Predecesores(v)} { OPT(u) + C_uv }**
* **Orden de Llenado:** Orden topológico de los vértices (etapa por etapa, de día 1 a día final).

**Pseudocódigo de Programación Dinámica**

```text
FUNCION InvapCaminoOptimoPD(grafo_etapas, ezeiza, bariloche):
    INICIALIZAR DP como diccionario con INFINITO para todo nodo
    INICIALIZAR predecesor como diccionario con NULO para todo nodo
    DP[ezeiza] <- 0

    // Procesamos los nodos etapa por etapa (orden topológico)
    PARA CADA etapa k <- 1 HASTA TotalEtapas:
        PARA CADA v EN NodosDeEtapa(k):
            PARA CADA (u, costo) EN AristasHacia(grafo_etapas, v):
                SI DP[u] + costo < DP[v]:
                    DP[v] <- DP[u] + costo
                    predecesor[v] <- u

    // Reconstrucción del camino óptimo
    INICIALIZAR ruta como lista vacía
    actual <- bariloche
    MIENTRAS actual != NULO:
        INSERTAR actual AL INICIO DE ruta
        actual <- predecesor[actual]

    RETORNAR (DP[bariloche], ruta)
```

* **Complejidad:** Cada arista se recorre una sola vez al procesar su nodo destino. Tiempo: O(V + E). Espacio: O(V).

---

#### 3. Resolución por Programación Lineal
* **Variables:** x_uv ∈ {0, 1} para cada arista dirigida (u, v) ∈ E (1 si se viaja por ese tramo, 0 si no).
* **Función Objetivo:**
  > **MINIMIZAR Z = ∑_{(u, v) ∈ E} C_uv · x_uv**
* **Restricciones de Conservación de Flujo Unitario:**  
  > **∑_{w: (v, w) ∈ E} x_vw - ∑_{u: (u, v) ∈ E} x_uv = 1** (si v = Ezeiza)  
  > **∑_{w: (v, w) ∈ E} x_vw - ∑_{u: (u, v) ∈ E} x_uv = -1** (si v = Bariloche)  
  > **∑_{w: (v, w) ∈ E} x_vw - ∑_{u: (u, v) ∈ E} x_uv = 0** (∀ v ∈ V \ {Ezeiza, Bariloche})
* **Conteo:** |E| variables binarias y |V| restricciones lineales.

---

### Ejercicio 33 — Asignación de Recursos con Restricción de Capacidad: Redes de Flujo vs PLI

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Integrador Sistemas de Distribución / Asignación

**Enunciado Integrador**  
Una empresa dispone de N servidores y M tareas. Cada tarea j requiere una cantidad de memoria R_j, y cada servidor i tiene una capacidad máxima C_i. Se sabe qué tareas pueden ejecutarse en qué servidores.  
1. Si todas las tareas tienen requerimiento unitario (R_j = 1), ¿qué paradigma conviene usar para maximizar tareas asignadas? Modelarlo.  
2. Si las tareas tienen requerimientos heterogéneos (R_j arbitrarios), ¿por qué Redes de Flujo estándar ya no puede modelar el problema directamente y se debe recurrir a Programación Lineal Entera?

**Resolución y Comparativa de Paradigmas**

#### 1. Caso Unitario (R_j = 1): Redes de Flujo
* Al ser las tareas de tamaño 1, el problema se modela directamente con **Redes de Flujo**:
  * Super-fuente s → Tareas con capacidad 1.
  * Tarea j → Servidor i con capacidad 1 (si es compatible).
  * Servidor i → Super-sumidero t con capacidad C_i.
* Se resuelve en tiempo polinomial estricto con Edmonds-Karp en O(V · E²). El Teorema de Integralidad asegura que las tareas se asignan enteras sin fraccionamiento.

#### 2. Caso Heterogéneo (R_j arbitrarios): Imposibilidad de Flujo y Formulación en PLI
* **Por qué falla Redes de Flujo:** En una red de flujo estándar, si mandamos R_j unidades de flujo a través de una arista, el algoritmo podría **partir el flujo** entre dos servidores distintos (ej: enviar 3 unidades a un servidor y 2 a otro para completar una tarea de 5). El flujo continuo no puede imponer la condición de indivisibilidad de un paquete que debe ir completo a un único destino.
* **Modelo en Programación Lineal Entera (PLI):**
  * Variables: x_ji ∈ {0, 1} (1 si la tarea j se asigna íntegramente al servidor i, 0 si no).
  * Maximizar ∑_j ∑_i x_ji
  * Sujeto a:
    * ∑_i x_ji ≤ 1 para cada tarea j (a lo sumo un servidor por tarea).
    * ∑_j R_j · x_ji ≤ C_i para cada servidor i (capacidad del servidor no superada).
    * x_ji = 0 si la tarea j no es compatible con el servidor i.

---

### Ejercicio 34 — Cobertura de Nodos en Redes: Vertex Cover por Backtracking, PLI y Aproximación 2

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Integrador Problemas NP-Hard (Vertex Cover)

**Enunciado Integrador**  
Para el problema de Vertex Cover Mínimo en un grafo G = (V, E), comparar tres estrategias de abordaje:  
1. **Solución Exacta Combinatoria:** Backtracking con Branch and Bound.  
2. **Solución Exacta Matemática:** Formulación en Programación Lineal Entera.  
3. **Solución Heurística Polinomial:** Algoritmo de Aproximación con factor 2 (basado en Maximal Matching).

**Comparativa Técnica Exhaustiva**

| Dimensión | 1. Backtracking con B&B | 2. Programación Lineal Entera (PLI) | 3. Algoritmo Aproximado (2-Aprox) |
| :--- | :--- | :--- | :--- |
| **Garantía de Solución** | Óptima exacta | Óptima exacta | Aproximada: \|C\| ≤ 2 · OPT |
| **Complejidad Temporal** | O(2ᵏ · \|E\|) (peor caso exponencial) | Exponencial en el peor caso (Branch & Cut) | **O(\|E\|)** (lineal en aristas) |
| **Escalabilidad** | Eficiente solo para k pequeño (k ≤ 40) | Eficiente para grafos medianos (\|V\| ≤ 500) | **Escala a millones de nodos y aristas** |
| **Formulación Central** | Ramificación en aristas no cubiertas: u ∈ C o v ∈ C con podas de tamaño. | min ∑ x_v sujeto a x_u + x_v ≥ 1, ∀ (u, v) ∈ E, con x_v ∈ {0, 1}. | Iterar sobre aristas: tomar ambos extremos de aristas disjuntas hasta cubrir el grafo. |

**Pseudocódigo del Algoritmo 2-Aproximado para Vertex Cover**

```text
FUNCION VertexCoverAproximado2(G):
    INICIALIZAR C como conjunto vacío
    INICIALIZAR aristas_disjuntas como conjunto vacío

    // Recorremos todas las aristas
    PARA CADA (u, v) EN E(G):
        // Si la arista no está cubierta por los nodos ya elegidos
        SI u NO PERTENECE A C Y v NO PERTENECE A C:
            AGREGAR u A C
            AGREGAR v A C
            AGREGAR (u, v) A aristas_disjuntas

    RETORNAR C
```

**Demostración de la Garantía de Aproximación 2:**  
1. Sea M el conjunto de aristas disjuntas seleccionadas por el algoritmo. Como ninguna arista en M comparte extremos, **cualquier Vertex Cover óptimo debe contener al menos un vértice distinto por cada arista en M**.
2. Por lo tanto: OPT ≥ |M|.
3. El algoritmo incorpora exactamente ambos extremos de cada arista en M, por lo que: |C| = 2 · |M|.
4. Combinando ambas relaciones:
   > **|C| = 2 · |M| ≤ 2 · OPT**
5. El algoritmo garantiza una cobertura que nunca supera el doble del óptimo y corre en tiempo O(|V| + |E|).
"""
