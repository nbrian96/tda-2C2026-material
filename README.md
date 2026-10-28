# Teoría de Algoritmos — Material de Cátedra (2C 2026)

<p align="center">
  <img src="logo-facultad.png" alt="Facultad de Ingeniería - UBA" width="160" />
</p>

<p align="center">
  <strong>Facultad de Ingeniería — Universidad de Buenos Aires (FIUBA)</strong><br>
  Repositorio centralizado de material de estudio, clases teóricas, guías prácticas, trabajos prácticos, exámenes parciales y <strong>Guía Interactiva Modular de Resolución de Parciales (83 Ejercicios)</strong> de la materia <em>Teoría de Algoritmos</em> (Segundo Cuatrimestre 2026).
</p>

---

## ⚡ Guía Interactiva de Parciales ("Salvando el Cuatrimestre" — 83 Ejercicios)

Para preparar el examen parcial de forma intensiva, el repositorio incluye una **aplicación web modular con Bootstrap 5.3** orientada a la práctica activa (*Active Recall*), filtrado por paradigma y **graduación de dificultad de 1★ a 5★**:

* 🌐 **Guía Online en GitHub Pages:** <a href="https://nbrian96.github.io/tda-2C2026-material/" target="_blank" rel="noopener noreferrer"><strong>https://nbrian96.github.io/tda-2C2026-material/</strong></a>
* 💻 **Catálogo Completo Local:** [index.html](index.html) (83 ejercicios interactivos)
* 🧩 **Vistas Modulares por Paradigma:**
  * 🔷 [División y Conquista (`dyc.html`)](dyc.html) — 12 ejercicios
  * 🔶 [Algoritmos Greedy (`greedy.html`)](greedy.html) — 26 ejercicios
  * 🟣 [Backtracking y Branch & Bound (`backtracking.html`)](backtracking.html) — 14 ejercicios
  * 🟢 [Programación Dinámica (`dp.html`)](dp.html) — 7 ejercicios
  * 🔵 [Programación Lineal y PLI (`pl.html`)](pl.html) — 6 ejercicios
  * 🔴 [Redes de Flujo (`flujo.html`)](flujo.html) — 5 ejercicios
  * 🟡 [Reducciones NP-Completas (`reducciones.html`)](reducciones.html) — 4 ejercicios
  * ⚡ [Problemas Integradores y Multi-Paradigma (`integradores.html`)](integradores.html) — 5 ejercicios
  * 📝 [Simulacros Tipo Parcial y Checklist (`tipo_parcial.html`)](tipo_parcial.html) — 4 ejercicios

### 🎯 Cómo estudiar con la Guía según tus días disponibles

#### 1. Plan de Emergencia (48 a 72 horas antes del examen)
1. Abrí [index.html](index.html) (o la <a href="https://nbrian96.github.io/tda-2C2026-material/" target="_blank" rel="noopener noreferrer">versión online</a>) y activá el botón **⚡ Modo Emergencia**.
2. Esto filtrará automáticamente los **ejercicios clave 🔴 IMPRESCINDIBLE** que salieron literalmente en los parciales recientes (`2024-2`, `2025-1` y `2026-2`) junto con los problemas canónicos de la guía.
3. Usá el **filtro por Dificultad (1★ a 5★)** del HUD superior para avanzar gradualmente desde ejercicios de entrada en calor (`1★` y `2★`) hasta problemas de cierre de examen (`4★` y `5★`).
4. Practicá con el **Entrenador de Reconocimiento en 30 Segundos** para distinguir al instante entre Greedy, Programación Dinámica, Backtracking, Programación Lineal o Redes de Flujo.
5. Repasá el drawer de **📐 Fórmulas y Recetas Rápidas** (Teorema Maestro, los 4 pasos de NP-C y los 5 pasos de PD).
6. En cada tarjeta, leé el enunciado e intentá resolverlo en papel **antes de desplegar la solución** (*Active Recall*). Al dominarlo, marcalo como `Dominado` para registrar tu progreso.

#### 2. Plan Táctico (1 semana antes)
1. Completá el Plan de Emergencia y cambiá a **🎯 Modo Táctico** para enfocarte en los ejercicios **🟡 IMPORTANTES** de la Guía Práctica v1.0 y en los que aún tengas pendientes de dominar.
2. Escribí en papel el pseudocódigo y análisis de complejidad de los ejercicios de Programación Dinámica multidimensional, Redes de Flujo y Branch & Bound.
3. Repasá los **Ejercicios Integradores Multi-Paradigma** ([`integradores.html`](integradores.html), Ejercicios 78 y 79) para comparar cómo resolver La Mochila y El Viajante (TSP) bajo cada paradigma.

#### 3. Plan Integral (2 semanas o más)
1. Recorré los **83 ejercicios** en **📚 Modo Todos** o navegando pestaña por pestaña en las páginas modulares de cada paradigma.
2. Probá las implementaciones en Python de la carpeta `Practicas/`.
3. Verificá la **Checklist de Entrada al Aula** en [`tipo_parcial.html`](tipo_parcial.html) antes de rendir.

---

## 🌐 Cómo desplegar la Guía en GitHub Pages

1. Ingresá a tu repositorio en GitHub: <a href="https://github.com/nbrian96/tda-2C2026-material" target="_blank" rel="noopener noreferrer">https://github.com/nbrian96/tda-2C2026-material</a>.
2. Hacé clic en **Settings** (⚙️ Configuración) $\to$ sección **Pages**.
3. En **Build and deployment**:
   * **Source:** `Deploy from a branch`.
   * **Branch:** `master` (o `main`) y carpeta `/ (root)`.
   * Hacé clic en **Save**.
4. En 1 a 2 minutos tu guía estará publicada en:
   👉 **<a href="https://nbrian96.github.io/tda-2C2026-material/" target="_blank" rel="noopener noreferrer">https://nbrian96.github.io/tda-2C2026-material/</a>**

---

## 🗂️ Estructura del Repositorio

```text
tda-2C2026-material/
├── index.html              # Catálogo interactivo completo (83 ejercicios)
├── dyc.html                # Vista modular: División y Conquista (12 ejercicios)
├── greedy.html             # Vista modular: Algoritmos Greedy (26 ejercicios)
├── backtracking.html       # Vista modular: Backtracking y B&B (14 ejercicios)
├── dp.html                 # Vista modular: Programación Dinámica (7 ejercicios)
├── pl.html                 # Vista modular: Programación Lineal y PLI (6 ejercicios)
├── flujo.html              # Vista modular: Redes de Flujo (5 ejercicios)
├── reducciones.html        # Vista modular: Reducciones NP-C (4 ejercicios)
├── integradores.html       # Vista modular: Integradores y Multi-Paradigma (5 ejercicios)
├── tipo_parcial.html       # Vista modular: Simulacros Tipo Parcial y Checklist (4 ejercicios)
├── assets/                 # Recursos estáticos modulares (Bootstrap 5.3 + Dark Mode)
│   ├── css/styles.css      # Estilos de tarjetas, badges de dificultad 1★-5★ y HUD
│   └── js/app.js           # Lógica de filtrado por modo/dificultad, búsqueda y simulador
├── builder/                # Motor de compilación modular en Python
│   ├── build_manual.py     # Script compilador de las 10 páginas HTML interactivas
│   ├── html_interactive_builder.py # Generador de componentes HTML5 + Bootstrap 5.3
│   └── sec01_... a sec11_  # Módulos temáticos de teoría y 83 ejercicios resueltos
├── DIapositivas/           # Diapositivas teóricas y prácticas oficiales (PDFs y scripts)
├── Guia-Ejercicios/        # Guías oficiales 01 a 09 y Guía consolidada v1.0
├── Practicas/              # Suite de ejercicios seleccionados en Python con tests
├── Parciales/              # Enunciados oficiales de parciales (2024, 2025 y 2026)
├── TP0/                    # Trabajo Práctico 0: Análisis asintótico y experimental
├── .nojekyll               # Configuración de GitHub Pages para servir assets estáticos
└── logo-facultad.png       # Identidad visual FIUBA
```

---

## 📖 Contenido Detallado de Carpetas

### 1. 📂 [DIapositivas/](DIapositivas/)
Presentaciones oficiales de las clases teóricas y prácticas, complementadas con scripts de seguimiento:
* **00 - 01:** Presentación del curso, introducción y repasos fundamentales.
* **02:** División y Conquista, Teorema Maestro y ejemplos de seguimiento.
* **03 - 04:** Algoritmos Greedy (Voraces), demostraciones ("Stays Ahead", intercambio).
* **05 - 06:** Backtracking, árboles de búsqueda, podas por factibilidad y optimalidad.
* **07:** Práctica integral: D&C, Greedy y Backtracking.
* **08 - 11:** Programación Dinámica (1D, 2D, reconstrucción de soluciones).
* **12 - 13:** Programación Lineal y Entera (modelado, variables, restricciones).
* **Subcarpetas temáticas:** `12 - Lindo/`, `12 - Mochila/` y `12 - Viajante/`.

---

### 2. 📂 [Guia-Ejercicios/](Guia-Ejercicios/)
Guías oficiales publicadas por la cátedra para el cuatrimestre:
* `GuiaDeEjercicios-v1.0.pdf` *(Guía consolidada Curso Echevarría — D&C, Greedy y Backtracking, íntegramente resuelta en la plataforma interactiva)*
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

### 3. 📂 [Practicas/](Practicas/)
Suite de **práctica en código Python** con 20 ejercicios resueltos con tests unitarios:
* **01_division_y_conquista:** `primer_cero`, `arreglo_pico`, `elemento_mayoritario`, `bolzano_biseccion`.
* **02_greedy:** `seleccion_charlas`, `mochila_fraccionaria`, `minimizar_latencia`, `antenas_ruta`.
* **03_backtracking:** `coloreo_grafos`, `n_reinas`, `independent_set_maximo`, `subset_sum`.
* **04_programacion_dinamica:** `interval_scheduling_ponderado`, `juan_el_vago`, `mochila_01`, `cambio_monedas`.
* **05_programacion_lineal:** `mochila_pl`, `juan_el_vago_pl`, `vertex_cover_pl`, `dos_particiones_min_max_pl`.

---

### 4. 📂 [Parciales/](Parciales/)
Exámenes parciales tomados en fechas recientes (todos resueltos paso a paso en la guía interactiva):
* `TP-2024-2-1.pdf`, `TP-2024-2-2.pdf`, `TP-2024-2-3.pdf`
* `TP-2025-1-1.pdf`, `TP-2025-1-2.pdf`
* `TP-2026-2-1.pdf` *(Nuevo parcial incorporado con sus 5 ejercicios resueltos)*

---

### 5. 📂 [TP0/](TP0/)
Primer trabajo práctico de la materia:
* `TP00-2026-2c.pdf`, `cuartetos.py`, `cuartetos_malo.py`, `grafico_tiempos.png` y `TP0_Nelson_Avila_100244.pdf`.

---

## 🛠️ Cómo recompilar la plataforma interactiva tras realizar cambios

Si editás los módulos de contenido en `builder/sec01_...` a `sec11_...` o los recursos en `assets/`, podés regenerar todas las páginas HTML corriendo:

```bash
python builder/build_manual.py
```

El compilador verificará automáticamente la integridad de los bloques de código, limpiará artefactos antiguos y generará `index.html` junto con las 9 páginas modulares por paradigma verificando el conteo de líneas de cada archivo.

---

## 📜 Licencia y Atribución
Material docente y práctico correspondiente a la cátedra de **Teoría de Algoritmos** de la **Facultad de Ingeniería de la Universidad de Buenos Aires (FIUBA)**.
