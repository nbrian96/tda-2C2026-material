"""Generador de HTML interactivo y optimizado para estudio intensivo de TDA."""

import re
import html
import markdown

PARADIGMS = {
    1: ("dyc", "División y Conquista", "badge-dyc"),
    2: ("dyc", "División y Conquista", "badge-dyc"),
    3: ("dyc", "División y Conquista", "badge-dyc"),
    4: ("greedy", "Greedy / Voraz", "badge-greedy"),
    5: ("greedy", "Greedy / Voraz", "badge-greedy"),
    6: ("greedy", "Greedy / Voraz", "badge-greedy"),
    7: ("greedy", "Greedy / Voraz", "badge-greedy"),
    8: ("greedy", "Greedy / Voraz", "badge-greedy"),
    9: ("backtracking", "Backtracking", "badge-backtracking"),
    10: ("backtracking", "Backtracking", "badge-backtracking"),
    11: ("backtracking", "Backtracking", "badge-backtracking"),
    12: ("backtracking", "Backtracking", "badge-backtracking"),
    13: ("dp", "Prog. Dinámica", "badge-dp"),
    14: ("dp", "Prog. Dinámica", "badge-dp"),
    15: ("dp", "Prog. Dinámica", "badge-dp"),
    16: ("dp", "Prog. Dinámica", "badge-dp"),
    17: ("dp", "Prog. Dinámica", "badge-dp"),
    18: ("dp", "Prog. Dinámica", "badge-dp"),
    19: ("pl", "Prog. Lineal", "badge-pl"),
    20: ("pl", "Prog. Lineal", "badge-pl"),
    21: ("pl", "Prog. Lineal", "badge-pl"),
    22: ("pl", "Prog. Lineal", "badge-pl"),
    23: ("pl", "Prog. Lineal", "badge-pl"),
    24: ("flujo", "Redes de Flujo", "badge-flujo"),
    25: ("flujo", "Redes de Flujo", "badge-flujo"),
    26: ("flujo", "Redes de Flujo", "badge-flujo"),
    27: ("flujo", "Redes de Flujo", "badge-flujo"),
    28: ("reducciones", "Reducciones NP", "badge-reducciones"),
    29: ("reducciones", "Reducciones NP", "badge-reducciones"),
    30: ("reducciones", "Reducciones NP", "badge-reducciones"),
    31: ("reducciones", "Reducciones NP", "badge-reducciones"),
    32: ("integradores", "Integrador", "badge-integrador"),
    33: ("integradores", "Integrador", "badge-integrador"),
    34: ("integradores", "Integrador", "badge-integrador"),
    35: ("integradores", "Multi-Paradigma", "badge-integrador"),
    36: ("integradores", "Multi-Paradigma", "badge-integrador"),
    37: ("tipo_parcial", "Tipo Parcial", "badge-tipo-parcial"),
    38: ("tipo_parcial", "Tipo Parcial", "badge-tipo-parcial"),
    39: ("tipo_parcial", "Tipo Parcial", "badge-tipo-parcial"),
    40: ("tipo_parcial", "Tipo Parcial", "badge-tipo-parcial")
}

SOLUTION_MARKERS = [
    r"<h4>1\.\s*Deducción Metodológica",
    r"<h4>2\.\s+",
    r"<p><strong>Resolución y Comparativa",
    r"<p><strong>Pseudocódigo del Algoritmo",
    r"<h4>1\.\s*(?:Resolución|Paradigma)",
    r"<p><strong>Idea de resolución",
    r"<p><strong>Pseudocódigo",
    r"<p><strong>Modelo Matemático",
    r"<p><strong>Resolución",
    r"<p><strong>Respuesta y Demostración",
    r"<p><strong>Demostración Paso a Paso",
    r"<p><strong>Demostración Formal",
    r"<p><strong>Explicación del modelo",
    r"<p><strong>Demostración de Optimalidad"
]

CODE_BLOCK_PATTERN = r"(<pre><code(?:\s+class=\"([^\"]*)\")?>)(.*?)(</code></pre>)"

def replace_code_block_match(match):
    code_tag_start = match.group(1)
    code_class = match.group(2) or ""
    code_content = match.group(3)
    code_tag_end = match.group(4)
    if "mermaid" in code_class:
        clean_content = html.unescape(code_content)
        return (
            f'<div class="mermaid-wrapper">'
            f'<pre class="mermaid">{clean_content}</pre>'
            f'</div>'
        )
    return (
        f'<div class="code-container">'
        f'<button class="copy-code-btn" type="button" title="Copiar código al portapapeles" onclick="copyCodeBlock(this)">📋 Copiar</button>'
        f'{code_tag_start}{code_content}{code_tag_end}'
        f'</div>'
    )

def format_exercise_card(num, title, body_html):
    paradigm_key, paradigm_name, paradigm_class = PARADIGMS.get(num, ("otro", "General", "badge-otro"))
    
    is_imprescindible = "🔴 IMPRESCINDIBLE" in body_html
    priority_slug = "imprescindible" if is_imprescindible else "importante"
    priority_label = "🔴 IMPRESCINDIBLE" if is_imprescindible else "🟡 IMPORTANTE"
    priority_class = "badge-priority-imprescindible" if is_imprescindible else "badge-priority-importante"
    
    origin_match = re.search(r"<strong>Origen:</strong>\s*(.*?)(</p>|<br\s*/?>|\n)", body_html, re.DOTALL)
    origin_text = origin_match.group(1).strip() if origin_match else "Parcial / Práctica FIUBA"
    
    clean_body = re.sub(r"<p><strong>Clasificación:</strong>.*?</p>", "", body_html, flags=re.DOTALL)
    
    split_pos = None
    for sm in SOLUTION_MARKERS:
        m = re.search(sm, clean_body)
        if m:
            if split_pos is None or m.start() < split_pos:
                split_pos = m.start()
                
    if split_pos is not None:
        statement_html = clean_body[:split_pos].strip()
        solution_html = clean_body[split_pos:].strip()
    else:
        statement_html = clean_body
        solution_html = ""
        
    if statement_html:
        statement_html = re.sub(CODE_BLOCK_PATTERN, replace_code_block_match, statement_html, flags=re.DOTALL)

    if solution_html:
        solution_html = re.sub(CODE_BLOCK_PATTERN, replace_code_block_match, solution_html, flags=re.DOTALL)
        
        trap_pattern = r"(<p><strong>(?:Trampas habituales de corrección|Puntos donde puedo equivocarme).*?</strong>.*?</p>(?:\s*<ul>.*?</ul>)?)"
        def replace_trap(m):
            return f'<div class="trap-callout"><div class="trap-header">⚠️ Trampa Típica de Corrección</div>{m.group(1)}</div>'
        solution_html = re.sub(trap_pattern, replace_trap, solution_html, flags=re.DOTALL)
        
    card_html = f"""
<article class="exercise-card" id="ej-{num}" data-num="{num}" data-priority="{priority_slug}" data-paradigm="{paradigm_key}" data-title="{html.escape(title.lower())}" data-origin="{html.escape(origin_text.lower())}">
  <header class="card-header">
    <div class="card-header-left">
      <span class="exercise-pill-number">EJ {num}</span>
      <h3 class="exercise-title">{title}</h3>
    </div>
    <div class="card-header-meta">
      <span class="badge badge-priority {priority_class}">{priority_label}</span>
      <span class="badge badge-paradigm {paradigm_class}">{paradigm_name}</span>
      <span class="badge badge-origin" title="{html.escape(origin_text)}">🏛️ {origin_text.split('/')[0].strip()}</span>
    </div>
    <div class="card-header-actions">
      <label class="mastered-label" title="Marcar como dominado (se guarda automáticamente)">
        <input type="checkbox" class="mastered-checkbox" data-ej-num="{num}" onchange="toggleMastered({num}, this.checked)">
        <span class="checkbox-custom"></span>
        <span class="label-text">Dominado</span>
      </label>
    </div>
  </header>

  <div class="card-body">
    <div class="exercise-statement-box">
      {statement_html}
    </div>

    <details class="exercise-solution-drawer" id="solution-drawer-{num}">
      <summary class="solution-summary">
        <span class="summary-toggle-icon">▶</span>
        <span class="summary-title">💡 Solución Completa, Pseudocódigo y Análisis Formal</span>
        <span class="summary-badge">Active Recall</span>
      </summary>
      <div class="solution-inner-content">
        {solution_html}
      </div>
    </details>
  </div>
</article>
"""
    return card_html

def process_html_exercises(html_body):
    parts = re.split(r"(<h3>Ejercicio \d+ [^<]+</h3>)", html_body)
    new_parts = [parts[0]]
    
    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i+1]
        
        num_m = re.search(r"Ejercicio (\d+) — (.*?)</h3>", header)
        if not num_m:
            new_parts.append(header)
            new_parts.append(body)
            continue
            
        num = int(num_m.group(1))
        title = num_m.group(2).strip()
        
        split_m = re.search(r"(?:<hr\s*/?>\s*)?(?:<h3>(?:Patrón de Ejercicio|Errores Frecuentes|Errores Fatales)|<h2>)", body)
        if split_m:
            ex_body = body[:split_m.start()]
            trailing = body[split_m.start():]
        else:
            ex_body = body
            trailing = ""
            
        card_html = format_exercise_card(num, title, ex_body)
        new_parts.append(card_html)
        if trailing:
            new_parts.append(trailing)
            
    return "".join(new_parts)

def inject_interactive_widgets(html_body):
    # Transformar cualquier bloque Mermaid o de código fuera de las tarjetas de ejercicios (ej. Árbol de Decisión en Sección 3)
    html_body = re.sub(CODE_BLOCK_PATTERN, replace_code_block_match, html_body, flags=re.DOTALL)

    trainer_html = """
<div class="trainer-box" id="entrenador-30s">
  <div class="trainer-header">
    <div class="trainer-title-wrap">
      <span class="trainer-badge-icon">⚡</span>
      <div>
        <h3 class="trainer-title">Entrenador Interactivo: Reconocimiento en 30 Segundos</h3>
        <p class="trainer-subtitle">Entrená la habilidad más crítica del parcial: identificar el paradigma exacto sin dudar.</p>
      </div>
    </div>
    <div class="trainer-stats">
      <span class="stat-pill">Aciertos: <strong id="trainerScore">0</strong> / <strong id="trainerTotal">0</strong></span>
    </div>
  </div>

  <div class="trainer-card">
    <div class="trainer-card-header">
      <span class="trainer-counter">Caso <span id="trainerCurrentIndex">1</span> de <span id="trainerTotalQuestions">16</span></span>
      <span class="trainer-timer-tag">⏱️ Meta: &lt; 30 segundos</span>
    </div>
    <div class="trainer-prompt" id="trainerPrompt">Cargando enunciado de examen...</div>

    <div class="trainer-options-grid" id="trainerOptions">
      <button class="trainer-btn" onclick="checkTrainerAnswer('dyc')">🔷 División y Conquista</button>
      <button class="trainer-btn" onclick="checkTrainerAnswer('greedy')">🔶 Greedy (Voraz)</button>
      <button class="trainer-btn" onclick="checkTrainerAnswer('backtracking')">🟣 Backtracking & B&B</button>
      <button class="trainer-btn" onclick="checkTrainerAnswer('dp')">🟢 Programación Dinámica</button>
      <button class="trainer-btn" onclick="checkTrainerAnswer('pl')">🔵 Programación Lineal (PLI)</button>
      <button class="trainer-btn" onclick="checkTrainerAnswer('flujo')">🔴 Redes de Flujo</button>
      <button class="trainer-btn" onclick="checkTrainerAnswer('reducciones')">🟡 Reducciones NP-C</button>
    </div>

    <div class="trainer-feedback" id="trainerFeedback" style="display: none;">
      <div class="feedback-result" id="feedbackResult"></div>
      <div class="feedback-trigger" id="feedbackTrigger"></div>
    </div>

    <div class="trainer-actions">
      <button class="btn btn-primary" id="trainerNextBtn" style="display: none;" onclick="nextTrainerQuestion()">Siguiente Enunciado ➔</button>
      <button class="btn btn-ghost" onclick="resetTrainer()">Reiniciar Simulador</button>
    </div>
  </div>
</div>
"""
    
    target_pos = html_body.find("### Árbol de Decisión Rápido")
    if target_pos == -1:
        target_pos = html_body.find("<h3>Árbol de Decisión Rápido</h3>")
        
    if target_pos != -1:
        end_of_tree = html_body.find("<h3>Tabla de Señales y Disparadores Léxicos</h3>", target_pos)
        if end_of_tree != -1:
            html_body = html_body[:end_of_tree] + trainer_html + html_body[end_of_tree:]
        else:
            html_body = html_body[:target_pos] + trainer_html + html_body[target_pos:]
    else:
        intro_pos = html_body.find("<h2>3. Guía Mental:")
        if intro_pos != -1:
            html_body = html_body[:intro_pos] + trainer_html + html_body[intro_pos:]

    def make_checkbox(m):
        raw_text = m.group(1)
        check_id = "chk_" + str(abs(hash(raw_text)) % 100000)
        return (
            f'<li class="checklist-interactive-item">'
            f'<label class="chk-label">'
            f'<input type="checkbox" class="exam-checklist-input" data-chk-id="{check_id}" onchange="toggleChecklistItem(\'{check_id}\', this.checked)">'
            f'<span class="chk-custom"></span>'
            f'<span class="chk-text">{raw_text}</span>'
            f'</label>'
            f'</li>'
        )
    html_body = re.sub(r"<li>\[ \]\s*(.*?)</li>", make_checkbox, html_body)

    empty_state_html = """
<div class="search-empty-state" id="searchEmptyState" style="display: none;">
  <div class="empty-state-icon">🔍</div>
  <h3 class="empty-state-title">No se encontraron ejercicios con los filtros actuales</h3>
  <p class="empty-state-desc">Probá con otro término de búsqueda o cambiá al modo <strong>Todos</strong> para visualizar el catálogo completo.</p>
  <button class="btn btn-primary" type="button" onclick="resetAllFilters()">Restablecer filtros y mostrar todos</button>
</div>
"""
    html_body = html_body + empty_state_html

    return html_body

def get_hud_and_drawer_html(active_paradigm="all"):
    pills_config = [
        ("all", "index.html", "📚 Todos (40)"),
        ("dyc", "dyc.html", "🔷 DyC (3)"),
        ("greedy", "greedy.html", "🔶 Greedy (5)"),
        ("backtracking", "backtracking.html", "🟣 Backtracking (4)"),
        ("dp", "dp.html", "🟢 Prog. Dinámica (6)"),
        ("pl", "pl.html", "🔵 Prog. Lineal (5)"),
        ("flujo", "flujo.html", "🔴 Redes de Flujo (4)"),
        ("reducciones", "reducciones.html", "🟡 Reducciones NP (4)"),
        ("integradores", "integradores.html", "⚡ Integradores (5)"),
        ("tipo_parcial", "tipo_parcial.html", "📝 Tipo Parcial (4)")
    ]
    pills_html = []
    for key, href, label in pills_config:
        is_active = (key == active_paradigm)
        active_cls = " active" if is_active else ""
        pills_html.append(f'<a href="{href}" class="pill-btn{active_cls}" data-paradigm="{key}">{label}</a>')
    rendered_pills = "\n        ".join(pills_html)

    html_template = r"""
<!-- Top Sticky HUD -->
<header class="hud-top-bar" id="hudTopBar">
  <div class="hud-container">
    <div class="hud-row-primary">
      <div class="hud-brand">
        <a href="index.html" style="text-decoration: none; color: inherit; display: flex; align-items: center; gap: 8px;">
          <span class="hud-logo-icon">🚀</span>
          <div>
            <h1 class="hud-title">TDA — Guía Interactiva de Parciales</h1>
            <span class="hud-subtitle">Edición Intensiva: Salvando el Cuatrimestre (2024–2025)</span>
          </div>
        </a>
      </div>

      <div class="hud-mode-selector" role="group" aria-label="Modo de Estudio">
        <button class="mode-btn active" id="btnModeEmergency" onclick="setStudyMode('emergency')" title="Mostrar solo los ejercicios 🔴 IMPRESCINDIBLES de examen">
          <span class="mode-icon">⚡</span>
          <span class="mode-label"><span class="mode-label-long">Modo Emergencia (48-72h)</span><span class="mode-label-short">48-72h</span></span>
          <span class="mode-badge" id="badgeEmergencyCount">32</span>
        </button>
        <button class="mode-btn" id="btnModeTactical" onclick="setStudyMode('tactical')" title="Mostrar ejercicios pendientes de dominar y casos 🟡 IMPORTANTES">
          <span class="mode-icon">🎯</span>
          <span class="mode-label"><span class="mode-label-long">Modo Táctico (Pendientes)</span><span class="mode-label-short">Táctico</span></span>
          <span class="mode-badge" id="badgeTacticalCount">40</span>
        </button>
        <button class="mode-btn" id="btnModeAll" onclick="setStudyMode('all')" title="Mostrar todos los ejercicios de esta vista">
          <span class="mode-icon">📚</span>
          <span class="mode-label"><span class="mode-label-long">Todos</span><span class="mode-label-short">Todos</span></span>
          <span class="mode-badge" id="badgeAllCount">40</span>
        </button>
      </div>

      <div class="hud-quick-tools">
        <button class="tool-btn highlight-tool" onclick="scrollToExercise(35)" title="Ver La Mochila resuelta en todos los paradigmas">
          <span class="tool-icon">🎒</span> <span class="tool-text">Mochila Multi-P</span>
        </button>
        <button class="tool-btn highlight-tool" onclick="scrollToExercise(36)" title="Ver El Viajante (TSP) resuelto en todos los paradigmas">
          <span class="tool-icon">🚗</span> <span class="tool-text">Viajante Multi-P</span>
        </button>
        <button class="tool-btn" onclick="toggleGlobalSolutions()" id="btnGlobalSolutions" title="Ocultar o mostrar todas las soluciones (Active Recall)">
          <span class="tool-icon">👁️</span> <span class="tool-text" id="lblGlobalSolutions">Soluciones</span>
        </button>
        <button class="tool-btn" onclick="openCheatsheet()" title="Abrir recetas rápidas y Teorema Maestro">
          <span class="tool-icon">📐</span> <span class="tool-text">Fórmulas</span>
        </button>
        <button class="tool-btn" onclick="scrollToTrainer()" title="Ir al simulador de reconocimiento en 30 segundos">
          <span class="tool-icon">⚡</span> <span class="tool-text">Simulador 30s</span>
        </button>
        <button class="tool-btn" onclick="toggleDarkMode()" id="btnDarkMode" title="Cambiar modo claro / oscuro">
          <span class="tool-icon" id="darkModeIcon">🌙</span>
        </button>
      </div>
    </div>

    <div class="hud-row-secondary">
      <div class="hud-progress-wrap">
        <div class="progress-info">
          <span class="progress-title">Progreso en vista activa:</span>
          <span class="progress-numbers"><strong id="progMastered">0</strong> de <span id="progTotal">32</span> dominados (<span id="progPercent">0%</span>)</span>
        </div>
        <div class="progress-track">
          <div class="progress-fill" id="progressFill" style="width: 0%;"></div>
        </div>
      </div>

      <div class="hud-search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="exerciseSearch" placeholder="Buscar ejercicio (tecla /): mochila, tsp, held-karp, arnook, invap..." oninput="handleSearch(this.value)">
        <button class="clear-search-btn" id="clearSearchBtn" onclick="clearSearch()" style="display: none;" title="Limpiar búsqueda">✕</button>
      </div>
    </div>

    <!-- Filter Pills por Paradigma (Enlaces modulares para GitHub Pages) -->
    <div class="hud-row-pills">
      <div class="filter-pills-scroll" id="paradigmPills">
        <!-- REND_PILLS -->
      </div>
    </div>
  </div>

  <!-- Notification Banner de Modo Emergencia -->
  <div class="emergency-banner" id="emergencyBanner">
    <div class="banner-inner">
      <span class="banner-icon">⚡</span>
      <span><strong>Modo Emergencia (48–72h):</strong> Mostrando los <strong id="emergencyBannerCount">32</strong> ejercicios 🔴 <strong>IMPRESCINDIBLES</strong> de exámenes reales en esta vista.</span>
      <button class="banner-dismiss" onclick="dismissBanner()" title="Ocultar aviso">✕</button>
    </div>
  </div>
</header>

<!-- Drawer de Fórmulas y Recetas Rápidas -->
<div class="drawer-backdrop" id="drawerBackdrop" onclick="closeCheatsheet()"></div>
<aside class="cheatsheet-drawer" id="cheatsheetDrawer" aria-hidden="true">
  <div class="drawer-header">
    <div class="drawer-title-group">
      <span class="drawer-icon">📐</span>
      <h2>Fórmulas y Recetas Rápidas de Parcial</h2>
    </div>
    <button class="drawer-close-btn" onclick="closeCheatsheet()" aria-label="Cerrar">✕</button>
  </div>

  <div class="drawer-content">
    <section class="drawer-section">
      <h3>1. Teorema Maestro (División y Conquista)</h3>
      <div class="formula-card">
        $$T(n) = a \cdot T(n/b) + \Theta(n^c) \quad (a \ge 1, \; b > 1, \; c \ge 0)$$
        <ul>
          <li><strong>Caso 1 (Hojas dominan):</strong> Si $\log_b a > c \implies T(n) = \Theta(n^{\log_b a})$</li>
          <li><strong>Caso 2 (Balance):</strong> Si $\log_b a = c \implies T(n) = \Theta(n^c \log n)$</li>
          <li><strong>Caso 3 (Raíz domina):</strong> Si $\log_b a < c \implies T(n) = \Theta(n^c)$ <em>(con $a \cdot f(n/b) \le k \cdot f(n)$)</em></li>
        </ul>
      </div>
    </section>

    <section class="drawer-section">
      <h3>2. Esquema de 4 Pasos Obligatorios para NP-C</h3>
      <ol class="steps-list">
        <li><strong>Certificado y Verificador en NP:</strong> Definir certificado polinomial $C$ y verificador $V(I_B, C)$ en tiempo $O(n^k)$.</li>
        <li><strong>Problema conocido en NPC:</strong> Seleccionar problema base $A \in \text{NPC}$ (Vertex Cover, 3-SAT, Ciclo Ham, Subset Sum) y reducir $A \le_P B$.</li>
        <li><strong>Transformación polinomial:</strong> Definir $f(I_A) \to I_B$ computable en tiempo polinomial.</li>
        <li><strong>Demostración Bidireccional:</strong>
          <ul>
            <li><strong>Ida ($\implies$):</strong> Si $I_A \in \text{YES}_A \implies f(I_A) \in \text{YES}_B$.</li>
            <li><strong>Vuelta ($\impliedby$):</strong> Si $f(I_A) \in \text{YES}_B \implies I_A \in \text{YES}_A$.</li>
          </ul>
        </li>
      </ol>
    </section>

    <section class="drawer-section">
      <h3>3. Los 5 Pasos de Programación Dinámica</h3>
      <ol class="steps-list">
        <li><strong>Definición semántica del Estado:</strong> Explicar con palabras qué significa $OPT(i, w)$.</li>
        <li><strong>Casos Base:</strong> Inicializar explícitamente celdas triviales y estados infactibles ($-\infty$ o $+\infty$).</li>
        <li><strong>Ecuación de Recurrencia:</strong> Decisión local, ej. $OPT(i, w) = \max\big(OPT(i-1, w), \; OPT(i-1, w - w_i) + v_i\big)$.</li>
        <li><strong>Orden de Llenado:</strong> Especificar dirección bottom-up (filas crecientes, columnas crecientes).</li>
        <li><strong>Algoritmo de Reconstrucción:</strong> Rastrear las decisiones hacia atrás en la tabla para devolver los ítems.</li>
      </ol>
    </section>

    <section class="drawer-section">
      <h3>4. Reglas de Oro de Programación Lineal (PLI)</h3>
      <ul>
        <li>Definir variables de decisión con su dominio explícito ($x_i \in \{0, 1\}$ o $y_j \ge 0$).</li>
        <li><strong>¡PROHIBIDO!</strong> Multiplicar variables de decisión ($x_i \cdot y_j$ anula el ejercicio; usar acotación con Big-$M$).</li>
        <li><strong>Linealizar Min-Max / Max-Min:</strong> $\min Z$ sujeto a $Z \ge f_i(x)$ para todo $i$.</li>
        <li>Contar explícitamente cantidad de variables y restricciones en función de la entrada.</li>
      </ul>
    </section>

    <section class="drawer-section">
      <h3>5. Redes de Flujo (Ford-Fulkerson / Edmonds-Karp)</h3>
      <ul>
        <li>Construir super-fuente $s$ y super-sumidero $t$ para entradas/salidas múltiples.</li>
        <li>Capacidades en aristas dirigidas. Red residual $G_f$ con aristas backward de capacidad $c_f(v, u) = f(u, v)$.</li>
        <li><strong>Teorema Max-Flow Min-Cut:</strong> $|f^*| = C(A, B) = \sum_{u \in A, v \in B} c(u, v)$.</li>
        <li><strong>Teorema de Integralidad:</strong> Capacidades enteras garantizan flujo entero $f(e) \in \mathbb{Z}_{\ge 0}$.</li>
      </ul>
    </section>

    <section class="drawer-section warning-box">
      <h3>⚠️ Errores Prohibidos que Anulan el Ejercicio</h3>
      <ul>
        <li>❌ <strong>Reducir al revés en NP-C:</strong> Jamás hagas $B \le_P A$. Siempre $A_{\text{conocido}} \le_P B_{\text{nuevo}}$.</li>
        <li>❌ <strong>Afirmar optimalidad en Greedy sin prueba:</strong> Requiere inducción por <em>Greedy Stays Ahead</em> o <em>Intercambio</em>.</li>
        <li>❌ <strong>Olvidar casos base en DP:</strong> Asumir $0$ en estados infactibles corrompe la solución.</li>
        <li>❌ <strong>Omitir aristas residuales backward en Flujo:</strong> No es Ford-Fulkerson sin ellas.</li>
      </ul>
    </section>
  </div>
</aside>

<!-- Floating Fast Button -->
<div class="floating-quick-btn" id="floatingQuickBtn">
  <button class="fab-btn" onclick="openCheatsheet()" title="Fórmulas Rápidas">📐 Recetas</button>
  <button class="fab-btn fab-secondary" onclick="scrollToTop()" title="Volver Arriba">⬆️</button>
</div>
"""
    return html_template.replace("<!-- REND_PILLS -->", rendered_pills)

def get_complete_css():
    return r"""
:root {
  --primary-color: #1a365d;
  --primary-light: #2b6cb0;
  --accent-color: #3182ce;
  --accent-soft: #ebf8ff;
  --bg-main: #f8fafc;
  --bg-card: #ffffff;
  --text-main: #1e293b;
  --text-muted: #64748b;
  --border-color: #e2e8f0;
  --shadow-sm: 0 1px 3px rgba(0, 0, 0, 0.05);
  --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.07), 0 2px 4px -2px rgba(0, 0, 0, 0.05);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
  --radius-sm: 6px;
  --radius-md: 10px;
  --radius-lg: 14px;
  --imprescindible-color: #e53e3e;
  --imprescindible-bg: #fff5f5;
  --importante-color: #d69e2e;
  --importante-bg: #fffaf0;
  --mastered-color: #38a169;
  --mastered-bg: #f0fff4;
  --font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  --font-mono: 'Liberation Mono', 'DejaVu Sans Mono', Consolas, 'Courier New', monospace;
}

body.dark-mode {
  --primary-color: #90cdf4;
  --primary-light: #63b3ed;
  --accent-color: #4299e1;
  --accent-soft: #2a4365;
  --bg-main: #0f172a;
  --bg-card: #1e293b;
  --text-main: #f1f5f9;
  --text-muted: #94a3b8;
  --border-color: #334155;
  --imprescindible-bg: #3c1e1e;
  --importante-bg: #3d3215;
  --mastered-bg: #143521;
}

* {
  box-sizing: border-box;
}

body {
  font-family: var(--font-family);
  font-size: 10.5pt;
  line-height: 1.55;
  color: var(--text-main);
  background-color: var(--bg-main);
  margin: 0;
  padding: 0;
  transition: background-color 0.2s ease, color 0.2s ease;
  overflow-x: hidden;
}

.main-content-wrapper {
  max-width: 1060px;
  margin: 0 auto;
  padding: 20px 20px 80px 20px;
}

/* Headings */
h1, h2, h3, h4 {
  color: var(--primary-color);
  font-weight: 700;
  margin-top: 24px;
  margin-bottom: 10px;
}

h1 {
  font-size: 22pt;
  border-bottom: 3px solid var(--accent-color);
  padding-bottom: 8px;
}

h2 {
  font-size: 15pt;
  border-bottom: 1.5px solid var(--border-color);
  padding-bottom: 6px;
  margin-top: 32px;
  scroll-margin-top: 175px;
}

h3 {
  font-size: 12pt;
  scroll-margin-top: 175px;
}

p {
  margin-top: 0;
  margin-bottom: 10px;
}

ul, ol {
  margin-top: 0;
  margin-bottom: 10px;
  padding-left: 24px;
}

li {
  margin-bottom: 4px;
}

hr {
  border: none;
  border-top: 1px solid var(--border-color);
  margin: 24px 0;
}

/* Pre & Code */
pre {
  background-color: #f1f5f9;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  padding: 12px 14px;
  font-family: var(--font-mono);
  font-size: 8.8pt;
  line-height: 1.4;
  overflow-x: auto;
  margin: 10px 0;
  color: #0f172a;
}

body.dark-mode pre {
  background-color: #0b1120;
  color: #e2e8f0;
  border-color: #334155;
}

code {
  font-family: var(--font-mono);
  font-size: 8.8pt;
  background-color: rgba(99, 102, 241, 0.08);
  padding: 2px 5px;
  border-radius: 4px;
  color: #2563eb;
}

body.dark-mode code {
  color: #93c5fd;
  background-color: rgba(147, 197, 253, 0.12);
}

pre code {
  background-color: transparent;
  padding: 0;
  color: inherit;
}

.code-container {
  position: relative;
  margin: 10px 0;
}

.code-container pre {
  margin: 0;
}

.copy-code-btn {
  position: absolute;
  top: 8px;
  right: 8px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: 4px;
  padding: 4px 8px;
  font-size: 7.8pt;
  font-weight: 600;
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.15s ease;
  z-index: 5;
}

.copy-code-btn:hover {
  background: var(--accent-color);
  color: #ffffff;
  border-color: var(--accent-color);
}

/* Tables */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0;
  font-size: 9.5pt;
  background: var(--bg-card);
  border-radius: var(--radius-sm);
  overflow: hidden;
  box-shadow: var(--shadow-sm);
}

th, td {
  border: 1px solid var(--border-color);
  padding: 8px 12px;
  text-align: left;
}

th {
  background-color: #edf2f7;
  font-weight: 700;
  color: var(--primary-color);
}

body.dark-mode th {
  background-color: #1e293b;
  color: #90cdf4;
}

tr:nth-child(even) {
  background-color: rgba(0, 0, 0, 0.02);
}

body.dark-mode tr:nth-child(even) {
  background-color: rgba(255, 255, 255, 0.02);
}

blockquote {
  border-left: 4px solid var(--accent-color);
  background-color: var(--accent-soft);
  padding: 10px 14px;
  margin: 12px 0;
  border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
}

/* KaTeX Mathematical Formulas */
.katex {
  font-size: 1.05em;
}
.katex-display {
  margin: 16px 0 !important;
  overflow-x: auto;
  overflow-y: hidden;
  padding: 8px 0;
}
body.dark-mode .katex {
  color: #e2e8f0;
}

/* Proof & Theoretical Cards */
.proof-card {
  background: #f8fafc;
  border: 1px solid #cbd5e1;
  border-left: 4px solid #3b82f6;
  border-radius: var(--radius-sm);
  padding: 14px 18px;
  margin: 14px 0;
}
body.dark-mode .proof-card {
  background: #1e293b;
  border-color: #334155;
  border-left-color: #60a5fa;
}
.proof-card-header {
  font-weight: 700;
  color: var(--primary-color);
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

/* Visual Decision & Flow Nodes */
.visual-trace-container {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  margin: 16px 0;
  padding: 14px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  box-shadow: var(--shadow-sm);
}
.trace-node {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: #f1f5f9;
  border: 2px solid var(--accent-color);
  border-radius: 8px;
  padding: 6px 12px;
  font-weight: 700;
  font-size: 9.5pt;
  color: var(--primary-color);
  min-width: 44px;
  box-shadow: var(--shadow-sm);
}
body.dark-mode .trace-node {
  background: #0f172a;
  border-color: #63b3ed;
  color: #90cdf4;
}
.trace-node.start-node {
  border-color: #10b981;
  color: #065f46;
}
body.dark-mode .trace-node.start-node {
  border-color: #34d399;
  color: #6ee7b7;
}
.trace-node.end-node {
  border-color: #8b5cf6;
  color: #5b21b6;
}
body.dark-mode .trace-node.end-node {
  border-color: #a78bfa;
  color: #c4b5fd;
}
.trace-arrow {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  font-size: 8pt;
  font-weight: 700;
  color: #059669;
  padding: 0 4px;
}
body.dark-mode .trace-arrow {
  color: #34d399;
}
.trace-arrow .arrow-op {
  background: rgba(16, 185, 129, 0.12);
  padding: 2px 6px;
  border-radius: 4px;
  margin-bottom: 2px;
}
body.dark-mode .trace-arrow .arrow-op {
  background: rgba(52, 211, 153, 0.2);
}

/* Mermaid Wrapper */
.mermaid-wrapper {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 16px;
  margin: 16px 0;
  overflow-x: auto;
  text-align: center;
  box-shadow: var(--shadow-sm);
}
body.dark-mode .mermaid-wrapper {
  background: #1e293b;
  border-color: #334155;
}
.mermaid {
  display: flex;
  justify-content: center;
  background: transparent !important;
  border: none !important;
  padding: 0 !important;
}
.mermaid svg {
  max-width: 100%;
  height: auto;
}

/* HUD Top Bar */
.hud-top-bar {
  position: sticky;
  top: 0;
  left: 0;
  right: 0;
  background: var(--bg-card);
  border-bottom: 1px solid var(--border-color);
  box-shadow: var(--shadow-md);
  z-index: 1000;
  backdrop-filter: blur(8px);
}

.hud-container {
  max-width: 1140px;
  margin: 0 auto;
  padding: 8px 16px;
}

.hud-row-primary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}

.hud-brand {
  display: flex;
  align-items: center;
  gap: 8px;
}

.hud-logo-icon {
  font-size: 20pt;
}

.hud-title {
  font-size: 11.5pt;
  margin: 0;
  font-weight: 800;
  color: var(--primary-color);
  line-height: 1.2;
}

.hud-subtitle {
  font-size: 8pt;
  color: var(--text-muted);
  display: block;
}

.hud-mode-selector {
  display: flex;
  background: rgba(0, 0, 0, 0.04);
  padding: 3px;
  border-radius: var(--radius-md);
  gap: 3px;
}

body.dark-mode .hud-mode-selector {
  background: rgba(255, 255, 255, 0.06);
}

.mode-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 5px 10px;
  font-size: 8.5pt;
  font-weight: 600;
  border: none;
  background: transparent;
  color: var(--text-muted);
  border-radius: var(--radius-sm);
  cursor: pointer;
  transition: all 0.15s ease;
}

.mode-btn:hover {
  color: var(--text-main);
}

.mode-btn.active {
  background: var(--accent-color);
  color: #ffffff;
  box-shadow: var(--shadow-sm);
}

.mode-badge {
  background: rgba(255, 255, 255, 0.25);
  font-size: 7.5pt;
  padding: 1px 5px;
  border-radius: 10px;
  font-weight: 700;
}

.mode-btn:not(.active) .mode-badge {
  background: var(--border-color);
  color: var(--text-main);
}

.hud-quick-tools {
  display: flex;
  align-items: center;
  gap: 6px;
}

.tool-btn {
  display: flex;
  align-items: center;
  gap: 5px;
  background: var(--bg-main);
  border: 1px solid var(--border-color);
  padding: 5px 10px;
  font-size: 8.5pt;
  font-weight: 600;
  border-radius: var(--radius-sm);
  cursor: pointer;
  color: var(--text-main);
  transition: all 0.15s ease;
}

.tool-btn:hover {
  background: var(--accent-soft);
  border-color: var(--accent-color);
  color: var(--accent-color);
}

.tool-btn.highlight-tool {
  background: linear-gradient(135deg, rgba(49, 130, 206, 0.12), rgba(128, 90, 213, 0.12));
  border-color: rgba(49, 130, 206, 0.5);
  color: var(--primary-color);
  font-weight: 700;
}

body.dark-mode .tool-btn.highlight-tool {
  background: linear-gradient(135deg, rgba(66, 153, 225, 0.22), rgba(159, 122, 234, 0.22));
  border-color: rgba(66, 153, 225, 0.6);
  color: #90cdf4;
}

.tool-btn.highlight-tool:hover {
  background: var(--accent-color);
  color: #ffffff;
  border-color: var(--accent-color);
  transform: translateY(-1px);
}

.hud-row-secondary {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  margin-top: 8px;
  flex-wrap: wrap;
}

.hud-progress-wrap {
  flex: 1;
  min-width: 250px;
}

.progress-info {
  display: flex;
  justify-content: space-between;
  font-size: 8pt;
  margin-bottom: 3px;
  color: var(--text-muted);
}

.progress-numbers strong {
  color: var(--mastered-color);
}

.progress-track {
  height: 7px;
  background: var(--border-color);
  border-radius: 4px;
  overflow: hidden;
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, #38a169, #48bb78);
  border-radius: 4px;
  transition: width 0.3s ease;
}

.hud-search-box {
  position: relative;
  width: 320px;
}

.hud-search-box input {
  width: 100%;
  padding: 6px 28px 6px 30px;
  font-size: 8.5pt;
  border: 1px solid var(--border-color);
  border-radius: 20px;
  background: var(--bg-main);
  color: var(--text-main);
  outline: none;
  transition: border-color 0.15s ease;
}

.hud-search-box input:focus {
  border-color: var(--accent-color);
  background: var(--bg-card);
}

.search-icon {
  position: absolute;
  left: 9px;
  top: 6px;
  font-size: 9pt;
  color: var(--text-muted);
}

.clear-search-btn {
  position: absolute;
  right: 8px;
  top: 5px;
  background: transparent;
  border: none;
  color: var(--text-muted);
  cursor: pointer;
  font-size: 9pt;
}

.hud-row-pills {
  margin-top: 6px;
}

.filter-pills-scroll {
  display: flex;
  gap: 5px;
  overflow-x: auto;
  padding-bottom: 3px;
  scrollbar-width: none;
}

.filter-pills-scroll::-webkit-scrollbar {
  display: none;
}

.pill-btn {
  white-space: nowrap;
  font-size: 7.8pt;
  font-weight: 600;
  padding: 3px 8px;
  border-radius: 12px;
  border: 1px solid var(--border-color);
  background: var(--bg-card);
  color: var(--text-muted);
  cursor: pointer;
  transition: all 0.15s ease;
  text-decoration: none;
}

.pill-btn:hover {
  background: var(--accent-soft);
  color: var(--accent-color);
}

.pill-btn.active {
  background: var(--primary-color);
  color: #ffffff;
  border-color: var(--primary-color);
}

body.dark-mode .pill-btn.active {
  background: var(--accent-color);
  border-color: var(--accent-color);
}

/* Emergency Banner */
.emergency-banner {
  background: #fff5f5;
  border-top: 1px solid #feb2b2;
  color: #c53030;
  font-size: 8.5pt;
  padding: 6px 16px;
}

body.dark-mode .emergency-banner {
  background: #3c1e1e;
  border-color: #742a2a;
  color: #feb2b2;
}

.banner-inner {
  max-width: 1140px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  gap: 8px;
}

.banner-icon {
  font-size: 11pt;
}

.banner-dismiss {
  margin-left: auto;
  background: transparent;
  border: none;
  color: inherit;
  cursor: pointer;
  font-size: 10pt;
}

/* Exercise Cards */
.exercise-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-left: 4px solid var(--primary-color);
  border-radius: var(--radius-md);
  margin: 22px 0;
  box-shadow: var(--shadow-sm);
  transition: all 0.2s ease;
  overflow: hidden;
  scroll-margin-top: 175px;
}

.exercise-card[data-priority="imprescindible"] {
  border-left-color: var(--imprescindible-color);
}

.exercise-card[data-priority="importante"] {
  border-left-color: var(--importante-color);
}

.exercise-card.is-mastered {
  border-left-color: var(--mastered-color) !important;
  background-color: var(--mastered-bg);
}

.exercise-card.is-hidden {
  display: none !important;
}

/* Search Empty State */
.search-empty-state {
  background: var(--bg-card);
  border: 1px dashed var(--border-color);
  border-radius: var(--radius-md);
  padding: 36px 24px;
  margin: 28px 0;
  text-align: center;
  box-shadow: var(--shadow-sm);
}

.empty-state-icon {
  font-size: 28pt;
  margin-bottom: 10px;
}

.empty-state-title {
  margin: 0 0 8px 0;
  font-size: 13pt;
  color: var(--primary-color);
}

.empty-state-desc {
  color: var(--text-muted);
  font-size: 9.5pt;
  max-width: 480px;
  margin: 0 auto 16px auto;
}

.card-header {
  padding: 12px 16px;
  background: rgba(0, 0, 0, 0.015);
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  flex-wrap: wrap;
}

body.dark-mode .card-header {
  background: rgba(255, 255, 255, 0.02);
}

.card-header-left {
  display: flex;
  align-items: center;
  gap: 10px;
}

.exercise-pill-number {
  background: var(--primary-color);
  color: #ffffff;
  font-size: 8.5pt;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: var(--radius-sm);
  letter-spacing: 0.5px;
}

body.dark-mode .exercise-pill-number {
  background: var(--accent-color);
}

.exercise-title {
  margin: 0;
  font-size: 11.5pt;
  font-weight: 700;
  color: var(--text-main);
}

.card-header-meta {
  display: flex;
  align-items: center;
  gap: 6px;
  flex-wrap: wrap;
}

.badge {
  font-size: 7.5pt;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 12px;
  text-transform: uppercase;
  letter-spacing: 0.3px;
}

.badge-priority-imprescindible {
  background: var(--imprescindible-bg);
  color: var(--imprescindible-color);
  border: 1px solid rgba(229, 62, 62, 0.3);
}

.badge-priority-importante {
  background: var(--importante-bg);
  color: var(--importante-color);
  border: 1px solid rgba(214, 158, 46, 0.3);
}

.badge-paradigm {
  background: var(--accent-soft);
  color: var(--accent-color);
  border: 1px solid rgba(49, 130, 206, 0.25);
}

.badge-origin {
  background: rgba(0, 0, 0, 0.04);
  color: var(--text-muted);
  border: 1px solid var(--border-color);
  text-transform: none;
  font-weight: 600;
  max-width: 240px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

body.dark-mode .badge-origin {
  background: rgba(255, 255, 255, 0.04);
}

.card-header-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.mastered-label {
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 8.5pt;
  font-weight: 600;
  cursor: pointer;
  user-select: none;
  padding: 4px 8px;
  border-radius: var(--radius-sm);
  background: rgba(0, 0, 0, 0.03);
  border: 1px solid var(--border-color);
  transition: all 0.15s ease;
}

body.dark-mode .mastered-label {
  background: rgba(255, 255, 255, 0.04);
}

.mastered-checkbox {
  cursor: pointer;
  accent-color: var(--mastered-color);
}

.card-body {
  padding: 16px;
}

.exercise-statement-box {
  margin-bottom: 14px;
}

.exercise-statement-box p {
  line-height: 1.5;
}

/* Solution Drawer / Accordion */
.exercise-solution-drawer {
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  background: rgba(0, 0, 0, 0.015);
  margin-top: 14px;
  overflow: hidden;
}

body.dark-mode .exercise-solution-drawer {
  background: rgba(255, 255, 255, 0.02);
}

.solution-summary {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 14px;
  background: var(--bg-card);
  cursor: pointer;
  font-size: 9.5pt;
  font-weight: 700;
  color: var(--accent-color);
  user-select: none;
  list-style: none;
  transition: background 0.15s ease;
}

.solution-summary::-webkit-details-marker {
  display: none;
}

.solution-summary:hover {
  background: var(--accent-soft);
}

.summary-toggle-icon {
  font-size: 8.5pt;
  transition: transform 0.2s ease;
}

details[open] .summary-toggle-icon {
  transform: rotate(90deg);
}

.summary-title {
  flex: 1;
}

.summary-badge {
  font-size: 7.5pt;
  font-weight: 600;
  background: #edf2f7;
  color: #4a5568;
  padding: 2px 6px;
  border-radius: 4px;
}

body.dark-mode .summary-badge {
  background: #334155;
  color: #cbd5e1;
}

.solution-inner-content {
  padding: 14px 16px;
  border-top: 1px solid var(--border-color);
  background: var(--bg-card);
}

.btn-toggle-solution {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px 8px;
  font-size: 8pt;
  font-weight: 600;
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  background: var(--bg-card);
  color: var(--accent-color);
  cursor: pointer;
}

.btn-toggle-solution:hover {
  background: var(--accent-soft);
}

/* Warning & Trap Callout */
.trap-callout {
  background: #fffaf0;
  border: 1px solid #fbd38d;
  border-left: 4px solid #dd6b20;
  border-radius: var(--radius-sm);
  padding: 10px 14px;
  margin: 14px 0;
}

body.dark-mode .trap-callout {
  background: #332612;
  border-color: #7b4e18;
  border-left-color: #ed8936;
}

.trap-header {
  font-size: 9pt;
  font-weight: 800;
  color: #c05621;
  margin-bottom: 6px;
  text-transform: uppercase;
  letter-spacing: 0.4px;
}

body.dark-mode .trap-header {
  color: #fbd38d;
}

/* Trainer Box */
.trainer-box {
  background: var(--bg-card);
  border: 2px solid var(--accent-color);
  border-radius: var(--radius-lg);
  padding: 20px;
  margin: 28px 0;
  box-shadow: var(--shadow-md);
  scroll-margin-top: 175px;
}

.trainer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 12px;
  margin-bottom: 16px;
  flex-wrap: wrap;
  gap: 10px;
}

.trainer-title-wrap {
  display: flex;
  align-items: center;
  gap: 12px;
}

.trainer-badge-icon {
  font-size: 24pt;
}

.trainer-title {
  margin: 0;
  font-size: 13.5pt;
  font-weight: 800;
}

.trainer-subtitle {
  margin: 0;
  font-size: 8.5pt;
  color: var(--text-muted);
}

.stat-pill {
  background: var(--accent-soft);
  color: var(--accent-color);
  padding: 5px 12px;
  border-radius: 20px;
  font-size: 9pt;
  font-weight: 600;
}

.trainer-card {
  background: var(--bg-main);
  border-radius: var(--radius-md);
  padding: 16px;
}

.trainer-card-header {
  display: flex;
  justify-content: space-between;
  font-size: 8.5pt;
  color: var(--text-muted);
  margin-bottom: 10px;
}

.trainer-prompt {
  font-size: 11pt;
  font-weight: 600;
  line-height: 1.5;
  margin-bottom: 18px;
  color: var(--text-main);
}

.trainer-options-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 10px;
  margin-bottom: 16px;
}

.trainer-btn {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  padding: 10px 12px;
  font-size: 9pt;
  font-weight: 600;
  color: var(--text-main);
  cursor: pointer;
  text-align: left;
  transition: all 0.15s ease;
}

.trainer-btn:hover:not(:disabled) {
  border-color: var(--accent-color);
  background: var(--accent-soft);
}

.trainer-btn.btn-correct {
  background: #f0fff4 !important;
  border-color: #38a169 !important;
  color: #22543d !important;
}

.trainer-btn.btn-wrong {
  background: #fff5f5 !important;
  border-color: #e53e3e !important;
  color: #742a2a !important;
}

.trainer-feedback {
  border-radius: var(--radius-sm);
  padding: 12px 14px;
  margin-bottom: 14px;
}

.trainer-feedback.feedback-success {
  background: #f0fff4;
  border-left: 4px solid #38a169;
  color: #22543d;
}

.trainer-feedback.feedback-error {
  background: #fff5f5;
  border-left: 4px solid #e53e3e;
  color: #742a2a;
}

body.dark-mode .trainer-feedback.feedback-success {
  background: #143521;
  color: #9ae6b4;
}

body.dark-mode .trainer-feedback.feedback-error {
  background: #3c1e1e;
  color: #feb2b2;
}

.feedback-result {
  font-weight: 700;
  margin-bottom: 4px;
}

.feedback-trigger {
  font-size: 9pt;
  line-height: 1.4;
}

.trainer-actions {
  display: flex;
  gap: 10px;
}

.btn {
  padding: 7px 14px;
  border-radius: var(--radius-sm);
  font-size: 9pt;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: all 0.15s ease;
}

.btn-primary {
  background: var(--accent-color);
  color: #ffffff;
}

.btn-primary:hover {
  background: var(--primary-light);
}

.btn-ghost {
  background: transparent;
  color: var(--text-muted);
  border: 1px solid var(--border-color);
}

.btn-ghost:hover {
  background: var(--bg-card);
  color: var(--text-main);
}

/* Interactive Checklist */
.checklist-interactive-item {
  list-style: none;
  margin-left: -20px;
  margin-bottom: 6px;
}

.chk-label {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  cursor: pointer;
  user-select: none;
}

.exam-checklist-input {
  margin-top: 3px;
  accent-color: var(--accent-color);
  cursor: pointer;
}

.exam-checklist-input:checked + .chk-custom + .chk-text {
  text-decoration: line-through;
  color: var(--text-muted);
}

/* Cheatsheet Drawer */
.drawer-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.4);
  backdrop-filter: blur(3px);
  z-index: 2000;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.25s ease;
}

.drawer-backdrop.is-open {
  opacity: 1;
  pointer-events: auto;
}

.cheatsheet-drawer {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  width: 500px;
  max-width: 90vw;
  background: var(--bg-card);
  box-shadow: -5px 0 20px rgba(0, 0, 0, 0.15);
  z-index: 2001;
  transform: translateX(100%);
  transition: transform 0.25s ease;
  display: flex;
  flex-direction: column;
}

.cheatsheet-drawer.is-open {
  transform: translateX(0);
}

.drawer-header {
  padding: 16px 20px;
  border-bottom: 1px solid var(--border-color);
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.drawer-title-group {
  display: flex;
  align-items: center;
  gap: 8px;
}

.drawer-title-group h2 {
  margin: 0;
  font-size: 13pt;
  border: none;
  padding: 0;
}

.drawer-close-btn {
  background: transparent;
  border: none;
  font-size: 14pt;
  color: var(--text-muted);
  cursor: pointer;
}

.drawer-content {
  padding: 20px;
  overflow-y: auto;
  flex: 1;
}

.drawer-section {
  margin-bottom: 24px;
}

.drawer-section h3 {
  font-size: 11pt;
  color: var(--accent-color);
  margin-top: 0;
  margin-bottom: 8px;
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 4px;
}

.formula-card {
  background: var(--bg-main);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-sm);
  padding: 10px 12px;
  font-size: 9pt;
}

.steps-list {
  padding-left: 18px;
  font-size: 9pt;
}

.steps-list li {
  margin-bottom: 6px;
}

.warning-box {
  background: #fff5f5;
  border: 1px solid #feb2b2;
  border-radius: var(--radius-sm);
  padding: 12px;
}

body.dark-mode .warning-box {
  background: #3c1e1e;
  border-color: #742a2a;
}

.warning-box h3 {
  color: #c53030;
  border-color: #feb2b2;
}

/* Floating Actions */
.floating-quick-btn {
  position: fixed;
  bottom: 20px;
  right: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
  z-index: 800;
}

.fab-btn {
  background: var(--accent-color);
  color: #ffffff;
  border: none;
  border-radius: 30px;
  padding: 10px 16px;
  font-size: 9.5pt;
  font-weight: 700;
  box-shadow: var(--shadow-md);
  cursor: pointer;
  transition: all 0.2s ease;
}

.fab-btn:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  background: var(--primary-light);
}

.fab-secondary {
  background: var(--bg-card);
  color: var(--text-main);
  border: 1px solid var(--border-color);
  padding: 8px 12px;
  align-self: flex-end;
}

/* RESPONSIVE DESIGN FOR MOBILE & TABLET */
@media (max-width: 768px) {
  body {
    font-size: 10pt;
  }

  .main-content-wrapper {
    padding: 12px 10px 80px 10px;
  }

  h1 {
    font-size: 16pt;
    line-height: 1.25;
  }

  h2 {
    font-size: 13pt;
    margin-top: 24px;
    scroll-margin-top: 130px;
  }

  h3 {
    font-size: 11pt;
    scroll-margin-top: 130px;
  }

  .hud-container {
    padding: 6px 8px;
  }

  .hud-brand {
    gap: 6px;
  }

  .hud-logo-icon {
    font-size: 16pt;
  }

  .hud-title {
    font-size: 9.6pt;
  }

  .hud-subtitle {
    display: none;
  }

  .mode-label-long {
    display: none;
  }

  .mode-label-short {
    display: inline;
  }

  .mode-btn {
    padding: 5px 6px;
    font-size: 8pt;
    gap: 3px;
  }

  .hud-quick-tools {
    gap: 4px;
  }

  .hud-quick-tools .tool-text {
    display: none;
  }

  .tool-btn {
    padding: 5px 7px;
    font-size: 9pt;
  }

  .hud-row-secondary {
    flex-direction: column;
    align-items: stretch;
    gap: 8px;
    margin-top: 6px;
  }

  .hud-progress-wrap {
    min-width: 100%;
  }

  .hud-search-box {
    width: 100%;
  }

  .hud-search-box input {
    font-size: 9pt;
    padding: 8px 28px 8px 30px;
  }

  .search-icon {
    top: 8px;
  }

  .clear-search-btn {
    top: 7px;
  }

  .card-header {
    flex-direction: column;
    align-items: stretch;
    gap: 8px;
    padding: 10px 12px;
  }

  .card-header-left {
    width: 100%;
  }

  .card-header-meta {
    width: 100%;
  }

  .badge-origin {
    max-width: 100%;
    white-space: normal;
  }

  .card-header-actions {
    width: 100%;
    display: flex;
    gap: 8px;
  }

  .mastered-label {
    flex: 1;
    justify-content: center;
    padding: 7px 10px;
    font-size: 8.8pt;
  }

  .btn-toggle-solution {
    flex: 1;
    justify-content: center;
    padding: 7px 10px;
    font-size: 8.8pt;
  }

  .card-body {
    padding: 12px 10px;
  }

  table {
    display: block;
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  pre {
    font-size: 7.8pt;
    padding: 10px 8px;
    max-width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
  }

  .trainer-box {
    padding: 14px 10px;
    margin: 20px 0;
  }

  .trainer-title {
    font-size: 11.5pt;
  }

  .trainer-options-grid {
    grid-template-columns: 1fr;
    gap: 8px;
  }

  .trainer-btn {
    padding: 12px 14px;
    font-size: 9.5pt;
  }

  .cheatsheet-drawer {
    width: 100vw;
    max-width: 100vw;
  }

  .floating-quick-btn {
    bottom: 12px;
    right: 12px;
    gap: 6px;
  }

  .fab-btn {
    padding: 8px 12px;
    font-size: 8.5pt;
  }

  .exercise-card {
    scroll-margin-top: 130px;
  }
}

@media (min-width: 769px) {
  .mode-label-short {
    display: none;
  }
}

/* PRINT RULES */
@media print {
  @page {
    size: A4;
    margin: 18mm 14mm 18mm 14mm;
    @bottom-center {
      content: "Teoría de Algoritmos — FIUBA | Página " counter(page);
      font-family: 'Liberation Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
      font-size: 8pt;
      color: #718096;
    }
  }

  body {
    padding-top: 0 !important;
    background: #ffffff !important;
    color: #2d3748 !important;
    font-size: 10pt !important;
  }

  .hud-top-bar,
  .emergency-banner,
  .cheatsheet-drawer,
  .drawer-backdrop,
  .floating-quick-btn,
  .card-header-actions,
  .copy-code-btn,
  .trainer-box,
  .solution-summary,
  .search-empty-state {
    display: none !important;
  }

  .exercise-card {
    border: 1px solid #e2e8f0 !important;
    border-left: 4px solid #3182ce !important;
    box-shadow: none !important;
    margin: 16px 0 !important;
    page-break-inside: avoid;
    break-inside: avoid;
  }

  .exercise-solution-drawer {
    border: none !important;
    background: transparent !important;
    display: block !important;
  }

  .solution-inner-content {
    display: block !important;
    padding: 0 !important;
    border: none !important;
  }

  .is-hidden {
    display: block !important;
  }
}
"""

def get_complete_js():
    return r"""
// Global state
let currentMode = 'emergency';
let currentParadigm = 'all';
let searchQuery = '';
let solutionsExpanded = false;
let masteredExercises = new Set();
let checklistState = {};

// 16 real exam scenario questions for the 30-second trainer
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
    trigger: "Mochila 0-1: subestructura óptima con superposición de subproblemas OPT(i, w). Requiere tabla (n+1) x (W+1) en O(n · W) pseudo-polinomial (Ejercicio 35)."
  },
  {
    prompt: "Dado un conjunto de n ciudades con matriz de distancias métricas, hallar un circuito cerrado que visite todas las ciudades con costo garantizado a lo sumo el doble del óptimo.",
    answer: "greedy",
    paradigmName: "Algoritmo de Aproximación (MST + Preorden)",
    trigger: "2-Aproximación de TSP Métrico: calcular Árbol Generador Mínimo (MST) con Prim o Kruskal y recorrer en preorden tomando atajos por desigualdad triangular (Ejercicio 36)."
  }
];

let trainerIndex = 0;
let trainerScore = 0;
let trainerAnswered = false;

function getPageForExercise(num) {
  if (num >= 1 && num <= 3) return "dyc.html";
  if (num >= 4 && num <= 8) return "greedy.html";
  if (num >= 9 && num <= 12) return "backtracking.html";
  if (num >= 13 && num <= 18) return "dp.html";
  if (num >= 19 && num <= 23) return "pl.html";
  if (num >= 24 && num <= 27) return "flujo.html";
  if (num >= 28 && num <= 31) return "reducciones.html";
  if (num >= 32 && num <= 36) return "integradores.html";
  if (num >= 37 && num <= 40) return "tipo_parcial.html";
  return "index.html";
}

// Initialization on DOM ready
document.addEventListener("DOMContentLoaded", async () => {
  loadSavedState();
  updateModeUI();
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
    const num = parseInt(cb.getAttribute("data-ej-num"));
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
  searchQuery = "";
  const searchInput = document.getElementById("exerciseSearch");
  if (searchInput) searchInput.value = "";
  const clearBtn = document.getElementById("clearSearchBtn");
  if (clearBtn) clearBtn.style.display = "none";
  saveState();
  updateModeUI();
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
    const num = parseInt(card.getAttribute("data-num"));
    const priority = card.getAttribute("data-priority");
    const paradigm = card.getAttribute("data-paradigm");
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

    // Search query filter
    let matchesSearch = true;
    if (searchQuery) {
      matchesSearch = title.includes(searchQuery) || origin.includes(searchQuery) || cardText.includes(searchQuery) || ("ej " + num) === searchQuery || ("ejercicio " + num) === searchQuery;
    }

    const isVisible = matchesMode && matchesParadigm && matchesSearch;
    card.classList.toggle("is-hidden", !isVisible);

    if (isVisible) {
      visibleCount++;
      if (isMastered) {
        masteredCount++;
      }
    }
  });

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

function updateProgressHUD(totalVisible, totalMastered) {
  if (totalVisible === undefined) {
    const cards = document.querySelectorAll(".exercise-card:not(.is-hidden)");
    totalVisible = cards.length;
    totalMastered = 0;
    cards.forEach(c => {
      const num = parseInt(c.getAttribute("data-num"));
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
  searchQuery = '';
  const searchInput = document.getElementById("exerciseSearch");
  if (searchInput) searchInput.value = "";
  const clearBtn = document.getElementById("clearSearchBtn");
  if (clearBtn) clearBtn.style.display = "none";

  saveState();
  updateModeUI();
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
"""

def normalize_markdown_lists(md_text):
    lines = md_text.split("\n")
    new_lines = []
    in_code_block = False
    bullet_regex = re.compile(r"^(\s*)([*\-+]|\d+\.)\s+")
    
    for line in lines:
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
        if in_code_block:
            new_lines.append(line)
            continue
            
        m = bullet_regex.match(line)
        if m:
            indent = m.group(1)
            # Normalizar indentación de sub-items (2 espacios) a 4 espacios para soporte de anidamiento
            if indent == "  ":
                line = "    " + line.lstrip()
            if new_lines:
                prev_line = new_lines[-1]
                # Si la línea anterior no está vacía y no es ya un ítem de lista, insertar línea en blanco
                if prev_line.strip() != "" and not bullet_regex.match(prev_line):
                    new_lines.append("")
                    
        new_lines.append(line)
    return "\n".join(new_lines)

def convert_markdown_to_html(md_text):
    # 1. Proteger bloques de código (fenced e inline) para no tocar math dentro de código
    code_placeholders = []

    def save_fenced_code(match):
        idx = len(code_placeholders)
        code_placeholders.append(match.group(0))
        return f"%%FENCED_CODE_{idx}%%"

    md_text = re.sub(r"(```[\s\S]*?```)", save_fenced_code, md_text)

    def save_inline_code(match):
        idx = len(code_placeholders)
        code_placeholders.append(match.group(0))
        return f"%%INLINE_CODE_{idx}%%"

    md_text = re.sub(r"(`[^`\n]+?`)", save_inline_code, md_text)

    # 2. Proteger bloques de matemáticas KaTeX (display e inline)
    math_placeholders = []

    def save_display_math(match):
        idx = len(math_placeholders)
        math_placeholders.append(match.group(0))
        return f"%%MATH_DISP_{idx}%%"

    md_text = re.sub(r"\$\$(.+?)\$\$", save_display_math, md_text, flags=re.DOTALL)

    def save_inline_math(match):
        idx = len(math_placeholders)
        math_placeholders.append(match.group(0))
        return f"%%MATH_INL_{idx}%%"

    md_text = re.sub(r"(?<!\\)\$(?!\$)([^\n]+?)(?<!\\)\$", save_inline_math, md_text)

    # 3. Restaurar bloques de código para que markdown los procese con sus extensiones
    for idx, raw_code in enumerate(code_placeholders):
        md_text = md_text.replace(f"%%FENCED_CODE_{idx}%%", raw_code)
        md_text = md_text.replace(f"%%INLINE_CODE_{idx}%%", raw_code)

    # 4. Procesar Markdown con extensiones
    html_raw = markdown.markdown(md_text, extensions=['fenced_code', 'tables'])

    # 5. Restaurar bloques de matemáticas escapando caracteres HTML (<, >, &)
    for idx, raw_math in enumerate(math_placeholders):
        safe_math = html.escape(raw_math)
        html_raw = html_raw.replace(f"%%MATH_DISP_{idx}%%", safe_math)
        html_raw = html_raw.replace(f"%%MATH_INL_{idx}%%", safe_math)

    return html_raw

def build_interactive_html(md_text, output_file, active_paradigm="all", page_title=None):
    title_text = "Teoría de Algoritmos — Guía Interactiva de Parciales (FIUBA)"
    if page_title:
        title_text = f"Teoría de Algoritmos — {page_title} (FIUBA)"

    md_text = normalize_markdown_lists(md_text)
    html_raw = convert_markdown_to_html(md_text)
    html_with_cards = process_html_exercises(html_raw)
    html_with_widgets = inject_interactive_widgets(html_with_cards)

    hud_and_drawer = get_hud_and_drawer_html(active_paradigm=active_paradigm)
    css_styles = get_complete_css()
    js_scripts = get_complete_js()

    final_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_text}</title>
<!-- KaTeX para renderizado matemático ultra veloz -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<!-- Mermaid para diagramas de flujo y grafos dinámicos -->
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<style>
{css_styles}
</style>
</head>
<body>
{hud_and_drawer}
<main class="main-content-wrapper">
{html_with_widgets}
</main>
<script>
{js_scripts}
</script>
</body>
</html>
"""

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)

    return output_file
