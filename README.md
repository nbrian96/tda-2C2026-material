# Teoría de Algoritmos — Material de Cátedra (2C 2026)

<p align="center">
  <img src="logo-facultad.png" alt="Facultad de Ingeniería - UBA" width="160" />
</p>

<p align="center">
  <strong>Facultad de Ingeniería — Universidad de Buenos Aires (FIUBA)</strong><br>
  Repositorio centralizado de material de estudio, clases teóricas, guías prácticas, trabajos prácticos y exámenes parciales de la materia <em>Teoría de Algoritmos</em> (Segundo Cuatrimestre 2026).
</p>

---

## 🗂️ Estructura del Repositorio

```text
tda-2C2026-material/
├── DIapositivas/          # Diapositivas teóricas y prácticas oficiales (PDFs y scripts de clase)
├── Guia-Ejercicios/       # Guías completas de problemas propuestos por la cátedra (PDFs 01 a 09)
├── Practicas/             # Suite interactiva de ejercicios seleccionados (.py) con tips y tests
├── Parciales/             # Enunciados y modelos de exámenes parciales anteriores (2024 - 2025)
├── TP0/                   # Trabajo Práctico 0: Análisis empírico y complejidad asintótica
├── logo-facultad.png      # Identidad visual FIUBA
└── .gitignore             # Configuración de exclusión para Git (bytecode, pycache, entornos)
```

---

## 📖 Contenido Detallado

### 1. 📂 [DIapositivas/](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material/DIapositivas)
Presentaciones oficiales de las clases teóricas y prácticas, complementadas con scripts de seguimiento:
* **00 - 01:** Presentación del curso, introducción y repasos fundamentales.
* **02:** División y Conquista, Teorema Maestro y ejemplos de seguimiento.
* **03 - 04:** Algoritmos Greedy (Voraces), demostraciones ("Stays Ahead", intercambio).
* **05 - 06:** Backtracking, árboles de búsqueda, podas por factibilidad y optimalidad.
* **07:** Práctica integral: D&C, Greedy y Backtracking.
* **08 - 11:** Programación Dinámica (1D, 2D, reconstrucción de soluciones).
* **12 - 13:** Programación Lineal y Entera (modelado, variables, restricciones).
* **Subcarpetas temáticas:**
  * `12 - Lindo/`: Modelos de optimización en formato LINDO (`.ltx`).
  * `12 - Mochila/`: Modelos y scripts para el problema de la mochila (`.lp`, `.py`).
  * `12 - Viajante/`: Formulaciones del Problema del Viajante de Comercio (TSP) con distintas restricciones de subtours (MTZ, puentes, fuerza bruta).
  * `Explicaciones/`: Guías teóricas complementarias (ej: `problema_mochila_y_greedy.md`).

---

### 2. 📂 [Guia-Ejercicios/](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material/Guia-Ejercicios)
Guías de ejercicios oficiales publicadas por la cátedra para el cuatrimestre:
* `01_division_y_conquista.pdf`
* `02_greedy.pdf`
* `03_backtracking.pdf`
* `04_programacion_dinamica.pdf`
* `05_programacion_lineal.pdf`
* `06_redes_de_flujo.pdf`
* `07_reducciones_np.pdf`
* `08_algoritmos_aproximados.pdf`
* `09_algoritmos_randomizados.pdf`

---

### 3. 📂 [Practicas/](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material/Practicas)
Suite de **práctica interactiva** pensada para optimizar el tiempo de estudio. Contiene una selección curada de 20 ejercicios clave (4 por cada paradigma de la primera parte de la materia) implementados como plantillas de práctica en Python:

* **01_division_y_conquista:**
  * `ej02_primer_cero_tests.py`: Detección del primer fallo (Git Bisect) — $O(\log n)$.
  * `ej04_arreglo_pico.py`: Arreglo en forma de pico (Peak Element) — $O(\log n)$.
  * `ej09_elemento_mayoritario.py`: Elemento mayoritario — $O(n \log n)$.
  * `ej14_bolzano_biseccion.py`: Raíz por Teorema de Bolzano — $O(\log(b - a))$.
* **02_greedy:**
  * `ej04_seleccion_charlas.py`: Interval Scheduling (maximizar charlas compatibles) — $O(n \log n)$.
  * `ej08_mochila_fraccionaria.py`: Mochila fraccionaria vs 0-1 (contraejemplo) — $O(n \log n)$.
  * `ej09_minimizar_latencia.py`: Scheduling con deadlines (EDF) — $O(n \log n)$.
  * `ej13_antenas_ruta.py`: Cobertura de casas con antenas (Point Covering 1D) — $O(n \log n)$.
* **03_backtracking:**
  * `ej02_coloreo_grafos.py`: $k$-Coloración de grafos (problema de decisión).
  * `ej03_n_reinas.py`: Problema de las N Reinas con podas en $O(1)$.
  * `ej04_independent_set_maximo.py`: Maximum Independent Set (podas por factibilidad y Branch & Bound).
  * `ej11_subset_sum.py`: Suma de subconjuntos que suman exactamente $n$.
* **04_programacion_dinamica:**
  * `ej02_interval_scheduling_ponderado.py`: Selección de charlas ponderadas con búsqueda binaria de $p(i)$ — $O(n \log n)$.
  * `ej04_juan_el_vago.py`: Juan el Vago (House Robber 1D) con reconstrucción — $O(n)$.
  * `ej07_mochila_01.py`: Mochila 0-1 (tabla 2D pseudo-polinomial) con reconstrucción — $O(n \cdot W)$.
  * `ej08_cambio_monedas.py`: Problema del cambio de monedas no acotado — $O(M \cdot K)$.
* **05_programacion_lineal:**
  * `ej01_mochila_pl.py`: Mochila 0-1 en Programación Lineal Entera.
  * `ej02_juan_el_vago_pl.py`: Restricción de no adyacencia ($x_i + x_{i+1} \le 1$).
  * `ej03_vertex_cover_pl.py`: Vertex Cover Mínimo ($x_u + x_v \ge 1$).
  * `ej12_dos_particiones_min_max_pl.py`: 2-Partition Problem (linealización de $\min \max$).

Cada archivo contiene: enunciado, concepto clave, tips paso a paso, cálculo formal de complejidad, esqueleto con `TODO` y tests unitarios ejecutables. Consulta [Practicas/README.md](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material/Practicas/README.md) para más detalles.

---

### 4. 📂 [Parciales/](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material/Parciales)
Enunciados de exámenes parciales tomados en cuatrimestres recientes para entrenar con casos reales:
* `TP-2024-2-1.pdf`, `TP-2024-2-2.pdf`, `TP-2024-2-3.pdf`
* `TP-2025-1-1.pdf`, `TP-2025-1-2.pdf`

---

### 5. 📂 [TP0/](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material/TP0)
Primer trabajo práctico de la materia:
* `TP00-2026-2c.pdf`: Enunciado oficial.
* `cuartetos.py` y `cuartetos_malo.py`: Implementaciones y mediciones de tiempos.
* `grafico_tiempos.png`: Curvas comparativas de tiempos empíricos vs asintóticos.
* `TP0_Nelson_Avila_100244.pdf`: Informe final presentado.

---

## 🚀 Cómo utilizar este material

1. **Clonar o abrir el repositorio:**
   ```bash
   cd /home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material
   ```

2. **Flujo de estudio recomendado:**
   * 1️⃣ Leer la teoría y ejemplos de seguimiento en [DIapositivas/](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material/DIapositivas).
   * 2️⃣ Explorar los ejercicios de la [Guia-Ejercicios/](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material/Guia-Ejercicios).
   * 3️⃣ Resolver los ejercicios seleccionados en [Practicas/](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material/Practicas) y verificar corriendo:
     ```bash
     python3 Practicas/01_division_y_conquista/ej04_arreglo_pico.py
     ```
   * 4️⃣ Practicar simulacros de examen cronometrados con los PDFs de [Parciales/](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material/Parciales).

---

## 📜 Licencia y Atribución
Material docente y práctico correspondiente a la cátedra de **Teoría de Algoritmos** de la **Facultad de Ingeniería de la Universidad de Buenos Aires (FIUBA)**.
