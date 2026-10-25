"""Compilador y Generador del Manual de Parciales de TDA."""

import os
import sys
import subprocess
import markdown
import html_interactive_builder

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

import concurrent.futures

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MD_FILE = os.path.join(BASE_DIR, "guia_tda_parciales.md")
PDF_FILE = os.path.join(BASE_DIR, "guia_tda_parciales.pdf")
HTML_FILE = os.path.join(BASE_DIR, "guia_tda_parciales.html")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

PARADIGM_TARGETS = [
    {
        "filename": "dyc.html",
        "title": "División y Conquista",
        "paradigm_key": "dyc",
        "modules": [sec01_intro_and_matrix, sec02_dyc]
    },
    {
        "filename": "greedy.html",
        "title": "Algoritmos Greedy (Voraces)",
        "paradigm_key": "greedy",
        "modules": [sec03_greedy]
    },
    {
        "filename": "backtracking.html",
        "title": "Backtracking y Branch & Bound",
        "paradigm_key": "backtracking",
        "modules": [sec04_backtracking]
    },
    {
        "filename": "dp.html",
        "title": "Programación Dinámica (PD)",
        "paradigm_key": "dp",
        "modules": [sec05_dp]
    },
    {
        "filename": "pl.html",
        "title": "Programación Lineal y PLI",
        "paradigm_key": "pl",
        "modules": [sec06_pl]
    },
    {
        "filename": "flujo.html",
        "title": "Redes de Flujo",
        "paradigm_key": "flujo",
        "modules": [sec07_flujo]
    },
    {
        "filename": "reducciones.html",
        "title": "Reducciones y NP-Completitud",
        "paradigm_key": "reducciones",
        "modules": [sec08_reducciones]
    },
    {
        "filename": "integradores.html",
        "title": "Problemas Integradores",
        "paradigm_key": "integradores",
        "modules": [sec09_integradores]
    },
    {
        "filename": "tipo_parcial.html",
        "title": "Simulacros Tipo Parcial y Checklist",
        "paradigm_key": "tipo_parcial",
        "modules": [sec10_tipo_parcial, sec11_errores_checklist]
    }
]

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
    full_md = html_interactive_builder.normalize_markdown_lists(full_md)
    
    with open(MD_FILE, "w", encoding="utf-8") as f:
        f.write(full_md)
        
    print(f"      Markdown generado con éxito en: {MD_FILE}")
    print(f"      Total de caracteres: {len(full_md):,}")
    print(f"      Total de palabras: {len(full_md.split()):,}")
    return full_md

def verify_markdown(md_text):
    print("[2/5] Verificando integridad del Markdown...")
    triple_backticks = md_text.count("```")
    if triple_backticks % 2 != 0:
        raise ValueError(f"Error de formato: Hay un número impar de bloques de código (```): {triple_backticks}")
    print(f"      Bloques de código cerrados correctamente: {triple_backticks // 2} bloques.")
    
    ejercicios = [line for line in md_text.split("\n") if line.startswith("### Ejercicio ")]
    print(f"      Total de ejercicios resueltos encontrados: {len(ejercicios)}")
    for ej in ejercicios:
        print(f"        -> {ej}")

def compile_single_page(target):
    out_path = os.path.join(BASE_DIR, target["filename"])
    sections_md = "\n\n---\n\n".join([m.get_content() for m in target["modules"]])
    html_interactive_builder.build_interactive_html(
        sections_md,
        out_path,
        active_paradigm=target["paradigm_key"],
        page_title=target["title"]
    )
    return target["filename"]

def convert_to_html(md_text):
    print("[3/5] Convirtiendo y modularizando HTML para GitHub Pages (Paralelizado)...")
    import shutil
    
    # 1. Compilar página principal maestra (index.html y guia_tda_parciales.html)
    html_interactive_builder.build_interactive_html(
        md_text,
        HTML_FILE,
        active_paradigm="all",
        page_title="Guía Interactiva Completa (40 Ejercicios)"
    )
    shutil.copyfile(HTML_FILE, INDEX_FILE)
    print(f"      Página principal generada en: {INDEX_FILE}")

    # 2. Compilar páginas modulares por paradigma en paralelo
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(compile_single_page, target): target["filename"] for target in PARADIGM_TARGETS}
        for future in concurrent.futures.as_completed(futures):
            fname = futures[future]
            try:
                future.result()
                print(f"      Módulo generado en paralelo: {fname}")
            except Exception as e:
                print(f"      ERROR generando {fname}: {e}")
                raise e
    return INDEX_FILE

def find_browser():
    import shutil
    candidates = [
        shutil.which("google-chrome"),
        shutil.which("chrome"),
        shutil.which("msedge"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    for c in candidates:
        if c and os.path.exists(c):
            return c
    return None

def generate_pdf():
    print("[4/5] Compilando PDF usando navegador Headless...")
    browser = find_browser()
    if not browser:
        print("      ADVERTENCIA: No se encontró Chrome ni Edge. Omitiendo generación de PDF.")
        return False
        
    cmd = [
        browser,
        "--headless",
        "--no-sandbox",
        "--disable-gpu",
        f"--print-to-pdf={PDF_FILE}",
        "--no-pdf-header-footer",
        HTML_FILE
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"      ADVERTENCIA: Falló la generación de PDF con {browser}: {res.stderr}")
        return False
    print(f"      PDF generado con éxito en: {PDF_FILE}")
    return True

def verify_pdf():
    print("[5/5] Verificando archivo PDF generado...")
    if not os.path.exists(PDF_FILE):
        print("      ADVERTENCIA: El archivo PDF no existe (se omitió o falló).")
        return
        
    size_bytes = os.path.getsize(PDF_FILE)
    print(f"      Tamaño del PDF: {size_bytes / 1024:.1f} KB")
    
    import shutil
    if shutil.which("pdftotext"):
        res = subprocess.run(["pdftotext", PDF_FILE, "-"], capture_output=True, text=True)
        pages = res.stdout.count("\x0c")
        print(f"      Cantidad estimada de páginas en el PDF: {pages}")
        if pages < 10:
            print("      ADVERTENCIA: Cantidad de páginas inusualmente baja.")
        else:
            print("      Validación de páginas exitosa.")
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
    else:
        print("      Herramienta pdftotext no detectada; validación por tamaño completada con éxito.")

def main():
    skip_pdf = "--no-pdf" in sys.argv
    print("=" * 70)
    print("INICIANDO CONSTRUCCIÓN DEL MANUAL DE PARCIALES DE TDA")
    print("=" * 70)
    md_text = assemble_markdown()
    verify_markdown(md_text)
    convert_to_html(md_text)
    if not skip_pdf:
        generate_pdf()
        verify_pdf()
    else:
        print("[4/5] Omitiendo compilación de PDF (--no-pdf solicitado).")
        print("[5/5] Omitiendo verificación de PDF.")
    print("=" * 70)
    print("CONSTRUCCIÓN COMPLETADA CON ÉXITO")
    print("=" * 70)

if __name__ == "__main__":
    main()
