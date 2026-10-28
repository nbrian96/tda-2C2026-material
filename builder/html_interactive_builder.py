"""Generador de HTML interactivo con Bootstrap 5.3 y assets modulares para TDA."""

import re
import html
import markdown

def get_paradigm_for_exercise(num):
    if 1 <= num <= 12:
        return ("dyc", "División y Conquista", "badge-dyc")
    if 13 <= num <= 38:
        return ("greedy", "Greedy / Voraz", "badge-greedy")
    if 39 <= num <= 52:
        return ("backtracking", "Backtracking", "badge-backtracking")
    if 53 <= num <= 59:
        return ("dp", "Prog. Dinámica", "badge-dp")
    if 60 <= num <= 65:
        return ("pl", "Prog. Lineal", "badge-pl")
    if 66 <= num <= 70:
        return ("flujo", "Redes de Flujo", "badge-flujo")
    if 71 <= num <= 74:
        return ("reducciones", "Reducciones NP", "badge-reducciones")
    if 75 <= num <= 79:
        label = "Multi-Paradigma" if num in (78, 79) else "Integrador"
        return ("integradores", label, "badge-integrador")
    if 80 <= num <= 83:
        return ("tipo_parcial", "Tipo Parcial", "badge-tipo-parcial")
    return ("otro", "General", "badge-otro")

SOLUTION_MARKERS = [
    r"<h4>1\.\s*Idea",
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
        return f'<div class="mermaid-wrapper"><pre class="mermaid">{clean_content}</pre></div>'
    return (
        f'<div class="code-container">'
        f'<button class="copy-code-btn" type="button" title="Copiar código al portapapeles" onclick="copyCodeBlock(this)">📋 Copiar</button>'
        f'{code_tag_start}{code_content}{code_tag_end}'
        f'</div>'
    )

def format_exercise_card(num, title, body_html):
    paradigm_key, paradigm_name, paradigm_class = get_paradigm_for_exercise(num)

    is_imprescindible = "🔴 IMPRESCINDIBLE" in body_html
    priority_slug = "imprescindible" if is_imprescindible else "importante"
    priority_label = "🔴 IMPRESCINDIBLE" if is_imprescindible else "🟡 IMPORTANTE"
    priority_class = "badge-priority-imprescindible" if is_imprescindible else "badge-priority-importante"

    diff_match = re.search(r"<strong>Dificultad:</strong>\s*(.*?)(?:</p>|<br\s*/?>|\n)", body_html)
    diff_num = 3
    if diff_match:
        diff_raw = diff_match.group(1)
        num_m = re.search(r"\(([1-5])/5\)", diff_raw)
        if num_m:
            diff_num = int(num_m.group(1))
        elif "★" in diff_raw:
            diff_num = max(1, min(5, diff_raw.count("★")))
    stars_str = "★" * diff_num + "☆" * (5 - diff_num)

    origin_match = re.search(r"<strong>Origen:</strong>\s*(.*?)(?:</p>|<br\s*/?>|\n)", body_html, re.DOTALL)
    origin_text = origin_match.group(1).strip() if origin_match else "Parcial / Práctica FIUBA"

    clean_body = re.sub(r"<p>\s*<strong>Clasificación:</strong>.*?</p>", "", body_html, flags=re.DOTALL)
    clean_body = re.sub(r"<p>\s*<strong>Dificultad:</strong>.*?</p>", "", clean_body, flags=re.DOTALL)
    clean_body = re.sub(r"<strong>(?:Clasificación|Dificultad):</strong>.*?(?:<br\s*/?>|\n)", "", clean_body)

    split_pos = None
    for sm in SOLUTION_MARKERS:
        m = re.search(sm, clean_body)
        if m and (split_pos is None or m.start() < split_pos):
            split_pos = m.start()

    if split_pos is not None:
        statement_html = clean_body[:split_pos].strip()
        solution_html = clean_body[split_pos:].strip()
    else:
        statement_html = clean_body.strip()
        solution_html = ""

    if statement_html:
        statement_html = re.sub(CODE_BLOCK_PATTERN, replace_code_block_match, statement_html, flags=re.DOTALL)

    if solution_html:
        solution_html = re.sub(CODE_BLOCK_PATTERN, replace_code_block_match, solution_html, flags=re.DOTALL)
        trap_pattern = r"(<p><strong>(?:Trampas habituales de corrección|Puntos donde puedo equivocarme).*?</strong>.*?</p>(?:\s*<ul>.*?</ul>)?)"
        solution_html = re.sub(
            trap_pattern,
            lambda m: f'<div class="trap-callout"><div class="trap-header">⚠️ Trampa Típica de Corrección</div>{m.group(1)}</div>',
            solution_html,
            flags=re.DOTALL
        )

    origin_short = html.escape(origin_text.split("/")[0].strip())
    return (
        f'<article class="exercise-card" id="ej-{num}" data-num="{num}" data-priority="{priority_slug}" '
        f'data-paradigm="{paradigm_key}" data-difficulty="{diff_num}" '
        f'data-title="{html.escape(title.lower())}" data-origin="{html.escape(origin_text.lower())}">'
        f'<header class="card-header">'
        f'<div class="card-header-left"><span class="exercise-pill-number">EJ {num}</span><h3 class="exercise-title">{title}</h3></div>'
        f'<div class="card-header-meta">'
        f'<span class="badge badge-priority {priority_class}">{priority_label}</span>'
        f'<span class="badge badge-difficulty diff-{diff_num}" title="Dificultad {diff_num} de 5">{stars_str} ({diff_num}/5)</span>'
        f'<span class="badge badge-paradigm {paradigm_class}">{paradigm_name}</span>'
        f'<span class="badge badge-origin" title="{html.escape(origin_text)}">🏛️ {origin_short}</span>'
        f'</div>'
        f'<div class="card-header-actions">'
        f'<label class="mastered-label" title="Marcar como dominado (se guarda automáticamente)">'
        f'<input type="checkbox" class="mastered-checkbox" data-ej-num="{num}" onchange="toggleMastered({num}, this.checked)">'
        f'<span class="checkbox-custom"></span><span class="label-text">Dominado</span>'
        f'</label></div></header>'
        f'<div class="card-body">'
        f'<div class="exercise-statement-box">{statement_html}</div>'
        f'<details class="exercise-solution-drawer" id="solution-drawer-{num}">'
        f'<summary class="solution-summary">'
        f'<span class="summary-toggle-icon">▶</span>'
        f'<span class="summary-title">💡 Solución Completa, Pseudocódigo y Análisis Formal</span>'
        f'<span class="summary-badge">Active Recall</span>'
        f'</summary>'
        f'<div class="solution-inner-content">{solution_html}</div>'
        f'</details></div></article>\n'
    )

def process_html_exercises(html_body):
    parts = re.split(r"(<h3>Ejercicio \d+ [^<]+</h3>)", html_body)
    new_parts = [parts[0]]
    for i in range(1, len(parts), 2):
        header = parts[i]
        body = parts[i + 1]
        num_m = re.search(r"Ejercicio (\d+) — (.*?)</h3>", header)
        if not num_m:
            new_parts.extend([header, body])
            continue
        num = int(num_m.group(1))
        title = num_m.group(2).strip()
        split_m = re.search(r"(?:<hr\s*/?>\s*)?(?:<h3>(?:Patrón de Ejercicio|Errores Frecuentes|Errores Fatales)|<h2>)", body)
        if split_m:
            ex_body, trailing = body[:split_m.start()], body[split_m.start():]
        else:
            ex_body, trailing = body, ""
        new_parts.append(format_exercise_card(num, title, ex_body))
        if trailing:
            new_parts.append(trailing)
    return "".join(new_parts)

def inject_interactive_widgets(html_body):
    html_body = re.sub(CODE_BLOCK_PATTERN, replace_code_block_match, html_body, flags=re.DOTALL)
    trainer_html = (
        '<div class="trainer-box" id="entrenador-30s">'
        '<div class="trainer-header"><div class="trainer-title-wrap"><span class="trainer-badge-icon">⚡</span>'
        '<div><h3 class="trainer-title">Entrenador Interactivo: Reconocimiento en 30 Segundos</h3>'
        '<p class="trainer-subtitle">Entrená la habilidad más crítica del parcial: identificar el paradigma exacto sin dudar.</p></div></div>'
        '<div class="trainer-stats"><span class="stat-pill">Aciertos: <strong id="trainerScore">0</strong> / <strong id="trainerTotal">0</strong></span></div></div>'
        '<div class="trainer-card"><div class="trainer-card-header">'
        '<span class="trainer-counter">Caso <span id="trainerCurrentIndex">1</span> de <span id="trainerTotalQuestions">16</span></span>'
        '<span class="trainer-timer-tag">⏱️ Meta: &lt; 30 segundos</span></div>'
        '<div class="trainer-prompt" id="trainerPrompt">Cargando enunciado de examen...</div>'
        '<div class="trainer-options-grid" id="trainerOptions">'
        '<button class="trainer-btn" onclick="checkTrainerAnswer(\'dyc\')">🔷 División y Conquista</button>'
        '<button class="trainer-btn" onclick="checkTrainerAnswer(\'greedy\')">🔶 Greedy (Voraz)</button>'
        '<button class="trainer-btn" onclick="checkTrainerAnswer(\'backtracking\')">🟣 Backtracking &amp; B&amp;B</button>'
        '<button class="trainer-btn" onclick="checkTrainerAnswer(\'dp\')">🟢 Programación Dinámica</button>'
        '<button class="trainer-btn" onclick="checkTrainerAnswer(\'pl\')">🔵 Programación Lineal (PLI)</button>'
        '<button class="trainer-btn" onclick="checkTrainerAnswer(\'flujo\')">🔴 Redes de Flujo</button>'
        '<button class="trainer-btn" onclick="checkTrainerAnswer(\'reducciones\')">🟡 Reducciones NP-C</button>'
        '</div>'
        '<div class="trainer-feedback" id="trainerFeedback" style="display: none;">'
        '<div class="feedback-result" id="feedbackResult"></div><div class="feedback-trigger" id="feedbackTrigger"></div></div>'
        '<div class="trainer-actions">'
        '<button class="btn btn-primary" id="trainerNextBtn" style="display: none;" onclick="nextTrainerQuestion()">Siguiente Enunciado ➔</button>'
        '<button class="btn btn-ghost" onclick="resetTrainer()">Reiniciar Simulador</button>'
        '</div></div></div>'
    )
    target_pos = html_body.find("### Árbol de Decisión Rápido")
    if target_pos == -1:
        target_pos = html_body.find("<h3>Árbol de Decisión Rápido</h3>")
    if target_pos != -1:
        end_of_tree = html_body.find("<h3>Tabla de Señales y Disparadores Léxicos</h3>", target_pos)
        insert_at = end_of_tree if end_of_tree != -1 else target_pos
        html_body = html_body[:insert_at] + trainer_html + html_body[insert_at:]
    else:
        intro_pos = html_body.find("<h2>3. Guía Mental:")
        if intro_pos != -1:
            html_body = html_body[:intro_pos] + trainer_html + html_body[intro_pos:]

    def make_checkbox(m):
        raw_text = m.group(1)
        check_id = "chk_" + str(abs(hash(raw_text)) % 100000)
        return (
            f'<li class="checklist-interactive-item"><label class="chk-label">'
            f'<input type="checkbox" class="exam-checklist-input" data-chk-id="{check_id}" onchange="toggleChecklistItem(\'{check_id}\', this.checked)">'
            f'<span class="chk-custom"></span><span class="chk-text">{raw_text}</span></label></li>'
        )
    html_body = re.sub(r"<li>\[ \]\s*(.*?)</li>", make_checkbox, html_body)

    empty_state_html = (
        '<div class="search-empty-state" id="searchEmptyState" style="display: none;">'
        '<div class="empty-state-icon">🔍</div>'
        '<h3 class="empty-state-title">No se encontraron ejercicios con los filtros actuales</h3>'
        '<p class="empty-state-desc">Probá con otro término de búsqueda, cambiá la dificultad o seleccioná el modo <strong>Todos</strong>.</p>'
        '<button class="btn btn-primary" type="button" onclick="resetAllFilters()">Restablecer filtros y mostrar todos</button>'
        '</div>'
    )
    return html_body + empty_state_html

def get_hud_and_drawer_html(active_paradigm="all"):
    pills_config = [
        ("all", "index.html", "📚 Todos (83)"),
        ("dyc", "dyc.html", "🔷 DyC (12)"),
        ("greedy", "greedy.html", "🔶 Greedy (26)"),
        ("backtracking", "backtracking.html", "🟣 Backtracking (14)"),
        ("dp", "dp.html", "🟢 Prog. Dinámica (7)"),
        ("pl", "pl.html", "🔵 Prog. Lineal (6)"),
        ("flujo", "flujo.html", "🔴 Redes de Flujo (5)"),
        ("reducciones", "reducciones.html", "🟡 Reducciones NP (4)"),
        ("integradores", "integradores.html", "⚡ Integradores (5)"),
        ("tipo_parcial", "tipo_parcial.html", "📝 Tipo Parcial (4)")
    ]
    rendered_pills = "".join(
        f'<a href="{href}" class="pill-btn{" active" if key == active_paradigm else ""}" data-paradigm="{key}">{label}</a>'
        for key, href, label in pills_config
    )
    html_template = r"""<header class="hud-top-bar" id="hudTopBar">
  <div class="hud-container">
    <div class="hud-row-primary">
      <div class="hud-brand">
        <a href="index.html" style="text-decoration: none; color: inherit; display: flex; align-items: center; gap: 8px;">
          <span class="hud-logo-icon">🚀</span>
          <div><h1 class="hud-title">TDA — Guía Interactiva de Parciales</h1><span class="hud-subtitle">Edición Intensiva: Salvando el Cuatrimestre (2024–2026)</span></div>
        </a>
      </div>
      <div class="hud-mode-selector" role="group" aria-label="Modo de Estudio">
        <button class="mode-btn active" id="btnModeEmergency" onclick="setStudyMode('emergency')" title="Mostrar solo los ejercicios 🔴 IMPRESCINDIBLES de examen">
          <span class="mode-icon">⚡</span><span class="mode-label"><span class="mode-label-long">Modo Emergencia (48-72h)</span><span class="mode-label-short">48-72h</span></span><span class="mode-badge" id="badgeEmergencyCount">50</span>
        </button>
        <button class="mode-btn" id="btnModeTactical" onclick="setStudyMode('tactical')" title="Mostrar ejercicios pendientes de dominar y casos 🟡 IMPORTANTES">
          <span class="mode-icon">🎯</span><span class="mode-label"><span class="mode-label-long">Modo Táctico (Pendientes)</span><span class="mode-label-short">Táctico</span></span><span class="mode-badge" id="badgeTacticalCount">83</span>
        </button>
        <button class="mode-btn" id="btnModeAll" onclick="setStudyMode('all')" title="Mostrar todos los ejercicios de esta vista">
          <span class="mode-icon">📚</span><span class="mode-label"><span class="mode-label-long">Todos</span><span class="mode-label-short">Todos</span></span><span class="mode-badge" id="badgeAllCount">83</span>
        </button>
      </div>
      <div class="hud-quick-tools">
        <button class="tool-btn highlight-tool" onclick="scrollToExercise(78)" title="Ver La Mochila resuelta en todos los paradigmas"><span class="tool-icon">🎒</span> <span class="tool-text">Mochila Multi-P</span></button>
        <button class="tool-btn highlight-tool" onclick="scrollToExercise(79)" title="Ver El Viajante (TSP) resuelto en todos los paradigmas"><span class="tool-icon">🚗</span> <span class="tool-text">Viajante Multi-P</span></button>
        <button class="tool-btn" onclick="toggleGlobalSolutions()" id="btnGlobalSolutions" title="Ocultar o mostrar todas las soluciones (Active Recall)"><span class="tool-icon">👁️</span> <span class="tool-text" id="lblGlobalSolutions">Soluciones</span></button>
        <button class="tool-btn" onclick="openCheatsheet()" title="Abrir recetas rápidas y Teorema Maestro"><span class="tool-icon">📐</span> <span class="tool-text">Fórmulas</span></button>
        <button class="tool-btn" onclick="scrollToTrainer()" title="Ir al simulador de reconocimiento en 30 segundos"><span class="tool-icon">⚡</span> <span class="tool-text">Simulador 30s</span></button>
        <button class="tool-btn" onclick="toggleDarkMode()" id="btnDarkMode" title="Cambiar modo claro / oscuro"><span class="tool-icon" id="darkModeIcon">🌙</span></button>
      </div>
    </div>
    <div class="hud-row-secondary">
      <div class="hud-progress-wrap">
        <div class="progress-info"><span class="progress-title">Progreso en vista activa:</span><span class="progress-numbers"><strong id="progMastered">0</strong> de <span id="progTotal">83</span> dominados (<span id="progPercent">0%</span>)</span></div>
        <div class="progress-track"><div class="progress-fill" id="progressFill" style="width: 0%;"></div></div>
      </div>
      <div class="difficulty-filter-group d-flex align-items-center gap-1 flex-wrap" role="group" aria-label="Filtrar por dificultad">
        <span class="diff-filter-label small text-muted fw-semibold me-1">Dificultad:</span>
        <button type="button" class="diff-btn active" data-diff="all" onclick="setDifficultyFilter('all')">Todas</button>
        <button type="button" class="diff-btn" data-diff="1" onclick="setDifficultyFilter('1')" title="Nivel 1/5">1★</button>
        <button type="button" class="diff-btn" data-diff="2" onclick="setDifficultyFilter('2')" title="Nivel 2/5">2★</button>
        <button type="button" class="diff-btn" data-diff="3" onclick="setDifficultyFilter('3')" title="Nivel 3/5">3★</button>
        <button type="button" class="diff-btn" data-diff="4" onclick="setDifficultyFilter('4')" title="Nivel 4/5">4★</button>
        <button type="button" class="diff-btn" data-diff="5" onclick="setDifficultyFilter('5')" title="Nivel 5/5">5★</button>
      </div>
      <div class="hud-search-box">
        <span class="search-icon">🔍</span>
        <input type="text" id="exerciseSearch" placeholder="Buscar ejercicio (tecla /): mochila, tsp, held-karp, arnook, invap..." oninput="handleSearch(this.value)">
        <button class="clear-search-btn" id="clearSearchBtn" onclick="clearSearch()" style="display: none;" title="Limpiar búsqueda">✕</button>
      </div>
    </div>
    <div class="hud-row-pills"><div class="filter-pills-scroll" id="paradigmPills"><!-- REND_PILLS --></div></div>
  </div>
  <div class="emergency-banner" id="emergencyBanner">
    <div class="banner-inner"><span class="banner-icon">⚡</span><span><strong>Modo Emergencia (48–72h):</strong> Mostrando los <strong id="emergencyBannerCount">50</strong> ejercicios 🔴 <strong>IMPRESCINDIBLES</strong> de exámenes reales en esta vista.</span><button class="banner-dismiss" onclick="dismissBanner()" title="Ocultar aviso">✕</button></div>
  </div>
</header>
<div class="drawer-backdrop" id="drawerBackdrop" onclick="closeCheatsheet()"></div>
<aside class="cheatsheet-drawer" id="cheatsheetDrawer" aria-hidden="true">
  <div class="drawer-header"><div class="drawer-title-group"><span class="drawer-icon">📐</span><h2>Fórmulas y Recetas Rápidas de Parcial</h2></div><button class="drawer-close-btn" onclick="closeCheatsheet()" aria-label="Cerrar">✕</button></div>
  <div class="drawer-content">
    <section class="drawer-section"><h3>1. Teorema Maestro (División y Conquista)</h3><div class="formula-card">$$T(n) = a \cdot T(n/b) + \Theta(n^c) \quad (a \ge 1, \; b > 1, \; c \ge 0)$$<ul><li><strong>Caso 1 (Hojas dominan):</strong> Si $\log_b a > c \implies T(n) = \Theta(n^{\log_b a})$</li><li><strong>Caso 2 (Balance):</strong> Si $\log_b a = c \implies T(n) = \Theta(n^c \log n)$</li><li><strong>Caso 3 (Raíz domina):</strong> Si $\log_b a < c \implies T(n) = \Theta(n^c)$ <em>(con $a \cdot f(n/b) \le k \cdot f(n)$)</em></li></ul></div></section>
    <section class="drawer-section"><h3>2. Esquema de 4 Pasos Obligatorios para NP-C</h3><ol class="steps-list"><li><strong>Certificado y Verificador en NP:</strong> Definir certificado polinomial $C$ y verificador $V(I_B, C)$ en tiempo $O(n^k)$.</li><li><strong>Problema conocido en NPC:</strong> Seleccionar problema base $A \in \text{NPC}$ (Vertex Cover, 3-SAT, Ciclo Ham, Subset Sum) y reducir $A \le_P B$.</li><li><strong>Transformación polinomial:</strong> Definir $f(I_A) \to I_B$ computable en tiempo polinomial.</li><li><strong>Demostración Bidireccional:</strong> Ida ($I_A \in \text{YES}_A \implies f(I_A) \in \text{YES}_B$) y Vuelta ($f(I_A) \in \text{YES}_B \implies I_A \in \text{YES}_A$).</li></ol></section>
    <section class="drawer-section"><h3>3. Los 5 Pasos de Programación Dinámica</h3><ol class="steps-list"><li><strong>Definición semántica del Estado:</strong> Explicar con palabras qué significa $OPT(i, w)$.</li><li><strong>Casos Base:</strong> Inicializar explícitamente celdas triviales y estados infactibles ($-\infty$ o $+\infty$).</li><li><strong>Ecuación de Recurrencia:</strong> Decisión local, ej. $OPT(i, w) = \max\big(OPT(i-1, w), \; OPT(i-1, w - w_i) + v_i\big)$.</li><li><strong>Orden de Llenado:</strong> Especificar dirección bottom-up (filas crecientes, columnas crecientes).</li><li><strong>Algoritmo de Reconstrucción:</strong> Rastrear las decisiones hacia atrás en la tabla para devolver los ítems.</li></ol></section>
    <section class="drawer-section"><h3>4. Reglas de Oro de Programación Lineal (PLI)</h3><ul><li>Definir variables de decisión con su dominio explícito ($x_i \in \{0, 1\}$ o $y_j \ge 0$).</li><li><strong>¡PROHIBIDO!</strong> Multiplicar variables de decisión ($x_i \cdot y_j$ anula el ejercicio; usar acotación con Big-$M$).</li><li><strong>Linealizar Min-Max / Max-Min:</strong> $\min Z$ sujeto a $Z \ge f_i(x)$ para todo $i$.</li><li>Contar explícitamente cantidad de variables y restricciones en función de la entrada.</li></ul></section>
    <section class="drawer-section"><h3>5. Redes de Flujo (Ford-Fulkerson / Edmonds-Karp)</h3><ul><li>Construir super-fuente $s$ y super-sumidero $t$ para entradas/salidas múltiples.</li><li>Capacidades en aristas dirigidas. Red residual $G_f$ con aristas backward de capacidad $c_f(v, u) = f(u, v)$.</li><li><strong>Teorema Max-Flow Min-Cut:</strong> $|f^*| = C(A, B) = \sum_{u \in A, v \in B} c(u, v)$.</li><li><strong>Teorema de Integralidad:</strong> Capacidades enteras garantizan flujo entero $f(e) \in \mathbb{Z}_{\ge 0}$.</li></ul></section>
    <section class="drawer-section warning-box"><h3>⚠️ Errores Prohibidos que Anulan el Ejercicio</h3><ul><li>❌ <strong>Reducir al revés en NP-C:</strong> Jamás hagas $B \le_P A$. Siempre $A_{\text{conocido}} \le_P B_{\text{nuevo}}$.</li><li>❌ <strong>Afirmar optimalidad en Greedy sin prueba:</strong> Requiere inducción por <em>Greedy Stays Ahead</em> o <em>Intercambio</em>.</li><li>❌ <strong>Olvidar casos base en DP:</strong> Asumir $0$ en estados infactibles corrompe la solución.</li><li>❌ <strong>Omitir aristas residuales backward en Flujo:</strong> No es Ford-Fulkerson sin ellas.</li></ul></section>
  </div>
</aside>
<div class="floating-quick-btn" id="floatingQuickBtn">
  <button class="fab-btn" onclick="openCheatsheet()" title="Fórmulas Rápidas">📐 Recetas</button>
  <button class="fab-btn fab-secondary" onclick="scrollToTop()" title="Volver Arriba">⬆️</button>
</div>"""
    return html_template.replace("<!-- REND_PILLS -->", rendered_pills)

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
            if m.group(1) == "  ":
                line = "    " + line.lstrip()
            if new_lines and new_lines[-1].strip() != "" and not bullet_regex.match(new_lines[-1]):
                new_lines.append("")
        new_lines.append(line)
    return "\n".join(new_lines)

def convert_markdown_to_html(md_text):
    code_placeholders = []
    def save_code(match):
        code_placeholders.append(match.group(0))
        return f"%%CODE_BLK_{len(code_placeholders) - 1}%%"

    md_text = re.sub(r"(```[\s\S]*?```)", save_code, md_text)
    md_text = re.sub(r"(`[^`\n]+?`)", save_code, md_text)

    math_placeholders = []
    def save_math(match):
        math_placeholders.append(match.group(0))
        return f"%%MATH_BLK_{len(math_placeholders) - 1}%%"

    md_text = re.sub(r"\$\$(.+?)\$\$", save_math, md_text, flags=re.DOTALL)
    md_text = re.sub(r"(?<!\\)\$(?!\$)([^\n]+?)(?<!\\)\$", save_math, md_text)

    for idx, raw_code in enumerate(code_placeholders):
        md_text = md_text.replace(f"%%CODE_BLK_{idx}%%", raw_code)

    html_raw = markdown.markdown(md_text, extensions=["fenced_code", "tables"])

    for idx, raw_math in enumerate(math_placeholders):
        html_raw = html_raw.replace(f"%%MATH_BLK_{idx}%%", html.escape(raw_math))

    return html_raw

def compact_html_outside_pre(html_str):
    pre_blocks = []
    def save_pre(m):
        pre_blocks.append(m.group(0))
        return f"%%PRE_BLOCK_{len(pre_blocks) - 1}%%"

    temp = re.sub(r"<pre[\s\S]*?</pre>", save_pre, html_str)
    lines = [line.strip() for line in temp.splitlines() if line.strip()]
    temp = "\n".join(lines)
    temp = re.sub(r"(</(?:li|tr|td|th|span|strong|em|a|button|label|summary)>)\n(<)", r"\1\2", temp)
    temp = re.sub(r"(<(?:ul|ol|thead|tbody|tr|div|header|article|details|section)[^>]*>)\n(<)", r"\1\2", temp)
    for idx, block in enumerate(pre_blocks):
        temp = temp.replace(f"%%PRE_BLOCK_{idx}%%", block)
    return temp + "\n"

def build_interactive_html(md_text, output_file, active_paradigm="all", page_title=None):
    import os
    import json
    title_text = "Teoría de Algoritmos — Guía Interactiva de Parciales (FIUBA)"
    if page_title:
        title_text = f"Teoría de Algoritmos — {page_title} (FIUBA)"

    md_text = normalize_markdown_lists(md_text)
    html_raw = convert_markdown_to_html(md_text)
    html_with_cards = process_html_exercises(html_raw)
    html_with_widgets = inject_interactive_widgets(html_with_cards)
    hud_and_drawer = get_hud_and_drawer_html(active_paradigm=active_paradigm)

    extra_bundle_script = ""
    if active_paradigm == "all":
        split_idx = html_with_widgets.find("<h2>4. Tema 1:")
        if split_idx != -1:
            intro_part = html_with_widgets[:split_idx]
            catalog_part = compact_html_outside_pre(html_with_widgets[split_idx:])
            base_dir = os.path.dirname(os.path.abspath(output_file))
            js_dir = os.path.join(base_dir, "assets", "js")
            os.makedirs(js_dir, exist_ok=True)
            bundle_path = os.path.join(js_dir, "catalog-bundle.js")
            with open(bundle_path, "w", encoding="utf-8") as bf:
                bf.write(
                    "// Catálogo modular precompilado de los 83 ejercicios para index.html\n"
                    "(function(){\n"
                    "  var mount = document.getElementById('tdaCatalogMount');\n"
                    "  if (mount) { mount.innerHTML = " + json.dumps(catalog_part, ensure_ascii=False) + "; }\n"
                    "})();\n"
                )
            html_with_widgets = intro_part + '\n<div id="tdaCatalogMount"></div>'
            extra_bundle_script = '<script src="assets/js/catalog-bundle.js"></script>\n'

    final_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_text}</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
{hud_and_drawer}
<main class="main-content-wrapper container-xl">
{html_with_widgets}
</main>
{extra_bundle_script}<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" defer></script>
<script src="assets/js/app.js" defer></script>
</body>
</html>
"""
    final_html = compact_html_outside_pre(final_html)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)
    return output_file
