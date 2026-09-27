# El Problema de la Mochila y Algoritmos Greedy (Voraces)

**Materia:** Teoría de Algoritmos (TB024 / 75.29 / 95.06) – FIUBA  
**Cátedra:** Echevarría  
**Referencias:** 
- [03a - Greedy I.pdf](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/DIapositivas/03a%20-%20Greedy%20I.pdf)
- [04 - Greedy II.pdf](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/DIapositivas/04%20-%20Greedy%20II.pdf)
- [TP1 - Enunciado](file:///home/rtadmin/Documentos/Facultad/teoria_de_algoritmos/tda-2c2026-tp01/README.md)

---

## Índice
1. [El Problema de la Mochila (Knapsack Problem)](#1-el-problema-de-la-mochila-knapsack-problem)
   - [Definición Formal](#definición-formal)
   - [Variantes Principales: 0/1 vs. Fraccionaria](#variantes-principales-01-vs-fraccionaria)
   - [Complejidad Intrínseca](#complejidad-intrínseca)
2. [¿Qué es un Algoritmo Greedy (Voraz / Goloso)?](#2-qué-es-un-algoritmo-greedy-voraz--goloso)
   - [Principio de Funcionamiento](#principio-de-funcionamiento)
   - [Pros y Contras](#pros-y-contras)
   - [Cuándo es Óptimo y Cuándo es Aproximación](#cuándo-es-óptimo-y-cuándo-es-aproximación)
3. [Resolución de la Mochila con Algoritmos Greedy](#3-resolución-de-la-mochila-con-algoritmos-greedy)
   - [Mochila Fraccionaria: Solución Óptima](#a-mochila-fraccionaria-solución-óptima)
   - [Mochila 0/1: Heurísticas Intuitivas y por qué fallan](#b-mochila-01-heurísticas-intuitivas-y-por-qué-fallan)
   - [Algoritmo Greedy con Garantía de Calidad 1/2](#c-algoritmo-greedy-con-garantía-de-calidad-12)
   - [Demostración de la Cota 1/2](#demostración-de-la-cota-12)
   - [Complejidad Temporal](#complejidad-temporal)
   - [Ejemplo Paso a Paso donde actúa la Garantía](#ejemplo-paso-a-paso-donde-actúa-la-garantía)

---

## 1. El Problema de la Mochila (Knapsack Problem)

El problema de la mochila es uno de los problemas fundamentales de la optimización combinatoria.

### Definición Formal
Se dispone de:
* Una mochila con capacidad de carga máxima $W \in \mathbb{R}^+$ (o $\mathbb{Z}^+$).
* Un conjunto de $n$ objetos disponibles $S = \{1, 2, \dots, n\}$.
* Cada objeto $i$ posee:
  * Un peso $w_i > 0$.
  * Un valor, beneficio o ganancia $v_i > 0$.

**Objetivo:**  
Seleccionar qué objetos colocar dentro de la mochila de modo que la suma de sus valores sea **máxima**, respetando la restricción de capacidad (la suma de los pesos no puede exceder $W$).

Matemáticamente, para la versión 0/1:
$$\max \sum_{i=1}^n v_i x_i \quad \text{sujeto a} \quad \sum_{i=1}^n w_i x_i \le W, \quad x_i \in \{0, 1\}$$

### Variantes Principales: 0/1 vs. Fraccionaria
1. **Mochila 0/1 (Indivisible):**
   * Cada objeto se toma entero o se descarta ($x_i \in \{0, 1\}$).
   * No se permite fraccionar objetos ni incluir duplicados (a menos que se especifique multiconjunto).
2. **Mochila Fraccionaria (Divisible):**
   * Se permite tomar una porción continua de cualquier objeto ($x_i \in [0, 1]$).
   * El peso aportado es $x_i \cdot w_i$ y el valor obtenido es $x_i \cdot v_i$.

### Complejidad Intrínseca
En la mochila 0/1, hay $2^n$ subconjuntos posibles de objetos. El problema es **NP-Hard**.
* Un enfoque de **Fuerza Bruta** explora las $2^n$ combinaciones ($O(2^n)$).
* Mediante **Backtracking** se poda el espacio de búsqueda descartando ramas que superen el peso o no puedan mejorar el mejor valor actual, pero en el peor caso sigue siendo exponencial.
* Mediante **Programación Dinámica** se alcanza una solución exacta en tiempo pseudo-polinomial ($O(n \cdot W)$ o $O(n \cdot V)$).
* Mediante **Greedy** se obtiene una solución aproximada muy rápidamente ($O(n \log n)$).

---

## 2. ¿Qué es un Algoritmo Greedy (Voraz / Goloso)?

### Principio de Funcionamiento
Un algoritmo voraz construye una solución paso a paso aplicando una **regla de selección localmente óptima**:
1. En cada iteración, toma la decisión que parece más conveniente en ese instante inmediato (la más "codiciosa"), sin considerar el impacto global futuro.
2. **Irrevocabilidad (sin marcha atrás):** Una vez tomada una decisión, esta se mantiene fija; nunca se desanda un paso (a diferencia de Backtracking).
3. Continúa iterando hasta completar una solución factible o agotar las alternativas.

### Pros y Contras
* **Ventajas:**
  * Muy simples e intuitivos de diseñar e implementar.
  * Extremadamente rápidos: habitualmente dominados por el ordenamiento inicial ($O(n \log n)$) o lineales ($O(n)$).
* **Desventajas:**
  * Rara vez garantizan hallar el óptimo global a menos que el problema exhiba la propiedad de elección greedy y subestructura óptima (como en matroides).
  * Pueden caer en soluciones subóptimas o incluso arbitrariamente malas si una elección temprana bloquea mejores combinaciones globales.

### Cuándo es Óptimo y Cuándo es Aproximación
* **Problemas donde Greedy es Óptimo:**
  * *Interval Scheduling* (Planificación de intervalos ordenando por tiempo de finalización más temprano).
  * *Árbol de Tendido Mínimo* (Algoritmos de Prim y Kruskal).
  * *Camino Mínimo en grafos con pesos no negativos* (Dijkstra).
  * *Códigos de Huffman* (Compresión de datos sin pérdida).
  * *Mochila Fraccionaria*.
* **Problemas donde Greedy NO es Óptimo (pero sirve como aproximación):**
  * *Mochila 0/1*.
  * *Problema del Viajante de Comercio (TSP)*.
  * *Vertex Cover*, *Set Cover*.

---

## 3. Resolución de la Mochila con Algoritmos Greedy

### A. Mochila Fraccionaria: Solución Óptima
En la mochila fraccionaria, la regla voraz por excelencia es ordenar por **densidad de valor** (relación valor/peso):
$$r_i = \frac{v_i}{w_i}$$
Se ordenan los elementos de mayor a menor según $r_i$ y se introducen enteros mientras quepan. Del primer objeto que no quepa entero, se toma la fracción exacta que complete la capacidad remanente. **Este algoritmo siempre garantiza el óptimo global.**

---

### B. Mochila 0/1: Heurísticas Intuitivas y por qué fallan
Para elementos indivisibles ($x_i \in \{0, 1\}$), se podrían considerar tres reglas naturales:

1. **Priorizar menor peso ($w_i$):**
   * *Idea:* Entran más objetos en la mochila.
   * *Falla:* Los objetos livianos pueden tener un valor insignificante.
   * *Contraejemplo:* $W = 5$. Objetos: $A(w=1, v=7), B(w=3, v=4), C(w=4, v=8)$. El algoritmo toma $A$ y $B$ (peso 4, valor 11), mientras que $\{A, C\}$ (peso 5, valor 15) es superior.

2. **Priorizar mayor valor ($v_i$):**
   * *Idea:* Asegurar los objetos más valiosos.
   * *Falla:* Un objeto de gran valor puede ser excesivamente pesado y bloquear la entrada de varios objetos con menor valor individual pero cuya suma sea superior.
   * *Contraejemplo:* $W = 5$. Objetos: $A(w=5, v=14), B(w=1, v=9), C(w=2, v=6)$. El algoritmo toma $A$ (valor 14), pero $\{B, C\}$ tiene peso 3 y valor 15.

3. **Priorizar mayor relación valor/peso ($v_i / w_i$):**
   * *Idea:* Maximizar el rendimiento por unidad de capacidad.
   * *Falla:* En la versión 0/1, puede dejar espacio ocioso no aprovechable que podría haber ocupado un único objeto de gran valor.
   * *Contraejemplo patológico:*  
     Capacidad $W = 100$.  
     - Objeto 1: $w_1 = 1$, $v_1 = 2 \implies r_1 = 2$  
     - Objeto 2: $w_2 = 100$, $v_2 = 100 \implies r_2 = 1$  
     El algoritmo toma el objeto 1 (ocupa 1 de capacidad, valor 2). Luego el objeto 2 ya no cabe.  
     **Resultado greedy:** Valor 2.  
     **Óptimo global:** Tomar el objeto 2 con valor 100.  
     *El error relativo puede ser arbitrariamente grande si no se corrige.*

---

### C. Algoritmo Greedy con Garantía de Calidad 1/2
Para evitar el fallo catastrófico de la heurística valor/peso en la mochila 0/1, se utiliza una modificación que otorga una **garantía de aproximación de factor 2** (o garantía de calidad $1/2$): la solución obtenida nunca será menor al 50% de la solución óptima.

#### Pasos del Algoritmo:
1. **Filtrado previo:** Descartar cualquier objeto que individualmente pese más que la capacidad de la mochila ($w_i > W$).
2. **Ordenamiento:** Ordenar los elementos restantes en forma decreciente según su relación valor/peso:
   $$\frac{v_1}{w_1} \ge \frac{v_2}{w_2} \ge \dots \ge \frac{v_n}{w_n}$$
3. **Llenado Greedy estándar:**
   * Recorrer los elementos en el orden anterior.
   * Si el elemento $i$ cabe en la capacidad restante, incluirlo en el conjunto solución $S_1$ y sumar su valor a $P_1$.
   * Al encontrar el **primer elemento que no puede ser incluido por falta de espacio**, se lo define como **Elemento Crítico ($c$)** con peso $w_c$ y valor $v_c$, y se detiene o se guarda aparte.
4. **Comparación Final:**
   * Se compara el valor de la solución greedy acumulada ($P_1$) contra el valor del elemento crítico en solitario ($v_c$).
   * Se define la solución final como:
     $$\text{Solución} = \begin{cases} 
     S_1 & \text{si } P_1 \ge v_c \\
     \{c\} & \text{si } v_c > P_1 
     \end{cases}$$
   * El valor resultante es $\max(P_1, v_c)$.

#### Pseudocódigo
```python
def mochila_greedy_con_garantia(objetos, W):
    # objetos es una lista de tuplas o estructuras (id, peso, valor)
    # 1. Filtrar los que no entran por sí solos
    candidatos = [obj for obj in objetos if obj.peso <= W]
    if not candidatos:
        return 0, []

    # 2. Ordenar por densidad valor/peso descendente
    candidatos.sort(key=lambda x: x.valor / x.peso, reverse=True)

    solucion_greedy = []
    peso_acumulado = 0
    valor_acumulado = 0
    elemento_critico = None

    # 3. Llenado voraz e identificación del elemento crítico
    for obj in candidatos:
        if peso_acumulado + obj.peso <= W:
            solucion_greedy.append(obj)
            peso_acumulado += obj.peso
            valor_acumulado += obj.valor
        elif elemento_critico is None:
            elemento_critico = obj

    # 4. Evaluación de la garantía de calidad (1/2)
    if elemento_critico is not None and elemento_critico.valor > valor_acumulado:
        return elemento_critico.valor, [elemento_critico]
    
    return valor_acumulado, solucion_greedy
```

---

### Demostración de la Cota 1/2
¿Por qué este algoritmo garantiza al menos la mitad del valor óptimo?

1. Sea $OPT$ el valor de la solución óptima del problema entero 0/1.
2. Sea $OPT_{\text{frac}}$ el valor de la solución óptima del problema fraccionario con los mismos elementos. Es directo que:
   $$OPT \le OPT_{\text{frac}}$$
3. En la solución fraccionaria óptima, se incorporan todos los elementos del conjunto greedy $S_1$ completos (con valor $P_1$) más una **fracción** $\alpha \in [0, 1)$ del elemento crítico $c$:
   $$OPT_{\text{frac}} = P_1 + \alpha \cdot v_c < P_1 + v_c$$
4. Por lo tanto:
   $$OPT \le OPT_{\text{frac}} < P_1 + v_c$$
5. El algoritmo elige $\text{Sol} = \max(P_1, v_c)$. Por propiedades de los números reales, el máximo de dos cantidades es mayor o igual a su promedio:
   $$\max(P_1, v_c) \ge \frac{P_1 + v_c}{2}$$
6. Combinando con la cota anterior:
   $$\text{Sol} \ge \frac{P_1 + v_c}{2} > \frac{OPT}{2}$$

Esto prueba formalmente que:
$$\frac{\text{Sol}}{OPT} > \frac{1}{2}$$
La solución greedy nunca cae por debajo de la mitad del óptimo.

---

### Complejidad Temporal
* **Filtrado inicial:** $O(n)$ operaciones.
* **Ordenamiento:** Ordenar $n$ elementos por $v_i/w_i$ requiere $O(n \log n)$ (con algoritmos como Timsort o Mergesort).
* **Recorrido voraz y selección:** Un único ciclo lineal de $O(n)$ pasos.
* **Complejidad Temporal Total:**
  $$\mathcal{O}(n \log n)$$
* **Complejidad Espacial:** $\mathcal{O}(n)$ para almacenar los objetos y la solución resultante.

---

### Ejemplo Paso a Paso donde actúa la Garantía
Este ejemplo ilustra el requerimiento del punto 4 del Problema 2 del TP1:

* **Capacidad de la mochila:** $W = 100$
* **Objetos disponibles:**
  * Objeto 1: $w_1 = 1$, $v_1 = 2 \implies r_1 = 2.0$
  * Objeto 2: $w_2 = 100$, $v_2 = 100 \implies r_2 = 1.0$

#### Ejecución:
1. **Ordenamiento:** Se ordenan como `[Objeto 1, Objeto 2]`.
2. **Llenado voraz:**
   * Entra el Objeto 1: Capacidad usada = 1, Capacidad restante = 99, $P_1 = 2$.
   * El Objeto 2 necesita 100 de capacidad, pero solo quedan 99. **No entra.**
   * Objeto 2 queda registrado como el **Elemento Crítico ($c$)** con $v_c = 100$.
3. **Comparación con la garantía:**
   * Valor solución greedy simple: $P_1 = 2$.
   * Valor elemento crítico: $v_c = 100$.
   * Como $v_c > P_1$ ($100 > 2$), **actúa la garantía de calidad** y el algoritmo descarta $S_1$ para devolver únicamente `{Objeto 2}`.
4. **Resultado:**
   * Solución obtenida: $\{ \text{Objeto 2} \}$ con valor 100.
   * Óptimo real: 100.
   * En este caso, la corrección no solo evitó un resultado arbitrariamente malo, sino que alcanzó el óptimo global.
