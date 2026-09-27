# Guía de Práctica Esencial — Teoría de Algoritmos (FIUBA)

Este repositorio contiene una **selección curada de los ejercicios más representativos y de alto valor pedagógico** de las 5 guías de ejercicios de la materia, pensada para **optimizar tu tiempo de estudio** y asegurar el dominio de los conceptos y arquetipos evaluados en parciales y exámenes finales.

---

## 🎯 ¿Cómo usar estos archivos para practicar?

Cada archivo `.py` está preparado como una **hoja de práctica interactiva**:
1. **Enunciado completo:** El problema formal tal como aparece en las guías oficiales.
2. **Concepto clave:** Por qué se eligió este ejercicio y qué arquetipo representa.
3. **Tips para resolver el problema:** Intuición paso a paso, qué observar para no trabarse, casos borde y trampas frecuentes.
4. **Cálculo y justificación de complejidad:** Deducción de recurrencias, aplicación del Teorema Maestro, árboles de recursión, podas, estados y transiciones en DP, y recuento de variables/restricciones en PL.
5. **Esqueleto de código (`TODO`):** Función lista para que implementes tu propia solución.
6. **Casos de prueba (`assert`s):** Bloque ejecutable para verificar tu implementación corriendo directamente:
   ```bash
   python3 <archivo>.py
   ```

---

## 📚 Mapa de Ejercicios Seleccionados

### 1. División y Conquista (`01_division_y_conquista/`)
Aprenderás a descartar mitades, dividir en subproblemas independientes, combinar linealmente y justificar con el **Teorema Maestro** ($T(n) = aT(n/b) + O(n^c)$).

| Archivo | Ejercicio Guía | Arquetipo / Concepto Clave | Complejidad |
| :--- | :--- | :--- | :--- |
| [`ej02_primer_cero_tests.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/01_division_y_conquista/ej02_primer_cero_tests.py) | Ej 2 (★) | **Búsqueda binaria de transición (Git Bisect)**: encontrar el primer 0. Descarte de mitades en orden monótono. | $O(\log n)$ |
| [`ej04_arreglo_pico.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/01_division_y_conquista/ej04_arreglo_pico.py) | Ej 4 (★) | **Búsqueda binaria no monótona (Peak Element)**: comparar con vecinos adyacentes sin arreglo ordenado globalmente. | $O(\log n)$ |
| [`ej09_elemento_mayoritario.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/01_division_y_conquista/ej09_elemento_mayoritario.py) | Ej 9 (★★★) | **D&C con combinación lineal**: resolver 2 mitades ($a=2, b=2$) y verificar candidatos en tiempo lineal ($c=1$). | $O(n \log n)$ |
| [`ej14_bolzano_biseccion.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/01_division_y_conquista/ej14_bolzano_biseccion.py) | Ej 14 (★★) | **Bisección en espacios continuos (Bolzano)**: complejidad logarítmica respecto al tamaño del intervalo continuo $L/\epsilon$. | $O(\log(b - a))$ |

---

### 2. Algoritmos Greedy / Voraces (`02_greedy/`)
Aprenderás a diseñar reglas voraces, justificar optimalidad con **Argumentos de Intercambio (Exchange Arguments)** o **"Stays Ahead"**, y reconocer cuándo Greedy falla mediante **contraejemplos**.

| Archivo | Ejercicio Guía | Arquetipo / Concepto Clave | Demostración / Criterio |
| :--- | :--- | :--- | :--- |
| [`ej04_seleccion_charlas.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/02_greedy/ej04_seleccion_charlas.py) | Ej 4 (★★) | **Interval Scheduling**: maximizar actividades compatibles. Ordenar por menor tiempo de fin. | Stays Ahead ($O(n \log n)$) |
| [`ej13_antenas_ruta.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/02_greedy/ej13_antenas_ruta.py) | Ej 13 (★★) | **Point Covering en 1D**: colocar antena lo más a la derecha posible ($x + R$) que cubra la primera casa desprotegida. | Argumento de intercambio ($O(n \log n)$) |
| [`ej08_mochila_fraccionaria.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/02_greedy/ej08_mochila_fraccionaria.py) | Ej 8 (★★) | **Mochila Fraccionaria vs 0-1**: ordenamiento por ratio valor/peso. Contraejemplo canónico de por qué Greedy falla en 0-1. | Ratio valor/peso ($O(n \log n)$) |
| [`ej09_minimizar_latencia.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/02_greedy/ej09_minimizar_latencia.py) | Ej 9 (★★) | **Scheduling con Deadlines (EDF)**: minimizar la latencia máxima ordenando por fecha límite más temprana. | Inversiones adyacentes ($O(n \log n)$) |

---

### 3. Backtracking (`03_backtracking/`)
Aprenderás a explorar espacios combinatorios en árboles de decisión, aplicar **Podas por Factibilidad** y **Podas por Optimalidad (Branch and Bound)**, y calcular la complejidad en el peor caso.

| Archivo | Ejercicio Guía | Arquetipo / Concepto Clave | Tipo de Poda |
| :--- | :--- | :--- | :--- |
| [`ej03_n_reinas.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/03_backtracking/ej03_n_reinas.py) | Ej 3 (★) | **Colocación en tablero (N-Queens)**: fila por fila, evitando $n^n$ y reduciendo a $O(n!)$. | Factibilidad en $O(1)$ con sets de diagonales |
| [`ej04_independent_set_maximo.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/03_backtracking/ej04_independent_set_maximo.py) | Ej 4 (★★) | **Subset selection en grafos**: inclusión / exclusión de vértices en problemas NP-Hard. | Factibilidad (adyacencia) + Cota Superior (Branch & Bound) |
| [`ej11_subset_sum.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/03_backtracking/ej11_subset_sum.py) | Ej 11 (★) | **Combinaciones con suma objetivo**: generación de todos los subconjuntos que suman exactamente $n$. | Poda por exceso y ordenamiento previo |
| [`ej02_coloreo_grafos.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/03_backtracking/ej02_coloreo_grafos.py) | Ej 2 (★★) | **Problema de decisión y asignación ($k$-Coloring)**: asignar colores sin conflictos entre vecinos. | Factibilidad temprana en vecinos |

---

### 4. Programación Dinámica (`04_programacion_dinamica/`)
Aprenderás a identificar la **subestructura óptima**, definir formalmente el estado $OPT(\dots)$, plantear la **ecuación de recurrencia**, construir la tabla (1D o 2D) y realizar la **reconstrucción** de la solución.

| Archivo | Ejercicio Guía | Arquetipo / Concepto Clave | Dimensión / Complejidad |
| :--- | :--- | :--- | :--- |
| [`ej04_juan_el_vago.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/04_programacion_dinamica/ej04_juan_el_vago.py) | Ej 4 (★★) | **1D DP (Exclusión de adyacentes / House Robber)**: $OPT(i) = \max(OPT(i-1), OPT(i-2) + g_i)$. | 1D — $O(n)$ tiempo, $O(n)$ espacio |
| [`ej07_mochila_01.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/04_programacion_dinamica/ej07_mochila_01.py) | Ej 7 (★★★) | **2D DP (Mochila 0-1)**: tabla elemento $\times$ capacidad disponible, con reconstrucción retrocediendo en la matriz. | 2D — $O(n \cdot W)$ pseudo-polinomial |
| [`ej02_interval_scheduling_ponderado.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/04_programacion_dinamica/ej02_interval_scheduling_ponderado.py) | Ej 2 (★★★) | **Híbrido (Ordenamiento + Búsqueda Binaria + DP)**: selección de charlas con pesos arbitrarios. Búsqueda de $p(i)$. | 1D + Búsqueda Binaria — $O(n \log n)$ |
| [`ej08_cambio_monedas.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/04_programacion_dinamica/ej08_cambio_monedas.py) | Ej 8 (★★) | **Subproblemas no acotados (Coin Change)**: mínima cantidad de monedas con loop sobre denominaciones y reconstrucción. | 1D — $O(M \cdot K)$ pseudo-polinomial |

---

### 5. Programación Lineal (`05_programacion_lineal/`)
Aprenderás a modelar problemas como **Programación Lineal Entera (ILP)**: definición de variables de decisión y dominios, función objetivo, restricciones lineales, y linealización de operadores no lineales (como $\min \max$).

| Archivo | Ejercicio Guía | Arquetipo / Concepto Clave | Variables y Restricciones |
| :--- | :--- | :--- | :--- |
| [`ej01_mochila_pl.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/05_programacion_lineal/ej01_mochila_pl.py) | Ej 1 (★) | **Mochila 0-1 en PL**: variables binarias $x_i \in \{0, 1\}$, maximizar valor sujeto a restricción lineal de peso. | $n$ variables, 1 restricción ($O(1)$) |
| [`ej02_juan_el_vago_pl.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/05_programacion_lineal/ej02_juan_el_vago_pl.py) | Ej 2 (★) | **Exclusión mutua adyacente**: modelar "no dos días seguidos" con inecuaciones $x_i + x_{i+1} \le 1$. | $n$ variables, $n-1$ restricciones ($O(n)$) |
| [`ej03_vertex_cover_pl.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/05_programacion_lineal/ej03_vertex_cover_pl.py) | Ej 3 (★) | **Cobertura de aristas en grafos**: modelar "al menos un extremo seleccionado" con $x_u + x_v \ge 1$. | $\|V\|$ variables, $\|E\|$ restricciones |
| [`ej12_dos_particiones_min_max_pl.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/05_programacion_lineal/ej12_dos_particiones_min_max_pl.py) | Ej 12 (★★) | **Linealización de $\min \max$**: transformar el objetivo no lineal usando una variable auxiliar continua $Z$. | $n + 1$ variables, 2 restricciones ($O(1)$) |

---

## 🔗 Conexiones Fundamentales entre Paradigmas (Preguntas Típicas de Examen)

1. **Mochila:**
   - **Fraccionaria:** Greedy óptimo ordenando por ratio $v_i / w_i$ en $O(n \log n)$ ([`02_greedy/ej08_mochila_fraccionaria.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/02_greedy/ej08_mochila_fraccionaria.py)).
   - **0-1 Discreta:** Greedy falla por capacidad ociosa. Requiere DP en $O(n \cdot W)$ ([`04_programacion_dinamica/ej07_mochila_01.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/04_programacion_dinamica/ej07_mochila_01.py)) o PL Entera ([`05_programacion_lineal/ej01_mochila_pl.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/05_programacion_lineal/ej01_mochila_pl.py)).
2. **Selección de Charlas:**
   - **No ponderada:** Greedy óptimo ordenando por tiempo de fin en $O(n \log n)$ ([`02_greedy/ej04_seleccion_charlas.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/02_greedy/ej04_seleccion_charlas.py)).
   - **Ponderada (con pesos/valores):** Greedy falla. Requiere DP + Búsqueda Binaria en $O(n \log n)$ ([`04_programacion_dinamica/ej02_interval_scheduling_ponderado.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/04_programacion_dinamica/ej02_interval_scheduling_ponderado.py)).
3. **Juan el Vago / Conjunto Independiente en Camino:**
   - Resuelto por DP 1D en $O(n)$ ([`04_programacion_dinamica/ej04_juan_el_vago.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/04_programacion_dinamica/ej04_juan_el_vago.py)).
   - Formulado como PL Entera con $n-1$ restricciones ([`05_programacion_lineal/ej02_juan_el_vago_pl.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/05_programacion_lineal/ej02_juan_el_vago_pl.py)).
4. **Independent Set vs Vertex Cover:**
   - Duales exactos en teoría de grafos: $S$ es Independent Set $\iff V \setminus S$ es Vertex Cover.
   - Resueltos por Backtracking con podas ([`03_backtracking/ej04_independent_set_maximo.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/03_backtracking/ej04_independent_set_maximo.py)).
   - Modelados en PL con inecuaciones de aristas $x_u + x_v \ge 1$ vs $x_u + x_v \le 1$ ([`05_programacion_lineal/ej03_vertex_cover_pl.py`](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/Practicas/05_programacion_lineal/ej03_vertex_cover_pl.py)).
