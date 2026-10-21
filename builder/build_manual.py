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

BASE_DIR = "/home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2C2026-material"
MD_FILE = os.path.join(BASE_DIR, "guia_tda_parciales.md")
PDF_FILE = os.path.join(BASE_DIR, "guia_tda_parciales.pdf")
HTML_FILE = os.path.join(BASE_DIR, "guia_tda_parciales.html")
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

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
    triple_backticks = md_text.count("```")
    if triple_backticks % 2 != 0:
        raise ValueError(f"Error de formato: Hay un número impar de bloques de código (```): {triple_backticks}")
    print(f"      Bloques de código cerrados correctamente: {triple_backticks // 2} bloques.")
    
    ejercicios = [line for line in md_text.split("\n") if line.startswith("### Ejercicio ")]
    print(f"      Total de ejercicios resueltos encontrados: {len(ejercicios)}")
    for ej in ejercicios:
        print(f"        -> {ej}")

def convert_to_html(md_text):
    print("[3/5] Convirtiendo Markdown a HTML interactivo y optimizado para estudio...")
    import shutil
    res = html_interactive_builder.build_interactive_html(md_text, HTML_FILE)
    shutil.copyfile(HTML_FILE, INDEX_FILE)
    print(f"      Copia para GitHub Pages generada en: {INDEX_FILE}")
    return res

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
