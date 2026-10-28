"""Compilador y Generador Modular de la Guía Interactiva de TDA (GitHub Pages)."""

import os
import concurrent.futures
import html_interactive_builder

# Importar los módulos individuales de cada sección
import sec01_intro_and_matrix
import sec02_dyc
import sec03_greedy
import sec03b_greedy_guia
import sec04_backtracking
import sec05_dp
import sec06_pl
import sec07_flujo
import sec08_reducciones
import sec09_integradores
import sec10_tipo_parcial
import sec11_errores_checklist

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_FILE = os.path.join(BASE_DIR, "index.html")

LEGACY_FILES = [
    os.path.join(BASE_DIR, "guia_tda_parciales.md"),
    os.path.join(BASE_DIR, "guia_tda_parciales.html"),
    os.path.join(BASE_DIR, "guia_tda_parciales.pdf"),
]

PARADIGM_TARGETS = [
    {
        "filename": "dyc.html",
        "title": "División y Conquista (12 Ejercicios)",
        "paradigm_key": "dyc",
        "modules": [sec01_intro_and_matrix, sec02_dyc]
    },
    {
        "filename": "greedy.html",
        "title": "Algoritmos Greedy / Voraces (26 Ejercicios)",
        "paradigm_key": "greedy",
        "modules": [sec03_greedy, sec03b_greedy_guia]
    },
    {
        "filename": "backtracking.html",
        "title": "Backtracking y Branch & Bound (14 Ejercicios)",
        "paradigm_key": "backtracking",
        "modules": [sec04_backtracking]
    },
    {
        "filename": "dp.html",
        "title": "Programación Dinámica (7 Ejercicios)",
        "paradigm_key": "dp",
        "modules": [sec05_dp]
    },
    {
        "filename": "pl.html",
        "title": "Programación Lineal y PLI (6 Ejercicios)",
        "paradigm_key": "pl",
        "modules": [sec06_pl]
    },
    {
        "filename": "flujo.html",
        "title": "Redes de Flujo (5 Ejercicios)",
        "paradigm_key": "flujo",
        "modules": [sec07_flujo]
    },
    {
        "filename": "reducciones.html",
        "title": "Reducciones y NP-Completitud (4 Ejercicios)",
        "paradigm_key": "reducciones",
        "modules": [sec08_reducciones]
    },
    {
        "filename": "integradores.html",
        "title": "Problemas Integradores y Multi-Paradigma (5 Ejercicios)",
        "paradigm_key": "integradores",
        "modules": [sec09_integradores]
    },
    {
        "filename": "tipo_parcial.html",
        "title": "Simulacros Tipo Parcial y Checklist (4 Ejercicios)",
        "paradigm_key": "tipo_parcial",
        "modules": [sec10_tipo_parcial, sec11_errores_checklist]
    }
]

def remove_legacy_files():
    for path in LEGACY_FILES:
        if os.path.exists(path):
            os.remove(path)
            print(f"      [Limpieza] Archivo obsoleto eliminado: {os.path.basename(path)}")

def assemble_markdown():
    print("[1/4] Ensamblando secciones en memoria...")
    sections = [
        sec01_intro_and_matrix.get_content(),
        sec02_dyc.get_content(),
        sec03_greedy.get_content(),
        sec03b_greedy_guia.get_content(),
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
    print(f"      Total de caracteres ensamblados: {len(full_md):,}")
    print(f"      Total de palabras: {len(full_md.split()):,}")
    return full_md

def verify_markdown(md_text):
    print("[2/4] Verificando integridad del Markdown y catálogo de ejercicios...")
    triple_backticks = md_text.count("```")
    if triple_backticks % 2 != 0:
        raise ValueError(f"Error de formato: Número impar de delimitadores de código (```): {triple_backticks}")
    print(f"      Bloques de código cerrados correctamente: {triple_backticks // 2} bloques.")

    ejercicios = [line for line in md_text.split("\n") if line.startswith("### Ejercicio ")]
    print(f"      Total de ejercicios resueltos encontrados: {len(ejercicios)}")
    return len(ejercicios)

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
    print("[3/4] Generando aplicación modular HTML con Bootstrap 5.3 y assets externos...")
    html_interactive_builder.build_interactive_html(
        md_text,
        INDEX_FILE,
        active_paradigm="all",
        page_title="Guía Interactiva Completa (83 Ejercicios)"
    )
    print(f"      Página maestra generada: {os.path.basename(INDEX_FILE)}")

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {executor.submit(compile_single_page, target): target["filename"] for target in PARADIGM_TARGETS}
        for future in concurrent.futures.as_completed(futures):
            fname = futures[future]
            future.result()
            print(f"      Módulo por paradigma generado: {fname}")

def verify_html_line_counts():
    print("[4/4] Reporte de tamaño y líneas de archivos HTML generados:")
    all_files = ["index.html"] + [t["filename"] for t in PARADIGM_TARGETS]
    for fname in all_files:
        fpath = os.path.join(BASE_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            lines = sum(1 for _ in f)
        size_kb = os.path.getsize(fpath) / 1024
        print(f"      - {fname:<20} : {lines:>5} líneas ({size_kb:>6.1f} KB)")

def main():
    print("=" * 70)
    print("INICIANDO CONSTRUCCIÓN DE LA GUÍA INTERACTIVA DE TDA (83 EJERCICIOS)")
    print("=" * 70)
    remove_legacy_files()
    md_text = assemble_markdown()
    verify_markdown(md_text)
    convert_to_html(md_text)
    verify_html_line_counts()
    print("=" * 70)
    print("CONSTRUCCIÓN MODULAR COMPLETADA CON ÉXITO")
    print("=" * 70)

if __name__ == "__main__":
    main()
