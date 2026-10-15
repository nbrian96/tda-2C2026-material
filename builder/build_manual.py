"""Compilador y Generador del Manual de Parciales de TDA."""

import os
import sys
import subprocess
import markdown

# Importar los módulos individuales de cada sección
import sec01_intro_and_matrix
import sec02_dyc
import sec03_greedy
import sec04_backtracking
import sec05_dp
import sec06_pl
import sec07_flujo
import sec08_reducciones
import sec09_integradores
import sec10_tipo_parcial
import sec11_errores_checklist

BASE_DIR = "/home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material"
MD_FILE = os.path.join(BASE_DIR, "guia_tda_parciales.md")
PDF_FILE = os.path.join(BASE_DIR, "guia_tda_parciales.pdf")
HTML_FILE = os.path.join(BASE_DIR, "guia_tda_parciales.html")

def assemble_markdown():
    print("[1/5] Ensamblando secciones en Markdown...")
    sections = [
        sec01_intro_and_matrix.get_content(),
        sec02_dyc.get_content(),
        sec03_greedy.get_content(),
        sec04_backtracking.get_content(),
        sec05_dp.get_content(),
        sec06_pl.get_content(),
        sec07_flujo.get_content(),
        sec08_reducciones.get_content(),
        sec09_integradores.get_content(),
        sec10_tipo_parcial.get_content(),
        sec11_errores_checklist.get_content()
    ]
    
    full_md = "\n\n---\n\n".join(sections)
    
    with open(MD_FILE, "w", encoding="utf-8") as f:
        f.write(full_md)
        
    print(f"      Markdown generado con éxito en: {MD_FILE}")
    print(f"      Total de caracteres: {len(full_md):,}")
    print(f"      Total de palabras: {len(full_md.split()):,}")
    return full_md

def verify_markdown(md_text):
    print("[2/5] Verificando integridad del Markdown...")
    # Verificar bloques de código cerrados
    triple_backticks = md_text.count("```")
    if triple_backticks % 2 != 0:
        raise ValueError(f"Error de formato: Hay un número impar de bloques de código (```): {triple_backticks}")
    print(f"      Bloques de código cerrados correctamente: {triple_backticks // 2} bloques.")
    
    # Contar ejercicios
    ejercicios = [line for line in md_text.split("\n") if line.startswith("### Ejercicio ")]
    print(f"      Total de ejercicios resueltos encontrados: {len(ejercicios)}")
    for ej in ejercicios:
        print(f"        -> {ej}")

def convert_to_html(md_text):
    print("[3/5] Convirtiendo Markdown a HTML con estilos tipográficos para impresión A4...")
    html_body = markdown.markdown(md_text, extensions=['fenced_code', 'tables'])
    
    # Envolver en un documento HTML con diseño profesional y reglas de paginación
    styled_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<title>Teoría de Algoritmos — Manual Práctico de Resolución de Parciales</title>
<style>
@page {{
    size: A4;
    margin: 18mm 14mm 18mm 14mm;
    @bottom-center {{
        content: "Teoría de Algoritmos — FIUBA | Página " counter(page);
        font-family: 'Liberation Sans', 'Helvetica Neue', Helvetica, Arial, sans-serif;
        font-size: 8pt;
        color: #718096;
    }}
}}

body {{
    font-family: 'Liberation Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.45;
    color: #2d3748;
    background-color: #ffffff;
}}

/* Jerarquía de Títulos */
h1 {{
    font-size: 20pt;
    font-weight: 800;
    color: #1a365d;
    border-bottom: 3px solid #3182ce;
    padding-bottom: 6px;
    margin-top: 0;
    margin-bottom: 12px;
    page-break-before: auto;
    break-after: avoid;
}}

h2 {{
    font-size: 14pt;
    font-weight: 700;
    color: #2b6cb0;
    border-bottom: 1.5px solid #e2e8f0;
    padding-bottom: 4px;
    margin-top: 24px;
    margin-bottom: 10px;
    break-after: avoid;
}}

h3 {{
    font-size: 11.5pt;
    font-weight: 700;
    color: #2c5282;
    margin-top: 18px;
    margin-bottom: 8px;
    break-after: avoid;
}}

h4 {{
    font-size: 10.5pt;
    font-weight: 600;
    color: #4a5568;
    margin-top: 12px;
    margin-bottom: 6px;
    break-after: avoid;
}}

p {{
    margin-top: 0;
    margin-bottom: 8px;
    text-align: justify;
}}

ul, ol {{
    margin-top: 0;
    margin-bottom: 8px;
    padding-left: 22px;
}}

li {{
    margin-bottom: 3px;
}}

hr {{
    border: none;
    border-top: 1px solid #cbd5e0;
    margin: 18px 0;
}}

/* Bloques de Pseudocódigo y Código */
pre {{
    background-color: #f7fafc;
    border: 1px solid #e2e8f0;
    border-left: 4px solid #3182ce;
    border-radius: 4px;
    padding: 8px 12px;
    font-family: 'Liberation Mono', 'DejaVu Sans Mono', Consolas, 'Courier New', monospace;
    font-size: 8.5pt;
    line-height: 1.35;
    color: #1a202c;
    overflow-x: auto;
    margin: 8px 0 12px 0;
    white-space: pre-wrap;
    word-wrap: break-word;
    page-break-inside: avoid;
    break-inside: avoid;
}}

code {{
    font-family: 'Liberation Mono', 'DejaVu Sans Mono', Consolas, 'Courier New', monospace;
    font-size: 8.5pt;
    background-color: #edf2f7;
    padding: 1px 4px;
    border-radius: 3px;
    color: #2c5282;
}}

pre code {{
    background-color: transparent;
    padding: 0;
    color: inherit;
    border-radius: 0;
}}

/* Tablas */
table {{
    width: 100%;
    border-collapse: collapse;
    margin: 10px 0 14px 0;
    font-size: 9pt;
    page-break-inside: avoid;
    break-inside: avoid;
}}

th, td {{
    border: 1px solid #cbd5e0;
    padding: 6px 9px;
    text-align: left;
    vertical-align: top;
}}

th {{
    background-color: #edf2f7;
    font-weight: 700;
    color: #2d3748;
}}

tr:nth-child(even) {{
    background-color: #f7fafc;
}}

/* Énfasis y Citas */
blockquote {{
    border-left: 3.5px solid #4299e1;
    background-color: #ebf8ff;
    padding: 8px 12px;
    margin: 8px 0;
    border-radius: 0 4px 4px 0;
    font-size: 9.5pt;
    color: #2b6cb0;
    page-break-inside: avoid;
    break-inside: avoid;
}}

/* Badges e insignias */
strong {{
    color: #1a202c;
}}

/* Reglas de Paginación para Impresión */
.page-break {{
    page-break-before: always;
    break-before: page;
}}
</style>
</head>
<body>
{html_body}
</body>
</html>
"""
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(styled_html)
    print(f"      HTML renderizado en: {HTML_FILE}")
    return HTML_FILE

def generate_pdf():
    print("[4/5] Compilando PDF usando Google Chrome Headless...")
    cmd = [
        "google-chrome",
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        f"--print-to-pdf={PDF_FILE}",
        "--no-pdf-header-footer",
        HTML_FILE
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"Error al ejecutar google-chrome headless: {res.stderr}")
    print(f"      PDF generado con éxito en: {PDF_FILE}")

def verify_pdf():
    print("[5/5] Verificando archivo PDF generado...")
    if not os.path.exists(PDF_FILE):
        raise FileNotFoundError(f"El archivo PDF no existe: {PDF_FILE}")
        
    size_bytes = os.path.getsize(PDF_FILE)
    print(f"      Tamaño del PDF: {size_bytes / 1024:.1f} KB")
    
    # Extraer texto del PDF con pdftotext para verificar páginas
    res = subprocess.run(["pdftotext", PDF_FILE, "-"], capture_output=True, text=True)
    pages = res.stdout.count("\x0c") # Carácter de salto de página de pdftotext
    print(f"      Cantidad estimada de páginas en el PDF: {pages}")
    
    if pages < 10:
        print("      ADVERTENCIA: Cantidad de páginas inusualmente baja.")
    else:
        print("      Validación de páginas exitosa.")
        
    # Verificar que los temas clave estén presentes en el texto del PDF
    keywords = [
        "Teoría de Algoritmos",
        "División y Conquista",
        "Greedy Stays Ahead",
        "Arnook",
        "Lagrange",
        "8 reinas",
        "Juan el vago",
        "Word Wrap",
        "Ford-Fulkerson",
        "Dominating Set",
        "Marco",
        "Checklist"
    ]
    missing = []
    pdf_text = res.stdout
    for kw in keywords:
        if kw.lower() not in pdf_text.lower():
            missing.append(kw)
            
    if missing:
        print(f"      ADVERTENCIA: No se encontraron las siguientes palabras clave en el PDF: {missing}")
    else:
        print("      Todas las palabras clave de los temas requeridos están verificadas en el PDF.")

def main():
    print("=" * 70)
    print("INICIANDO CONSTRUCCIÓN DEL MANUAL DE PARCIALES DE TDA")
    print("=" * 70)
    md_text = assemble_markdown()
    verify_markdown(md_text)
    convert_to_html(md_text)
    generate_pdf()
    verify_pdf()
    print("=" * 70)
    print("CONSTRUCCIÓN COMPLETADA CON ÉXITO")
    print("=" * 70)

if __name__ == "__main__":
    main()
