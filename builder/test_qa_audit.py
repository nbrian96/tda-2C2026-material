import os
import re
import glob

print("=== AUDITORIA INTEGRAL QA ===")

# 1. Total exercises across modules
modules = sorted(glob.glob("builder/sec*.py"))
all_ex_nums = []
for m in modules:
    with open(m, "r", encoding="utf-8") as f:
        txt = f.read()
    nums = [int(match.group(1)) for match in re.finditer(r"### Ejercicio (\d+)", txt)]
    all_ex_nums.extend(nums)

all_ex_nums.sort()
print(f"1. Total ejercicios en builder: {len(all_ex_nums)}")
expected = list(range(1, 80))
missing = [n for n in expected if n not in all_ex_nums]
duplicates = [n for n in set(all_ex_nums) if all_ex_nums.count(n) > 1]
print(f"   Faltantes (1..79): {missing}")
print(f"   Duplicados: {duplicates}")
assert missing == [], f"Faltan ejercicios: {missing}"
assert duplicates == [], f"Hay duplicados: {duplicates}"

# 2. Check parciales.html
with open("parciales.html", "r", encoding="utf-8") as f:
    parcial_html = f.read()

card_matches = list(re.finditer(r'<article class="exercise-card"[^>]*id="ej-(\d+)"[^>]*data-num="(\d+)"[^>]*data-difficulty="(\d+)"[^>]*data-parcial="true"[^>]*data-title="([^"]*)"[^>]*data-origin="([^"]*)"', parcial_html))
print(f"2. Ejercicios encontrados en parciales.html: {len(card_matches)}")
nums = [int(m.group(2)) for m in card_matches]
difficulties = [int(m.group(3)) for m in card_matches]
print("   data-num encontrados:", nums)
import collections
counts = collections.Counter(nums)
duplicates = [n for n, c in counts.items() if c > 1]
print("   Numeros duplicados:", duplicates)
assert duplicates == [], f"Hay ejercicios duplicados en parciales.html: {duplicates}"
assert len(card_matches) == 29, f"Esperaba 29 en parciales.html, encontre {len(card_matches)}"

assert difficulties == sorted(difficulties), "Las tarjetas en parciales.html NO estan ordenadas ascendentemente por dificultad"
print("   Orden ascendente por dificultad en parciales.html: OK")

# 3. Check star format: only active stars, NO empty stars '☆'
diff_badge_texts = re.findall(r'<span class="badge badge-difficulty[^"]*"[^>]*>(.*?)</span>', parcial_html)
has_empty_stars = any("☆" in b for b in diff_badge_texts)
print(f"3. Hay estrellas vacias en parciales.html?: {has_empty_stars}")
assert not has_empty_stars, "Se encontraron estrellas vacías en badge-difficulty"
print("   Muestra de estrellas activas en badges (longitudes):", [len(b.split()[0]) for b in diff_badge_texts[:5]])

# 4. Check drawer title
drawer_titles = re.findall(r'<span class="summary-title">(.*?)</span>', parcial_html)
print(f"4. Titulo de drawer en tarjetas: {drawer_titles[0].encode('ascii', 'replace').decode('ascii')}")
assert "Respuesta para la Hoja del Parcial" in drawer_titles[0], "El drawer title no coincide"

# 5. Check all HTML line counts
html_files = glob.glob("*.html")
print("5. Archivos HTML:")
for hf in sorted(html_files):
    with open(hf, "r", encoding="utf-8") as f:
        lc = sum(1 for _ in f)
    print(f"   - {hf:<20}: {lc:>5} lineas")
    assert lc < 3000, f"{hf} supera las 3000 lineas"

assert "tipo_parcial.html" not in html_files, "tipo_parcial.html todavia existe"
print("6. tipo_parcial.html eliminado y reemplazado por parciales.html: OK")

# 7. Check KaTeX Math Delimiters and No Leaked Raw Escaped Dollars
print("7. Verificación de Fórmulas Matemáticas y KaTeX:")
total_math_blocks = 0
for m in modules:
    with open(m, "r", encoding="utf-8") as f:
        content = f.read()
    clean = re.sub(r"```[\s\S]*?```", "", content)
    clean = re.sub(r"`[^`\n]+?`", "", clean)
    clean_no_display = re.sub(r"\$\$[\s\S]*?\$\$", "", clean)

    # Check balanced delimiters
    unescaped = [match for match in re.finditer(r"(?<!\\)\$", clean_no_display)]
    assert len(unescaped) % 2 == 0, f"Delimitadores '$' impares en {m}: {len(unescaped)}"

    # Check no bare \$ outside math
    clean_no_math = re.sub(r"(?<!\\)\$(?!\$)[^\n]+?(?<!\\)\$", "", clean_no_display)
    bare_dollars = list(re.finditer(r"\\\$", clean_no_math))
    assert len(bare_dollars) == 0, f"Signos '\\$' sueltos fuera de fórmulas en {m}: {len(bare_dollars)}"

    total_math_blocks += len(unescaped) // 2

print(f"   Fórmulas matemáticas validadas ({total_math_blocks} bloques inline, 0 fugas '\\$'): OK")

print("\n>>> TODAS LAS VERIFICACIONES PASARON CON EXITO (100% OK) <<<")
