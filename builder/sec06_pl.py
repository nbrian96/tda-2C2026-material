"""Módulo 6: Programación Lineal y Entera (PL / PLI)."""

def get_content():
    return r"""## 8. Tema 5: Programación Lineal y Entera (PL / PLI)

### Conceptos Mínimos de Supervivencia

1. **Estructura Formal de un Modelo de Programación Lineal:**
   Un modelo debe presentarse obligatoriamente con estos cuatro componentes:
   * **Variables de Decisión:** Definir claramente qué representa cada variable física o lógicamente en el problema, indicando sus índices y conjuntos.
   * **Dominios de las Variables:** Restricciones de signo e integralidad (x_i ∈ {0, 1}, y_j ≥ 0, z_k ∈ ℤ⁺).
   * **Función Objetivo:** Maximizar o minimizar una combinación lineal exacta de las variables (nunca multiplicar variables entre sí ni usar operadores max, min o |·| directamente).
   * **Restricciones Lineales:** Sistema de igualdades o desigualdades lineales (≤, ≥, =) que definen la región factible.
   * **Conteo Explícito de Variables y Restricciones:** En la cátedra Echevarría es un requerimiento frecuente indicar el número exacto de variables y restricciones en función de los parámetros del problema.
2. **Técnicas de Linealización Clásicas:**
   * **Minimizar un Máximo (min max(f₁, f₂, ...)):**  
     Se introduce una variable auxiliar continua Z.  
     Objetivo: min Z  
     Sujeto a: Z ≥ f₁, Z ≥ f₂, ...
   * **Relación Lógica "Al menos uno":**  
     Para asegurar que al menos un elemento del conjunto S sea seleccionado: ∑_{j ∈ S} y_j ≥ 1.
   * **Relación Lógica "Activación / Cobertura":**  
     Si la entidad i solo puede considerarse cubierta (x_i = 1) cuando al menos un proveedor j que la abastece está activo (y_j = 1):
     > **x_i ≤ ∑_{j ∈ Proveedores(i)} y_j**
     (Si ningún y_j = 1, la sumatoria es 0, forzando x_i = 0. Si al menos uno es 1, x_i puede ser 1).

---

### Patrón de Ejercicio 5.1: Máxima Cobertura con Presupuesto de Recursos

Problemas donde se busca maximizar la cantidad de elementos cubiertos o beneficiados sujeto a un límite estricto de tiempo, dinero o capacidad disponible.

---

### Ejercicio 19 — Observación de Aves de Paolo Casanova (Máxima Cobertura con Presupuesto de Tiempo)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-1 (5 de noviembre de 2024), Ejercicio 4

**Enunciado**  
Paolo Casanova dispone de 2 días para realizar salidas a diferentes lugares cercanos y observar la mayor cantidad posible de especies de aves. Hay 10 especies en particular que desea encontrar (E = {1, ..., 10}) y 6 lugares posibles a visitar (L = {1, ..., 6}). Algunos lugares insumen medio día (0.5 días) y otros un día completo (1.0 días). Para cada lugar se conoce exactamente qué especies habitan allí según una matriz binaria de presencia A_ij (A_ij = 1 si la especie i habita en el lugar j, 0 si no). Plantear un modelo de Programación Lineal Entera que determine qué lugares visitar para maximizar la cantidad de especies distintas encontradas en el tiempo disponible. Indicar la cantidad de variables y restricciones del modelo.

**Qué está evaluando**  
Modelado de *Maximum Coverage Problem* en PLI, variables de cobertura vs variables de selección de recursos, y formulación de restricciones de enlace (*linking constraints*).

**Idea de resolución**  
* Definir variables binarias para cada lugar: y_j = 1 si Paolo visita el lugar j, 0 si no.
* Definir variables binarias para cada especie: x_i = 1 si Paolo logra ver la especie i, 0 si no.
* Función objetivo: Maximizar el total de especies distintas vistas: ∑_{i=1}^{10} x_i.
* Restricción de presupuesto de tiempo: La suma de las duraciones de los lugares visitados no puede superar 2 días: ∑_{j=1}^6 d_j · y_j ≤ 2.
* Restricción de enlace: La especie i solo puede considerarse vista (x_i = 1) si visita al menos un lugar j donde esa especie habita.

**Modelo Matemático Formal**

```text
CONJUNTOS Y PARÁMETROS:
  E = {1, ..., 10}        // Conjunto de especies
  L = {1, ..., 6}         // Conjunto de lugares
  d_j                     // Duración en días del lugar j (d_j ∈ {0.5, 1.0})
  A_ij ∈ {0, 1}           // 1 si la especie i habita en el lugar j, 0 en otro caso

VARIABLES DE DECISIÓN:
  y_j ∈ {0, 1}   ∀ j ∈ L  // 1 si se visita el lugar j, 0 si no
  x_i ∈ {0, 1}   ∀ i ∈ E  // 1 si se observa la especie i, 0 si no

FUNCIÓN OBJETIVO:
  MAXIMIZAR Z = ∑_{i ∈ E} x_i

RESTRICCIONES:
  // 1. Presupuesto máximo de tiempo (2 días)
  ∑_{j ∈ L} (d_j * y_j) <= 2

  // 2. Cobertura de cada especie (enlace lógico entre x_i e y_j)
  x_i <= ∑_{j ∈ L} (A_ij * y_j)    ∀ i ∈ E
```

**Explicación del modelo**  
Si Paolo no visita ningún lugar donde habita la especie i, todos los y_j con A_ij = 1 valen 0, por lo que la sumatoria es 0 y la restricción x_i ≤ 0 fuerza a que x_i = 0. Como el objetivo es maximizar la suma de x_i, en cuanto visite al menos un lugar con esa especie (y_j = 1), el solucionador pondrá automáticamente x_i = 1. Visitar dos lugares con la misma especie no duplica el valor porque x_i está acotada en 1.

**Conteo de Variables y Restricciones**  
* **Variables:**  
  * 6 variables binarias y_j (lugares).  
  * 10 variables binarias x_i (especies).  
  * **Total de variables:** 6 + 10 = 16 variables binarias.
* **Restricciones:**  
  * 1 restricción de tiempo.  
  * 10 restricciones de cobertura de especies (una por cada i ∈ E).  
  * **Total de restricciones:** 1 + 10 = 11 restricciones lineales (más las cotas de dominio).

**Puntos donde puedo equivocarme**  
* Poner x_i = ∑ A_ij · y_j con igualdad: si visita 2 lugares que tienen la misma especie, x_i tomaría el valor 2, sumando dos veces la misma especie en el objetivo.
* Declarar y_j o x_i como continuas: daría valores fraccionarios absurdos (como visitar 0.3 de un lugar).

---

### Patrón de Ejercicio 5.2: Cobertura de Celdas con Umbral Porcentual

Problemas de infraestructura (antenas, sensores, cámaras) sobre grillas donde se exige cubrir una fracción mínima del total de objetivos con costo mínimo.

---

### Ejercicio 20 — Cobertura de Antenas Celulares con Umbral del 70% de Vecindarios

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-3 (10 de diciembre de 2024), Ejercicio 3

**Enunciado**  
Una empresa de telefonía celular colocará antenas en una grilla de celdas para prestar servicio a vecindarios distribuidos en un mapa. Si se coloca una antena en la celda (i, j), brindará servicio a 9 celdas (la celda (i, j) y sus 8 vecinas). Instalar una antena tiene un costo fijo CTE en cualquier celda. Se dispone de un conjunto de V vecindarios en la zona. La empresa requiere prestar servicio a **por lo menos el 70% de los vecindarios** al menor costo posible. Plantear un modelo de Programación Lineal Entera que resuelva el problema. Indicar variables y restricciones.

**Qué está evaluando**  
Modelado de *Partial Set Cover* en PLI, agregación porcentual de cobertura y función objetivo de minimización de costos.

**Modelo Matemático Formal**

```text
CONJUNTOS Y PARÁMETROS:
  C                    // Conjunto de todas las celdas candidatas de la grilla
  V                    // Conjunto de vecindarios que requieren servicio
  Vecinos(c) ⊆ C       // Las celdas alcanzadas por una antena en c (hasta 9 celdas)
  CeldaVecindario(v)   // Celda exacta de la grilla donde se ubica el vecindario v
  CTE > 0              // Costo de instalar una antena en cualquier celda

VARIABLES DE DECISIÓN:
  y_c ∈ {0, 1}   ∀ c ∈ C   // 1 si se instala antena en la celda c, 0 si no
  x_v ∈ {0, 1}   ∀ v ∈ V   // 1 si el vecindario v recibe servicio, 0 si no

FUNCIÓN OBJETIVO:
  MINIMIZAR Costo = CTE * ∑_{c ∈ C} y_c

RESTRICCIONES:
  // 1. Umbral mínimo de servicio del 70% de los vecindarios
  ∑_{v ∈ V} x_v >= 0.70 * |V|

  // 2. Cobertura del vecindario v por al menos una antena en su rango de 3x3
  x_v <= ∑_{c ∈ AntenasQueCubren(v)} y_c    ∀ v ∈ V
```

**Conteo de Variables y Restricciones**  
* **Variables:** |C| + |V| variables binarias.
* **Restricciones:** 1 restricción del umbral del 70% + |V| restricciones de cobertura. Total: |V| + 1 restricciones lineales.

---

### Patrón de Ejercicio 5.3: Flujo de Costo Mínimo / Transporte Multizona

Problemas de balance de oferta y demanda con capacidades máximas y costos de transporte por arista.

---

### Ejercicio 21 — Distribución Energética Multizona con Costos de Transporte (Flujo de Costo Mínimo)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2025-1-1 (27 de mayo de 2025), Ejercicio 3

**Enunciado**  
El sistema energético argentino está dividido en 9 regiones. Para cada región i se conoce su Generación prevista G_i (MWh) y su Demanda esperada D_i (MWh). Desde cualquier región i se puede enviar energía a la región j con un costo unitario de transporte C_ij pesos por MWh transportado. Además, cada línea de transmisión tiene una capacidad máxima de transporte de CAP_ij MWh por día. Plantear un modelo de Programación Lineal continuo que encuentre la asignación de transporte más económica para cubrir exactamente la demanda de todas las regiones.

**Qué está evaluando**  
Modelado de *Min-Cost Flow* en Programación Lineal continua, conservación de flujo nodal con generación y demanda, y restricciones de capacidad.

**Modelo Matemático Formal**

```text
CONJUNTOS Y PARÁMETROS:
  R = {1, ..., 9}              // Conjunto de las 9 regiones
  G_i >= 0        ∀ i ∈ R      // Generación local en la región i
  D_i >= 0        ∀ i ∈ R      // Demanda requerida en la región i
  C_ij >= 0       ∀ i, j ∈ R   // Costo unitario de transporte de i a j
  CAP_ij >= 0     ∀ i, j ∈ R   // Capacidad máxima de la línea (i, j)

VARIABLES DE DECISIÓN:
  x_ij >= 0       ∀ i, j ∈ R (i ≠ j)  // MWh transportados desde la región i hacia la región j

FUNCIÓN OBJETIVO:
  MINIMIZAR CostoTotal = ∑_{i ∈ R} ∑_{j ∈ R, j ≠ i} (C_ij * x_ij)

RESTRICCIONES:
  // 1. Balance de energía en cada región i (Generación + Entradas - Salidas >= Demanda)
  G_i + ∑_{k ∈ R, k ≠ i} x_ki - ∑_{j ∈ R, j ≠ i} x_ij >= D_i    ∀ i ∈ R

  // 2. Capacidad máxima en cada línea de transporte
  x_ij <= CAP_ij    ∀ i, j ∈ R (i ≠ j)
```

**Conteo de Variables y Restricciones**  
* Con 9 regiones, hay a lo sumo 9 × 8 = 72 pares de transporte posibles:
  * **Variables:** 72 variables continuas x_ij ≥ 0.
  * **Restricciones:** 9 restricciones de balance nodal (una por región) + 72 restricciones de capacidad de línea = 81 restricciones lineales.

---

### Patrón de Ejercicio 5.4: Camino Mínimo Formulado como Flujo Unitario

Formulación de la búsqueda de rutas óptimas en grafos de decisión multietapa como problemas de flujo de una sola unidad desde el origen hasta el destino.

---

### Ejercicio 22 — Camino de Mínimo Riesgo (INVAP) como Flujo Unitario en PL

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Parcial 2025-1-2 (17 de junio de 2025), Ejercicio 5

**Enunciado**  
Para el traslado de la carga peligrosa del INVAP desde Ezeiza (s) hasta Bariloche (t) a través de un grafo dirigido acíclico de etapas donde cada tramo (u, v) tiene un costo de seguro C_uv:  
Plantear un modelo de Programación Lineal que determine la ruta de menor costo de seguro. Indicar la cantidad de variables y restricciones del modelo.

**Idea de resolución**  
* Modelamos el problema inyectando **1 unidad de flujo** en el nodo origen s y extrayendo **1 unidad de flujo** en el sumidero t.
* Variables: x_uv ∈ {0, 1} indica si el tramo (u, v) forma parte de la ruta elegida.
* Conservación de flujo nodal:
  * En el origen s: ∑_v x_sv - ∑_u x_us = 1.
  * En el destino t: ∑_v x_tv - ∑_u x_ut = -1.
  * En cualquier ciudad intermedia k ∉ {s, t}: ∑_v x_kv - ∑_u x_uk = 0.

**Modelo Matemático Formal**

```text
VARIABLES DE DECISIÓN:
  x_uv ∈ {0, 1}    ∀ (u, v) ∈ E   // 1 si se transita por el tramo (u, v), 0 si no

FUNCIÓN OBJETIVO:
  MINIMIZAR SeguroTotal = ∑_{(u, v) ∈ E} (C_uv * x_uv)

RESTRICCIONES:
  // Conservación de flujo unitario en cada nodo i ∈ V
  ∑_{v: (i, v) ∈ E} x_iv - ∑_{u: (u, i) ∈ E} x_ui = 
      1   si i = s (Ezeiza)
     -1   si i = t (Bariloche)
      0   si i ∈ V \ {s, t} (ciudades intermedias)
```

**Conteo de Variables y Restricciones**  
* **Variables:** |E| variables binarias (una por cada tramo factible).  
* **Restricciones:** |V| restricciones de conservación de flujo (una por cada nodo).  
*(Nota teórica importante: Debido a la Unimodularidad Total de la matriz de incidencia de grafos, las variables x_uv pueden relajarse a continuas 0 ≤ x_uv ≤ 1 y el método Simplex garantiza soluciones enteras automáticamente).*

---

### Patrón de Ejercicio 5.5: Linealización de Funciones No Lineales (min max)

Transformación de funciones objetivo no lineales como min max o minimización de discrepancias en sistemas lineales estándar.

---

### Ejercicio 23 — 2-Partition Min-Max con Linealización de Variable Auxiliar

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Guía de Ejercicios 05, Ejercicio 12 / Práctica

**Enunciado**  
Dado un conjunto de n números positivos T = {T₁, T₂, ..., Tₙ}, se desea particionar los números en dos subconjuntos S₁ y S₂ disjuntos cuya unión sea T, de forma de minimizar la suma del subconjunto más pesado: min max(Suma(S₁), Suma(S₂)). Formular el problema como Programación Lineal Entera linealizando el operador max.

**Modelo Matemático Formal**

```text
VARIABLES DE DECISIÓN:
  x_i ∈ {0, 1}    ∀ i ∈ {1, ..., n}  // 1 si T_i va a S_1, 0 si va a S_2
  Z >= 0                              // Variable continua auxiliar (cota del máximo)

FUNCIÓN OBJETIVO:
  MINIMIZAR Z

RESTRICCIONES:
  // Z debe ser mayor o igual a la suma del subconjunto S_1
  Z >= ∑_{i=1}^n (T_i * x_i)

  // Z debe ser mayor o igual a la suma del subconjunto S_2
  Z >= ∑_{i=1}^n (T_i * (1 - x_i))
```

**Conteo de Variables y Restricciones**  
* **Variables:** n variables binarias + 1 variable continua auxiliar = n + 1 variables.  
* **Restricciones:** 2 restricciones lineales de cota superior sobre Z.

---

### Errores Frecuentes en Exámenes sobre Programación Lineal

1. **Multiplicar dos variables de decisión:** Escribir términos como x_i · y_j destruye la linealidad del modelo y anula el ejercicio.
2. **Usar operadores max, min o abs() directamente en las fórmulas:** Deben linealizarse obligatoriamente mediante variables auxiliares continuas (Z) y desigualdades.
3. **No declarar el dominio de las variables:** Omitir x_i ∈ {0, 1} o x_ij ≥ 0.
4. **Olvidar contar variables y restricciones:** Cuando el enunciado pide explícitamente *"indicar la cantidad de variables y restricciones"*, omitir este punto resta hasta un 25% de la nota de la pregunta.
"""
