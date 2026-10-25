"""Módulo 2: División y Conquista (DyC)."""

def get_content():
    return r"""## 4. Tema 1: División y Conquista (DyC)

### Conceptos Mínimos de Supervivencia

1. **Definición del Paradigma:**
   Un algoritmo de División y Conquista divide un problema de tamaño $n$ en $a$ subproblemas independientes de tamaño $n/b$, resuelve cada subproblema recursivamente (conquista), y luego combina sus soluciones con un costo $f(n)$ (combinación).

2. **Teorema Maestro (Master Theorem):**
   Para recurrencias de la forma:
   > $$T(n) = a \cdot T(n/b) + \Theta(n^c)$$
   
   con $a \ge 1, b > 1, c \ge 0$:
   * **Caso 1 (Dominio de Hojas):** Si $\log_b a > c \implies T(n) = \Theta(n^{\log_b a})$. El costo computacional está dominado por las hojas del árbol de recursión.
   * **Caso 2 (Balance Equitativo):** Si $\log_b a = c \implies T(n) = \Theta(n^c \log n)$. Cada nivel del árbol recursivo aporta la misma cantidad asintótica de trabajo.
   * **Caso 3 (Dominio de la Raíz):** Si $\log_b a < c \implies T(n) = \Theta(n^c)$ (sujeto a la condición de regularidad $a \cdot f(n/b) \le k \cdot f(n)$ con $k < 1$). El costo de combinar en la raíz domina todo el proceso.

3. **Requisitos de Factibilidad:**
   * Los subproblemas deben ser **estrictamente disjuntos** (sin solapamiento; si hay solapamiento, corresponde Programación Dinámica).
   * La reducción del tamaño debe ser multiplicativa ($n/b$), no sustractiva ($n - 1$). Si es sustractiva ($T(n) = T(n - 1) + O(1)$), no aplica Teorema Maestro y la complejidad es lineal o cuadrática.

---

### Patrón de Ejercicio 1.1: Álgebra Matricial y Partición en Bloques

En los parciales aparece el requerimiento de formular algoritmos multiplicativos dividiendo estructuras bidimensionales en cuadrantes y deduciendo la complejidad formal con el Teorema Maestro.

---

### Ejercicio 1 — Multiplicación de Matrices Cuadradas por Bloques

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2025-1-2 (17 de junio de 2025), Ejercicio 1

**Enunciado**  
Realizar un algoritmo que resuelva la multiplicación de dos matrices cuadradas de orden $n$ ($A$ y $B$) mediante división y conquista. Recordemos la definición: $C = A \times B$ donde $C_{ij} = \sum_{k=1}^n A_{ik} \cdot B_{kj}$ para todo $i, j \in \{1, \dots, n\}$. Para simplificar el algoritmo se puede suponer que $n$ es una potencia de 2. Indicar y justificar el orden de complejidad temporal y espacial del algoritmo.

**Qué está evaluando la cátedra**  
Partición de matrices en 4 bloques de orden $n/2$, formulación de las llamadas recursivas de multiplicación, suma de matrices en la etapa de combinación, y aplicación rigurosa del Teorema Maestro sin saltarse el análisis de casos.

#### 1. Deducción Metodológica Formal (Los 5 Pasos de DyC)

1. **Paso 1: División:**
   Se dividen las matrices cuadradas $A$ y $B$ de orden $n \times n$ en 4 submatrices (cuadrantes) de tamaño $(n/2) \times (n/2)$:
   $$A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}, \quad B = \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{pmatrix}$$

2. **Paso 2: Casos Base:**
   Cuando $n = 1$, las matrices se reducen a un único escalar cada una:
   $$C_{11} = A_{11} \cdot B_{11}$$
   Esta multiplicación escalar elemental se ejecuta en tiempo $O(1)$.

3. **Paso 3: Conquista (Llamadas Recursivas):**
   De acuerdo al producto matricial por bloques, la matriz resultante $C$ satisface:
   $$C = \begin{pmatrix} C_{11} & C_{12} \\ C_{21} & C_{22} \end{pmatrix} = \begin{pmatrix} A_{11} B_{11} + A_{12} B_{21} & A_{11} B_{12} + A_{12} B_{22} \\ A_{21} B_{11} + A_{22} B_{21} & A_{21} B_{12} + A_{22} B_{22} \end{pmatrix}$$
   Cada cuadrante requiere 2 productos de matrices de tamaño $(n/2) \times (n/2)$. En total se disparan **$a = 8$ llamadas recursivas**:
   * $M_1 = A_{11} \cdot B_{11}$, $M_2 = A_{12} \cdot B_{21}$
   * $M_3 = A_{11} \cdot B_{12}$, $M_4 = A_{12} \cdot B_{22}$
   * $M_5 = A_{21} \cdot B_{11}$, $M_6 = A_{22} \cdot B_{21}$
   * $M_7 = A_{21} \cdot B_{12}$, $M_8 = A_{22} \cdot B_{22}$

4. **Paso 4: Combinación:**
   Se calculan los 4 cuadrantes finales mediante 4 sumas de matrices de tamaño $(n/2) \times (n/2)$:
   * $C_{11} = M_1 + M_2$
   * $C_{12} = M_3 + M_4$
   * $C_{21} = M_5 + M_6$
   * $C_{22} = M_7 + M_8$
   Cada suma matricial de $(n/2) \times (n/2)$ elementos insume $(n/2)^2 = n^2 / 4$ operaciones. En total, las 4 sumas insumen $4 \cdot (n^2 / 4) = n^2$ operaciones, es decir, costo $\Theta(n^2)$.

5. **Paso 5: Ecuación de Recurrencia y Teorema Maestro:**
   $$T(n) = \begin{cases} \Theta(1) & \text{si } n = 1 \\ 8 \cdot T\left(\frac{n}{2}\right) + \Theta(n^2) & \text{si } n > 1 \end{cases}$$
   Identificamos los parámetros del Teorema Maestro:
   * $a = 8$ (número de subproblemas recursivos)
   * $b = 2$ (factor de reducción del tamaño de entrada)
   * $f(n) = \Theta(n^c)$ con $c = 2$ (costo de división y combinación de bloques)
   
   Calculamos el exponente crítico:
   $$\log_b a = \log_2 8 = 3$$
   Comparamos $\log_b a$ con $c$:
   $$\log_b a = 3 > 2 = c$$
   Dado que $\log_b a > c$, aplica estrictamente el **Caso 1 del Teorema Maestro** (el trabajo en las hojas del árbol domina el costo global):
   $$T(n) = \Theta(n^{\log_b a}) = \Theta(n^{\log_2 8}) = \Theta(n^3)$$

#### 2. Demostración Formal de Correctitud por Inducción Matemática

* **Proposición $P(k)$:** El algoritmo calcula exactamente el producto $C = A \times B$ para cualquier par de matrices de orden $n = 2^k$.
* **Caso Base ($k = 0 \implies n = 2^0 = 1$):**
  Las matrices $A$ y $B$ tienen dimensión $1 \times 1$. El algoritmo ejecuta $C[0][0] = A[0][0] \cdot B[0][0]$, lo cual coincide exactamente con la definición del producto escalar $C_{11} = A_{11} \cdot B_{11}$. $P(0)$ es verdadero.
* **Hipótesis Inductiva:** Supongamos que el algoritmo calcula correctamente el producto de matrices para toda dimensión $m = 2^j$ con $j \le k - 1$.
* **Paso Inductivo ($k$ con $n = 2^k$):**
  La matriz se divide en bloques de dimensión $m = 2^{k-1}$. Por hipótesis inductiva, cada uno de los 8 productos recursivos $M_1, \dots, M_8$ produce el resultado exacto de multiplicar los bloques correspondientes. Por las propiedades distributivas del álgebra lineal:
  $$C_{ij} = \sum_{k=1}^n A_{ik} B_{kj} = \sum_{k=1}^{n/2} A_{ik} B_{kj} + \sum_{k=n/2 + 1}^n A_{ik} B_{kj}$$
  La primera sumatoria corresponde al producto del primer bloque y la segunda sumatoria al segundo bloque. Al sumar matricialmente $M_1 + M_2$ se obtiene la suma exacta de ambas componentes para cada celda $(i, j)$ del cuadrante superior izquierdo, e idénticamente para los demás cuadrantes. Por lo tanto, $P(k)$ es verdadero $\forall k \ge 0$. $\blacksquare$

#### 3. Ejemplo Concreto y Traza Paso a Paso ($n = 2$)

Sean las matrices $2 \times 2$:
$$A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$$

| Cuadrante / Operación | Definición Algebraica | Cálculo Numérico | Resultado |
| :--- | :--- | :--- | :--- |
| **Bloques de $A$** | $A_{11}=[1], A_{12}=[2], A_{21}=[3], A_{22}=[4]$ | Descomposición en $1 \times 1$ | 4 escalares |
| **Bloques de $B$** | $B_{11}=[5], B_{12}=[6], B_{21}=[7], B_{22}=[8]$ | Descomposición en $1 \times 1$ | 4 escalares |
| **$M_1$** | $A_{11} \cdot B_{11}$ | $1 \cdot 5$ | $5$ |
| **$M_2$** | $A_{12} \cdot B_{21}$ | $2 \cdot 7$ | $14$ |
| **$M_3$** | $A_{11} \cdot B_{12}$ | $1 \cdot 6$ | $6$ |
| **$M_4$** | $A_{12} \cdot B_{22}$ | $2 \cdot 8$ | $16$ |
| **$M_5$** | $A_{21} \cdot B_{11}$ | $3 \cdot 5$ | $15$ |
| **$M_6$** | $A_{22} \cdot B_{21}$ | $4 \cdot 7$ | $28$ |
| **$M_7$** | $A_{21} \cdot B_{12}$ | $3 \cdot 6$ | $18$ |
| **$M_8$** | $A_{22} \cdot B_{22}$ | $4 \cdot 8$ | $32$ |
| **$C_{11} = M_1 + M_2$** | $A_{11} B_{11} + A_{12} B_{21}$ | $5 + 14$ | **$19$** |
| **$C_{12} = M_3 + M_4$** | $A_{11} B_{12} + A_{12} B_{22}$ | $6 + 16$ | **$22$** |
| **$C_{21} = M_5 + M_6$** | $A_{21} B_{11} + A_{22} B_{21}$ | $15 + 28$ | **$43$** |
| **$C_{22} = M_7 + M_8$** | $A_{21} B_{12} + A_{22} B_{22}$ | $18 + 32$ | **$50$** |

Matriz final ensamblada:
$$C = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}$$
*Verificación por producto tradicional:*
* Fila 1 × Columna 1: $1 \cdot 5 + 2 \cdot 7 = 19$. Correcto.
* Fila 1 × Columna 2: $1 \cdot 6 + 2 \cdot 8 = 22$. Correcto.
* Fila 2 × Columna 1: $3 \cdot 5 + 4 \cdot 7 = 43$. Correcto.
* Fila 2 × Columna 2: $3 \cdot 6 + 4 \cdot 8 = 50$. Correcto.

#### 4. Diagrama del Árbol de Recursión

```mermaid
flowchart TD
    R["Raiz: T(n)"] --> L1["Submatriz M1"]
    R --> L2["Submatriz M2"]
    R --> L3["Submatriz M3"]
    R --> L4["Submatriz M4"]
    R --> L5["Submatriz M5"]
    R --> L6["Submatriz M6"]
    R --> L7["Submatriz M7"]
    R --> L8["Submatriz M8"]
    L1 --> H1["Hojas caso base"]
    L8 --> H8["Hojas caso base"]
```

#### 5. Implementación en Python (Tipada y Ejecutable)

```python
def multiplicar_matrices_dyc(a: list[list[float]], b: list[list[float]]) -> list[list[float]]:
    # Multiplica dos matrices cuadradas de orden n (potencia de 2) por DyC en O(n^3).
    n = len(a)
    if n == 1:
        return [[a[0][0] * b[0][0]]]

    m = n // 2
    # Partición en 4 submatrices de m x m
    a11 = [row[:m] for row in a[:m]]
    a12 = [row[m:] for row in a[:m]]
    a21 = [row[:m] for row in a[m:]]
    a22 = [row[m:] for row in a[m:]]

    b11 = [row[:m] for row in b[:m]]
    b12 = [row[m:] for row in b[:m]]
    b21 = [row[:m] for row in b[m:]]
    b22 = [row[m:] for row in b[m:]]

    # 8 multiplicaciones recursivas
    m1 = multiplicar_matrices_dyc(a11, b11)
    m2 = multiplicar_matrices_dyc(a12, b21)
    m3 = multiplicar_matrices_dyc(a11, b12)
    m4 = multiplicar_matrices_dyc(a12, b22)
    m5 = multiplicar_matrices_dyc(a21, b11)
    m6 = multiplicar_matrices_dyc(a22, b21)
    m7 = multiplicar_matrices_dyc(a21, b12)
    m8 = multiplicar_matrices_dyc(a22, b22)

    # 4 sumas de bloques de m x m
    c11 = [[m1[i][j] + m2[i][j] for j in range(m)] for i in range(m)]
    c12 = [[m3[i][j] + m4[i][j] for j in range(m)] for i in range(m)]
    c21 = [[m5[i][j] + m6[i][j] for j in range(m)] for i in range(m)]
    c22 = [[m7[i][j] + m8[i][j] for j in range(m)] for i in range(m)]

    # Ensamblado de la matriz C final de n x n
    c = []
    for i in range(m):
        c.append(c11[i] + c12[i])
    for i in range(m):
        c.append(c21[i] + c22[i])
    return c
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Afirmar que DyC clásico reduce la complejidad a $O(n^2)$ o $O(n^{2.81})$:</strong> El algoritmo estándar por cuadrantes realiza 8 multiplicaciones ($a = 8$), lo que da exactamente $\Theta(n^3)$, igual que el método iterativo cúbico de 3 bucles. Para bajar a $O(n^{\log_2 7}) \approx O(n^{2.81})$ es indispensable el truco algebraico de Volker Strassen (7 multiplicaciones).</li>
    <li><strong>Confusión de índices en los productos cruzados:</strong> Un error muy penalizado es escribir $A_{12} B_{12}$ en lugar de $A_{12} B_{21}$. Recuerde que la fila de $A$ multiplica a la columna de $B$.</li>
    <li><strong>Olvidar el costo de partición y combinación:</strong> Copiar matrices o sumarlas no es gratis; toma $\Theta(n^2)$. Omitir este término en la recurrencia anula la justificación del Teorema Maestro.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 1.2: Búsqueda Binaria sobre Propiedades Monótonas

Se busca un elemento o punto crítico en arreglos que no están completamente ordenados pero que presentan una propiedad monótona o un cambio de tendencia detectable en tiempo $O(\log n)$.

---

### Ejercicio 2 — Elemento Pico en un Arreglo Unimodal

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Guía de Ejercicios 01, Ejercicio 4 / Parcial FIUBA

**Enunciado**  
Dado un arreglo $A$ de $n$ enteros distintos donde no hay dos elementos adyacentes iguales, un elemento $A[i]$ se define como "pico" si es estrictamente mayor que sus vecinos existentes (es decir, $A[i] > A[i-1]$ y $A[i] > A[i+1]$, considerando los extremos con un único vecino). Diseñar un algoritmo por División y Conquista que encuentre un elemento pico en tiempo $O(\log n)$. Justificar la correctitud y la complejidad.

**Qué está evaluando la cátedra**  
Capacidad de descarte logarítmico aprovechando la dirección de la pendiente local, manejo riguroso de condiciones de borde en índices y demostración formal de que siempre existe al menos un pico en la mitad elegida.

#### 1. Deducción Metodológica Formal (Los 5 Pasos de DyC)

1. **Paso 1: Definición del Invariante de Búsqueda:**
   En cada llamada sobre el rango $[ini, fin]$, se mantiene el siguiente invariante: **garantizadamente existe al menos un pico local dentro del subarreglo $A[ini \dots fin]$**.
2. **Paso 2: Caso Base:**
   Cuando $ini = fin$, el rango contiene un único elemento. Por el invariante de búsqueda, este elemento debe ser un pico local. Se retorna $ini$ en tiempo $O(1)$.
3. **Paso 3: División:**
   Se calcula el índice central:
   $$m = \lfloor(ini + fin) / 2\rfloor$$
   Como $ini < fin$, necesariamente $m < fin$, lo cual garantiza que la posición $m + 1$ es siempre un índice válido dentro del arreglo (sin desbordamiento).
4. **Paso 4: Conquista y Criterio de Descarte:**
   Se comparan los elementos contiguos $A[m]$ y $A[m + 1]$:
   * **Caso A ($A[m] < A[m + 1]$):** La pendiente asciende hacia la derecha. Por el Teorema de Existencia, existe al menos un pico en el subrango $[m + 1, fin]$. Se descarta toda la mitad izquierda $[ini, m]$.
   * **Caso B ($A[m] > A[m + 1]$):** La pendiente desciende hacia la derecha (asciende hacia la izquierda). Por lo tanto, existe al menos un pico en el subrango $[ini, m]$ (el propio $m$ podría ser el pico). Se descarta el subrango $[m + 1, fin]$.
5. **Paso 5: Ecuación de Recurrencia y Teorema Maestro:**
   En cada paso se realiza exactamente una llamada recursiva sobre un subarreglo de tamaño a lo sumo $\lceil n/2 \rceil$ con trabajo de comparación $O(1)$:
   $$T(n) = 1 \cdot T(n/2) + \Theta(1)$$
   Parámetros: $a = 1, b = 2, c = 0$.
   $$\log_b a = \log_2 1 = 0 = c$$
   Aplica el **Caso 2 del Teorema Maestro** con $k = 0$:
   $$T(n) = \Theta(n^c \log n) = \Theta(n^0 \log n) = \Theta(\log n)$$

#### 2. Demostración Formal de Existencia del Pico

* **Lema de la Pendiente:** Si $A[m] < A[m + 1]$, entonces el subarreglo $A[m + 1 \dots fin]$ contiene al menos un elemento pico.
* **Demostración por el Principio del Buen Orden / Contradicción:**
  Consideremos el subarreglo $A[m + 1 \dots fin]$. Si el último elemento $A[fin]$ es mayor que $A[fin - 1]$, entonces $A[fin]$ es un pico (pues no tiene vecino derecho). Si no lo es, retrocedemos: como $A[m] < A[m + 1]$, no todos los elementos pueden ser decrecientes hacia la izquierda sin toparse con una cresta. Dado que no hay elementos adyacentes iguales, debe existir un primer índice $k \in \{m + 1, \dots, fin - 1\}$ tal que $A[k] > A[k + 1]$. Como $k$ es el primer punto de caída, necesariamente $A[k] > A[k - 1]$, lo que convierte a $A[k]$ en un pico. $\blacksquare$

#### 3. Ejemplo Concreto y Traza Paso a Paso

Sea el arreglo de $n = 7$ elementos:
$$A = [1, 2, 1, 3, 5, 6, 4]$$

| Paso | Rango $[ini, fin]$ | $m$ | $A[m]$ | $A[m+1]$ | Comparación | Decisión / Rango Siguiente |
| :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | $[0, 6]$ | $3$ | $3$ | $5$ | $3 < 5$ (sube a derecha) | Descartar izquierda $\implies [4, 6]$ |
| **2** | $[4, 6]$ | $5$ | $6$ | $4$ | $6 > 4$ (baja a derecha) | Descartar derecha $\implies [4, 5]$ |
| **3** | $[4, 5]$ | $4$ | $5$ | $6$ | $5 < 6$ (sube a derecha) | Descartar izquierda $\implies [5, 5]$ |
| **4** | $[5, 5]$ | - | - | - | **$ini == fin = 5$** | **Caso base: Pico en índice 5 ($A[5] = 6$)** |

*Verificación:* $A[5] = 6$ es estrictamente mayor que su vecino izquierdo $A[4] = 5$ y su vecino derecho $A[6] = 4$. Es un pico válido encontrado en solo 3 iteraciones ($<\log_2 7 \approx 2.8$).

#### 4. Diagrama Visual de Búsqueda Binaria de la Pendiente

```mermaid
graph TD
    A["Rango (0 a 6): A(3)=3 sube hacia A(4)=5"] -->|Descartar mitad izq| B["Rango (4 a 6): A(5)=6 baja hacia A(6)=4"]
    B -->|Conservar m=5| C["Rango (4 a 5): A(4)=5 sube hacia A(5)=6"]
    C -->|Descartar m=4| D["Rango (5 a 5): Caso Base"]
    D --> E["Retorna Indice 5: Elemento Pico = 6"]:::opt
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

#### 5. Implementación en Python (Tipada y Ejecutable)

```python
def encontrar_pico(arr: list[int]) -> int:
    # Encuentra el índice de un elemento pico en O(log n) mediante DyC.
    if not arr:
        return -1
    
    ini, fin = 0, len(arr) - 1
    while ini < fin:
        m = (ini + fin) // 2
        # Si la pendiente sube hacia la derecha, el pico está a la derecha
        if arr[m] < arr[m + 1]:
            ini = m + 1
        else:
            # Si la pendiente baja hacia la derecha, m puede ser el pico
            fin = m
            
    return ini
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Hacer <code>fin = m - 1</code> en la rama descendente:</strong> Si $A[m] > A[m+1]$, el elemento $A[m]$ podría ser precisamente el pico. Si ajustas <code>fin = m - 1</code>, excluyes a $m$ y el algoritmo puede retornar un índice incorrecto o fallar. Debe ser obligatoriamente <code>fin = m</code>.</li>
    <li><strong>Desbordamiento de índice al calcular $m+1$:</strong> Si el bucle tiene condición <code>ini &le; fin</code>, en la última iteración $m = fin$ y la consulta <code>arr[m + 1]</code> arroja <code>IndexError</code>. La condición estricta debe ser <code>ini &lt; fin</code>.</li>
    <li><strong>Creer que el arreglo debe estar ordenado:</strong> Este algoritmo funciona sobre arreglos desordenados gracias al Lema de la Pendiente. Afirmar en el examen que se requiere ordenar previamente ($O(n \log n)$) invalida la cota $O(\log n)$.</li>
  </ul>
</div>

---

### Ejercicio 3 — Búsqueda del Primer Cero en un Arreglo de Unos y Ceros

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Guía de Ejercicios 01, Ejercicio 2 / Final FIUBA

**Enunciado**  
Se tiene un arreglo $A$ de $n$ elementos compuesto exclusivamente por números 1 seguidos por números 0 (es decir, de la forma $[1, 1, \dots, 1, 0, 0, \dots, 0]$). Puede ocurrir que todos sean 1 o todos sean 0. Implementar un algoritmo por División y Conquista que determine la posición del primer 0 en tiempo $O(\log n)$. Si el arreglo no contiene ceros, retornar $-1$.

**Qué está evaluando la cátedra**  
Identificación de la propiedad de frontera de transición, manejo riguroso de casos donde el cero está en el índice 0 o no existe, y parada anticipada sin incurrir en recorridos lineales.

#### 1. Deducción Metodológica Formal (Los 5 Pasos de DyC)

1. **Paso 1: Propiedad de Monotonía y Frontera:**
   El arreglo $A$ es monótonamente decreciente no estricto: $A[i] \ge A[i+1]$ para todo $i$. El "primer cero" es el único índice $k$ que satisface:
   $$A[k] = 0 \quad \land \quad (k = 0 \lor A[k - 1] = 1)$$
2. **Paso 2: Casos Base de Rango Vacío:**
   Si $ini > fin$, el subrango colapsó sin encontrar ningún cero (ocurre cuando el arreglo es puramente de unos). Se retorna $-1$.
3. **Paso 3: División:**
   Se evalúa el elemento en la posición media:
   $$m = \lfloor(ini + fin) / 2\rfloor$$
4. **Paso 4: Conquista y Reducción del Espacio de Búsqueda:**
   * **Condición de Éxito Inmediato:** Si $A[m] == 0$ y además ($m == 0$ o $A[m - 1] == 1$), entonces $m$ es por definición el primer cero. Se retorna $m$ inmediatamente en $O(1)$.
   * **Rama Izquierda ($A[m] == 0$ pero $A[m - 1] == 0$):** Hay más ceros hacia la izquierda. Se descarta la mitad derecha y se busca recursivamente en $[ini, m - 1]$.
   * **Rama Derecha ($A[m] == 1$):** Por monotonía, todos los elementos desde $ini$ hasta $m$ son 1. El primer cero solo puede estar estrictamente a la derecha. Se busca en $[m + 1, fin]$.
5. **Paso 5: Ecuación de Recurrencia y Teorema Maestro:**
   $$T(n) = 1 \cdot T(n/2) + \Theta(1)$$
   Con $a = 1, b = 2, c = 0$:
   $$\log_2 1 = 0 = c \implies T(n) = \Theta(\log n)$$
   Espacio auxiliar: $O(1)$ en implementación iterativa, $O(\log n)$ en la pila de recursión.

#### 2. Demostración Formal de Correctitud por Inducción Fuerte

* **Hipótesis:** Para cualquier subrango $A[ini \dots fin]$ de longitud $L = fin - ini + 1$:
  * Si contiene al menos un cero, el algoritmo retorna el menor índice $k \in [ini, fin]$ tal que $A[k] = 0$.
  * Si no contiene ceros, retorna $-1$.
* **Base ($L = 0 \implies ini > fin$):** El subarreglo es vacío. Retorna $-1$. Correcto.
* **Paso Inductivo ($L \ge 1$):**
  Se inspecciona $A[m]$. 
  * Si $A[m] = 1$: Como el arreglo tiene la estructura $1^* 0^*$, si la posición $m$ tiene un 1, todas las posiciones $j \le m$ tienen $A[j] = 1$. Por lo tanto, ningún índice $\le m$ puede ser cero. El primer cero, de existir, debe residir en $[m + 1, fin]$, un subrango de longitud $\le \lfloor L/2 \rfloor$. Por hipótesis inductiva, la llamada recursiva devolverá el resultado correcto.
  * Si $A[m] = 0$: Si $m = 0$ o $A[m-1] = 1$, por definición $m$ es el primer cero y se retorna. Si $A[m-1] = 0$, el primer cero está estrictamente antes de $m$, residiendo en $[ini, m - 1]$. Por hipótesis inductiva, la recursión encuentra el resultado exacto. $\blacksquare$

#### 3. Ejemplo Concreto y Traza Paso a Paso

Sea el arreglo de $n = 8$ elementos:
$$A = [1, 1, 1, 1, 0, 0, 0, 0]$$

| Iteración | Rango $[ini, fin]$ | $m$ | $A[m]$ | Verificación $A[m-1]$ | Decisión / Rango Siguiente |
| :---: | :---: | :---: | :---: | :---: | :--- |
| **1** | $[0, 7]$ | $3$ | $1$ | No aplica ($A[m]=1$) | $A[3]=1 \implies$ Descartar $[0, 3]$. Nuevo rango: $[4, 7]$ |
| **2** | $[4, 7]$ | $5$ | $0$ | $A[4] = 0$ | $A[5]=0$ pero $A[4]=0 \implies$ Hay ceros antes. Nuevo rango: $[4, 4]$ |
| **3** | $[4, 4]$ | $4$ | $0$ | $A[3] = 1$ | **$A[4] = 0 \land A[3] = 1 \implies$ ¡Primer cero hallado en índice 4!** |

*Resultado devuelto:* $4$. Complejidad real: 3 comparaciones ($\le \lceil \log_2 8 \rceil = 3$).

#### 4. Diagrama Visual del Corte de Frontera

```mermaid
graph LR
    subgraph Unos [Zona de 1s]
        N0["A[0] = 1"] --> N1["A[1] = 1"] --> N2["A[2] = 1"] --> N3["A[3] = 1"]
    end
    subgraph Ceros [Zona de 0s]
        N4["A[4] = 0 (PRIMER CERO)"]:::primer --> N5["A[5] = 0"] --> N6["A[6] = 0"] --> N7["A[7] = 0"]
    end
    N3 -. Frontera de Transición .-> N4
    classDef primer fill:#15803d,stroke:#166534,stroke-width:3px,color:#fff
```

#### 5. Implementación en Python (Tipada y Ejecutable)

```python
def buscar_primer_cero(arr: list[int]) -> int:
    # Retorna el índice del primer 0 en un arreglo de 1s seguidos de 0s en O(log n).
    if not arr:
        return -1

    ini, fin = 0, len(arr) - 1
    primer_cero = -1

    while ini <= fin:
        m = (ini + fin) // 2
        if arr[m] == 0:
            primer_cero = m
            # Intentar buscar un cero aún más a la izquierda
            fin = m - 1
        else:
            # arr[m] == 1, el primer cero debe estar a la derecha
            ini = m + 1

    return primer_cero
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Acceder a <code>arr[m - 1]</code> cuando $m = 0$:</strong> Si el primer cero está en la posición 0, evaluar <code>arr[m - 1]</code> en Python consultará <code>arr[-1]</code> (el último elemento del arreglo), produciendo un falso positivo o error lógico en otros lenguajes (C/Java) con <code>IndexOutOfBoundsException</code>. Siempre se debe anteponer la guarda <code>m == 0 or arr[m - 1] == 1</code>.</li>
    <li><strong>Arreglos sin ceros (todos 1s):</strong> Si el arreglo no contiene ceros, el algoritmo debe retornar $-1$. Si no se maneja la condición de parada <code>ini &gt; fin</code>, el algoritmo puede retornar un índice erróneo.</li>
    <li><strong>Hacer un recorrido lineal desde $m$:</strong> Al encontrar un 0 en $m$, algunos estudiantes retroceden linealmente con un bucle mientras <code>arr[i] == 0</code>. Eso degrada la complejidad a $O(n)$ en el peor caso (por ejemplo, en un arreglo compuesto íntegramente por ceros), anulando completamente el beneficio de la búsqueda binaria.</li>
  </ul>
</div>

---

### Errores Frecuentes en Exámenes sobre División y Conquista

1. **Olvidar el Caso Base:** Omitir la condición de parada cuando $n = 1$ o $ini \ge fin$, provocando recursión infinita en la traza.
2. **Calcular erróneamente los parámetros del Teorema Maestro:** Confundir $a$ (cantidad de subproblemas) con $b$ (factor de reducción del tamaño). Ejemplo clásico: en multiplicación de matrices, poner $a = 4$ en lugar de $a = 8$.
3. **No justificar el costo de combinación $f(n)$:** Poner directamente $O(n^2)$ sin detallar que proviene de recorrer las submatrices sumando elemento a elemento.
4. **Dividir en subproblemas no balanceados:** Si la división reduce el tamaño a $n - 1$ (como Quicksort en el peor caso), no se puede aplicar el Teorema Maestro básico; se debe resolver mediante sumatoria telescópica.
"""
