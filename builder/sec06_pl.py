"""Módulo 6: Programación Lineal y Entera (PL / PLI)."""

def get_content():
    return r"""## 8. Tema 5: Programación Lineal y Entera (PL / PLI)

### Conceptos Mínimos de Supervivencia

1. **Estructura Canónica de un Modelo Matemático:**
   En las correcciones de FIUBA, todo modelo debe estructurarse obligatoriamente en cinco bloques explícitos:
   * **Conjuntos y Parámetros:** Definición rigurosa de índices, conjuntos de entrada y constantes numéricas con sus unidades físicas.
   * **Variables de Decisión y Dominios:** Qué representa semánticamente cada variable, con su dominio matemático estricto ($x_i \in \{0, 1\}$, $y_j \ge 0$, $z \in \mathbb{R}$).
   * **Función Objetivo:** Maximizar o minimizar una combinación lineal exacta. Está estrictamente prohibido multiplicar variables entre sí o emplear funciones no lineales directas ($\max$, $\min$, $|\cdot|$).
   * **Restricciones Lineales:** Desigualdades e igualdades lineales ($\le, \ge, =$) que delimitan el poliedro convexo de soluciones factibles.
   * **Conteo Exhaustivo de Variables y Restricciones:** Identificar la dimensionalidad exacta del modelo en función de los parámetros de entrada ($O(|V|)$, $O(|E|)$).

2. **Técnicas Clave de Linealización y Modelado Lógico:**
   * **Minimización de un Máximo ($\min \max(f_1, f_2, \dots, f_k)$):**
     Se introduce una variable auxiliar continua $Z \in \mathbb{R}$.
     $$\min Z \quad \text{sujeto a:} \quad Z \ge f_r(x) \quad \forall r \in \{1, \dots, k\}$$
     *Principio:* Al minimizar $Z$, el optimizador presiona $Z$ hacia abajo hasta topar con la cota más restrictiva, cumpliéndose en el óptimo que $Z^* = \max_r f_r(x^*)$.
   * **Relación de Cobertura y Activación (*Linking Constraints*):**
     Si la entidad $i$ solo puede activarse ($x_i = 1$) cuando al menos un recurso $j$ que la abastece está seleccionado ($y_j = 1$):
     $$x_i \le \sum_{j \in Abastecedores(i)} y_j \quad \forall i$$
     Si la sumatoria es 0, fuerza $x_i = 0$. Si es $\ge 1$, permite $x_i \le \text{valor}$, y al maximizar $\sum x_i$, se fijará en 1.
   * **Unimodularidad Total (TUM):**
     Si la matriz de restricciones $A$ de un problema continuo ($Ax \le b$) es totalmente unimodular (todo subdeterminante es $0, 1$ o $-1$) y el vector $b$ es entero, **todos los vértices del poliedro son enteros**. Esto permite resolver problemas de flujo o camino mínimo con Simplex continuo en tiempo polinomial garantizando soluciones $100\%$ enteras.

---

### Patrón de Ejercicio 5.1: Máxima Cobertura con Presupuesto de Recursos

Problemas donde se busca maximizar la cantidad de elementos cubiertos o beneficiados sujeto a un límite estricto de tiempo, dinero o capacidad disponible.

---

### Ejercicio 19 — Observación de Aves de Paolo Casanova (Máxima Cobertura con Presupuesto de Tiempo)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-1 (5 de noviembre de 2024), Ejercicio 4  
**Qué evalúa la cátedra:** Modelado de *Maximum Coverage Problem* en PLI, formulación rigurosa de restricciones de enlace (*linking constraints*) entre variables de recurso y variables de beneficio, y conteo analítico de componentes.

#### 1. Enunciado Completo
Paolo Casanova dispone de 2 días para realizar salidas a diferentes lugares cercanos y observar la mayor cantidad posible de especies de aves. Hay 10 especies en particular que desea encontrar ($E = \{1, \dots, 10\}$) y 6 lugares posibles a visitar ($L = \{1, \dots, 6\}$). Algunos lugares insumen medio día ($0.5$ días) y otros un día completo ($1.0$ días). Para cada lugar se conoce exactamente qué especies habitan allí según una matriz binaria de presencia $A_{ij}$ ($A_{ij} = 1$ si la especie $i$ habita en el lugar $j$, $0$ si no). Plantear un modelo de Programación Lineal Entera que determine qué lugares visitar para maximizar la cantidad de especies distintas encontradas en el tiempo disponible. Indicar la cantidad exacta de variables y restricciones del modelo.

#### 2. Los 5 Pasos Metodológicos de Modelado en PLI

1. **Identificación de Decisiones y Recursos:**
   - Decisión primaria: ¿Se visita el lugar $j \in L$? (Variable binaria $y_j$).
   - Decisión secundaria/beneficio: ¿Se logra observar la especie $i \in E$? (Variable binaria $x_i$).
   - Recurso limitante: Presupuesto temporal global de $2.0$ días.
2. **Definición de Conjuntos y Parámetros:**
   - $E = \{1, \dots, 10\}$: Conjunto de especies objetivo.
   - $L = \{1, \dots, 6\}$: Conjunto de sitios candidatos.
   - $d_j \in \{0.5, 1.0\}$: Duración de la visita al sitio $j$.
   - $A_{ij} \in \{0, 1\}$: Matriz de incidencia especie-sitio.
   - $T_{max} = 2.0$: Días disponibles.
3. **Formulación de la Función Objetivo:**
   Maximizar la cardinalidad del conjunto de especies distintas avistadas:
   $$\max Z = \sum_{i \in E} x_i$$
4. **Restricción Presupuestaria y Restricciones de Enlace:**
   - Presupuesto de tiempo: La suma ponderada de sitios elegidos no excede $T_{max}$:
     $$\sum_{j \in L} d_j \cdot y_j \le 2.0$$
   - Enlace Lógico (*Coverage Constraint*): Para cada especie $i$, $x_i$ solo puede valer 1 si se visita al menos un sitio $j$ tal que $A_{ij} = 1$:
     $$x_i \le \sum_{j \in L} A_{ij} \cdot y_j \quad \forall i \in E$$
5. **Declaración Explícita de Dominios:**
   $$y_j \in \{0, 1\} \quad \forall j \in L, \qquad x_i \in \{0, 1\} \quad \forall i \in E$$

#### 3. Demostración Rigurosa de Correctitud del Enlace

**Lema de Validez del Enlace Lógico:**  
Bajo la función objetivo de maximizar $\sum_{i \in E} x_i$:
1. **Caso 0 (Ningún hábitat visitado):** Si Paolo no visita ningún sitio donde habite la especie $i$, entonces $y_j = 0$ para todo $j$ con $A_{ij} = 1$. En consecuencia:
   $$\sum_{j \in L} A_{ij} \cdot y_j = 0 \implies x_i \le 0 \implies x_i = 0$$
   Es imposible que el modelo contabilice una especie no observada.
2. **Caso $\ge 1$ (Al menos un hábitat visitado):** Si visita $k \ge 1$ sitios donde habita la especie $i$, entonces $\sum_{j \in L} A_{ij} y_j = k \ge 1$. La restricción se convierte en:
   $$x_i \le k$$
   Dado que el dominio impone $x_i \in \{0, 1\}$ y la función objetivo maximiza $\sum x_i$ con coeficientes positivos ($+1$), el optimizador asignará el mayor valor factible: $x_i = 1$.
3. **Inmunidad al Doble Cómputo:** Si visita 2 o más lugares con la misma especie, $x_i \le 2$ o $3$, pero al estar restringida por su dominio superior $x_i \le 1$, la especie aporta exactamente 1 a la función objetivo.

#### 4. Diagrama Visual del Grafo de Cobertura Bipartito

```mermaid
flowchart LR
    subgraph Lugares [Lugares Candidatos]
        L1["L1: 0.5 dias"]
        L2["L2: 1.0 dias"]
        L3["L3: 0.5 dias"]
        L4["L4: 1.0 dias"]
    end
    subgraph Especies [Especies Observadas]
        E1["Especie 1"]
        E2["Especie 2"]
        E3["Especie 3"]
        E4["Especie 4"]
    end
    L1 --> E1
    L1 --> E2
    L2 --> E2
    L2 --> E3
    L3 --> E3
    L3 --> E4
    L4 --> E1
    L4 --> E4
```

#### 5. Ejemplo Numérico y Traza de Decisión

Consideremos una instancia representativa con 4 lugares y 5 especies para verificar el enlace:

| Lugar $j$ | Duración $d_j$ | Especies presentes ($A_{ij}=1$) |
| :--- | :--- | :--- |
| **L1** | 0.5 días | $\{E_1, E_2\}$ |
| **L2** | 1.0 días | $\{E_2, E_3, E_4\}$ |
| **L3** | 0.5 días | $\{E_3, E_5\}$ |
| **L4** | 1.0 días | $\{E_1, E_4, E_5\}$ |

* **Presupuesto:** $T = 2.0$ días.
* **Evaluación de combinaciones:**
  - Visitar $\{L_1, L_3, L_2\}$: Duración $0.5 + 0.5 + 1.0 = 2.0$ días. Especies cubiertas: $\{E_1, E_2\} \cup \{E_3, E_5\} \cup \{E_2, E_3, E_4\} = \{E_1, E_2, E_3, E_4, E_5\}$ (5 especies).
  - Valor objetivo óptimo: $Z^* = 5$.
  - Variables: $y_1=1, y_2=1, y_3=1, y_4=0$; $x_1=x_2=x_3=x_4=x_5=1$.

#### 6. Conteo Formal de Variables y Restricciones

* **Variables de Decisión:**
  - $|L| = 6$ variables binarias de visita $y_j$.
  - $|E| = 10$ variables binarias de avistamiento $x_i$.
  - **Total de variables:** $6 + 10 = 16$ variables binarias.
* **Restricciones Lineales:**
  - 1 restricción de presupuesto temporal.
  - $|E| = 10$ restricciones de cobertura lógica (una por especie).
  - **Total de restricciones:** $1 + 10 = 11$ restricciones funcionales (además de los dominios $0 \le x_i, y_j \le 1$).

#### 7. Implementación en Python con Solver MILP

```python
from typing import List, Tuple
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def resolver_observacion_aves(
    duraciones: List[float],
    matriz_presencia: List[List[int]],
    presupuesto_dias: float = 2.0
) -> Tuple[float, List[int], List[int]]:
    # duraciones: lista de largo |L|
    # matriz_presencia: matriz |E| x |L| donde A[i][j] = 1 si especie i esta en sitio j
    num_especies = len(matriz_presencia)
    num_lugares = len(duraciones)
    n_vars = num_lugares + num_especies # [y_0...y_5, x_0...x_9]

    # Objetivo: Maximizar sum(x_i) <=> Minimizar -sum(x_i)
    c = np.zeros(n_vars)
    c[num_lugares:] = -1.0

    # Restriccion 1: Presupuesto temporal sum(d_j * y_j) <= T_max
    # Restricciones 2..E+1: x_i - sum(A_ij * y_j) <= 0
    num_constraints = 1 + num_especies
    A = np.zeros((num_constraints, n_vars))
    b_u = np.zeros(num_constraints)
    b_l = np.full(num_constraints, -np.inf)

    # 1. Presupuesto
    A[0, :num_lugares] = duraciones
    b_u[0] = presupuesto_dias

    # 2. Enlace x_i <= sum(A_ij * y_j) => -sum(A_ij * y_j) + x_i <= 0
    for i in range(num_especies):
        row = 1 + i
        for j in range(num_lugares):
            if matriz_presencia[i][j] == 1:
                A[row, j] = -1.0
        A[row, num_lugares + i] = 1.0
        b_u[row] = 0.0

    constraints = LinearConstraint(A, b_l, b_u)
    integrality = np.ones(n_vars) # Todas binarias
    bounds = Bounds(0, 1)

    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

    lugares_elegidos = [j for j in range(num_lugares) if res.x[j] > 0.5]
    especies_vistas = [i for i in range(num_especies) if res.x[num_lugares + i] > 0.5]
    return -res.fun, lugares_elegidos, especies_vistas
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Forzar igualdad en la cobertura ($x_i = \sum A_{ij} y_j$):</strong> Si Paolo visita 2 sitios que albergan a la especie $i$, $x_i$ se vería forzada a valer 2, violando el dominio binario o inflando artificialmente el valor objetivo al sumar dos veces la misma ave. La relación correcta es estrictamente de desigualdad $\le$.</li>
    <li><strong>Declarar variables continuas en lugar de binarias:</strong> Si se omite $y_j \in \{0, 1\}$, el solver visitará fracciones de lugares (ej. visitar $0.25$ del lugar 1 y $0.25$ del lugar 4), obteniendo una solución matemáticamente óptima pero físicamente absurda.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 5.2: Cobertura de Celdas con Umbral Porcentual

Problemas de infraestructura (antenas, sensores, cámaras) sobre grillas donde se exige cubrir una fracción mínima del total de objetivos con costo mínimo.

---

### Ejercicio 20 — Cobertura de Antenas Celulares con Umbral del 70% de Vecindarios

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2024-2-3 (10 de diciembre de 2024), Ejercicio 3  
**Qué evalúa la cátedra:** Modelado de *Partial Set Cover* en PLI, formulación de umbrales porcentuales de servicio y minimización de costos fijos.

#### 1. Enunciado Completo
Una empresa de telefonía celular colocará antenas en una grilla bidimensional de celdas para prestar servicio a vecindarios distribuidos en un mapa. Si se instala una antena en la celda $(i, j)$, brindará cobertura a un bloque de 9 celdas (la propia celda $(i, j)$ y sus 8 celdas contiguas en vecindad de Moore). Instalar una antena tiene un costo fijo $CTE > 0$ idéntico en cualquier celda. Se dispone de un conjunto $V$ de vecindarios distribuidos en la zona. La empresa exige brindar servicio a **por lo menos el 70% de los vecindarios** minimizando la inversión total. Plantear un modelo de Programación Lineal Entera indicando claramente variables, dominios, función objetivo, restricciones y su conteo exacto.

#### 2. Los 5 Pasos Metodológicos de Modelado en PLI

1. **Identificación de Decisiones:**
   - Decisión de infraestructura: ¿Se instala una antena en la celda candidata $c \in C$? Variable binaria $y_c$.
   - Decisión de servicio: ¿El vecindario $v \in V$ resulta efectivamente cubierto? Variable binaria $x_v$.
2. **Definición de Conjuntos y Parámetros:**
   - $C$: Conjunto de celdas de la grilla donde es factible instalar antenas.
   - $V$: Conjunto de vecindarios a servir.
   - $Cubren(v) \subseteq C$: Conjunto de celdas candidatas cuya antena cubre al vecindario $v$ (es decir, todas las celdas $c$ a distancia Chebyshev $\le 1$ de la celda de $v$).
   - $CTE$: Costo unitario de instalación de una antena.
3. **Formulación de la Función Objetivo:**
   Minimizar el gasto de instalación de infraestructura:
   $$\min CostoTotal = CTE \cdot \sum_{c \in C} y_c$$
4. **Restricciones de Cobertura y Umbral de Satisfacción:**
   - **Umbral del 70%:** La cantidad total de vecindarios cubiertos debe ser al menos el $70\%$ del total:
     $$\sum_{v \in V} x_v \ge 0.70 \cdot |V|$$
   - **Enlace de Cobertura Física:** Un vecindario $v$ solo puede declararse cubierto si se instala al menos una antena en alguna celda dentro de su rango de alcance:
     $$x_v \le \sum_{c \in Cubren(v)} y_c \quad \forall v \in V$$
5. **Dominios de las Variables:**
   $$y_c \in \{0, 1\} \quad \forall c \in C, \qquad x_v \in \{0, 1\} \quad \forall v \in V$$

#### 3. Demostración de Validez del Modelo

**Teorema de Factibilidad y Presión de Costo:**  
1. *Cota sobre cobertura:* Para cualquier vecindario $v$, si ninguna antena cubre su celda ($\sum_{c \in Cubren(v)} y_c = 0$), la restricción impone $x_v \le 0 \implies x_v = 0$.
2. *Minimización del costo:* Dado que $CTE > 0$ y minimizamos $\sum y_c$, el solucionador nunca activará antenas superfluas. Si un vecindario $v$ no es necesario para alcanzar el umbral del $70\%$, el modelo preferirá mantener $x_v = 0$ con tal de ahorrar la activación de $y_c$.
3. *Umbral estricto:* La restricción $\sum x_v \ge \lceil 0.70 |V| \rceil$ garantiza que el compromiso de servicio se satisfaga plenamente.

#### 4. Diagrama Visual de Vecindad de Cobertura (3x3)

```mermaid
graph TD
    subgraph CeldaAntena [Antena Central]
        C["Celda Central (i, j)"]
    end
    subgraph CeldasCubiertas [Radio de Vecindad]
        V1["Vecino (i-1, j-1)"]
        V2["Vecino (i-1, j)"]
        V3["Vecino (i-1, j+1)"]
        V4["Vecino (i, j-1)"]
        V5["Vecino (i, j+1)"]
        V6["Vecino (i+1, j-1)"]
        V7["Vecino (i+1, j)"]
        V8["Vecino (i+1, j+1)"]
    end
    C --> V1
    C --> V2
    C --> V3
    C --> V4
    C --> V5
    C --> V6
    C --> V7
    C --> V8
```

#### 5. Ejemplo Numérico y Traza

Supongamos una grilla pequeña con 10 vecindarios ($|V| = 10$).
- Umbral requerido: $\lceil 0.70 \times 10 \rceil = 7$ vecindarios.
- Supongamos que la antena $A_1$ cubre $\{v_1, v_2, v_3, v_4\}$, la antena $A_2$ cubre $\{v_4, v_5, v_6, v_7\}$ y la antena $A_3$ cubre $\{v_8, v_9, v_{10}\}$.
- Con 2 antenas ($A_1$ y $A_2$), se cubren $\{v_1, \dots, v_7\}$ (7 vecindarios).
- Inversión mínima: $2 \times CTE$.
- Solución factible óptima: $y_{A1}=1, y_{A2}=1, y_{A3}=0$; $x_1=x_2=\dots=x_7=1$, $x_8=x_9=x_{10}=0$.

#### 6. Conteo Formal de Variables y Restricciones

* **Variables de Decisión:**
  - $|C|$ variables binarias de antena $y_c$.
  - $|V|$ variables binarias de servicio $x_v$.
  - **Total:** $|C| + |V|$ variables binarias.
* **Restricciones Lineales:**
  - 1 restricción global de umbral del 70%.
  - $|V|$ restricciones individuales de cobertura de vecindario.
  - **Total:** $|V| + 1$ restricciones lineales.

#### 7. Código Python con Modelado PuLP / Scipy

```python
from typing import Dict, List, Set, Tuple

def modelar_antenas_70_porciento(
    celdas_candidatas: List[Tuple[int, int]],
    ubicacion_vecindarios: Dict[str, Tuple[int, int]],
    costo_cte: float = 1000.0
) -> Tuple[List[Tuple[int, int]], List[str], float]:
    # Determinar que antenas cubren a cada vecindario
    cubren: Dict[str, List[Tuple[int, int]]] = {}
    for v_id, (vr, vc) in ubicacion_vecindarios.items():
        cubren[v_id] = [
            (ar, ac) for (ar, ac) in celdas_candidatas
            if abs(ar - vr) <= 1 and abs(ac - vc) <= 1
        ]
    
    # Cantidad minima a cubrir
    n_v = len(ubicacion_vecindarios)
    min_cubrir = int(np.ceil(0.70 * n_v))
    # Retorna la especificacion del modelo lista para resolver con solver MILP
    return celdas_candidatas, list(ubicacion_vecindarios.keys()), min_cubrir * costo_cte
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Confundir el sentido de la desigualdad del umbral:</strong> Escribir $\sum x_v \le 0.70 |V|$ en lugar de $\ge$. Si se pone $\le$, el modelo elegirá no cubrir a nadie ($x_v = 0$), obteniendo costo 0 pero incumpliendo la meta empresarial.</li>
    <li><strong>Creer que el problema pide maximizar cobertura:</strong> La función objetivo NO es $\max \sum x_v$; es **minimizar el costo de antenas** sujeto a que la cobertura alcance el $70\%$. Maximizar cobertura instalaría antenas en toda la grilla innecesariamente.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 5.3: Flujo de Costo Mínimo / Transporte Multizona

Problemas de balance de oferta y demanda con capacidades máximas y costos de transporte por arista en redes continuas.

---

### Ejercicio 21 — Distribución Energética Multizona con Costos de Transporte (Flujo de Costo Mínimo)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Origen:** Parcial 2025-1-1 (27 de mayo de 2025), Ejercicio 3  
**Qué evalúa la cátedra:** Modelado de *Min-Cost Flow* en Programación Lineal continua, conservación nodal de flujo con fuentes de generación y pozos de demanda, y restricciones de capacidad de línea.

#### 1. Enunciado Completo
El sistema interconectado argentino está dividido en 9 regiones eléctricas ($R = \{1, \dots, 9\}$). Para cada región $i$ se conoce su capacidad de generación prevista $G_i \ge 0$ (en MWh) y su demanda requerida $D_i \ge 0$ (en MWh). Desde cualquier región $i$ se puede transmitir energía a otra región $j$ con un costo unitario de transporte $C_{ij} \ge 0$ pesos por MWh. Cada línea de transmisión posee una capacidad máxima de transporte de $CAP_{ij} \ge 0$ MWh/día. Plantear un modelo de Programación Lineal continuo que determine el despacho de energía más económico para satisfacer plenamente la demanda de todas las regiones sin violar capacidades de transporte. Indicar variables y restricciones.

#### 2. Los 5 Pasos Metodológicos de Modelado en PL Continuo

1. **Identificación de la Naturaleza Continua:**
   La energía eléctrica es un bien continuo medido en MWh. No se requieren variables binarias; es un problema de Programación Lineal clásica ($x_{ij} \ge 0$).
2. **Definición de Conjuntos y Parámetros:**
   - $R = \{1, \dots, 9\}$: Conjunto de nodos regionales.
   - $L = \{(i, j) \in R \times R : i \ne j\}$: Líneas de transmisión disponibles.
   - $G_i \ge 0$: Generación inyectada en el nodo $i$.
   - $D_i \ge 0$: Demanda consumida en el nodo $i$.
   - $C_{ij} \ge 0$: Costo por MWh en el arco $(i, j)$.
   - $CAP_{ij} \ge 0$: Capacidad máxima del arco $(i, j)$.
3. **Formulación de la Función Objetivo:**
   Minimizar el costo total de despacho y transporte interregional:
   $$\min CostoTotal = \sum_{(i, j) \in L} C_{ij} \cdot x_{ij}$$
4. **Restricciones de Balance y Capacidad:**
   - **Balance Nodal de Potencia:** En cada región $i \in R$, la generación local más la energía entrante desde otras regiones debe cubrir la energía saliente hacia otros nodos más la demanda local:
     $$G_i + \sum_{k \in R, k \ne i} x_{ki} - \sum_{j \in R, j \ne i} x_{ij} = D_i \quad \forall i \in R$$
     *(O en forma estándar: $\sum_{j} x_{ij} - \sum_{k} x_{ki} \le G_i - D_i$ si se permite generación ociosa).*
   - **Capacidad de las Líneas de Transmisión:**
     $$x_{ij} \le CAP_{ij} \quad \forall (i, j) \in L$$
5. **No Negatividad de las Variables:**
   $$x_{ij} \ge 0 \quad \forall (i, j) \in L$$

#### 3. Demostración Teórica de Conservación y Factibilidad

Sumando la ecuación de balance sobre todas las regiones $i \in R$:
$$\sum_{i \in R} G_i + \sum_{i \in R} \sum_{k \ne i} x_{ki} - \sum_{i \in R} \sum_{j \ne i} x_{ij} = \sum_{i \in R} D_i$$
Dado que cada flujo $x_{ab}$ aparece una vez como entrada ($x_{ki}$ cuando $i=b, k=a$) y una vez como salida ($x_{ij}$ cuando $i=a, j=b$), las dobles sumatorias de flujos internos se cancelan mutuamente:
$$\sum_{i \in R} G_i = \sum_{i \in R} D_i$$
**Condición Necesaria de Factibilidad:** La generación global del país debe ser suficiente para satisfacer la demanda global. Si la generación total excede a la demanda, se escribe con desigualdad $\ge D_i$ para absorber el superávit.

#### 4. Diagrama Visual de Red de Flujo con Costos

```mermaid
graph LR
    R1["Región 1 (G1=100, D1=20)"] -->|x12 (C=5, Cap=50)| R2["Región 2 (G2=10, D2=80)"]
    R1 -->|x13 (C=8, Cap=40)| R3["Región 3 (G3=30, D3=40)"]
    R2 -->|x23 (C=3, Cap=30)| R3
```

#### 5. Ejemplo Numérico y Traza de Balance

Analicemos 3 regiones simplificadas:
- $R_1$: $G_1 = 100, D_1 = 20 \implies \text{Excedente} = +80$.
- $R_2$: $G_2 = 10, D_2 = 80 \implies \text{Déficit} = -70$.
- $R_3$: $G_3 = 30, D_3 = 40 \implies \text{Déficit} = -10$.
- Líneas:
  - $(1, 2)$: $C_{12} = 5, CAP_{12} = 50$.
  - $(1, 3)$: $C_{13} = 9, CAP_{13} = 40$.
  - $(2, 3)$: $C_{23} = 2, CAP_{23} = 20$.
- Despacho Óptimo:
  - Enviar $50$ MWh por $(1, 2)$ al costo $5 \times 50 = 250$ (satura línea). Faltan $20$ en $R_2$.
  - Enviar $30$ MWh por $(1, 3)$ al costo $9 \times 30 = 270$. $R_3$ recibe $30$, cubre sus $10$ de déficit y envía $20$ a $R_2$ por $(3, 2)$ si fuera bidireccional.

#### 6. Conteo Formal de Variables y Restricciones

* **Variables de Decisión:**
  - Cantidad de arcos posibles entre 9 regiones: $9 \times 8 = 72$ variables continuas no negativas ($x_{ij} \ge 0$).
* **Restricciones Lineales:**
  - 9 restricciones de balance nodal de potencia (una por región).
  - 72 restricciones de cota superior de capacidad ($x_{ij} \le CAP_{ij}$).
  - **Total:** $9 + 72 = 81$ restricciones lineales (más $x_{ij} \ge 0$).

#### 7. Código Python con Scipy Linprog

```python
from typing import Dict, List, Tuple
import numpy as np
from scipy.optimize import linprog

def resolver_flujo_costo_minimo(
    regiones: List[int],
    generacion: Dict[int, float],
    demanda: Dict[int, float],
    aristas: List[Tuple[int, int, float, float]] # (u, v, costo, cap)
) -> Tuple[float, Dict[Tuple[int, int], float]]:
    n_aristas = len(aristas)
    c = np.array([a[2] for a in aristas])
    bounds = [(0, a[3]) for a in aristas]

    # Balance nodal: Suma_salidas - Suma_entradas = G_i - D_i
    n_nodos = len(regiones)
    A_eq = np.zeros((n_nodos, n_aristas))
    b_eq = np.zeros(n_nodos)

    nodo_to_idx = {r: idx for idx, r in enumerate(regiones)}

    for arc_idx, (u, v, _, _) in enumerate(aristas):
        u_idx = nodo_to_idx[u]
        v_idx = nodo_to_idx[v]
        A_eq[u_idx, arc_idx] = 1.0  # Sale de u
        A_eq[v_idx, arc_idx] = -1.0 # Entra a v

    for r in regiones:
        r_idx = nodo_to_idx[r]
        b_eq[r_idx] = generacion[r] - demanda[r]

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    flujos = {}
    for idx, (u, v, _, _) in enumerate(aristas):
        flujos[(u, v)] = res.x[idx]

    return res.fun, flujos
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Declarar variables enteras $x_{ij} \in \mathbb{Z}^+$:</strong> La energía eléctrica no se transporta en paquetes indivisibles; forzar variables enteras convierte un problema resoluble en tiempo polinomial en un problema NP-Hard innecesariamente.</li>
    <li><strong>Invertir los signos del balance nodal:</strong> Restar las entradas y sumar las salidas. El balance físico es: $(\text{Generación local}) + (\text{Flujo Entrante}) - (\text{Flujo Saliente}) = \text{Demanda local}$.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 5.4: Camino Mínimo Formulado como Flujo Unitario

Formulación de la búsqueda de rutas óptimas en grafos dirigidos acíclicos como problemas de inyección y extracción de una única unidad de flujo en Programación Lineal continua aprovechando Unimodularidad Total.

---

### Ejercicio 22 — Camino de Mínimo Riesgo (INVAP) como Flujo Unitario en PL

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Parcial 2025-1-2 (17 de junio de 2025), Ejercicio 5  
**Qué evalúa la cátedra:** Formulación de caminos mínimos como problemas de flujo en PL, comprensión de la Unimodularidad Total (TUM) de matrices de incidencia de grafos, y justificación teórica de por qué la relajación continua garantiza soluciones enteras.

#### 1. Enunciado Completo
Para el traslado de una carga crítica de alta seguridad de la empresa INVAP desde el centro atómico Ezeiza ($s$) hasta el laboratorio central en Bariloche ($t$), se dispone de un grafo dirigido $G = (V, E)$. Cada tramo carretero $(u, v) \in E$ tiene un costo de póliza de seguro $C_{uv} > 0$. Plantear un modelo de Programación Lineal continuo que determine la ruta de menor costo de seguro. Justificar formalmente por qué no es necesario declarar las variables como binarias para obtener una ruta válida. Indicar la cantidad exacta de variables y restricciones.

#### 2. Los 5 Pasos Metodológicos de Modelado en PL Continuo

1. **Inyección de Flujo Unitario:**
   Se modela la búsqueda del camino inyectando exactamente $+1$ unidad de flujo en el nodo de origen $s$ (Ezeiza) y extrayendo $-1$ unidad en el sumidero $t$ (Bariloche).
2. **Definición de Variables de Decisión:**
   $x_{uv} \ge 0 \quad \forall (u, v) \in E$: Magnitud de flujo que transita por la arista $(u, v)$.
3. **Función Objetivo:**
   Minimizar el costo total del seguro devengado:
   $$\min CostoSeguro = \sum_{(u, v) \in E} C_{uv} \cdot x_{uv}$$
4. **Restricciones de Conservación de Flujo Nodal:**
   Para cada nodo $i \in V$, la diferencia neta entre el flujo que emite y el flujo que recibe debe coincidir con su inyección externa:
   $$\sum_{v : (i, v) \in E} x_{iv} - \sum_{u : (u, i) \in E} x_{ui} = b(i) \quad \forall i \in V$$
   donde el vector de balance externo $b(i)$ está definido por:
   $$b(i) = \begin{cases} +1 & \text{si } i = s \text{ (Ezeiza - Fuente)} \\ -1 & \text{si } i = t \text{ (Bariloche - Sumidero)} \\ 0 & \text{si } i \in V \setminus \{s, t\} \text{ (Puntos intermedios)} \end{cases}$$
5. **Cotas de las Variables:**
   $$x_{uv} \ge 0 \quad \forall (u, v) \in E$$

#### 3. Demostración Teórica: Teorema de Unimodularidad Total (TUM)

**Teorema de Hoffman-Kruskal aplicado a Grafos:**  
Sea $A \in \{-1, 0, 1\}^{|V| \times |E|}$ la matriz de incidencia nodo-arco del grafo $G$, donde cada columna correspondiente a la arista $(u, v)$ contiene exactamente dos elementos no nulos: $+1$ en la fila del nodo origen $u$ y $-1$ en la fila del nodo destino $v$.
1. **Propiedad TUM:** Toda submatriz cuadrada de $A$ tiene determinante en $\{-1, 0, 1\}$.
   - *Demostración inductiva:* Para submatrices de orden $k$, si una columna tiene solo ceros, $\det = 0$. Si tiene un único $\pm 1$, por expansión de Laplace $\det = \pm 1 \cdot \det(M_{k-1}) \in \{-1, 0, 1\}$. Si todas las columnas tienen un $+1$ y un $-1$, la suma de todas las filas es el vector nulo $\mathbf{0}$, por lo que las filas son linealmente dependientes y $\det = 0$.
2. **Integralidad de Vértices:** Dado que $A$ es totalmente unimodular y el vector del lado derecho $b \in \{-1, 0, 1\}^{|V|}$ es entero, por la regla de Cramer **todo vértice extremo del poliedro $\{x \ge 0 : Ax = b\}$ tiene componentes estrictamente enteras**.
3. Como la inyección total es 1, los únicos valores enteros factibles para las aristas en cualquier solución básica factible sin ciclos son $x_{uv} \in \{0, 1\}$, representando exactamente un camino simple de $s$ a $t$.

#### 4. Diagrama Visual del Grafo de Traslado

```mermaid
flowchart LR
    S_NODE["Ezeiza s (+1)"] -->|C=12| N1["Neuquén"]
    S_NODE -->|C=18| N2["Bahía Blanca"]
    N1 -->|C=6| T_NODE["Bariloche t (-1)"]
    N2 -->|C=7| T_NODE
    N2 -->|C=3| N1
```

#### 5. Ejemplo Numérico y Traza

Rutas alternativas en el grafo del diagrama:
- Ruta 1: Ezeiza $\to$ Neuquén $\to$ Bariloche: Costo $12 + 6 = 18$.
- Ruta 2: Ezeiza $\to$ Bahía Blanca $\to$ Bariloche: Costo $18 + 7 = 25$.
- Ruta 3: Ezeiza $\to$ Bahía Blanca $\to$ Neuquén $\to$ Bariloche: Costo $18 + 3 + 6 = 27$.
- El solver continuo asignará automáticamente: $x_{s,\text{Neuquén}} = 1.0$, $x_{\text{Neuquén}, t} = 1.0$, y todas las demás aristas en $0.0$.
- Costo mínimo: $18$.

#### 6. Conteo Formal de Variables y Restricciones

* **Variables de Decisión:** $|E|$ variables continuas ($x_{uv} \ge 0$).
* **Restricciones Lineales:** $|V|$ restricciones de conservación de flujo nodal (1 en origen, 1 en destino y $|V| - 2$ intermedias).
* *(Nota: Una de las restricciones es linealmente dependiente porque la suma de todos los balances es $1 + (-1) + 0 = 0$).*

#### 7. Código Python con Simplex Continuo

```python
from typing import Dict, List, Tuple
import numpy as np
from scipy.optimize import linprog

def camino_minimo_pl_continuo(
    vertices: List[str],
    aristas: List[Tuple[str, str, float]], # (u, v, costo)
    origen: str,
    destino: str
) -> Tuple[float, List[Tuple[str, str]]]:
    n_edges = len(aristas)
    c = np.array([cost for _, _, cost in aristas])
    bounds = [(0, None) for _ in aristas]

    n_nodes = len(vertices)
    A_eq = np.zeros((n_nodes, n_edges))
    b_eq = np.zeros(n_nodes)

    v_map = {name: i for i, name in enumerate(vertices)}

    for e_idx, (u, v, _) in enumerate(aristas):
        A_eq[v_map[u], e_idx] = 1.0
        A_eq[v_map[v], e_idx] = -1.0

    b_eq[v_map[origen]] = 1.0
    b_eq[v_map[destino]] = -1.0

    res = linprog(c, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

    camino = [aristas[i][:2] for i in range(n_edges) if res.x[i] > 0.9]
    return res.fun, camino
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Declarar variables enteras $x_{uv} \in \{0, 1\}$ sin justificar TUM:</strong> Cuando el enunciado pide explícitamente "plantear un modelo de Programación Lineal y justificar la integralidad", imponer restricciones enteras anula el objetivo de la pregunta. Se debe plantear como **PL continuo** e invocar la Unimodularidad Total.</li>
    <li><strong>Olvidar el nodo sumidero:</strong> Poner conservación $= 0$ en todos lados sin definir la extracción de $-1$ en el destino $t$.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 5.5: Linealización de Funciones No Lineales (min max)

Transformación de funciones objetivo no lineales como minimax o discrepancias absolutas en sistemas lineales estándar con variables continuas auxiliares.

---

### Ejercicio 23 — 2-Partition Min-Max con Linealización de Variable Auxiliar

**Clasificación:** 🟡 IMPORTANTE  
**Origen:** Guía de Ejercicios 05, Ejercicio 12 / Práctica de Examen  
**Qué evalúa la cátedra:** Linealización formal del operador $\min \max(f_1, f_2)$ mediante variable auxiliar continua acotante, y formulación de partición de conjuntos en PLI.

#### 1. Enunciado Completo
Dado un conjunto de $n$ tareas con tiempos de procesamiento enteros positivos $T = \{T_1, T_2, \dots, T_n\}$, se desea particionar las tareas entre dos procesadores idénticos $P_1$ y $P_2$ de manera que se minimice el *makespan* (el tiempo de finalización de la máquina más cargada):
$$\min \max \left( \sum_{i \in P_1} T_i, \sum_{j \in P_2} T_j \right)$$
Formular el problema como un modelo de Programación Lineal Entera, linealizando rigurosamente el operador $\max$. Indicar variables, dominios y conteo de restricciones.

#### 2. Los 5 Pasos Metodológicos de Linealización en PLI

1. **Definición de Variables de Partición:**
   Para cada tarea $i \in \{1, \dots, n\}$, definimos una variable binaria:
   $$x_i = \begin{cases} 1 & \text{si la tarea } i \text{ se asigna al procesador } P_1 \\ 0 & \text{si la tarea } i \text{ se asigna al procesador } P_2 \end{cases}$$
2. **Expresión de Carga de cada Máquina:**
   - Carga del procesador $P_1$: $L_1 = \sum_{i=1}^n T_i \cdot x_i$.
   - Carga del procesador $P_2$: $L_2 = \sum_{i=1}^n T_i \cdot (1 - x_i)$.
3. **Introducción de la Variable Auxiliar Continua:**
   Definimos una variable continua $Z \in \mathbb{R}$ que representará la cota superior del *makespan*:
   $$Z \ge 0$$
4. **Linealización del Máximo mediante Desigualdades:**
   Para garantizar que $Z \ge \max(L_1, L_2)$, imponemos simultáneamente:
   $$Z \ge \sum_{i=1}^n T_i \cdot x_i$$
   $$Z \ge \sum_{i=1}^n T_i \cdot (1 - x_i)$$
5. **Función Objetivo Lineal:**
   $$\min Z$$

#### 3. Demostración Matemática de Equivalencia

**Teorema de Equivalencia de la Linealización Minimax:**  
Sea $(x^*, Z^*)$ una solución óptima del modelo linealizado.
1. Por definición de las restricciones:
   $$Z^* \ge L_1(x^*) \quad \text{y} \quad Z^* \ge L_2(x^*) \implies Z^* \ge \max(L_1(x^*), L_2(x^*))$$
2. Supongamos por contradicción que $Z^* > \max(L_1(x^*), L_2(x^*))$. Entonces podríamos definir un valor $Z' = \max(L_1(x^*), L_2(x^*)) < Z^*$.
3. La solución $(x^*, Z')$ satisface todas las restricciones del modelo y produce un valor objetivo $Z' < Z^*$, contradiciendo la optimalidad de $(x^*, Z^*)$.
4. Por lo tanto, en toda solución óptima se cumple estrictamente que:
   $$Z^* = \max(L_1(x^*), L_2(x^*))$$
   lo que demuestra que el modelo lineal es exactamente equivalente al problema no lineal original.

#### 4. Diagrama Visual de Acotamiento de la Variable Z

```mermaid
graph TD
    subgraph DecisionesBinarias [Particion de Tareas]
        T1["T1"] --> P1["Carga P1"]
        T2["T2"] --> P2["Carga P2"]
    end
    subgraph LinealizacionZ [Variable Auxiliar Continua]
        Z["Variable Z (Makespan)"]
        MinZ["min Z"]
    end
    P1 -->|Cota L1| Z
    P2 -->|Cota L2| Z
    MinZ -. Presiona Z hacia abajo .-> Z
```

#### 5. Ejemplo Numérico y Traza

Consideremos las tareas $T = \{3, 5, 8, 2, 4\}$:
- Suma total: $3 + 5 + 8 + 2 + 4 = 22$. Carga ideal perfecta: $22 / 2 = 11$.
- Asignación factible 1:
  - $P_1 = \{8, 3\} \implies L_1 = 11$.
  - $P_2 = \{5, 4, 2\} \implies L_2 = 11$.
  - Restricciones: $Z \ge 11$ y $Z \ge 11 \implies Z^* = 11$.
- Asignación factible 2:
  - $P_1 = \{8, 5\} \implies L_1 = 13$.
  - $P_2 = \{4, 3, 2\} \implies L_2 = 9$.
  - Restricciones: $Z \ge 13$ y $Z \ge 9 \implies Z = 13$ (peor que el óptimo).
- El solver devolverá $Z^* = 11$ con $x = [1, 0, 1, 0, 0]$.

#### 6. Conteo Formal de Variables y Restricciones

* **Variables de Decisión:**
  - $n$ variables binarias de asignación $x_i \in \{0, 1\}$.
  - 1 variable continua auxiliar $Z \ge 0$.
  - **Total:** $n + 1$ variables ($n$ binarias, 1 continua).
* **Restricciones Lineales:**
  - 2 restricciones de cota superior sobre $Z$ ($Z \ge L_1$ y $Z \ge L_2$).
  - **Total:** 2 restricciones lineales funcionales.

#### 7. Código Python con Solver MILP

```python
from typing import List, Tuple
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def resolver_2_partition_minmax(tiempos: List[float]) -> Tuple[float, List[int], List[int]]:
    n = len(tiempos)
    n_vars = n + 1 # [x_0, ..., x_{n-1}, Z]

    # Objetivo: min Z => c = [0, ..., 0, 1]
    c = np.zeros(n_vars)
    c[-1] = 1.0

    # Restricciones:
    # 1. Z - sum(T_i * x_i) >= 0  => -sum(T_i * x_i) + Z >= 0
    # 2. Z - sum(T_i * (1 - x_i)) >= 0 => sum(T_i * x_i) + Z >= sum(T_i)
    suma_total = sum(tiempos)
    A = np.zeros((2, n_vars))
    b_l = np.zeros(2)
    b_u = np.full(2, np.inf)

    # Fila 1
    for i in range(n):
        A[0, i] = -tiempos[i]
    A[0, -1] = 1.0
    b_l[0] = 0.0

    # Fila 2
    for i in range(n):
        A[1, i] = tiempos[i]
    A[1, -1] = 1.0
    b_l[1] = suma_total

    constraints = LinearConstraint(A, b_l, b_u)
    integrality = np.zeros(n_vars)
    integrality[:n] = 1 # x_i son binarias
    integrality[-1] = 0 # Z es continua

    bounds = Bounds(
        lb=[0]*n + [0],
        ub=[1]*n + [np.inf]
    )

    res = milp(c=c, constraints=constraints, integrality=integrality, bounds=bounds)

    p1 = [i for i in range(n) if res.x[i] > 0.5]
    p2 = [i for i in range(n) if res.x[i] <= 0.5]
    return res.fun, p1, p2
```

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Intentar linealizar $\max \min$ con el mismo truco:</strong> La técnica de variable auxiliar superior $Z \ge f_i$ solo funciona cuando la función objetivo es de **minimización**. Si se quisiera maximizar el mínimo ($\max \min$), se debe usar $Z \le f_i$. Aplicar $Z \ge f_i$ al maximizar $Z$ haría que $Z$ crezca hasta el infinito sin acotarse al valor mínimo real.</li>
    <li><strong>Declarar $Z$ como entera innecesariamente:</strong> Si los tiempos son enteros, $Z$ adoptará un valor entero automáticamente; forzarla a entera solo recarga el árbol de Branch and Bound del solver sin ninguna necesidad matemática.</li>
  </ul>
</div>

---

### Errores Frecuentes en Exámenes sobre Programación Lineal

1. **Multiplicar dos variables de decisión:** Escribir términos como $x_i \cdot y_j$ destruye la linealidad del modelo. En PL/PLI todos los términos deben ser el producto de una constante conocida por una única variable.
2. **Usar operadores $\max$, $\min$ o valores absolutos $|\cdot|$ directamente:** Deben linealizarse obligatoriamente mediante variables auxiliares continuas ($Z$) y sistemas de desigualdades.
3. **No declarar el dominio estricto de las variables:** Omitir si una variable es binaria ($x_i \in \{0, 1\}$), continua no negativa ($x_{ij} \ge 0$) o entera no negativa ($z_k \in \mathbb{Z}^+$) es motivo de descuento directo del $40\%$ del valor de la pregunta.
4. **Omitir el conteo analítico de variables y restricciones:** Si la consigna indica *"indicar variables y restricciones"*, debe tabularse cuántas variables continuas, cuántas binarias y cuántas restricciones lineales componen el modelo en función de los parámetros de entrada.
"""
