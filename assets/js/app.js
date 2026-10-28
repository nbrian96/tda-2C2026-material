// ==========================================================================
// TDA — Guía Interactiva de Parciales (FIUBA)
// Lógica Frontend Modular (83 Ejercicios + Filtro de Dificultad 1★-5★ + Simulador)
// ==========================================================================

// Global state
let currentMode = 'all';
let currentParadigm = 'all';
let currentDifficulty = 'all';
let searchQuery = '';
let solutionsExpanded = false;
let masteredExercises = new Set();
let checklistState = {};

// 20 real exam scenario questions for the 30-second trainer (incluye Parcial 2026-2-1)
const TRAINER_QUESTIONS = [
  {
    prompt: "Dado un número entero positivo K, determinar la mínima cantidad de operaciones necesarias para llegar desde 0 hasta K, sabiendo que las únicas operaciones permitidas son sumar 1 o duplicar el valor actual.",
    answer: "dp",
    paradigmName: "Programación Dinámica",
    trigger: "Subproblemas con superposición: llegar a K depende de K-1 o K/2. Ecuación OPT(x) = 1 + min(OPT(x-1), OPT(x/2)). Es DP clásico de caminos mínimos en DAG de estados (Parcial 2024-2-2)."
  },
  {
    prompt: "Se tienen N solicitudes de mafias para operar en tramos de ruta costera [s_i, f_i]. Dos tramos no pueden superponerse. Se desea otorgar la máxima cantidad de permisos sin conflictos.",
    answer: "greedy",
    paradigmName: "Greedy (Voraz)",
    trigger: "Interval Scheduling sin pesos: se resuelve vorazmente ordenando por tiempo de finalización más temprano (f_i). Optimalidad demostrada por Greedy Stays Ahead (Parcial 2024-2-2, Arnook)."
  },
  {
    prompt: "Dado un entero n, encontrar cuatro enteros w, x, y, z >= 0 tales que n = w² + x² + y² + z². Si hay múltiples soluciones, retornar una con estructuras de poda temprana por cotas.",
    answer: "backtracking",
    paradigmName: "Backtracking & B&B",
    trigger: "Búsqueda exhaustiva en espacio de estados con podas por cotas numéricas (w² <= n). Teorema de los 4 cuadrados de Lagrange (Parcial 2024-2-1)."
  },
  {
    prompt: "Demostrar formalmente que el problema de decidir si un grafo G tiene un conjunto dominante de tamaño a lo sumo k (Dominating Set) es NP-Completo, sabiendo que Vertex Cover es NP-Completo.",
    answer: "reducciones",
    paradigmName: "Reducciones NP-C",
    trigger: "Consigna explícita: 'Demostrar que X es NP-Completo'. Requiere el esquema de 4 pasos: Verificador en NP + Problema conocido VC <=_P DS + Transformación de grafo + Demostración ida y vuelta (Parcial 2024-2-2 y 2024-2-3)."
  },
  {
    prompt: "Un hospital dispone de M médicos y P pacientes. Cada médico tiene turnos disponibles y cada paciente tiene turnos compatibles. Determinar la asignación que maximice las citas sin superposición.",
    answer: "flujo",
    paradigmName: "Redes de Flujo",
    trigger: "Matching bipartito con capacidades unitarias: modelar red en 4 capas s -> Pacientes -> Turnos (m, h) -> t y resolver con Edmonds-Karp por Teorema de Integralidad (Parcial 2024-2-2)."
  },
  {
    prompt: "Dada una grilla de comunidades, se desea decidir en qué celdas instalar antenas para cubrir al menos el 70% de comunidades con costo mínimo, indicando cantidad de variables y restricciones.",
    answer: "pl",
    paradigmName: "Programación Lineal (PLI)",
    trigger: "Consigna: 'Formular un modelo matemático con variables y restricciones'. Es Set Cover formulado como Programación Lineal Entera con variables binarias x_i in {0, 1} (Parcial 2024-2-3)."
  },
  {
    prompt: "Dadas dos matrices cuadradas de n x n, multiplicarlas particionando en 4 bloques de n/2 x n/2 y deduciendo la complejidad formal con el Teorema Maestro.",
    answer: "dyc",
    paradigmName: "División y Conquista",
    trigger: "Partición recursiva en subproblemas disjuntos de tamaño n/b y aplicación del Teorema Maestro T(n) = 8·T(n/2) + Θ(n²) = Θ(n³) (Parcial 2025-1-2)."
  },
  {
    prompt: "Juan el Vago recibe ofertas de changas diarias v_i. Si trabaja el día i, debe descansar obligatoriamente el día i+1. Maximizar su beneficio total.",
    answer: "dp",
    paradigmName: "Programación Dinámica",
    trigger: "Subproblemas dependientes con exclusión de días adyacentes: OPT(i) = max(OPT(i-1), OPT(i-2) + v_i). (Guía 04, Ej 4)."
  },
  {
    prompt: "Dada una red energética con generadores (oferta), ciudades (demanda) y líneas de transmisión con capacidades máximas, determinar el balance óptimo y los cuellos de botella.",
    answer: "flujo",
    paradigmName: "Redes de Flujo",
    trigger: "Ford-Fulkerson / Edmonds-Karp con super-fuente y super-sumidero para balancear múltiples fuentes y sumideros con capacidades y análisis de Corte Mínimo (Parcial 2025-1-1)."
  },
  {
    prompt: "Un cadete debe repartir encomiendas recorriendo n ciudades y regresar al punto de partida. Demostrar que este problema no es más fácil que Ciclo Hamiltoniano.",
    answer: "reducciones",
    paradigmName: "Reducciones NP-C",
    trigger: "Reducción polinomial de Ciclo Hamiltoniano a TSP (Problema del Viajante) con grafo completo y pesos {1, 2} con cota k = n (Parcial 2025-1-1, Marco el cadete)."
  },
  {
    prompt: "Ubicar 8 reinas en un tablero de ajedrez sin que se ataquen, verificando conflictos de columna y diagonales en O(1) con arreglos booleanos.",
    answer: "backtracking",
    paradigmName: "Backtracking & B&B",
    trigger: "Exploración exhaustiva de tablero con control de factibilidad O(1) mediante arreglos auxiliares y vuelta atrás del estado (Parcial 2025-1-2)."
  },
  {
    prompt: "Formatear un párrafo de palabras minimizando la suma de cubos/cuadrados de espacios sobrantes al final de cada línea (Word Wrap / Knuth-Plass).",
    answer: "dp",
    paradigmName: "Programación Dinámica",
    trigger: "La elección del corte de palabras en la línea actual define la longitud de los renglones restantes: OPT(i) = min_{j >= i} (costo(i, j) + OPT(j+1)) (Parcial 2024-2-3)."
  },
  {
    prompt: "Dado un arreglo donde no hay adyacentes iguales, encontrar un elemento pico (mayor a sus vecinos) en tiempo O(log n).",
    answer: "dyc",
    paradigmName: "División y Conquista",
    trigger: "Búsqueda binaria sobre la pendiente local: comparar A[m] con A[m+1] descartando la mitad del arreglo en cada paso en O(log n) (Guía 01, Ej 4)."
  },
  {
    prompt: "Dadas n tareas con tiempos de procesamiento y fechas límite d_i, ordenar la secuencia para minimizar la latencia máxima L = max(0, f_i - d_i).",
    answer: "greedy",
    paradigmName: "Greedy (Voraz)",
    trigger: "Earliest Deadline First (EDF): ordenar por fecha de entrega más temprana d_i. Se demuestra óptimo por argumento de intercambio de inversiones adyacentes (Guía 02, Ej 9)."
  },
  {
    prompt: "Se tienen n objetos indivisibles con pesos w_i y valores v_i, y una mochila de capacidad máxima W. Encontrar la combinación de máximo valor respetando la capacidad entera.",
    answer: "dp",
    paradigmName: "Programación Dinámica",
    trigger: "Mochila 0-1: subestructura óptima con superposición de subproblemas OPT(i, w). Requiere tabla (n+1) x (W+1) en O(n · W) pseudo-polinomial (Ejercicio 78)."
  },
  {
    prompt: "Dado un conjunto de n ciudades con matriz de distancias métricas, hallar un circuito cerrado que visite todas las ciudades con costo garantizado a lo sumo el doble del óptimo.",
    answer: "greedy",
    paradigmName: "Algoritmo de Aproximación (MST + Preorden)",
    trigger: "2-Aproximación de TSP Métrico: calcular Árbol Generador Mínimo (MST) con Prim o Kruskal y recorrer en preorden tomando atajos por desigualdad triangular (Ejercicio 79)."
  },
  {
    prompt: "Dado un arreglo de números enteros (positivos y negativos), encontrar el subarreglo contiguo cuya suma de elementos sea máxima, partiendo el arreglo a la mitad y analizando el cruce central.",
    answer: "dyc",
    paradigmName: "División y Conquista",
    trigger: "Subarreglo de Suma Máxima por División y Conquista: el óptimo está en la mitad izquierda, mitad derecha o cruza el centro expandiendo desde m hacia ambos lados. Recurrencia T(n) = 2T(n/2) + O(n) = O(n log n) (Parcial 2026-2-1)."
  },
  {
    prompt: "Dada una matriz que representa un laberinto con paredes, trampas y una celda con un tesoro, encontrar un camino válido desde la entrada hasta el tesoro sin pasar dos veces por la misma celda.",
    answer: "backtracking",
    paradigmName: "Backtracking & B&B",
    trigger: "Búsqueda de camino en grilla/laberinto con restricciones de celdas visitadas: exploración exhaustiva DFS con marcado de visitados y vuelta atrás (desmarcado) al retroceder (Parcial 2026-2-1)."
  },
  {
    prompt: "Un sistema de transporte recorre N estaciones en línea recta con costos de peaje c_i en cada estación. El vehículo tiene una autonomía que le permite saltar a la estación i+1 o i+2. Minimizar el costo total para llegar a la estación N.",
    answer: "dp",
    paradigmName: "Programación Dinámica",
    trigger: "Decisiones secuenciales con superposición de subproblemas sobre prefijos de estaciones: OPT(i) = c_i + min(OPT(i-1), OPT(i-2)) en tiempo O(N) (Parcial 2026-2-1)."
  },
  {
    prompt: "En una jornada electoral se deben trasladar urnas desde múltiples centros de votación hacia la sede central del CNE a través de rutas con capacidades máximas de transporte seguras por hora. Determinar si es posible trasladar todas las urnas a tiempo.",
    answer: "flujo",
    paradigmName: "Redes de Flujo",
    trigger: "Transporte de múltiples orígenes a destino con capacidades en rutas: se modela con super-fuente s conectada a cada centro de votación con capacidad igual a sus urnas y se verifica si el Flujo Máximo hacia el CNE satura la oferta total (Parcial 2026-2-1)."
  }
];

let trainerIndex = 0;
let trainerScore = 0;
let trainerAnswered = false;

function getPageForExercise(num) {
  if (num >= 1 && num <= 12) return "dyc.html";
  if (num >= 13 && num <= 38) return "greedy.html";
  if (num >= 39 && num <= 52) return "backtracking.html";
  if (num >= 53 && num <= 59) return "dp.html";
  if (num >= 60 && num <= 65) return "pl.html";
  if (num >= 66 && num <= 70) return "flujo.html";
  if (num >= 71 && num <= 74) return "reducciones.html";
  if (num >= 75 && num <= 79) return "integradores.html";
  if (num >= 80 && num <= 83) return "tipo_parcial.html";
  return "index.html";
}

// Initialization on DOM ready
document.addEventListener("DOMContentLoaded", async () => {
  loadSavedState();
  updateModeUI();
  updateDifficultyUI();
  updateDarkModeButtonIcon();

  if (document.getElementById("entrenador-30s")) {
    initTrainer();
  }

  // Abrir temporalmente todos los drawers para que Mermaid calcule la geometría real
  const drawers = document.querySelectorAll(".exercise-solution-drawer");
  drawers.forEach(drawer => {
    drawer.open = true;
  });

  if (typeof initMermaidDiagrams === "function") {
    await initMermaidDiagrams();
  }
  initMathRendering();

  // Colapsar soluciones por defecto para incentivar el Active Recall
  drawers.forEach(drawer => {
    drawer.open = false;
  });

  // Aplicar filtros después del renderizado para evitar que tarjetas en display:none rompan los SVGs
  applyFilters();

  // Navegación automática por hash (#ej-XX o #entrenador-30s)
  handleInitialHashNavigation();
});

function handleInitialHashNavigation() {
  const hash = window.location.hash;
  if (!hash) return;
  const ejMatch = hash.match(/^#ej-(\d+)$/);
  if (ejMatch) {
    const ejNum = parseInt(ejMatch[1], 10);
    setTimeout(() => scrollToExercise(ejNum), 120);
  } else if (hash === "#entrenador-30s") {
    setTimeout(() => scrollToTrainer(), 120);
  }
}

function initMathRendering() {
  if (typeof renderMathInElement === "function") {
    renderMathInElement(document.body, {
      delimiters: [
        { left: "$$", right: "$$", display: true },
        { left: "$", right: "$", display: false }
      ],
      ignoredClasses: ["mermaid", "mermaid-wrapper", "code-container", "copy-code-btn"],
      ignoredTags: ["script", "noscript", "style", "textarea", "pre", "code", "svg"],
      throwOnError: false
    });
  }
}

async function initMermaidDiagrams() {
  if (typeof mermaid === "undefined") return;
  const isDark = document.body.classList.contains("dark-mode");

  // Preservar el código fuente original de cada diagrama Mermaid para poder re-renderizar al cambiar tema
  document.querySelectorAll(".mermaid").forEach(el => {
    if (!el.getAttribute("data-mermaid-src")) {
      el.setAttribute("data-mermaid-src", el.textContent.trim());
    } else {
      el.removeAttribute("data-processed");
      el.textContent = el.getAttribute("data-mermaid-src");
    }
  });

  mermaid.initialize({
    startOnLoad: false,
    theme: isDark ? "dark" : "neutral",
    securityLevel: "loose",
    themeVariables: {
      fontFamily: '-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif'
    }
  });
  try {
    await mermaid.run({ querySelector: ".mermaid" });
  } catch (e) {
    console.warn("Mermaid render notice:", e);
  }
}

// Al imprimir desde el navegador (Ctrl+P), expandir todas las soluciones
window.addEventListener("beforeprint", () => {
  document.querySelectorAll(".exercise-solution-drawer").forEach(drawer => {
    drawer.open = true;
  });
});

window.addEventListener("afterprint", () => {
  if (!solutionsExpanded) {
    document.querySelectorAll(".exercise-solution-drawer").forEach(drawer => {
      drawer.open = false;
    });
  }
});

function loadSavedState() {
  try {
    const savedMastered = localStorage.getItem("tda_mastered_exercises");
    if (savedMastered) {
      masteredExercises = new Set(JSON.parse(savedMastered));
    }
    const savedChecklist = localStorage.getItem("tda_exam_checklist");
    if (savedChecklist) {
      checklistState = JSON.parse(savedChecklist);
    }
    const savedTheme = localStorage.getItem("tda_theme");
    if (savedTheme === "dark") {
      document.body.classList.add("dark-mode");
    }
    const savedMode = localStorage.getItem("tda_study_mode");
    if (savedMode && ["emergency", "tactical", "all"].includes(savedMode)) {
      currentMode = savedMode;
    }
  } catch (e) {
    console.error("Error reading localStorage", e);
  }

  // Restore checkboxes in exercise cards
  document.querySelectorAll(".mastered-checkbox").forEach(cb => {
    const num = parseInt(cb.getAttribute("data-ej-num"), 10);
    if (masteredExercises.has(num)) {
      cb.checked = true;
      const card = document.getElementById("ej-" + num);
      if (card) card.classList.add("is-mastered");
    }
  });

  // Restore checklist inputs
  document.querySelectorAll(".exam-checklist-input").forEach(inp => {
    const id = inp.getAttribute("data-chk-id");
    if (checklistState[id]) {
      inp.checked = true;
    }
  });
}

function saveState() {
  try {
    localStorage.setItem("tda_mastered_exercises", JSON.stringify(Array.from(masteredExercises)));
    localStorage.setItem("tda_exam_checklist", JSON.stringify(checklistState));
    localStorage.setItem("tda_study_mode", currentMode);
  } catch (e) {
    console.error("Error saving state", e);
  }
}

// Mastered exercise toggle
function toggleMastered(num, isMastered) {
  if (isMastered) {
    masteredExercises.add(num);
  } else {
    masteredExercises.delete(num);
  }
  const card = document.getElementById("ej-" + num);
  if (card) {
    if (isMastered) card.classList.add("is-mastered");
    else card.classList.remove("is-mastered");
  }
  saveState();
  applyFilters();
}

// Checklist item toggle
function toggleChecklistItem(id, isChecked) {
  checklistState[id] = isChecked;
  saveState();
}

// Filter and View Logic
function setStudyMode(mode) {
  currentMode = mode;
  saveState();
  updateModeUI();
  applyFilters();
}

function updateModeUI() {
  const btnEmergency = document.getElementById("btnModeEmergency");
  const btnTactical = document.getElementById("btnModeTactical");
  const btnAll = document.getElementById("btnModeAll");
  if (btnEmergency) btnEmergency.classList.toggle("active", currentMode === "emergency");
  if (btnTactical) btnTactical.classList.toggle("active", currentMode === "tactical");
  if (btnAll) btnAll.classList.toggle("active", currentMode === "all");

  const banner = document.getElementById("emergencyBanner");
  if (banner) {
    banner.style.display = currentMode === "emergency" ? "block" : "none";
  }
}

function filterByParadigm(paradigm) {
  currentParadigm = paradigm;
  document.querySelectorAll("#paradigmPills .pill-btn").forEach(btn => {
    btn.classList.toggle("active", btn.getAttribute("data-paradigm") === paradigm);
  });
  applyFilters();
}

function setDifficultyFilter(diff) {
  currentDifficulty = String(diff);
  updateDifficultyUI();
  applyFilters();
}

function filterByDifficulty(diff) {
  setDifficultyFilter(diff);
}

function updateDifficultyUI() {
  document.querySelectorAll(".diff-btn").forEach(btn => {
    const btnDiff = btn.getAttribute("data-difficulty") || btn.getAttribute("data-diff");
    if (btnDiff !== null && btnDiff !== undefined) {
      btn.classList.toggle("active", String(btnDiff) === String(currentDifficulty));
    } else {
      const onclickAttr = btn.getAttribute("onclick") || "";
      const isMatch =
        onclickAttr.includes("'" + currentDifficulty + "'") ||
        onclickAttr.includes('"' + currentDifficulty + '"') ||
        onclickAttr.includes("(" + currentDifficulty + ")");
      btn.classList.toggle("active", isMatch);
    }
  });
}

function handleSearch(val) {
  searchQuery = val.trim().toLowerCase();
  const clearBtn = document.getElementById("clearSearchBtn");
  if (clearBtn) clearBtn.style.display = searchQuery ? "block" : "none";
  applyFilters();
}

function clearSearch() {
  const searchInput = document.getElementById("exerciseSearch");
  if (searchInput) searchInput.value = "";
  searchQuery = "";
  const clearBtn = document.getElementById("clearSearchBtn");
  if (clearBtn) clearBtn.style.display = "none";
  applyFilters();
}

function resetAllFilters() {
  currentMode = "all";
  currentParadigm = "all";
  currentDifficulty = "all";
  searchQuery = "";
  const searchInput = document.getElementById("exerciseSearch");
  if (searchInput) searchInput.value = "";
  const clearBtn = document.getElementById("clearSearchBtn");
  if (clearBtn) clearBtn.style.display = "none";
  saveState();
  updateModeUI();
  updateDifficultyUI();
  applyFilters();
}

function dismissBanner() {
  const banner = document.getElementById("emergencyBanner");
  if (banner) banner.style.display = "none";
}

function applyFilters() {
  const cards = document.querySelectorAll(".exercise-card");
  let visibleCount = 0;
  let masteredCount = 0;
  let totalEmergencyOnPage = 0;
  let totalTacticalOnPage = 0;
  const totalCardsOnPage = cards.length;

  cards.forEach(card => {
    const num = parseInt(card.getAttribute("data-num"), 10);
    const priority = card.getAttribute("data-priority");
    const paradigm = card.getAttribute("data-paradigm");
    const difficulty = card.getAttribute("data-difficulty") || "";
    const title = card.getAttribute("data-title") || "";
    const origin = card.getAttribute("data-origin") || "";
    const cardText = card.textContent.toLowerCase();
    const isMastered = masteredExercises.has(num);

    if (priority === "imprescindible") {
      totalEmergencyOnPage++;
    }
    if (!isMastered || priority === "importante") {
      totalTacticalOnPage++;
    }

    // Mode filter:
    // - emergency: solo ejercicios 🔴 IMPRESCINDIBLE
    // - tactical: ejercicios pendientes de dominar (!isMastered) o 🟡 IMPORTANTE
    // - all: todos los ejercicios de la vista actual
    let matchesMode = true;
    if (currentMode === "emergency") {
      matchesMode = (priority === "imprescindible");
    } else if (currentMode === "tactical") {
      matchesMode = (!isMastered || priority === "importante");
    }

    // Paradigm filter
    let matchesParadigm = true;
    if (currentParadigm !== "all") {
      matchesParadigm = (paradigm === currentParadigm);
    }

    // Difficulty filter (1 a 5)
    let matchesDifficulty = true;
    if (currentDifficulty !== "all") {
      matchesDifficulty = (difficulty === String(currentDifficulty));
    }

    // Search query filter
    let matchesSearch = true;
    if (searchQuery) {
      matchesSearch =
        title.includes(searchQuery) ||
        origin.includes(searchQuery) ||
        cardText.includes(searchQuery) ||
        ("ej " + num) === searchQuery ||
        ("ejercicio " + num) === searchQuery;
    }

    const isVisible = matchesMode && matchesParadigm && matchesDifficulty && matchesSearch;
    card.classList.toggle("is-hidden", !isVisible);

    if (isVisible) {
      visibleCount++;
      if (isMastered) {
        masteredCount++;
      }
    }
  });

  // Actualizar visibilidad de encabezados h2 y subsecciones h3 ("Patrón...", etc.) cuando se filtra
  updateSectionHeadingsVisibility();

  // Actualizar contadores dinámicos de las píldoras de modo según la página actual
  const badgeEmergency = document.getElementById("badgeEmergencyCount");
  const badgeTactical = document.getElementById("badgeTacticalCount");
  const badgeAll = document.getElementById("badgeAllCount");
  const bannerCount = document.getElementById("emergencyBannerCount");

  if (badgeEmergency) badgeEmergency.textContent = totalEmergencyOnPage;
  if (badgeTactical) badgeTactical.textContent = totalTacticalOnPage;
  if (badgeAll) badgeAll.textContent = totalCardsOnPage;
  if (bannerCount) bannerCount.textContent = totalEmergencyOnPage;

  const emptyState = document.getElementById("searchEmptyState");
  if (emptyState) {
    emptyState.style.display = (totalCardsOnPage > 0 && visibleCount === 0) ? "block" : "none";
  }

  updateProgressHUD(visibleCount, masteredCount);
}

function updateSectionHeadingsVisibility() {
  const mainEl = document.querySelector(".main-content-wrapper");
  if (!mainEl) return;

  const isAnyFilterActive =
    currentMode !== "all" ||
    currentParadigm !== "all" ||
    currentDifficulty !== "all" ||
    searchQuery !== "";

  if (!isAnyFilterActive) {
    mainEl.querySelectorAll(".is-hidden-section").forEach(el => {
      el.classList.remove("is-hidden-section");
    });
    return;
  }

  // Evaluar cada bloque H2 que contenga tarjetas de ejercicio
  const h2Elements = Array.from(mainEl.querySelectorAll("h2"));
  h2Elements.forEach(h2 => {
    let sibling = h2.nextElementSibling;
    const sectionCards = [];
    const synthesisElements = [];
    let inSynthesisBlock = false;

    while (sibling && sibling.tagName !== "H2") {
      if (sibling.classList && sibling.classList.contains("exercise-card")) {
        sectionCards.push(sibling);
        inSynthesisBlock = false;
      } else if (sibling.tagName === "H3") {
        const h3Text = sibling.textContent.trim();
        if (
          h3Text.startsWith("Patrón") ||
          h3Text.startsWith("Errores Frecuentes") ||
          h3Text.startsWith("Errores Fatales")
        ) {
          inSynthesisBlock = true;
          synthesisElements.push(sibling);
        } else {
          inSynthesisBlock = false;
        }
      } else if (inSynthesisBlock && sibling.id !== "searchEmptyState" && sibling.id !== "entrenador-30s") {
        synthesisElements.push(sibling);
      }
      sibling = sibling.nextElementSibling;
    }

    if (sectionCards.length > 0) {
      const hasVisibleCards = sectionCards.some(c => !c.classList.contains("is-hidden"));
      h2.classList.toggle("is-hidden-section", !hasVisibleCards);
      synthesisElements.forEach(el => {
        el.classList.toggle("is-hidden-section", !hasVisibleCards);
      });
    }
  });

  // Evaluar sub-encabezados H3 que agrupan tarjetas de ejercicio (ej. 5.1, 5.2...)
  const h3Elements = Array.from(mainEl.querySelectorAll("h3"));
  h3Elements.forEach(h3 => {
    if (h3.closest(".exercise-card") || h3.closest(".trainer-box") || h3.closest(".search-empty-state")) {
      return;
    }
    const h3Text = h3.textContent.trim();
    if (
      h3Text.startsWith("Patrón") ||
      h3Text.startsWith("Errores Frecuentes") ||
      h3Text.startsWith("Errores Fatales")
    ) {
      return;
    }

    let sibling = h3.nextElementSibling;
    const subCards = [];
    while (sibling && sibling.tagName !== "H2" && sibling.tagName !== "H3") {
      if (sibling.classList && sibling.classList.contains("exercise-card")) {
        subCards.push(sibling);
      }
      sibling = sibling.nextElementSibling;
    }

    if (subCards.length > 0) {
      const hasVisibleSub = subCards.some(c => !c.classList.contains("is-hidden"));
      h3.classList.toggle("is-hidden-section", !hasVisibleSub);
    }
  });
}

function updateProgressHUD(totalVisible, totalMastered) {
  if (totalVisible === undefined) {
    const cards = document.querySelectorAll(".exercise-card:not(.is-hidden)");
    totalVisible = cards.length;
    totalMastered = 0;
    cards.forEach(c => {
      const num = parseInt(c.getAttribute("data-num"), 10);
      if (masteredExercises.has(num)) totalMastered++;
    });
  }

  const progMastered = document.getElementById("progMastered");
  const progTotal = document.getElementById("progTotal");
  const progPercent = document.getElementById("progPercent");
  const progressFill = document.getElementById("progressFill");

  if (progMastered && progTotal && progPercent && progressFill) {
    progMastered.textContent = totalMastered;
    progTotal.textContent = totalVisible;
    const pct = totalVisible > 0 ? Math.round((totalMastered / totalVisible) * 100) : 0;
    progPercent.textContent = pct + "%";
    progressFill.style.width = pct + "%";
  }
}

// Active recall solution controls
function toggleCardSolution(num) {
  const drawer = document.getElementById("solution-drawer-" + num);
  if (drawer) {
    drawer.open = !drawer.open;
  }
}

function scrollToExercise(num) {
  const card = document.getElementById("ej-" + num);
  if (!card) {
    // Si estamos en una subpágina modular donde no existe el ejercicio, redirigir a la página correspondiente
    const targetPage = getPageForExercise(num);
    window.location.href = targetPage + "#ej-" + num;
    return;
  }

  // Asegurar que se muestre el ejercicio independientemente del filtro activo
  currentMode = 'all';
  currentParadigm = 'all';
  currentDifficulty = 'all';
  searchQuery = '';
  const searchInput = document.getElementById("exerciseSearch");
  if (searchInput) searchInput.value = "";
  const clearBtn = document.getElementById("clearSearchBtn");
  if (clearBtn) clearBtn.style.display = "none";

  saveState();
  updateModeUI();
  updateDifficultyUI();
  applyFilters();

  const drawer = document.getElementById("solution-drawer-" + num);
  if (drawer) drawer.open = true;

  // Desplazamiento suave con compensación por el HUD fijo
  const rect = card.getBoundingClientRect();
  const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
  const hudHeight = document.getElementById("hudTopBar") ? document.getElementById("hudTopBar").offsetHeight : 140;
  const targetY = rect.top + scrollTop - hudHeight - 16;

  window.scrollTo({ top: targetY, behavior: 'smooth' });

  card.style.transition = 'box-shadow 0.4s ease, border-color 0.4s ease';
  card.style.borderColor = 'var(--accent-color)';
  card.style.boxShadow = '0 0 0 4px rgba(49, 130, 206, 0.4)';
  setTimeout(() => {
    card.style.borderColor = '';
    card.style.boxShadow = '';
  }, 2800);
}

function toggleGlobalSolutions() {
  solutionsExpanded = !solutionsExpanded;
  document.querySelectorAll(".exercise-solution-drawer").forEach(drawer => {
    drawer.open = solutionsExpanded;
  });
  const lbl = document.getElementById("lblGlobalSolutions");
  if (lbl) {
    lbl.textContent = solutionsExpanded ? "Ocultar Soluciones" : "Soluciones";
  }
}

// Cheatsheet drawer
function openCheatsheet() {
  const drawer = document.getElementById("cheatsheetDrawer");
  const backdrop = document.getElementById("drawerBackdrop");
  if (drawer) {
    drawer.classList.add("is-open");
    drawer.setAttribute("aria-hidden", "false");
  }
  if (backdrop) backdrop.classList.add("is-open");
}

function closeCheatsheet() {
  const drawer = document.getElementById("cheatsheetDrawer");
  const backdrop = document.getElementById("drawerBackdrop");
  if (drawer) {
    drawer.classList.remove("is-open");
    drawer.setAttribute("aria-hidden", "true");
  }
  if (backdrop) backdrop.classList.remove("is-open");
}

function updateDarkModeButtonIcon() {
  const iconEl = document.getElementById("darkModeIcon");
  if (iconEl) {
    const isDark = document.body.classList.contains("dark-mode");
    iconEl.textContent = isDark ? "☀️" : "🌙";
  }
}

// Theme
async function toggleDarkMode() {
  const isDark = document.body.classList.toggle("dark-mode");
  updateDarkModeButtonIcon();
  try {
    localStorage.setItem("tda_theme", isDark ? "dark" : "light");
  } catch (e) {}
  if (typeof initMermaidDiagrams === "function") {
    await initMermaidDiagrams();
  }
}

// Copy Code Block
function copyCodeBlock(btn) {
  const pre = btn.nextElementSibling;
  if (!pre) return;
  const text = pre.textContent;
  navigator.clipboard.writeText(text).then(() => {
    const original = btn.textContent;
    btn.textContent = "¡Copiado! ✓";
    btn.style.background = "#38a169";
    btn.style.color = "#ffffff";
    setTimeout(() => {
      btn.textContent = original;
      btn.style.background = "";
      btn.style.color = "";
    }, 1800);
  });
}

// Trainer 30s logic
function initTrainer() {
  trainerIndex = 0;
  trainerScore = 0;
  trainerAnswered = false;
  const totalEl = document.getElementById("trainerTotalQuestions");
  if (totalEl) totalEl.textContent = TRAINER_QUESTIONS.length;
  const scoreEl = document.getElementById("trainerScore");
  if (scoreEl) scoreEl.textContent = "0";
  const answeredEl = document.getElementById("trainerTotal");
  if (answeredEl) answeredEl.textContent = "0";
  loadTrainerQuestion();
}

function loadTrainerQuestion() {
  const promptEl = document.getElementById("trainerPrompt");
  if (!promptEl) return;
  trainerAnswered = false;
  const q = TRAINER_QUESTIONS[trainerIndex];

  const idxEl = document.getElementById("trainerCurrentIndex");
  if (idxEl) idxEl.textContent = trainerIndex + 1;
  promptEl.textContent = q.prompt;

  const fbEl = document.getElementById("trainerFeedback");
  if (fbEl) fbEl.style.display = "none";
  const nextBtn = document.getElementById("trainerNextBtn");
  if (nextBtn) nextBtn.style.display = "none";

  const buttons = document.querySelectorAll("#trainerOptions .trainer-btn");
  buttons.forEach(btn => {
    btn.disabled = false;
    btn.classList.remove("btn-correct", "btn-wrong");
  });
}

function checkTrainerAnswer(selected) {
  if (trainerAnswered) return;
  trainerAnswered = true;

  const q = TRAINER_QUESTIONS[trainerIndex];
  const isCorrect = (selected === q.answer);

  if (isCorrect) {
    trainerScore++;
  }

  document.getElementById("trainerScore").textContent = trainerScore;
  document.getElementById("trainerTotal").textContent = trainerIndex + 1;

  const buttons = document.querySelectorAll("#trainerOptions .trainer-btn");
  buttons.forEach(btn => {
    btn.disabled = true;
    const btnClickAttr = btn.getAttribute("onclick") || "";
    if (btnClickAttr.includes("'" + q.answer + "'")) {
      btn.classList.add("btn-correct");
    } else if (btnClickAttr.includes("'" + selected + "'") && !isCorrect) {
      btn.classList.add("btn-wrong");
    }
  });

  const feedback = document.getElementById("trainerFeedback");
  const result = document.getElementById("feedbackResult");
  const trigger = document.getElementById("feedbackTrigger");

  feedback.style.display = "block";
  feedback.className = "trainer-feedback " + (isCorrect ? "feedback-success" : "feedback-error");

  result.textContent = isCorrect
    ? "¡Excelente! Respuesta correcta 🎉 (" + q.paradigmName + ")"
    : "No es la técnica ideal. El paradigma correcto es: " + q.paradigmName;

  trigger.innerHTML = "<strong>Disparador Léxico de Examen:</strong> " + q.trigger;

  const nextBtn = document.getElementById("trainerNextBtn");
  if (trainerIndex < TRAINER_QUESTIONS.length - 1) {
    nextBtn.style.display = "inline-block";
    nextBtn.textContent = "Siguiente Enunciado (" + (trainerIndex + 2) + "/" + TRAINER_QUESTIONS.length + ") ➔";
  } else {
    nextBtn.style.display = "inline-block";
    nextBtn.textContent = "Ver Diagnóstico Final 🏁";
  }
}

function nextTrainerQuestion() {
  if (trainerIndex < TRAINER_QUESTIONS.length - 1) {
    trainerIndex++;
    loadTrainerQuestion();
  } else {
    const pct = Math.round((trainerScore / TRAINER_QUESTIONS.length) * 100);
    const feedback = document.getElementById("trainerFeedback");
    const result = document.getElementById("feedbackResult");
    const trigger = document.getElementById("feedbackTrigger");
    const nextBtn = document.getElementById("trainerNextBtn");

    if (feedback && result && trigger) {
      feedback.style.display = "block";
      feedback.className = "trainer-feedback " + (pct >= 75 ? "feedback-success" : "feedback-error");
      result.textContent = "🏁 Simulación completada: " + trainerScore + " de " + TRAINER_QUESTIONS.length + " aciertos (" + pct + "%)";
      trigger.innerHTML = pct >= 75
        ? "<strong>Diagnóstico:</strong> ¡Excelente velocidad de reconocimiento! Estás listo para identificar los paradigmas del parcial sin dudar."
        : "<strong>Diagnóstico:</strong> Repasá el Árbol de Decisión Rápido y la Tabla de Disparadores Léxicos y volvé a intentar el simulador.";
    }
    if (nextBtn) {
      nextBtn.style.display = "none";
    }
  }
}

function resetTrainer() {
  initTrainer();
}

function scrollToTrainer() {
  const trainer = document.getElementById("entrenador-30s");
  if (trainer) {
    const rect = trainer.getBoundingClientRect();
    const scrollTop = window.pageYOffset || document.documentElement.scrollTop;
    const hudHeight = document.getElementById("hudTopBar") ? document.getElementById("hudTopBar").offsetHeight : 140;
    window.scrollTo({ top: rect.top + scrollTop - hudHeight - 16, behavior: "smooth" });
  } else {
    window.location.href = "index.html#entrenador-30s";
  }
}

function scrollToTop() {
  window.scrollTo({ top: 0, behavior: "smooth" });
}

// Keyboard shortcuts: Escape closes drawer, '/' or Ctrl+K focuses search
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    closeCheatsheet();
  } else if ((e.key === "/" || (e.ctrlKey && e.key.toLowerCase() === "k")) && !["INPUT", "TEXTAREA"].includes(document.activeElement.tagName)) {
    const searchInput = document.getElementById("exerciseSearch");
    if (searchInput) {
      e.preventDefault();
      searchInput.focus();
      searchInput.select();
    }
  }
});
