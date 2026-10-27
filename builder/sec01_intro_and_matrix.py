"""Módulo 1: Introducción, Estrategia, Radiografía de Parciales y Guía Mental."""

def get_content():
    return r"""# Teoría de Algoritmos (FIUBA — TB024 / 75.29 / 95.06)
## Manual Práctico de Resolución de Parciales
### Edición Intensiva: "Salvando el Cuatrimestre"

---

## 1. Cómo usar esta guía

Este documento fue diseñado con un único objetivo en mente: **aprobar el parcial de Teoría de Algoritmos optimizando cada minuto de estudio**. No es un compendio enciclopédico de teoría ni una transcripción de diapositivas. Es un manual de ingeniería algorítmica para el examen, estructurado a partir del análisis riguroso de los parciales reales tomados por la cátedra (Curso Echevarría) en 2024 y 2025, cruzados con la guía práctica oficial.

### Planes de preparación según tu tiempo disponible

* **Plan de Emergencia (48 a 72 horas antes del examen):**
  1. Leé la **Sección 3: Guía mental para reconocer el ejercicio en 30 segundos**.
  2. Resolvé exclusivamente los **32 ejercicios** marcados como 🔴 **IMPRESCINDIBLE**.
  3. Memorizá el esquema de 4 pasos obligatorios para **Reducciones NP-Completas** (Sección 10).
  4. Revisá el **Catálogo de Errores Típicos** y la **Checklist antes de entrar al parcial**.
* **Plan Táctico (1 semana antes del examen):**
  1. Realizá el Plan de Emergencia completo.
  2. Sumá los **8 ejercicios** marcados como 🟡 **IMPORTANTE** y enfocá el repaso en tus ejercicios pendientes de dominar.
  3. Escribí en papel (sin mirar la solución) el pseudocódigo de cada ejercicio de Programación Dinámica, Backtracking y Greedy.
  4. Resolvé los **Ejercicios Integradores Multi-Paradigma** (Sección 11, destacando **La Mochila — Ej 35** y **El Viajante TSP — Ej 36** en todos los paradigmas) y los **Ejercicios Tipo Parcial Generados** (Sección 12).
* **Plan Integral (2 o más semanas):**
  1. Recorré los **40 ejercicios** de la guía completa (32 🔴 **IMPRESCINDIBLE** + 8 🟡 **IMPORTANTE**).
  2. Implementá en tu computadora los algoritmos más sensibles (o revisá las implementaciones en Python de la carpeta `Practicas/`).
  3. Dominá las demostraciones formales de optimalidad por *Greedy Stays Ahead*, argumento de intercambio y las recurrencias del Teorema Maestro.

### Reglas de oro para rendir el examen
1. **Cada ejercicio se entrega en hoja separada:** La cátedra exige entregar cada pregunta en una hoja individual. Planteá la solución de forma limpia, separando claramente: *Idea conceptual*, *Pseudocódigo*, *Justificación de optimalidad/reconstrucción*, y *Cálculo de complejidad temporal y espacial*.
2. **El pseudocódigo debe ser concreto:** No uses abstracciones vagas como `resolver_problema(grafo)`. Empleá estructuras de control estándar (`SI`, `PARA`, `MIENTRAS`, `RETORNAR`) y manipulá arreglos, matrices o listas explícitamente.
3. **No omitir casos borde:** Estructura vacía, un solo elemento, elementos repetidos, grafo disconexo o capacidades nulas restan puntos valiosos si no están cubiertos.
4. **La complejidad debe estar justificada:** Decir únicamente $O(n^2)$ sin explicar cuántas iteraciones hace cada bucle y qué costo tiene cada operación interna equivale a puntaje parcial.

---

## 2. Radiografía de los Parciales de TDA

Un examen típico de esta cátedra consta exactamente de **5 ejercicios prácticos** (20 puntos cada uno), distribuidos estratégicamente para evaluar si el alumno sabe elegir la herramienta adecuada para cada problema.

### Inventario de Parciales Reales Analizados

1. **Parcial 2024-2 — 1ª Oportunidad (5 de noviembre de 2024):**
   * *Ej 1 (Backtracking):* Teorema de los cuatro cuadrados de Lagrange ($n = w^2 + x^2 + y^2 + z^2$).
   * *Ej 2 (Greedy):* Alan Turing y descifrado de código de submarinos por sustitución de palabras de 4 letras.
   * *Ej 3 (Programación Dinámica):* Mochila 2D de Paolo Casanova (peso y volumen) con restricción excluyente y obligatoria de guías de aves.
   * *Ej 4 (Programación Lineal):* Salidas de observación de aves con presupuesto de tiempo y máxima cobertura de especies.
   * *Ej 5 (Reducciones NP):* Demostrar que Cambio de Monedas no es más difícil que Subset Sum ($\le_P$).
2. **Parcial 2024-2 — 2ª Oportunidad (26 de noviembre de 2024):**
   * *Ej 1 (Backtracking / Exacto):* Vertex Cover Mínimo en grafo no dirigido con podas.
   * *Ej 2 (Programación Dinámica):* Mínima cantidad de operaciones para llegar de $0$ a $K$ sumando $1$ o duplicando.
   * *Ej 3 (Greedy):* Mafioso Arnook en Ciudad República (*Interval Scheduling* en kilómetros de ruta costera).
   * *Ej 4 (Redes de Flujo):* Emparejamiento de médicos y pacientes con franjas horarias en hospital (*Matching Bipartito*).
   * *Ej 5 (Reducciones NP):* Demostrar que Dominating Set es NP-Completo reduciendo desde Vertex Cover.
3. **Parcial 2024-2 — 3ª Oportunidad / Recuperatorio (10 de diciembre de 2024):**
   * *Ej 1 (Redes de Flujo):* Análisis V/F con contraejemplo: "Si se suma $1$ a la capacidad de cada arista, ¿el corte mínimo sigue siendo mínimo?".
   * *Ej 2 (Programación Dinámica):* Justificación de texto (*Word Wrap / Knuth-Plass*) minimizando la suma de cuadrados de sobrantes.
   * *Ej 3 (Programación Lineal):* Ubicación de antenas de celular en grilla para cubrir al menos el $70\%$ de vecindarios con costo mínimo.
   * *Ej 4 (Greedy):* Antenas celulares con costos variables por celda mediante heurística voraz de cobertura.
   * *Ej 5 (Reducciones NP):* Dominating Set es NP-Completo (desde Vertex Cover).
4. **Parcial 2025-1 — 1ª Oportunidad (27 de mayo de 2025):**
   * *Ej 1 (Redes de Flujo):* Sistema energético argentino (9 regiones) con generación, demanda y capacidades de transporte vía Ford-Fulkerson.
   * *Ej 2 (Greedy):* Algoritmo voraz para el sistema energético y discusión de optimalidad.
   * *Ej 3 (Programación Lineal):* Modelo de Programación Lineal (Flujo de Costo Mínimo) para el sistema energético.
   * *Ej 4 (Programación Dinámica):* Problema del delivery (Mochila con peso, volumen y tope de seguro financiero).
   * *Ej 5 (Reducciones NP):* El dilema de Marco el cadete: Reducción de Ciclo Hamiltoniano a TSP de decisión.
5. **Parcial 2025-1 — 2ª Oportunidad (17 de junio de 2025):**
   * *Ej 1 (División y Conquista):* Multiplicación de matrices cuadradas $n \times n$ por bloques y Teorema Maestro.
   * *Ej 2 (Programación Dinámica):* Traslado de carga crítica INVAP (Ezeiza a Bariloche en etapas de $\le 400\text{ km/día}$ con seguro).
   * *Ej 3 (Greedy):* Algoritmo voraz para el traslado INVAP y contraejemplo de por qué no es óptimo.
   * *Ej 4 (Backtracking):* Problema de las 8 Reinas con estructuras de datos para chequeo en $O(1)$.
   * *Ej 5 (Programación Lineal):* Modelo de PL para el camino óptimo INVAP (o 8 Reinas) con recuento de variables y restricciones.

### Matriz de Frecuencia y Dificultad por Tema

| Tema / Paradigma | Frecuencia en Exámenes | Presencia Relativa | Dificultad Típica | Tipos de Pregunta Habituales |
| :--- | :---: | :---: | :---: | :--- |
| **Programación Dinámica (PD)** | 5 de 5 parciales | **100%** | Alta | Mochila multidimensional o con condiciones lógicas, secuencias/texto, mínimas operaciones, caminos en DAGs por etapas. |
| **Algoritmos Greedy (Voraces)** | 5 de 5 parciales | **100%** | Media-Alta | *Interval Scheduling*, heurísticas de cobertura con costos, comparación con soluciones óptimas y demostración de contraejemplos. |
| **Programación Lineal (PL / PLI)** | 4 de 5 parciales | **80%** | Media-Alta | Cobertura de conjuntos (*Set Cover*), Flujo de Costo Mínimo, caminos en grafos, linealización de funciones no lineales. Recuento de variables y restricciones. |
| **Reducciones Polinomiales / NP-C** | 4 de 5 parciales | **80%** | Muy Alta | Demostración formal de NP-Completitud (*Dominating Set*, *TSP*), reducciones numéricas ($\le_P$), verificadores polinomiales. |
| **Redes de Flujo (Flujo / Corte)** | 3 de 5 parciales | **60%** | Alta | *Matching Bipartito* (médicos/pacientes), transporte multipunto con super-fuente/sumidero, V/F teórico sobre cortes mínimos. |
| **Backtracking & Branch and Bound** | 3 de 5 parciales | **60%** | Media | 8 Reinas con estructuras $O(1)$, descomposición numérica (Lagrange), *Vertex Cover* exacto con podas por factibilidad y cota. |
| **División y Conquista (DyC)** | 1 de 5 parciales | **20%** | Media | Multiplicación de matrices por bloques, Teorema Maestro, búsquedas binarias adaptadas sobre arreglos unimodales/pico. |

---

## 3. Guía Mental: "Cómo Reconocer el Ejercicio en 30 Segundos"

Uno de los errores más costosos en un parcial es intentar resolver con Greedy un problema que requiere Programación Dinámica, o plantear Programación Dinámica para un problema NP-Duro que pide Backtracking o Programación Lineal Entera. Utilizá este árbol de decisión rápido en el examen:

### Árbol de Decisión Rápido

```mermaid
flowchart TD
    Q(["¿QUÉ PIDE EL ENUNCIADO DEL EXAMEN?"])
    Q -->|"Demostrar NP-Completo / no es más difícil"| NPC["🟡 REDUCCIONES NP-C<br/>4 Pasos: Verificador NP + A conocido ≤_P B nuevo + Transformación + Ida y Vuelta"]
    Q -->|"Modelo matemático / variables y restricciones"| PL["🔵 PROGRAMACIÓN LINEAL (PL / PLI)<br/>Variables + Dominios + Función Objetivo Lineal + Restricciones + Conteo"]
    Q -->|"Asignar turnos / matching / oferta-demanda en red"| FL["🔴 REDES DE FLUJO<br/>Super-fuente s y super-sumidero t + Capacidades + Edmonds-Karp / Corte Mínimo"]
    Q -->|"Partir en subproblemas disjuntos n/b o búsqueda O(log n)"| DYC["🔷 DIVISIÓN Y CONQUISTA<br/>Caso base + División disjunta + Combinación + Teorema Maestro"]
    Q -->|"Optimizar (Maximizar / Minimizar) valor"| OPT{"¿Estructura de las decisiones?"}

    OPT -->|"Elección local irrevocable sin comprometer futuro"| GR["🔶 GREEDY (VORAZ)<br/>Ordenamiento voraz + Prueba (Stays Ahead / Intercambio) o Contraejemplo"]
    OPT -->|"Subproblemas superpuestos / recursos acoplados"| DP["🟢 PROGRAMACIÓN DINÁMICA<br/>5 Pasos: Estado OPT(...) + Casos Base + Recurrencia + Orden Bottom-Up + Reconstrucción"]
    OPT -->|"NP-Hard exacto en espacio combinatorio / tablero"| BT["🟣 BACKTRACKING & B&B<br/>Árbol de decisiones + Poda Factibilidad O(1) + Poda por Cota (Branch & Bound)"]

    classDef root fill:#1e3a8a,stroke:#1d4ed8,stroke-width:2px,color:#fff
    classDef dyc fill:#0284c7,stroke:#0369a1,stroke-width:2px,color:#fff
    classDef gr fill:#d97706,stroke:#b45309,stroke-width:2px,color:#fff
    classDef bt fill:#7c3aed,stroke:#6d28d9,stroke-width:2px,color:#fff
    classDef dp fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
    classDef pl fill:#2563eb,stroke:#1d4ed8,stroke-width:2px,color:#fff
    classDef fl fill:#dc2626,stroke:#b91c1c,stroke-width:2px,color:#fff
    classDef npc fill:#ca8a04,stroke:#a16207,stroke-width:2px,color:#fff

    class Q,OPT root
    class DYC dyc
    class GR gr
    class BT bt
    class DP dp
    class PL pl
    class FL fl
    class NPC npc
```

### Tabla de Señales y Disparadores Léxicos

| Si el enunciado menciona... | Señal clave | Paradigma sugerido | Estructura / Técnica |
| :--- | :--- | :--- | :--- |
| "Intervalos de tiempo", "pedidos no solapados", "deadlines" | Maximizar cantidad sin pesos | **Greedy** | Ordenar por tiempo de finalización más temprano ($f_i$). |
| "Intervalos con pesos o beneficios", "Juan el Vago" | Decisión sobre días/turnos adyacentes | **Programación Dinámica** | $OPT(i) = \max(OPT(i-1), \; OPT(p(i)) + v_i)$. |
| "Mochila con peso y volumen", "delivery", "límite de seguro" | Recursos múltiples acoplados | **Programación Dinámica** | Matriz 2D/3D: $OPT(i, w, v, m)$. |
| "Ubicar antenas en celdas", "visitar lugares para ver especies" | Cobertura de conjuntos (*Set Cover*) | **Programación Lineal (PLI)** | Variables binarias $x_i \in \{0, 1\}$, restricciones $x_i \le \sum y_j$. |
| "Médicos y turnos", "estudiantes y cupos", "red de cañerías" | Capacidad unitaria o integral de transporte | **Redes de Flujo** | Super-fuente $s$, super-sumidero $t$, Ford-Fulkerson / Edmonds-Karp. |
| "Tablero", "ubicar piezas sin ataques", "4 cuadrados que sumen $n$" | Espacio de búsqueda combinatorio | **Backtracking** | Recursión con estructuras booleanas de poda en $O(1)$. |
| "Demostrar que $X$ es NP-Completo", "compró software para $Y$" | Relación de dificultad de problemas | **Reducciones NP** | Reducción de Karp $A \le_P B$ con demostración en 4 pasos. |
"""
