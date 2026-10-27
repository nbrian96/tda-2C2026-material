"""Módulo 11: Catálogo de Errores Típicos de Parcial y Checklist Definitiva."""

def get_content():
    return r"""## 13. Catálogo de Errores Típicos de Parcial y Trampas Frecuentes

Este catálogo compila las fallas y penalizaciones más comunes detectadas en las correcciones de exámenes de la cátedra:

### 1. En Reducciones NP-Completitud (Las fallas más costosas)
* ❌ **Reducir al revés ($B \le_P A$ en vez de $A \le_P B$):** Es el error que anula inmediatamente el ejercicio. Recordá la regla mnemotécnica: *"Reduzco DESDE el problema difícil que ya conozco ($A$) HACIA el problema nuevo ($B$)"*.
* ❌ **Olvidar probar que $B \in \text{NP}$:** No incluir el certificado y el algoritmo verificador polinomial reduce la nota del ejercicio al $50\%$, pues solo probaste que es NP-Hard.
* ❌ **Probar únicamente la implicación de ida ($\implies$):** Si solo probás la ida, no demostraste que resolver $B$ resuelve $A$. La vuelta ($\impliedby$) es obligatoria.
* ❌ **Usar certificados de tamaño exponencial:** El certificado debe poder escribirse en espacio polinomial $O(n^k)$.

### 2. En Programación Dinámica
* ❌ **No definir formalmente qué almacena la tabla $OPT(\dots)$:** Escribir una matriz o una fórmula sin explicar en palabras qué significan los índices $i, w$ es fuertemente penalizado.
* ❌ **Olvidar los Casos Base:** Dejar celdas no inicializadas o asumir $0$ en estados que representan configuraciones infactibles (los cuales deben inicializarse con $-\infty$ o $+\infty$).
* ❌ **Omitir la reconstrucción de la solución:** Si el problema pide "cuáles son los elementos" o "qué días trabajar", dar únicamente el número del valor máximo equivale a respuesta incompleta.
* ❌ **No justificar la dirección de llenado:** La tabla debe llenarse en un orden donde cada estado consulte celdas previamente computadas.

### 3. En Algoritmos Greedy (Voraces)
* ❌ **Afirmar optimalidad sin demostración:** Decir *"es óptimo porque en cada paso elijo lo que más conviene"* no es una demostración. Se debe aplicar *Greedy Stays Ahead* o *Argumento de Intercambio*.
* ❌ **Dar un contraejemplo abstracto:** Escribir *"podría pasar que después haya un costo más alto"* no refuta nada. Un contraejemplo debe tener nodos, aristas y valores numéricos exactos donde Greedy obtenga un resultado peor que la alternativa.
* ❌ **Confundir la mochila fraccionaria con la 0-1:** La mochila fraccionaria es voraz en $O(n \log n)$; la 0-1 es NP-Hard y requiere Programación Dinámica en $O(n \cdot W)$.

### 4. En Programación Lineal (PL / PLI)
* ❌ **Multiplicar variables de decisión ($x_i \cdot y_j$):** Destruye la condición de linealidad y anula el modelo.
* ❌ **No declarar el dominio de las variables:** Olvidar explicitar $x_i \in \{0, 1\}$ o $y_j \ge 0$.
* ❌ **Olvidar contar variables y restricciones:** Si el enunciado pide el recuento, debe presentarse la sumatoria algebraica explícita de variables y restricciones.
* ❌ **Usar operadores no lineales directos:** Como $\max(a, b)$ o $|x - y|$; deben linealizarse con variables auxiliares continuas y desigualdades.

### 5. En Redes de Flujo
* ❌ **Olvidar las aristas hacia atrás (residuales):** Si la red residual no permite cancelar flujo hacia atrás, el algoritmo no es Ford-Fulkerson y no alcanzará el flujo máximo.
* ❌ **Confundir la capacidad de un corte:** Sumar aristas que van de $B$ hacia $A$ en vez de sumar estrictamente las aristas dirigidas desde $A$ hacia $B$.
* ❌ **No justificar por qué la solución es entera:** En problemas de emparejamiento, debe citarse el **Teorema de Integralidad de Flujo**.

### 6. En Backtracking
* ❌ **Olvidar deshacer la modificación (Backtrack):** Dejar marcadas variables globales o booleanos al retornar de la recursión corrompe las ramas posteriores.
* ❌ **Validar en $O(n)$ en vez de $O(1)$:** En problemas como N-Reinas, chequear conflictos con bucles es penalizado; se deben usar arreglos booleanos de columnas y diagonales.

---

## 14. Checklist Definitiva Antes de Entrar al Parcial

Utilizá esta lista de verificación durante tu última hora de repaso antes de ingresar al aula:

### A. Dominio de Paradigmas
- [ ] **División y Conquista:** Me sé de memoria los 3 casos del Teorema Maestro ($T(n) = a \cdot T(n/b) + \Theta(n^c)$) y sé identificar $a, b$ y $c$.
- [ ] **Greedy:** Sé aplicar la demostración por inducción *Greedy Stays Ahead* y sé diseñar un contraejemplo numérico si el algoritmo voraz no es óptimo.
- [ ] **Backtracking:** Sé implementar podas de factibilidad y cotas de Branch & Bound, usando tablas booleanas de control en $O(1)$ y deshaciendo el estado al retornar.
- [ ] **Programación Dinámica:** Cumplo siempre los 5 pasos: 1) Definición formal del estado, 2) Casos base, 3) Ecuación de recurrencia, 4) Orden de llenado bottom-up, 5) Reconstrucción.
- [ ] **Programación Lineal:** Sé definir variables con sus dominios, función objetivo lineal, restricciones lineales, linealización de $\min \max$ y conteo de variables/restricciones.
- [ ] **Redes de Flujo:** Sé construir la super-fuente y el super-sumidero, formular la red residual con aristas hacia atrás y calcular la capacidad del corte mínimo.
- [ ] **Reducciones NP-Completitud:** Sigo estrictamente los 4 pasos: 1) Certificado y Verificador en NP, 2) Problema conocido en NPC, 3) Transformación polinomial en tiempo polinomial, 4) Demostración de ida ($\implies$) y vuelta ($\impliedby$).

### B. Ejecución en la Hoja de Examen
- [ ] Cada ejercicio está escrito en una **hoja separada** con nombre y padrón.
- [ ] El pseudocódigo usa palabras clave claras (`PROCEDIMIENTO`, `FUNCION`, `SI`, `SINO`, `MIENTRAS`, `PARA`, `RETORNAR`).
- [ ] Contemplé los **casos borde** relevantes (estructuras vacías, un elemento, capacidades nulas, grafos sin aristas).
- [ ] Justifiqué la **complejidad temporal y espacial** explicando de dónde sale cada término ($O(n \log n)$, $O(V \cdot E)$, etc.), sin limitarme a tirar una fórmula suelta.
"""
