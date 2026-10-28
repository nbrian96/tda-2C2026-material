"""Pruebas unitarias para la validación del comportamiento responsive en Mobile Landscape.

Verifica que:
1. styles.css incluya la media query para landscape / alturas reducidas (<= 520px).
2. Se compacte el HUD Top Bar en landscape: ocultando subtítulo, texto largo de modos, texto de herramientas, barra de progreso y banner de emergencia.
3. Se soporte el auto-ocultamiento del HUD (.hud-hidden) mediante transform: translateY(-100%) y transición suave.
4. app.js contenga la lógica de auto-hide al hacer scroll hacia abajo en dispositivos móviles/landscape.
"""

import os
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestResponsiveLandscape(unittest.TestCase):

    def setUp(self):
        self.css_path = os.path.join(BASE_DIR, "assets", "css", "styles.css")
        self.js_path = os.path.join(BASE_DIR, "assets", "js", "app.js")
        with open(self.css_path, "r", encoding="utf-8") as f:
            self.css = f.read()
        with open(self.js_path, "r", encoding="utf-8") as f:
            self.js = f.read()

    def test_landscape_media_query_present(self):
        """Verifica que exista la media query específica para mobile horizontal / altura reducida."""
        self.assertIn("@media (max-height: 520px)", self.css,
                      "Debe existir una media query para max-height: 520px que optimice mobile landscape.")

    def test_landscape_hud_compact_rules(self):
        """Verifica que en landscape se oculten los elementos que abarrotan la pantalla."""
        self.assertIn(".hud-subtitle", self.css)
        self.assertIn(".hud-progress-wrap", self.css)
        self.assertIn(".emergency-banner", self.css)
        # Verificar que se fuerce ocultar en landscape
        self.assertIn("display: none !important;", self.css)

    def test_hud_auto_hide_css_classes(self):
        """Verifica que .hud-top-bar tenga transición y soporte .hud-hidden."""
        self.assertIn(".hud-top-bar.hud-hidden", self.css,
                      "Debe existir la regla .hud-top-bar.hud-hidden para ocultar el navbar en scroll.")
        self.assertIn("transform: translateY(-100%);", self.css,
                      "La clase hud-hidden debe desplazar el HUD fuera de la pantalla.")

    def test_app_js_scroll_auto_hide(self):
        """Verifica que app.js gestione el scroll para auto-ocultar el HUD en móviles/landscape."""
        self.assertIn("initHudScrollAutoHide", self.js,
                      "app.js debe implementar la función de auto-ocultamiento initHudScrollAutoHide.")
        self.assertIn("hud-hidden", self.js,
                      "app.js debe agregar o quitar la clase hud-hidden según la dirección del scroll.")
        self.assertIn("passive: true", self.js,
                      "El listener de scroll debe ser pasivo para máxima fluidez táctil.")

if __name__ == "__main__":
    unittest.main()
