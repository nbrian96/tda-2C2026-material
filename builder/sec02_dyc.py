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
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2025-1-2 (17 de junio de 2025), Ejercicio 1

**Enunciado**  
Realizar un algoritmo que resuelva la multiplicación de dos matrices cuadradas de orden $n$ ($A$ y $B$) mediante división y conquista. Recordemos la definición: $C = A \times B$ donde $C_{ij} = \sum_{k=1}^n A_{ik} \cdot B_{kj}$ para todo $i, j \in \{1, \dots, n\}$. Para simplificar el algoritmo se puede suponer que $n$ es una potencia de 2. Indicar y justificar el orden de complejidad temporal y espacial del algoritmo.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Caso Base ($n = 1$):** Cuando las matrices son de $1 \times 1$, tienen un solo número cada una y devolvemos directamente el producto $A[0][0] \cdot B[0][0]$ en tiempo $O(1)$.
* **División ($n > 1$):** Partimos las matrices $A$ y $B$ de $n \times n$ en **4 submatrices (cuadrantes)** de tamaño $(n/2) \times (n/2)$ cada una:
  $$A = \begin{pmatrix} A_{11} & A_{12} \\ A_{21} & A_{22} \end{pmatrix}, \quad B = \begin{pmatrix} B_{11} & B_{12} \\ B_{21} & B_{22} \end{pmatrix}$$
* **Conquista (8 llamadas recursivas):** Por propiedad de multiplicación de matrices por bloques, para obtener cada cuadrante de $C$ multiplicamos las mitades de las filas de $A$ por las mitades de las columnas de $B$ y sumamos ambos resultados parciales (2 productos por cuadrante, dando **$a = 8$ llamadas recursivas** de tamaño $n/2$):
  * Cuadrante superior izquierdo: $C_{11} = A_{11} B_{11} + A_{12} B_{21}$
  * Cuadrante superior derecho: $C_{12} = A_{11} B_{12} + A_{12} B_{22}$
  * Cuadrante inferior izquierdo: $C_{21} = A_{21} B_{11} + A_{22} B_{21}$
  * Cuadrante inferior derecho: $C_{22} = A_{21} B_{12} + A_{22} B_{22}$
* **Combinación:** Realizamos las 4 sumas de matrices de tamaño $(n/2) \times (n/2)$ y ensamblamos los 4 cuadrantes para devolver la matriz producto $C$ de $n \times n$.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo MultiplicarMatricesDyC(A, B, n):
    // Caso Base: matriz de 1x1
    si n == 1:
        devolver [[ A[0][0] * B[0][0] ]]

    m = n / 2
    // 1. Dividir A y B en 4 cuadrantes de m x m cada una
    (A11, A12, A21, A22) = PartirEn4Bloques(A, m)
    (B11, B12, B21, B22) = PartirEn4Bloques(B, m)

    // 2. Conquista: 8 multiplicaciones recursivas de tamaño n/2
    C11 = MultiplicarMatricesDyC(A11, B11, m) + MultiplicarMatricesDyC(A12, B21, m)
    C12 = MultiplicarMatricesDyC(A11, B12, m) + MultiplicarMatricesDyC(A12, B22, m)
    C21 = MultiplicarMatricesDyC(A21, B11, m) + MultiplicarMatricesDyC(A22, B21, m)
    C22 = MultiplicarMatricesDyC(A21, B12, m) + MultiplicarMatricesDyC(A22, B22, m)

    // 3. Combinar los 4 cuadrantes en la matriz C de n x n
    devolver EnsamblarMatriz(C11, C12, C21, C22)
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* **Complejidad Temporal:**
  - En cada paso se hacen **$a = 8$ llamadas recursivas** sobre submatrices de tamaño $n/2$ (**$b = 2$**).
  - Dividir en cuadrantes y sumar las 4 parejas de matrices de $(n/2) \times (n/2)$ recorre $4 \cdot (n/2)^2 = n^2$ elementos, por lo que cuesta **$f(n) = \Theta(n^2)$** (**$c = 2$**).
  - Ecuación de recurrencia:
    $$T(n) = 8 \cdot T(n/2) + \Theta(n^2)$$
  - Por el **Teorema Maestro**, comparamos $\log_b a = \log_2 8 = 3$ con $c = 2$. Como $\log_b a = 3 > 2 = c$, aplica el **Caso 1** (dominan las hojas) y la complejidad temporal es **$\Theta(n^{\log_2 8}) = \Theta(n^3)$**.
* **Complejidad Espacial:**
  - En cada nivel activo de la pila recursiva (de altura $\log_2 n$) se reservan matrices auxiliares cuyo tamaño se reduce geométricamente: $n^2 + (n/2)^2 + (n/4)^2 + \dots = \Theta(n^2)$. Por lo tanto, la complejidad espacial es **$\Theta(n^2)$**.

```mermaid
flowchart TD
    R["Raíz: T(n) — Costo combinación Θ(n²)"]:::root --> L1["M1 = A11·B11<br/>T(n/2)"]:::mid
    R --> L2["M2 = A12·B21<br/>T(n/2)"]:::mid
    R --> L3["M3 = A11·B12<br/>T(n/2)"]:::mid
    R --> L4["M4 = A12·B22<br/>T(n/2)"]:::mid
    R --> L5["M5 = A21·B11<br/>T(n/2)"]:::mid
    R --> L6["M6 = A22·B21<br/>T(n/2)"]:::mid
    R --> L7["M7 = A21·B12<br/>T(n/2)"]:::mid
    R --> L8["M8 = A22·B22<br/>T(n/2)"]:::mid
    L1 & L2 & L3 & L4 & L5 & L6 & L7 & L8 --> H["Nivel h = log₂(n): 8^(log₂ n) = n³ hojas de costo Θ(1) ⇒ Total Θ(n³)"]:::leaf
    classDef root fill:#1e40af,stroke:#1e3a8a,stroke-width:2px,color:#fff
    classDef mid fill:#334155,stroke:#1e293b,stroke-width:1px,color:#fff
    classDef leaf fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
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

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 1.6 / Guía 01, Ejercicio 4 / Parcial FIUBA

**Enunciado**  
Se tiene un arreglo de $n \ge 3$ elementos en forma de pico, esto es: estrictamente creciente hasta una determinada posición $p$, y estrictamente decreciente a partir de ella (con $0 < p < n - 1$). Por ejemplo, en el arreglo `[1, 2, 3, 1, 0, -2]` la posición del pico es $p = 2$. Se pide:
a. Implementar un algoritmo de división y conquista de orden $O(\log n)$ *(nota: en la Guía v1.0 figura por errata tipográfica $O(\log \log n)$)* que encuentre la posición $p$ del pico: `PosicionPico(v, ini, fin)`.
b. Justificar el orden del algoritmo mediante el Teorema Maestro.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Idea de la pendiente:** En vez de recorrer todo el arreglo, miramos la posición central `m = (ini + fin) / 2` y la comparamos con su vecino inmediato `v[m + 1]`:
  1. **Caso Base (`ini == fin`):** Cuando el subarreglo tiene un solo elemento, ese único candidato es garantizadamente el pico y devolvemos su índice `ini` en $O(1)$.
  2. **Si `v[m] < v[m + 1]` (sube hacia la derecha):** Como el arreglo sube estrictamente hasta el pico y recién después baja, si en `m` todavía estamos subiendo, el pico **está sí o sí a la derecha de `m`**. Descartamos toda la mitad izquierda y buscamos recursivamente en `[m + 1, fin]`.
  3. **Si `v[m] > v[m + 1]` (baja hacia la derecha):** Significa que ya pasamos el pico o bien `m` mismo es el pico. Descartamos la derecha y buscamos recursivamente en `[ini, m]` (incluyendo a `m` porque puede ser el pico).

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo PosicionPico(v, ini, fin):
    // Caso Base: queda un único elemento y es el pico
    si ini == fin:
        devolver ini

    m = (ini + fin) / 2

    // Si la pendiente sube hacia la derecha, el pico está en [m + 1 .. fin]
    si v[m] < v[m + 1]:
        devolver PosicionPico(v, m + 1, fin)
    sino:
        // Si la pendiente baja, el pico está en [ini .. m] (m puede ser el pico)
        devolver PosicionPico(v, ini, m)
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* En cada paso descartamos la mitad del arreglo y realizamos **$a = 1$ llamada recursiva** sobre un subproblema de tamaño $n/2$ (**$b = 2$**), haciendo solo una comparación en tiempo constante **$f(n) = \Theta(1)$** (**$c = 0$**).
* Ecuación de recurrencia:
  $$T(n) = 1 \cdot T(n/2) + \Theta(1)$$
* Aplicando el **Teorema Maestro**: $\log_b a = \log_2 1 = 0 = c$ (**Caso 2**), por lo que la complejidad temporal es **$T(n) = \Theta(n^0 \log n) = O(\log n)$**.

```mermaid
flowchart LR
    A["Rango [0..6]: m=3<br/>A[3]=3 &lt; A[4]=5"]:::step -->|Descarta izq [0..3]| B["Rango [4..6]: m=5<br/>A[5]=6 &gt; A[6]=4"]:::step
    B -->|Conserva m=5| C["Rango [4..5]: m=4<br/>A[4]=5 &lt; A[5]=6"]:::step
    C -->|Descarta m=4| D["Rango [5..5]: ini=fin"]:::step
    D --> E(["Pico Hallado: Índice 5 (A[5] = 6)"]):::opt
    classDef step fill:#1e40af,stroke:#1e3a8a,stroke-width:2px,color:#fff
    classDef opt fill:#15803d,stroke:#166534,stroke-width:2px,color:#fff
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Hacer <code>fin = m - 1</code> en la rama descendente:</strong> Si $v[m] > v[m+1]$, el elemento $v[m]$ podría ser precisamente el pico. Si pasas <code>m - 1</code>, excluyes a $m$ y el algoritmo puede retornar un índice incorrecto. Debe ser <code>PosicionPico(v, ini, m)</code>.</li>
    <li><strong>Desbordamiento de índice al consultar $m+1$:</strong> Como el caso base corta en <code>ini == fin</code> y la división entera redondea hacia abajo, siempre se cumple $m < fin$, por lo que <code>v[m + 1]</code> nunca se sale de rango.</li>
  </ul>
</div>

---

### Ejercicio 3 — Búsqueda del Primer Cero en un Arreglo de Unos y Ceros

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★☆☆☆☆ (1/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 1.4 / Guía 01, Ejercicio 2

**Enunciado**  
Se tiene un arreglo tal que `[1, 1, 1, ..., 0, 0, ...]` (es decir, unos seguidos de ceros). Se pide:
a. Una función de orden $O(\log n)$ *(nota: en la Guía v1.0 figura por errata tipográfica $O(\log \log n)$)* que encuentre el índice del primer `0`. Si no hay ningún `0` (solo hay unos), debe devolver `-1`.
b. Demostrar con el Teorema Maestro que la función es, en efecto, $O(\log n)$.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* Como el arreglo tiene todos los `1` al principio y todos los `0` al final, podemos partir al medio en cada paso buscando el punto exacto donde cambia de `1` a `0`:
  1. **Caso Base (`ini > fin`):** Si el rango se queda sin elementos, significa que no había ningún `0` en todo el arreglo y devolvemos `-1`.
  2. Calculamos la posición del medio `m = (ini + fin) / 2` y miramos `A[m]`:
     - **Si `A[m] == 0` y su anterior es `1` (o `m == 0`):** Estamos parados justo en el primer `0` del arreglo, así que devolvemos `m` inmediatamente.
     - **Si `A[m] == 0` y su anterior también es `0`:** El primer `0` está más hacia la izquierda; descartamos la mitad derecha y buscamos recursivamente en `[ini, m - 1]`.
     - **Si `A[m] == 1`:** Como antes de un `1` solo puede haber otros `1`, el primer `0` solo puede estar a la derecha; descartamos la mitad izquierda y buscamos recursivamente en `[m + 1, fin]`.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo BuscarPrimerCero(A, ini, fin):
    // Caso Base: rango vacío (no existen ceros en el arreglo)
    si ini > fin:
        devolver -1

    m = (ini + fin) / 2

    si A[m] == 0:
        // Si está en el borde izquierdo o su anterior es 1, es el primer cero
        si m == 0 o A[m - 1] == 1:
            devolver m
        // Si su anterior también es 0, buscar más a la izquierda
        devolver BuscarPrimerCero(A, ini, m - 1)
    sino:
        // A[m] == 1: descartar mitad izquierda y buscar a la derecha
        devolver BuscarPrimerCero(A, m + 1, fin)
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* En cada paso descartamos una mitad completa y hacemos **$a = 1$ llamada recursiva** de tamaño $n/2$ (**$b = 2$**), realizando un número constante de comparaciones en tiempo **$f(n) = \Theta(1)$** (**$c = 0$**).
* Ecuación de recurrencia:
  $$T(n) = 1 \cdot T(n/2) + \Theta(1)$$
* Por el **Teorema Maestro**, como $\log_b a = \log_2 1 = 0 = c$ (**Caso 2**), la complejidad temporal es **$T(n) = \Theta(n^0 \log n) = O(\log n)$**.

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

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Acceder a <code>A[m - 1]</code> cuando $m = 0$:</strong> Si el primer cero está en la posición 0, evaluar <code>A[m - 1]</code> sin chequear antes <code>m == 0</code> consulta <code>A[-1]</code> o lanza error de índice fuera de rango. Siempre poner primero <code>m == 0 o A[m - 1] == 1</code>.</li>
    <li><strong>Hacer un recorrido lineal hacia atrás desde $m$:</strong> Al encontrar un 0 en $m$, retroceder con un bucle <code>while</code> hasta el primer cero degrada el peor caso a $O(n)$ (cuando todo el arreglo son ceros). Siempre debe seguir partiendo a la mitad con recursión.</li>
  </ul>
</div>

---

### Ejercicio 4 — Subarreglo Contiguo de Suma Máxima

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2026-2-1 (Enunciados), Ejercicio 1 / Guía 01 (Resuelto)

**Enunciado**  
Dada una lista de números enteros (positivos y negativos), se desea obtener el subarreglo contiguo cuya suma sea máxima. Justificar la complejidad temporal del algoritmo realizado mediante División y Conquista.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **¿Cómo pensamos la división?** Partimos el arreglo a la mitad en dos partes iguales: `izquierda` y `derecha`. El subarreglo contiguo de suma máxima tiene **solo tres lugares posibles** donde estar:
  1. **Completamente en la mitad izquierda:** lo encontramos llamando recursivamente sobre la parte izquierda.
  2. **Completamente en la mitad derecha:** lo encontramos llamando recursivamente sobre la parte derecha.
  3. **Cruzando el medio (empieza en la izquierda y termina en la derecha):** como tiene que ser contiguo, sí o sí pasa por el centro. Para que sume lo máximo posible, caminamos desde el centro hacia la izquierda acumulando la mejor suma parcial, y desde el centro hacia la derecha acumulando la mejor suma parcial. Uniendo esos dos tramos tenemos el mejor subarreglo cruzado en tiempo lineal $O(n)$.
* Finalmente, comparamos las sumas de los tres candidatos (`izquierda`, `derecha` y `cruzado`) y devolvemos el que tenga mayor suma.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo SubarregloMaximaSuma(A, ini, fin):
    // Caso base: un solo elemento
    si ini == fin:
        devolver (A[ini], ini, fin)   // (suma, inicio, fin)

    medio = (ini + fin) / 2

    // 1. Resolver recursivamente mitad izquierda y mitad derecha
    cand_izq = SubarregloMaximaSuma(A, ini, medio)
    cand_der = SubarregloMaximaSuma(A, medio + 1, fin)

    // 2. Calcular el mejor subarreglo que cruza por el medio
    cand_cruzado = MejorCruzado(A, ini, medio, fin)

    // 3. Devolver el candidato de mayor suma entre los tres
    devolver el de mayor suma entre (cand_izq, cand_der, cand_cruzado)

función MejorCruzado(A, ini, medio, fin):
    // Extender desde medio hacia la izquierda
    mejor_izq = -infinito, suma = 0, idx_izq = medio
    para i desde medio bajando hasta ini:
        suma = suma + A[i]
        si suma > mejor_izq:
            mejor_izq = suma
            idx_izq = i

    // Extender desde medio + 1 hacia la derecha
    mejor_der = -infinito, suma = 0, idx_der = medio + 1
    para j desde medio + 1 hasta fin:
        suma = suma + A[j]
        si suma > mejor_der:
            mejor_der = suma
            idx_der = j

    devolver (mejor_izq + mejor_der, idx_izq, idx_der)
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* Hacemos **$a = 2$ llamadas recursivas**, cada una con la mitad de elementos (**$b = 2$**).
* La función `MejorCruzado` recorre desde el centro hacia ambos extremos pasando una sola vez por cada elemento del intervalo actual, por lo que cuesta tiempo lineal **$f(n) = O(n)$** (es decir, **$c = 1$**).
* Ecuación de recurrencia:
  $$T(n) = 2 \cdot T(n/2) + O(n)$$
* Por el **Teorema Maestro**, como $\log_b a = \log_2 2 = 1 = c$ (**Caso 2**), la complejidad temporal total es **$O(n \log n)$**.

---

### Ejercicio 5 — Compra y Venta de Acciones para Máxima Ganancia

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Problema Resuelto 1.A

**Enunciado**  
Se consideran $n$ días consecutivos de cotización de una acción, numerados $i = 1, 2, \dots, n$, con precio $p(i)$ por acción. Se desea comprar 1000 acciones en algún día $i$ y venderlas todas en un día posterior $j$. Determinar por División y Conquista la máxima ganancia que puede obtenerse con complejidad mejor que $O(n^2)$ (en $O(n)$).

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* Si dividimos los días en una **mitad izquierda** (días anteriores) y una **mitad derecha** (días posteriores), la mejor compra-venta puede ocurrir:
  1. Comprando y vendiendo dentro de la mitad izquierda (ganancia `g1`).
  2. Comprando y vendiendo dentro de la mitad derecha (ganancia `g2`).
  3. **Comprando en la mitad izquierda y vendiendo en la mitad derecha:** para ganar lo máximo posible cruzando las mitades, nos conviene comprar en el día **más barato** de la izquierda (`min1`) y vender en el día **más caro** de la derecha (`max2`), ganando `max2 - min1`.
* Para no recalcular mínimos y máximos con un ciclo en cada paso (lo que llevaría a $O(n \log n)$), hacemos que cada llamada recursiva devuelva directamente una tripla `(mínimo, máximo, ganancia)`. Así combinamos las dos mitades con solo un par de comparaciones en tiempo constante $O(1)$.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo AnalizarIntervalo(precios, inicio, fin):
    // Caso base: un único día (no se puede comprar y vender en días distintos)
    si inicio == fin:
        devolver (precios[inicio], precios[inicio], 0)

    medio = (inicio + fin) / 2

    // Resolver ambas mitades
    (min1, max1, g1) = AnalizarIntervalo(precios, inicio, medio)
    (min2, max2, g2) = AnalizarIntervalo(precios, medio + 1, fin)

    // Combinar en O(1)
    minimo = min(min1, min2)
    maximo = max(max1, max2)
    cruce = max2 - min1
    ganancia = max(g1, g2, cruce)

    devolver (minimo, maximo, ganancia)
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* Se realizan **$a = 2$ llamadas recursivas** sobre mitades de tamaño $n/2$ (**$b = 2$**), y la combinación hace únicamente restas y comparaciones en tiempo constante **$f(n) = \Theta(1)$** (**$c = 0$**).
* Ecuación de recurrencia:
  $$T(n) = 2 \cdot T(n/2) + \Theta(1)$$
* Aplicando el **Teorema Maestro**, $\log_b a = \log_2 2 = 1 > 0 = c$ (**Caso 1**), por lo que la complejidad es **$T(n) = O(n^{\log_2 2}) = O(n)$**.

---

### Ejercicio 6 — Aplicación Sistemática del Teorema Maestro (9 Recurrencias)

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★☆☆☆☆ (1/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 1.1

**Enunciado**  
Indicar, utilizando el Teorema Maestro, la complejidad de cada una de las siguientes ecuaciones de recurrencia:
* $A(n) = 2A(n/4) + \sqrt{n}$, $\quad B(n) = 2B(n/4) + n$, $\quad C(n) = 2C(n/4) + n^2$
* $D(n) = 3D(n/3) + \sqrt{n}$, $\quad E(n) = 3E(n/3) + n$, $\quad F(n) = 3F(n/3) + n^2$
* $G(n) = 4G(n/2) + \sqrt{n}$, $\quad H(n) = 4H(n/2) + n$, $\quad I(n) = 4I(n/2) + n^2$

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

Para cualquier recurrencia $T(n) = a \cdot T(n/b) + \Theta(n^c)$, solo debemos comparar el exponente de las hojas **$\log_b a$** contra el exponente del trabajo exterior **$c$** (recordando que $\sqrt{n} = n^{0.5}$, por lo que $c = 0.5$):
* Si **$\log_b a > c$** (ganan las hojas, Caso 1): el orden es **$O(n^{\log_b a})$**.
* Si **$\log_b a = c$** (empatados, Caso 2): el orden es **$O(n^c \log n)$**.
* Si **$\log_b a < c$** (gana el trabajo exterior, Caso 3): el orden es **$O(n^c)$**.

#### 2. Resolución Completa de las 9 Ecuaciones

| Recurrencia | $a$ | $b$ | $\log_b a$ | $f(n) = n^c$ | Comparación ($\log_b a$ vs $c$) | Caso TM | Complejidad Final |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **$A(n) = 2A(n/4) + \sqrt{n}$** | $2$ | $4$ | $\log_4 2 = 0.5$ | $n^{0.5}$ ($c=0.5$) | $0.5 = 0.5$ | Caso 2 | **$O(\sqrt{n} \log n)$** |
| **$B(n) = 2B(n/4) + n$** | $2$ | $4$ | $\log_4 2 = 0.5$ | $n^1$ ($c=1$) | $0.5 < 1$ | Caso 3 | **$O(n)$** |
| **$C(n) = 2C(n/4) + n^2$** | $2$ | $4$ | $\log_4 2 = 0.5$ | $n^2$ ($c=2$) | $0.5 < 2$ | Caso 3 | **$O(n^2)$** |
| **$D(n) = 3D(n/3) + \sqrt{n}$** | $3$ | $3$ | $\log_3 3 = 1$ | $n^{0.5}$ ($c=0.5$) | $1 > 0.5$ | Caso 1 | **$O(n)$** |
| **$E(n) = 3E(n/3) + n$** | $3$ | $3$ | $\log_3 3 = 1$ | $n^1$ ($c=1$) | $1 = 1$ | Caso 2 | **$O(n \log n)$** |
| **$F(n) = 3F(n/3) + n^2$** | $3$ | $3$ | $\log_3 3 = 1$ | $n^2$ ($c=2$) | $1 < 2$ | Caso 3 | **$O(n^2)$** |
| **$G(n) = 4G(n/2) + \sqrt{n}$** | $4$ | $2$ | $\log_2 4 = 2$ | $n^{0.5}$ ($c=0.5$) | $2 > 0.5$ | Caso 1 | **$O(n^2)$** |
| **$H(n) = 4H(n/2) + n$** | $4$ | $2$ | $\log_2 4 = 2$ | $n^1$ ($c=1$) | $2 > 1$ | Caso 1 | **$O(n^2)$** |
| **$I(n) = 4I(n/2) + n^2$** | $4$ | $2$ | $\log_2 4 = 2$ | $n^2$ ($c=2$) | $2 = 2$ | Caso 2 | **$O(n^2 \log n)$** |

---

### Ejercicio 7 — Determinar si un Arreglo está Ordenado

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★☆☆☆☆ (1/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 1.2

**Enunciado**  
Implementar, por división y conquista, una función que, dado un arreglo y su tamaño (cantidad de elementos), determine si el mismo se encuentra ordenado de forma ascendente. Indicar y justificar el orden.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* Un arreglo de 0 o 1 elementos siempre está ordenado.
* Si tiene más elementos, lo partimos a la mitad. Para que todo el arreglo esté ordenado deben cumplirse **tres condiciones a la vez**:
  1. Que la mitad izquierda esté ordenada.
  2. Que la mitad derecha esté ordenada.
  3. **Condición de enganche en la frontera:** que el último elemento de la mitad izquierda sea menor o igual al primer elemento de la mitad derecha (`A[medio] <= A[medio + 1]`).

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo EstaOrdenado(A, ini, fin):
    // Caso base: 0 o 1 elemento siempre está ordenado
    si ini >= fin:
        devolver Verdadero

    medio = (ini + fin) / 2

    // Si en el borde del medio ya está desordenado, cortamos rápido
    si A[medio] > A[medio + 1]:
        devolver Falso

    // Ambas mitades deben estar ordenadas
    devolver EstaOrdenado(A, ini, medio) y EstaOrdenado(A, medio + 1, fin)
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* En el peor caso (cuando el arreglo sí está ordenado), el algoritmo verifica las **$a = 2$ mitades** de tamaño $n/2$ (**$b = 2$**) y hace una sola comparación en el borde en tiempo **$O(1)$** (**$c = 0$**).
* Recurrencia: $T(n) = 2 \cdot T(n/2) + O(1)$.
* Por el **Teorema Maestro** ($\log_2 2 = 1 > 0 = c$, **Caso 1**), el orden es **$O(n)$**.

---

### Ejercicio 8 — Encontrar el Único Número Duplicado en Arreglo Ordenado

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 1.3 / Guía 01, Ejercicio 1

**Enunciado**  
Se cuenta con un arreglo de enteros ordenado de manera ascendente, que contiene exactamente un número duplicado (es decir, todos los demás elementos son distintos, sin duplicados). Implementar una función que encuentre dicho número utilizando división y conquista. Indicar y justificar la complejidad del algoritmo, utilizando el Teorema Maestro.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* *(Nota de cátedra: En la versión clásica de FIUBA los elementos son consecutivos, o bien comparamos la diferencia de valores contra la diferencia de índices).*
* **Idea clave de los índices:** Como el arreglo está ordenado de forma estrictamente creciente salvo por el único par duplicado, entre dos posiciones `ini` y `medio` sin duplicados los valores están obligados a crecer **al menos tanto como la cantidad de pasos dados**: `A[medio] - A[ini] >= medio - ini` (o si son enteros consecutivos a partir de `A[0]`, antes del duplicado se cumple `A[i] == A[0] + i` y después del duplicado se atrasa en 1: `A[i] == A[0] + i - 1`).
* Miramos el elemento del medio `m`:
  - Si `A[m]` es igual a `A[m - 1]` o a `A[m + 1]`, ¡ya encontramos el duplicado!
  - Si en la mitad izquierda la diferencia de valores `A[m] - A[ini]` es **menor** que la cantidad de pasos `m - ini` (en elementos consecutivos), significa que hubo una repetición que "achicó" el crecimiento en la izquierda: buscamos en `[ini, m]`.
  - Si no, el duplicado está garantizadamente en la mitad derecha: buscamos en `[m + 1, fin]`.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo EncontrarDuplicado(A, ini, fin):
    medio = (ini + fin) / 2

    // 1. Verificar si el duplicado está justo en el medio
    si (medio > ini y A[medio] == A[medio - 1]) o (medio < fin y A[medio] == A[medio + 1]):
        devolver A[medio]

    // 2. Si los valores a la izquierda crecieron menos que la distancia de índices,
    //    el número repetido está en la mitad izquierda
    si (A[medio] - A[ini]) < (medio - ini):
        devolver EncontrarDuplicado(A, ini, medio - 1)
    sino:
        devolver EncontrarDuplicado(A, medio + 1, fin)
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* En cada paso descartamos una mitad completa y hacemos **$a = 1$ llamada recursiva** de tamaño $n/2$ (**$b = 2$**) con comparaciones en tiempo constante **$O(1)$** (**$c = 0$**).
* Ecuación de recurrencia: $T(n) = 1 \cdot T(n/2) + O(1)$.
* Aplicando el **Teorema Maestro**: $\log_2 1 = 0 = c$ (**Caso 2**), por lo que la complejidad es **$O(\log n)$**.

---

### Ejercicio 9 — Parte Entera de la Raíz Cuadrada

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 1.5 / Guía 01, Ejercicio 3

**Enunciado**  
Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la raíz cuadrada de un número $n$, en tiempo $O(\log n)$ *(nota: en la Guía v1.0 figura por errata tipográfica $O(\log \log n)$)*. Por ejemplo, para $n = 10$ debe devolver $3$, y para $n = 25$ debe devolver $5$.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* Buscamos el mayor entero $m \in [0, n]$ tal que $m^2 \le n$ y $(m + 1)^2 > n$.
* Como la función $f(m) = m^2$ es estrictamente creciente para números positivos, podemos aplicar búsqueda binaria sobre el rango de candidatos `[ini, fin]` (inicialmente `[0, n]`):
  - Probamos el valor central `m = (ini + fin) / 2`.
  - Si `m * m <= n` y `(m + 1) * (m + 1) > n`, entonces `m` es exactamente la parte entera de $\sqrt{n}$.
  - Si `m * m > n`, nos pasamos: buscamos en la mitad menor `[ini, m - 1]`.
  - Si `m * m <= n` pero `(m + 1)^2 <= n`, todavía nos quedamos cortos: buscamos en la mitad mayor `[m + 1, fin]`.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo RaizEntera(n):
    devolver BuscarRaiz(n, 0, n)

función BuscarRaiz(n, ini, fin):
    medio = (ini + fin) / 2

    // Si medio^2 no supera n, pero (medio + 1)^2 ya lo supera, encontramos la parte entera
    si (medio * medio <= n) y ((medio + 1) * (medio + 1) > n):
        devolver medio

    si medio * medio > n:
        devolver BuscarRaiz(n, ini, medio - 1)   // Nos pasamos, probar más chicos
    sino:
        devolver BuscarRaiz(n, medio + 1, fin)   // Falta crecer, probar más grandes
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* El rango inicial tiene tamaño $n$, y en cada paso se realiza **$a = 1$ llamada recursiva** sobre la mitad del intervalo (**$b = 2$**), realizando multiplicaciones y comparaciones en tiempo **$O(1)$** (**$c = 0$**).
* Por el **Teorema Maestro**, $T(n) = T(n/2) + O(1)$ tiene $\log_2 1 = 0 = c$ (**Caso 2**), resultando en tiempo **$O(\log n)$**.

---

### Ejercicio 10 — MergeSort Modificado (División en 3 y en K Partes)

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 1.7

**Enunciado**  
Se quiere implementar MergeSort pero, en vez de dividir en dos partes el arreglo, dividirlo en tres, llamando recursivamente al algoritmo para cada una de las partes y luego uniéndolas.
a. Suponiendo que el merge de las tres partes se realiza en tiempo lineal, calcular el orden del algoritmo.
b. Si en vez de dividir en tres partes, se dividiera el arreglo en $n$, siendo $n$ la cantidad de elementos del arreglo, ¿a qué otro algoritmo de ordenamiento se asemeja esta implementación? ¿Cuál es el orden de dicho algoritmo?
c. Dado lo obtenido en los puntos anteriores, ¿tiene sentido implementar MergeSort con $k$ separaciones, para $k > 2$?

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Punto a (Dividir en 3 partes):**
  - Llamamos recursivamente a **$a = 3$ subproblemas** de tamaño **$n / 3$** ($b = 3$) y los unimos en tiempo lineal **$O(n)$** ($c = 1$).
  - Recurrencia: $T(n) = 3 \cdot T(n/3) + O(n)$.
  - Por el **Teorema Maestro**, $\log_3 3 = 1 = c$ (**Caso 2**), por lo que el orden sigue siendo **$O(n \log n)$** (cambia únicamente la base del logaritmo de $\log_2 n$ a $\log_3 n$, que difiere solo en una constante multiplicativa).
* **Punto b (Dividir en $n$ partes de tamaño 1):**
  - Si partimos el arreglo directamente en $n$ pedacitos de $1$ elemento, las llamadas recursivas caen directo en el caso base sin hacer nada, y todo el trabajo ocurre en el `merge` de las $n$ partes de tamaño $1$.
  - Para hacer el merge de $n$ listas de 1 elemento, en cada paso debemos buscar el mínimo entre las $n$ listas (tarda $O(n)$), luego entre las $n - 1$ restantes, y así $n$ veces.
  - Esto equivale exactamente a **Selection Sort** (Ordenamiento por Selección), cuya complejidad es **$O(n^2)$**.
* **Punto c (¿Tiene sentido usar $k > 2$ en memoria principal?):**
  - **No tiene sentido** en memoria RAM estándar: al dividir en $k$ partes, la altura del árbol baja a $\log_k n$, pero en cada paso del `merge` hay que comparar entre $k$ candidatos para elegir el mínimo (haciendo $k - 1$ comparaciones por elemento, o $\log_2 k$ con un heap, lo que da $n \log_2 k \cdot \log_k n = n \log_2 n$ igual que con $k = 2$, pero con código más complejo y mayor sobrecarga de constantes). *(Solo tiene utilidad en ordenamiento externo en disco para reducir lecturas/escrituras).*

---

### Ejercicio 11 — Producto de Matrices de la Profesora Manterola vs Strassen

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 1.8

**Enunciado**  
Un algoritmo sencillo para multiplicar matrices de $n \times n$ demora $O(n^3)$. El algoritmo de Strassen (que utiliza División y Conquista) lo hace en $O(n^{\log_2 7}) \approx O(n^{2.81})$. La profesora Manterola quiere implementar un algoritmo de División y Conquista que sea aún más veloz, donde divida al problema en $A$ subproblemas de tamaño de $n/4$, y que juntar las soluciones parciales sea $O(n^2)$. ¿Cuál es el máximo $A$ entero para que el orden del algoritmo sea menor que el del algoritmo de Strassen? Justificar.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* Planteamos la ecuación de recurrencia del algoritmo de la profesora Manterola:
  - Cantidad de subproblemas: **$a = A$**.
  - Tamaño de cada subproblema: $n / 4 \implies$ **$b = 4$**.
  - Costo de combinar soluciones: $O(n^2) \implies$ **$c = 2$**.
  $$T(n) = A \cdot T(n/4) + O(n^2)$$
* Por el **Teorema Maestro**, como buscamos un orden que sea **menor que el de Strassen** ($\log_2 7 \approx 2.807$), pero sabemos que es mayor a $2$, estamos en el **Caso 1** donde el orden del algoritmo está dado por el exponente de las hojas: **$O(n^{\log_4 A})$**.
* Para que sea estrictamente más veloz que Strassen, necesitamos que su exponente sea menor que $\log_2 7$:
  $$\log_4 A < \log_2 7$$
* Cambiamos a base 2 sabiendo que $\log_4 A = \frac{\log_2 A}{\log_2 4} = \frac{\log_2 A}{2}$:
  $$\frac{\log_2 A}{2} < \log_2 7 \implies \log_2 A < 2 \cdot \log_2 7 = \log_2(7^2) = \log_2 49$$
  $$A < 49$$
* Como $A$ es una cantidad entera de subproblemas recursivos, el **máximo valor entero posible es $A = 48$** (con $A = 48$, la complejidad queda $O(n^{\log_4 48}) \approx O(n^{2.792}) < O(n^{2.807})$).

---

### Ejercicio 12 — Elemento Mayoritario (Más de la Mitad de las Veces)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 1.9 / Guía 01, Ejercicio 9

**Enunciado**  
Implementar una función (que utilice división y conquista) de orden $O(n \log n)$ *(nota: en la Guía v1.0 figura por errata tipográfica $O(n \log \log n)$)* que, dado un arreglo de $n$ números enteros, devuelva `true` o `false` según si existe algún elemento que aparezca más de la mitad de las veces, sin ordenar el arreglo ni usar tabla de hash. Justificar el orden de la solución.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Propiedad clave:** Si un número aparece **más de la mitad de las veces** en todo el arreglo ($> n/2$), entonces es matemáticamente imposible que aparezca la mitad o menos en ambas mitades a la vez. **Obligatoriamente tiene que ser el elemento mayoritario en la mitad izquierda, o en la mitad derecha (o en ambas)**.
* Entonces creamos una función recursiva `BuscarMayoritario(A, ini, fin)` que devuelve el elemento mayoritario del rango (o `nulo` si no hay):
  1. **Caso Base:** Si el rango tiene 1 solo elemento, ese elemento es el mayoritario de su rango.
  2. **División y Conquista:** Si tiene más, pedimos el candidato mayoritario de la mitad izquierda (`cand_izq`) y el de la mitad derecha (`cand_der`).
  3. **Combinación:** Si ambos coinciden, ese mismo es el ganador. Si son distintos, **contamos cuántas veces aparece cada uno** en todo el rango actual `[ini, fin]` recorriéndolo con un ciclo lineal $O(n)$. Si alguno supera la mitad del tamaño del rango, lo devolvemos; si ninguno supera la mitad, devolvemos `nulo`.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo TieneMayoritario(A, n):
    candidato = BuscarMayoritario(A, 0, n - 1)
    devolver (candidato != nulo)

función BuscarMayoritario(A, ini, fin):
    // Caso base: un único elemento es mayoritario de sí mismo
    si ini == fin:
        devolver A[ini]

    medio = (ini + fin) / 2
    cand_izq = BuscarMayoritario(A, ini, medio)
    cand_der = BuscarMayoritario(A, medio + 1, fin)

    tamanio = fin - ini + 1

    // Contar apariciones de los candidatos en el rango [ini..fin] en O(n)
    si cand_izq != nulo y contarApariciones(A, ini, fin, cand_izq) > tamanio / 2:
        devolver cand_izq

    si cand_der != nulo y contarApariciones(A, ini, fin, cand_der) > tamanio / 2:
        devolver cand_der

    devolver nulo
```

#### 3. Justificación de Complejidad (Para entregar en el parcial)

* Dividimos el problema en **$a = 2$ llamadas recursivas** de tamaño $n/2$ (**$b = 2$**).
* En la etapa de combinación, contar cuántas veces aparecen `cand_izq` y `cand_der` en el subarreglo actual recorre sus elementos en tiempo lineal **$f(n) = O(n)$** (**$c = 1$**).
* Ecuación de recurrencia:
  $$T(n) = 2 \cdot T(n/2) + O(n)$$
* Por el **Teorema Maestro**, $\log_2 2 = 1 = c$ (**Caso 2**), lo que demuestra que la complejidad temporal es **$O(n \log n)$**.

---

### Errores Frecuentes en Exámenes sobre División y Conquista

1. **Olvidar el Caso Base:** Omitir la condición de parada cuando $n = 1$ o $ini \ge fin$, provocando recursión infinita en la traza.
2. **Calcular erróneamente los parámetros del Teorema Maestro:** Confundir $a$ (cantidad de subproblemas) con $b$ (factor de reducción del tamaño). Ejemplo clásico: en multiplicación de matrices, poner $a = 4$ en lugar de $a = 8$.
3. **No justificar el costo de combinación $f(n)$:** Poner directamente $O(n^2)$ sin detallar que proviene de recorrer las submatrices sumando elemento a elemento.
4. **Dividir en subproblemas no balanceados:** Si la división reduce el tamaño a $n - 1$ (como Quicksort en el peor caso), no se puede aplicar el Teorema Maestro básico; se debe resolver mediante sumatoria telescópica.
"""
