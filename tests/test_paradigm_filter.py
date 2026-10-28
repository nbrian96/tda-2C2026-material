"""Pruebas unitarias y de integración para la persistencia y filtrado por paradigma.

Verifica que:
1. No existan reordenamientos destructivos del DOM que desprendan las tarjetas de sus patrones.
2. Las tarjetas de ejercicio se encuentren adyacentes a sus patrones correspondientes.
3. El filtrado por paradigma y el restablecimiento a 'all' conserve la visibilidad e integridad de los 79 ejercicios.
"""

import os
import re
import json
import unittest

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TestParadigmFilterIntegrity(unittest.TestCase):

    def test_no_destructive_dom_sorting_in_app_js(self):
        """Verifica que app.js no contenga sortCardsByDifficulty() que desmonte las tarjetas del DOM."""
        app_js_path = os.path.join(BASE_DIR, "assets", "js", "app.js")
        with open(app_js_path, "r", encoding="utf-8") as f:
            content = f.read()
        self.assertNotIn("function sortCardsByDifficulty", content,
                         "sortCardsByDifficulty no debe estar definido en app.js porque rompe la jerarquía de patrones.")
        self.assertNotIn("sortCardsByDifficulty()", content,
                         "sortCardsByDifficulty() no debe ejecutarse en DOMContentLoaded.")

    def test_catalog_bundle_cards_under_patterns(self):
        """Verifica que en el bundle de index.html cada patrón contenga su tarjeta inmediatamente adyacente."""
        bundle_path = os.path.join(BASE_DIR, "assets", "js", "catalog-bundle.js")
        with open(bundle_path, "r", encoding="utf-8") as f:
            raw = f.read()

        prefix = "mount.innerHTML = "
        start = raw.find(prefix)
        end = raw.rfind("; }")
        self.assertNotEqual(start, -1, "No se encontró mount.innerHTML en catalog-bundle.js")
        content = json.loads(raw[start + len(prefix):end].strip())

        # En DP, verificar que Ejercicio 53 esté entre Patrón 4.1 y Patrón 4.2
        pos_p41 = content.find("Patrón de Ejercicio 4.1")
        pos_ej53 = content.find('id="ej-53"')
        pos_p42 = content.find("Patrón de Ejercicio 4.2")
        pos_ej54 = content.find('id="ej-54"')

        self.assertNotEqual(pos_p41, -1, "Debe existir Patrón 4.1")
        self.assertNotEqual(pos_ej53, -1, "Debe existir ej-53")
        self.assertNotEqual(pos_p42, -1, "Debe existir Patrón 4.2")
        self.assertNotEqual(pos_ej54, -1, "Debe existir ej-54")

        self.assertTrue(pos_p41 < pos_ej53 < pos_p42,
                        "El Ejercicio 53 debe ubicarse inmediatamente debajo del Patrón 4.1 y antes del Patrón 4.2.")
        self.assertTrue(pos_p42 < pos_ej54,
                        "El Ejercicio 54 debe ubicarse inmediatamente debajo del Patrón 4.2.")

    def test_all_79_cards_have_valid_paradigm_attribute(self):
        """Verifica que las 79 tarjetas posean un data-paradigm válido correspondiente a uno de los 8 temas."""
        bundle_path = os.path.join(BASE_DIR, "assets", "js", "catalog-bundle.js")
        with open(bundle_path, "r", encoding="utf-8") as f:
            raw = f.read()

        prefix = "mount.innerHTML = "
        start = raw.find(prefix)
        end = raw.rfind("; }")
        content = json.loads(raw[start + len(prefix):end].strip())

        cards = re.findall(r'<article class="exercise-card"[^>]*id="(ej-\d+)"[^>]*data-paradigm="([^"]+)"', content)
        self.assertEqual(len(cards), 79, "Deben existir exactamente 79 tarjetas en el catálogo.")

        valid_paradigms = {"dyc", "greedy", "backtracking", "dp", "pl", "flujo", "reducciones", "integradores"}
        counts = {}
        for ej, p in cards:
            self.assertIn(p, valid_paradigms, f"{ej} tiene un data-paradigm inválido: {p}")
            counts[p] = counts.get(p, 0) + 1

        self.assertEqual(counts["dyc"], 12)
        self.assertEqual(counts["greedy"], 26)
        self.assertEqual(counts["backtracking"], 14)
        self.assertEqual(counts["dp"], 7)
        self.assertEqual(counts["pl"], 6)
        self.assertEqual(counts["flujo"], 5)
        self.assertEqual(counts["reducciones"], 4)
        self.assertEqual(counts["integradores"], 5)

    def test_filter_simulation_all_and_paradigm_cycles(self):
        """Simula los ciclos de filtrado: all -> dp -> all -> parciales -> all, validando los conteos esperados."""
        bundle_path = os.path.join(BASE_DIR, "assets", "js", "catalog-bundle.js")
        with open(bundle_path, "r", encoding="utf-8") as f:
            raw = f.read()

        prefix = "mount.innerHTML = "
        start = raw.find(prefix)
        end = raw.rfind("; }")
        content = json.loads(raw[start + len(prefix):end].strip())

        card_matches = list(re.finditer(r'<article class="exercise-card"[^>]*id="(ej-\d+)"[^>]*data-paradigm="([^"]+)"[^>]*data-parcial="([^"]+)"', content))
        self.assertEqual(len(card_matches), 79)

        def simulate_filter(paradigm):
            visible = []
            for m in card_matches:
                ej = m.group(1)
                p = m.group(2)
                is_parcial = m.group(3) == "true"
                if paradigm == "all":
                    matches = True
                elif paradigm == "parciales":
                    matches = is_parcial
                else:
                    matches = (p == paradigm)
                if matches:
                    visible.append(ej)
            return visible

        # 1. Todos activo
        self.assertEqual(len(simulate_filter("all")), 79)

        # 2. Filtrar por DP
        dp_cards = simulate_filter("dp")
        self.assertEqual(len(dp_cards), 7)
        self.assertIn("ej-53", dp_cards)
        self.assertIn("ej-59", dp_cards)

        # 3. Volver a elegir Todos
        all_cards = simulate_filter("all")
        self.assertEqual(len(all_cards), 79)
        self.assertIn("ej-1", all_cards)
        self.assertIn("ej-53", all_cards)
        self.assertIn("ej-79", all_cards)

        # 4. Filtrar por Parciales
        parcial_cards = simulate_filter("parciales")
        self.assertEqual(len(parcial_cards), 29)

        # 5. Volver a elegir Todos nuevamente
        self.assertEqual(len(simulate_filter("all")), 79)

if __name__ == "__main__":
    unittest.main()
