# Teoría de Algoritmos — Material de Cátedra (2C 2026)

<p align="center">
  <img src="logo-facultad.png" alt="Facultad de Ingeniería - UBA" width="160" />
</p>

<p align="center">
  <strong>Facultad de Ingeniería — Universidad de Buenos Aires (FIUBA)</strong><br>
  Repositorio centralizado de material de estudio, clases teóricas, guías prácticas, trabajos prácticos, exámenes parciales y <strong>Guía Interactiva de Resolución de Parciales</strong> de la materia <em>Teoría de Algoritmos</em> (Segundo Cuatrimestre 2026).
</p>

---

## ⚡ Guía Interactiva de Parciales ("Salvando el Cuatrimestre")

Para preparar el examen parcial en poco tiempo, el repositorio incluye una **aplicación de estudio interactiva autocontenida** orientada a la práctica intensiva y al *Active Recall*:

* 🌐 **Guía Online en GitHub Pages:** <a href="https://nbrian96.github.io/tda-2C2026-material/" target="_blank" rel="noopener noreferrer"><strong>https://nbrian96.github.io/tda-2C2026-material/</strong></a> (abre en una nueva pestaña)
* 💻 **Versión Web Local:** [index.html](index.html) / [guia_tda_parciales.html](guia_tda_parciales.html)
* 📄 **Manual Imprimible en PDF (73 páginas A4):** [guia_tda_parciales.pdf](guia_tda_parciales.pdf)
* 📝 **Fuente estructurada en Markdown:** [guia_tda_parciales.md](guia_tda_parciales.md)

### 🎯 Cómo estudiar con la Guía según tus días disponibles

#### 1. Plan de Emergencia (48 a 72 horas antes del examen)
1. Abrí [index.html](index.html) (o la <a href="https://nbrian96.github.io/tda-2C2026-material/" target="_blank" rel="noopener noreferrer">versión online</a>) y activá el botón **⚡ Modo Emergencia**.
2. Esto filtrará automáticamente los **30 ejercicios clave 🔴 IMPRESCINDIBLE** que salieron literalmente en los parciales recientes (2024-2 y 2025-1).
3. Hacé el **Entrenador de Reconocimiento en 30 Segundos** (en la Sección 3) para no dudar entre Greedy, Programación Dinámica, Backtracking, Programación Lineal o Redes de Flujo.
4. Repasá el drawer de **📐 Fórmulas y Recetas Rápidas** (Teorema Maestro, los 4 pasos de NP-C y los 5 pasos de PD).
5. En cada ejercicio, lee el enunciado e intenta resolverlo en papel **antes de desplegar la solución** (*Active Recall*). Al dominarlo, márcalo como `Dominado` para registrar tu avance.

#### 2. Plan Táctico (1 semana antes)
1. Completá el Plan de Emergencia y cambiá a **🎯 Modo Táctico** para sumar los 8 ejercicios 🟡 **IMPORTANTES** de la guía práctica.
2. Escribí en papel el pseudocódigo completo de los ejercicios de Programación Dinámica multidimensional, Flujo y Branch & Bound.
3. Repasá los **Ejercicios Integradores Multi-Paradigma** (Sección 11) para comparar cómo resolver un mismo problema por Greedy vs PD vs PL.

#### 3. Plan Integral (2 semanas o más)
1. Recorré los 38 ejercicios en **📚 Modo Completo**.
2. Probá las implementaciones en Python de la carpeta `Practicas/`.
3. Verificá la **Checklist de Entrada al Aula** antes de rendir.

---

## 🌐 Cómo desplegar la Guía en GitHub Pages

Para tener la guía interactiva online accesible desde cualquier computadora, tablet o celular:

1. Ingresá a tu repositorio en GitHub: <a href="https://github.com/nbrian96/tda-2C2026-material" target="_blank" rel="noopener noreferrer">https://github.com/nbrian96/tda-2C2026-material</a>.
2. Hacé clic en la pestaña **Settings** (⚙️ Configuración) del repositorio.
3. En el menú lateral izquierdo, seleccioná la sección **Pages** (dentro del grupo *Code and automation*).
4. En **Build and deployment**:
   * **Source:** Seleccioná `Deploy from a branch`.
   * **Branch:** Elegí la rama `master` (o `main`) y en la carpeta seleccioná `/ (root)`.
   * Hacé clic en **Save** (Guardar).
5. Esperá entre 1 y 2 minutos mientras GitHub Actions ejecuta el deploy automático.
6. ¡Listo! Tu guía estará disponible en la URL pública (hacé clic para abrir en una nueva pestaña):
   
   👉 **<a href="https://nbrian96.github.io/tda-2C2026-material/" target="_blank" rel="noopener noreferrer">https://nbrian96.github.io/tda-2C2026-material/</a>**

   *(El archivo `.nojekyll` y la copia `index.html` ya incluidos en el repositorio garantizan que el sitio cargue de inmediato sin errores de rutas ni procesamiento de Jekyll).*

---

## 🗂️ Estructura del Repositorio

```text
tda-2C2026-material/
├── index.html              # Guía Interactiva lista para GitHub Pages
├── guia_tda_parciales.html # Aplicación web de estudio interactivo (Active Recall + HUD)
├── guia_tda_parciales.pdf  # Manual completo de parciales en PDF (73 páginas A4)
├── guia_tda_parciales.md   # Compendio completo de teoría y ejercicios en Markdown
├── .nojekyll               # Configuración de GitHub Pages para assets estáticos
├── builder/                # Motor de compilación y ensamble automatizado
│   ├── build_manual.py     # Script compilador de Markdown, HTML interactivo y PDF
│   ├── html_interactive_builder.py # Generador de interfaz, Active Recall y widgets
│   └── sec01_... a sec11_  # Módulos temáticos individuales
├── DIapositivas/           # Diapositivas teóricas y prácticas oficiales (PDFs y scripts)
├── Guia-Ejercicios/        # Guías completas de problemas propuestos (PDFs 01 a 09)
├── Practicas/              # Suite de ejercicios seleccionados en Python con tests
├── Parciales/              # Enunciados oficiales de parciales (2024 - 2025)
├── TP0/                    # Trabajo Práctico 0: Análisis asintótico y experimental
├── logo-facultad.png       # Identidad visual FIUBA
└── .gitignore              # Exclusiones de Git (entornos, cachés, temporales)
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
* **Subcarpetas temáticas:**
  * `12 - Lindo/`: Modelos de optimización en formato LINDO (`.ltx`).
  * `12 - Mochila/`: Modelos y scripts para el problema de la mochila (`.lp`, `.py`).
  * `12 - Viajante/`: Formulaciones de TSP con distintas restricciones de subtours (MTZ, puentes).

---

### 2. 📂 [Guia-Ejercicios/](Guia-Ejercicios/)
Guías oficiales publicadas por la cátedra para el cuatrimestre:
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

Consulta [Practicas/README.md](Practicas/README.md) para más detalles.

---

### 4. 📂 [Parciales/](Parciales/)
Exámenes parciales tomados en fechas recientes:
* `TP-2024-2-1.pdf`, `TP-2024-2-2.pdf`, `TP-2024-2-3.pdf`
* `TP-2025-1-1.pdf`, `TP-2025-1-2.pdf`

---

### 5. 📂 [TP0/](TP0/)
Primer trabajo práctico de la materia:
* `TP00-2026-2c.pdf`: Enunciado oficial.
* `cuartetos.py` y `cuartetos_malo.py`: Implementaciones y mediciones de tiempos.
* `grafico_tiempos.png`: Curvas comparativas de tiempos empíricos vs asintóticos.
* `TP0_Nelson_Avila_100244.pdf`: Informe final presentado.

---

## 🛠️ Cómo recompilar el manual tras realizar cambios

Si editás los módulos de contenido en `builder/sec01_...` a `sec11_...`, podés reconstruir todo el ecosistema (Markdown, HTML interactivo y PDF) corriendo:

```bash
cd builder
python3 build_manual.py
```

El script verificará automáticamente la integridad de los bloques de código, ensamblará `guia_tda_parciales.md`, generará la aplicación `guia_tda_parciales.html` e `index.html`, y compilará el PDF `guia_tda_parciales.pdf` mediante Google Chrome headless.

---

## 📜 Licencia y Atribución
Material docente y práctico correspondiente a la cátedra de **Teoría de Algoritmos** de la **Facultad de Ingeniería de la Universidad de Buenos Aires (FIUBA)**.
