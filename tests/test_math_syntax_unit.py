"""Pruebas unitarias para la sintaxis matemática, delimitadores KaTeX y conversiones en todos los ejercicios."""

import os
import re
import glob
import unittest
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUILDER_DIR = os.path.join(BASE_DIR, "builder")
if BUILDER_DIR not in sys.path:
    sys.path.insert(0, BUILDER_DIR)

import html_interactive_builder


class TestMathSyntaxUnit(unittest.TestCase):
    """Pruebas unitarias sobre las fórmulas matemáticas y el compilador Markdown -> HTML."""

    @classmethod
    def setUpClass(cls):
        cls.module_paths = sorted(glob.glob(os.path.join(BUILDER_DIR, "sec*.py")))
        if len(cls.module_paths) == 0:
            raise RuntimeError("No se encontraron módulos sec*.py en builder/")

    def _get_clean_content_no_code(self, content):
        """Elimina bloques de código cercados y código inline para analizar solo texto y fórmulas."""
        clean = re.sub(r"```[\s\S]*?```", "", content)
        clean = re.sub(r"`[^`\n]+?`", "", clean)
        return clean

    def test_all_modules_balanced_math_delimiters(self):
        """Verifica que todos los delimitadores matemáticos ($ y $$) estén perfectamente balanceados y cerrados."""
        for mod_path in self.module_paths:
            mod_name = os.path.basename(mod_path)
            with open(mod_path, "r", encoding="utf-8") as f:
                content = f.read()

            clean = self._get_clean_content_no_code(content)

            # 1. Verificar $$ display math
            display_count = clean.count("$$")
            self.assertEqual(
                display_count % 2, 0,
                f"[{mod_name}] Cantidad impar de delimitadores '$$' ({display_count}). Hay un display math sin cerrar."
            )

            # 2. Remover $$...$$ para analizar inline math $
            clean_no_display = re.sub(r"\$\$[\s\S]*?\$\$", "", clean)

            # Contar delimitadores de inline math (excluyendo \$ escapados)
            inline_delimiters = list(re.finditer(r"(?<!\\)\$", clean_no_display))
            self.assertEqual(
                len(inline_delimiters) % 2, 0,
                f"[{mod_name}] Cantidad impar de delimitadores inline '$' ({len(inline_delimiters)}). "
                f"Hay una fórmula inline sin cerrar."
            )

    def test_no_bare_escaped_dollars_outside_math(self):
        """Verifica que ningún módulo contenga '\\$' suelto en texto plano que provoque backslashes visibles."""
        for mod_path in self.module_paths:
            mod_name = os.path.basename(mod_path)
            with open(mod_path, "r", encoding="utf-8") as f:
                content = f.read()

            clean = self._get_clean_content_no_code(content)
            # Quitar display math
            clean = re.sub(r"\$\$[\s\S]*?\$\$", "", clean)
            # Quitar inline math bien formado
            clean = re.sub(r"(?<!\\)\$(?!\$)[^\n]+?(?<!\\)\$", "", clean)

            # Buscar cualquier '\$' restante en texto plano
            bare_dollars = list(re.finditer(r"\\\$", clean))
            self.assertEqual(
                len(bare_dollars), 0,
                f"[{mod_name}] Se encontraron {len(bare_dollars)} signos '\\$' sueltos fuera de modo matemático. "
                f"En KaTeX/HTML esto produce barras invertidas visibles como '\\$10'. "
                f"Deben envolverse en modo matemático '$\\$10$' o formatearse numéricamente."
            )

    def test_no_leaked_latex_commands_in_plain_text(self):
        """Verifica que comandos canónicos de LaTeX no aparezcan sueltos como texto plano sin renderizar."""
        latex_commands = [
            r"\\ge\b", r"\\le\b", r"\\sum\b", r"\\Theta\b", r"\\Omega\b",
            r"\\forall\b", r"\\exists\b", r"\\in\b", r"\\subset\b",
            r"\\dots\b", r"\\cdots\b", r"\\times\b", r"\\div\b"
        ]

        for mod_path in self.module_paths:
            mod_name = os.path.basename(mod_path)
            with open(mod_path, "r", encoding="utf-8") as f:
                content = f.read()

            clean = self._get_clean_content_no_code(content)
            clean = re.sub(r"\$\$[\s\S]*?\$\$", "", clean)
            clean = re.sub(r"(?<!\\)\$(?!\$)[^\n]+?(?<!\\)\$", "", clean)

            for cmd in latex_commands:
                leaks = list(re.finditer(cmd, clean))
                self.assertEqual(
                    len(leaks), 0,
                    f"[{mod_name}] El comando LaTeX '{cmd}' aparece suelto en texto plano sin delimitar por '$'."
                )

    def test_math_blocks_balanced_braces(self):
        """Verifica que dentro de cada bloque matemático las llaves de agrupación { } estén balanceadas."""
        for mod_path in self.module_paths:
            mod_name = os.path.basename(mod_path)
            with open(mod_path, "r", encoding="utf-8") as f:
                content = f.read()

            clean = self._get_clean_content_no_code(content)

            # Extraer display math
            display_blocks = re.findall(r"\$\$(.+?)\$\$", clean, flags=re.DOTALL)
            # Extraer inline math
            clean_no_display = re.sub(r"\$\$[\s\S]*?\$\$", "", clean)
            inline_blocks = re.findall(r"(?<!\\)\$(?!\$)([^\n]+?)(?<!\\)\$", clean_no_display)

            for block in display_blocks + inline_blocks:
                # Quitar \{ y \} que son llaves literales escapadas
                braces_only = re.sub(r"\\[{}]", "", block)
                open_braces = braces_only.count("{")
                close_braces = braces_only.count("}")
                self.assertEqual(
                    open_braces, close_braces,
                    f"[{mod_name}] Llaves desbalanceadas en fórmula: '${block}$' ({open_braces} '{{' vs {close_braces} '}}')"
                )

    def test_no_empty_math_blocks(self):
        """Verifica que no existan delimitadores vacíos ($$ o $$$$)."""
        for mod_path in self.module_paths:
            mod_name = os.path.basename(mod_path)
            with open(mod_path, "r", encoding="utf-8") as f:
                content = f.read()

            clean = self._get_clean_content_no_code(content)
            display_blocks = re.findall(r"\$\$(.*?)\$\$", clean, flags=re.DOTALL)
            empty_display = [b for b in display_blocks if not b.strip()]
            self.assertEqual(
                len(empty_display), 0,
                f"[{mod_name}] Se encontraron {len(empty_display)} bloques display vacíos '$$ $$'."
            )

            clean_no_display = re.sub(r"\$\$[\s\S]*?\$\$", "", clean)
            inline_blocks = re.findall(r"(?<!\\)\$(?!\$)([^\n]*?)(?<!\\)\$", clean_no_display)
            empty_inline = [b for b in inline_blocks if not b.strip()]
            self.assertEqual(
                len(empty_inline), 0,
                f"[{mod_name}] Se encontraron {len(empty_inline)} bloques inline vacíos '$ $'."
            )

    def test_html_builder_math_conversion_unit(self):
        """Prueba unitaria de convert_markdown_to_html para casos límite de KaTeX."""
        sample_md = (
            "Texto inicial.\n\n"
            "* Fórmula simple: $i + 3 \\ge N + 1$\n"
            "* Fórmula con conjunto: $\\{i+1, \\; i+2, \\; i+3\\}$\n"
            "* Fórmula con moneda: **Costo = $\\$5 + \\$6 = \\$11$**\n"
            "* Fórmula con comparación: **Costo Óptimo = $\\$6 < \\$11$**\n"
            "* Display math:\n"
            "$$OPT(i) = T[i] + \\min(OPT(i-1), OPT(i-2))$$\n\n"
            "Código que contiene signos pesos no debe romperse:\n"
            "```bash\n"
            "export PATH=$PATH:/usr/local/bin\n"
            "```\n"
        )
        html_out = html_interactive_builder.convert_markdown_to_html(sample_md)

        # 1. Asegurar que los delimitadores de math permanecen para KaTeX auto-render
        self.assertIn("$i + 3 \\ge N + 1$", html_out)
        self.assertIn("$\\{i+1, \\; i+2, \\; i+3\\}$", html_out)
        self.assertIn("$\\$5 + \\$6 = \\$11$", html_out)
        self.assertIn("$$OPT(i) = T[i] + \\min(OPT(i-1), OPT(i-2))$$", html_out)

        # 2. Asegurar que no hay placeholders de math sin resolver
        self.assertNotIn("%%MATH_BLK_", html_out)
        self.assertNotIn("%%CODE_BLK_", html_out)

        # 3. Asegurar que no hay barras invertidas sueltas fuera de math
        self.assertNotIn("(\\$10)", html_out)

    def test_exercise_18_formulas_exact(self):
        """Verificación unitaria específica para el Ejercicio 18: todas las fórmulas deben estar bien formadas."""
        import sec03_greedy
        content = sec03_greedy.get_content()

        self.assertIn("### Ejercicio 18 — Ruta de Transporte con Estaciones", content)
        ej18_text = content[content.find("### Ejercicio 18"):content.find("### Ejercicio 18") + 3500]

        # Comprobar fórmulas clave de la Regla Voraz
        self.assertIn("$i + 3 \\ge N + 1$", ej18_text)
        self.assertIn("$\\{i+1, \\; i+2, \\; i+3\\}$", ej18_text)
        self.assertIn("$(i+1, \\; i+2, \\; i+3)$", ej18_text)

        # Comprobar instancia óptima
        self.assertIn("$T = [10, 20, 5]$", ej18_text)
        self.assertIn("($\\$10$)", ej18_text)
        self.assertIn("($\\$20$)", ej18_text)
        self.assertIn("($\\$5$)", ej18_text)
        self.assertIn("**Costo Greedy = $\\$5$**", ej18_text)

        # Comprobar contraejemplo
        self.assertIn("$T = [5, 6, 100, 100]$", ej18_text)
        self.assertIn("($\\$5$)", ej18_text)
        self.assertIn("($\\$6$)", ej18_text)
        self.assertIn("($\\$100$)", ej18_text)
        self.assertIn("**Costo Greedy = $\\$5 + \\$6 = \\$11$**", ej18_text)
        self.assertIn("**Costo Óptimo = $\\$6 < \\$11$**", ej18_text)

        # Verificar que NO queden signos \$ sueltos sin $ en Ejercicio 18
        clean = self._get_clean_content_no_code(ej18_text)
        clean = re.sub(r"(?<!\\)\$(?!\$)[^\n]+?(?<!\\)\$", "", clean)
        self.assertNotIn("\\$", clean, "El Ejercicio 18 todavía tiene signos '\\$' sueltos en texto plano.")


if __name__ == "__main__":
    unittest.main()
