"""Pruebas unitarias y de integración para Modo Oscuro (Dark Mode) y Responsividad Móvil (Vertical y Horizontal)."""

import os
import glob
import re
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestDarkModeAndResponsive(unittest.TestCase):

    def setUp(self):
        self.css_path = os.path.join(BASE_DIR, "assets", "css", "styles.css")
        self.js_path = os.path.join(BASE_DIR, "assets", "js", "app.js")
        self.html_avanzados_path = os.path.join(BASE_DIR, "teoria-avanzados.html")
        self.html_index_path = os.path.join(BASE_DIR, "index.html")
        
        with open(self.css_path, "r", encoding="utf-8") as f:
            self.css = f.read()
        with open(self.js_path, "r", encoding="utf-8") as f:
            self.js = f.read()
        with open(self.html_avanzados_path, "r", encoding="utf-8") as f:
            self.html_avanzados = f.read()
        with open(self.html_index_path, "r", encoding="utf-8") as f:
            self.html_index = f.read()

    def test_dark_mode_alerts_and_katex(self):
        """Verifica que las alertas Bootstrap y KaTeX tengan soporte completo y alto contraste en dark mode."""
        self.assertIn("body.dark-mode .alert-warning", self.css)
        self.assertIn("body.dark-mode .alert-danger", self.css)
        self.assertIn("body.dark-mode .alert-info", self.css)
        self.assertIn("body.dark-mode .alert-success", self.css)
        self.assertIn("body.dark-mode .alert-secondary", self.css)
        self.assertIn("body.dark-mode .alert-primary", self.css)

        # Fórmulas KaTeX dentro de alertas no deben ser blancas sobre fondo claro
        self.assertIn("body.dark-mode .alert-warning .katex", self.css)
        self.assertIn("body.dark-mode .alert-danger .katex", self.css)
        self.assertIn("body.dark-mode .alert-info .katex", self.css)
        self.assertIn("body.dark-mode .alert-success .katex", self.css)

    def test_dark_mode_badges_and_emphasis_text(self):
        """Verifica que badges y clases de énfasis tengan colores contrastados en dark mode."""
        self.assertIn("body.dark-mode .badge.bg-warning", self.css)
        self.assertIn("body.dark-mode .badge.bg-success", self.css)
        self.assertIn("body.dark-mode .text-warning-emphasis", self.css)
        self.assertIn("body.dark-mode .text-success-emphasis", self.css)
        self.assertIn("body.dark-mode .table", self.css)
        self.assertIn("body.dark-mode .progress", self.css)
        self.assertIn("body.dark-mode .text-muted", self.css)
        self.assertIn("[data-bs-theme=\"dark\"] .text-muted", self.css)

    def test_mobile_portrait_rules(self):
        """Verifica que existan reglas de navegación deslizable y elementos adaptables en mobile vertical."""
        self.assertIn(".site-nav-links", self.css)
        self.assertIn("overflow-x: auto;", self.css)
        self.assertIn("flex-wrap: nowrap;", self.css)
        self.assertIn(".nav-tabs-sticky", self.css)

    def test_mobile_landscape_rules(self):
        """Verifica que existan reglas para celulares en posición horizontal (altura <= 550px)."""
        self.assertIn("@media (max-height: 550px) and (orientation: landscape)", self.css)
        self.assertIn(".graph-svg", self.css)
        self.assertIn("max-height: 160px;", self.css)

    def test_mermaid_dark_mode_styling_and_app_js(self):
        """Verifica que Mermaid tenga reglas CSS específicas para etiquetas de aristas y configuración dark en JS."""
        self.assertIn(".mermaid .edgeLabel", self.css)
        self.assertIn("body.dark-mode .mermaid .edgeLabel", self.css)
        self.assertIn("background-color: #0b1120 !important;", self.css)
        self.assertIn("edgeLabelBackground", self.js)
        self.assertIn("darkMode: true", self.js)

    def test_all_12_html_files_have_early_dark_detection(self):
        """Verifica que los 12 archivos HTML incluyan el script de detección temprana de tema en <head>."""
        html_files = sorted(glob.glob(os.path.join(BASE_DIR, "*.html")))
        self.assertGreaterEqual(len(html_files), 12, "Debe haber al menos 12 archivos HTML en el proyecto.")

        for fpath in html_files:
            fname = os.path.basename(fpath)
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()

            self.assertIn("data-bs-theme", content, f"El archivo {fname} debe incluir detección de tema con data-bs-theme en <head>.")
            self.assertIn("width=device-width", content, f"El archivo {fname} debe incluir la etiqueta viewport responsive.")
            self.assertIn("styles.css", content, f"El archivo {fname} debe cargar assets/css/styles.css.")

    def test_index_html_rules_and_portal_badges(self):
        """Verifica que index.html use clases semánticas para listas de examen y badges de portal."""
        self.assertIn("exam-rules-list", self.html_index)
        self.assertIn("exam-errors-list", self.html_index)
        self.assertIn("badge-portal-exam", self.html_index)
        self.assertIn("badge-portal-teoria", self.html_index)
        self.assertIn("site-nav-link-adv", self.html_index)

    def test_teoria_avanzados_mermaid_and_cheatsheet(self):
        """Verifica que teoria-avanzados.html sincronice tema antes de Mermaid y tenga drawer de fórmulas."""
        self.assertIn("id=\"cheatsheetDrawer\"", self.html_avanzados)
        self.assertIn("openCheatsheet()", self.html_avanzados)
        self.assertIn("closeCheatsheet()", self.html_avanzados)
        mermaid_idx = self.html_avanzados.find("mermaid.initialize")
        dark_sync_idx = self.html_avanzados.find("document.body.classList.add(\"dark-mode\")")
        self.assertNotEqual(mermaid_idx, -1)
        self.assertNotEqual(dark_sync_idx, -1)
        self.assertLess(dark_sync_idx, mermaid_idx, "El tema dark-mode debe aplicarse antes de llamar a mermaid.initialize.")

if __name__ == "__main__":
    unittest.main()
