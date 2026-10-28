"""Módulo 6: Programación Lineal y Entera (PL / PLI)."""

def get_content():
    return r"""## 8. Tema 5: Programación Lineal y Entera (PL / PLI)

### Conceptos Mínimos de Supervivencia

1. **Qué Escribir en la Hoja del Parcial (Estructura Directa de 3 Bloques):**
   En los parciales de TDA, un ejercicio de Programación Lineal se responde en papel de forma directa y ordenada en tres partes:
   1. **Idea y Justificación en Lenguaje Natural:** Explicar brevemente qué decisión representa cada variable, qué se busca minimizar o maximizar, y por qué las restricciones modelan las reglas del enunciado (o cómo funciona la linealización si hay un $\min \max$).
   2. **Modelo de Programación Lineal:**
      * **Variables de decisión y dominios:** Definir qué significa cada variable y si es binaria ($x_i \in \{0, 1\}$), entera o continua no negativa ($x_{ij} \ge 0$).
      * **Función Objetivo:** Expresión lineal a minimizar ($\min Z = \dots$) o maximizar ($\max Z = \dots$). Prohibido multiplicar dos variables entre sí o usar $\max, \min, |\cdot|$ sin linealizar.
      * **Restricciones lineales:** Cada grupo de desigualdades o igualdades explicado en un renglón con su cuantificador ($\forall i \dots$).
   3. **Cantidad y Tipo de Variables y Restricciones:** El recuento exacto en función de los datos de entrada (ej: *"$N$ variables binarias y $N - 2$ restricciones lineales"*).

2. **Trucos Clásicos de Examen:**
   * **Minimizar un Máximo ($\min \max(f_1, \dots, f_k)$):** Crear una variable continua auxiliar $Z \ge 0$, pedir $\min Z$ y agregar las restricciones $Z \ge f_r(x)$ para cada $r$. Al minimizar $Z$, el modelo la empuja hacia abajo hasta chocar con el mayor de los $f_r$.
   * **Restricción de Enlace / Cobertura ($x_i \le \sum y_j$):** Si un beneficio $x_i \in \{0, 1\}$ depende de activar al menos un recurso $y_j \in \{0, 1\}$ que lo cubre, escribimos $x_i \le \sum_{j \in \text{Cubren}(i)} y_j$. Si ningún $y_j$ vale $1$, la suma da $0$ y obliga a $x_i = 0$.
   * **Unimodularidad Total (TUM):** En problemas de camino mínimo o flujo con conservación nodal pura ($\text{Sale} - \text{Entra} = b_i$ con $b_i \in \mathbb{Z}$), la matriz es Totalmente Unimodular. Esto garantiza que la **PL continua** da soluciones $100\%$ enteras en tiempo polinomial sin necesidad de declarar variables binarias.

---

### Patrón de Ejercicio 5.1: Máxima Cobertura con Presupuesto de Recursos

Problemas donde se busca maximizar la cantidad de elementos cubiertos o beneficiados sujeto a un límite estricto de tiempo, dinero o capacidad disponible.

---

### Ejercicio 60 — Observación de Aves de Paolo Casanova (Máxima Cobertura con Presupuesto de Tiempo)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2024-2-1 (5 de noviembre de 2024), Ejercicio 4

**Enunciado**  
Paolo Casanova dispone de 2 días para realizar salidas a diferentes lugares cercanos y observar la mayor cantidad posible de especies de aves. Hay 10 especies en particular que desea encontrar ($E = \{1, \dots, 10\}$) y 6 lugares posibles a visitar ($L = \{1, \dots, 6\}$). Algunos lugares insumen medio día ($0.5$ días) y otros un día completo ($1.0$ días). Para cada lugar se conoce exactamente qué especies habitan allí según una matriz binaria de presencia $A_{ij}$ ($A_{ij} = 1$ si la especie $i$ habita en el lugar $j$, $0$ si no). Plantear un modelo de Programación Lineal Entera que determine qué lugares visitar para maximizar la cantidad de especies distintas encontradas en el tiempo disponible. Indicar la cantidad exacta de variables y restricciones del modelo.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Dos familias de decisiones binarias:**
  1. Por cada lugar $j \in \{1, \dots, 6\}$ definimos una variable binaria $y_j \in \{0, 1\}$ que vale $1$ si decidimos visitar ese lugar y $0$ si no.
  2. Por cada especie de ave $i \in \{1, \dots, 10\}$ definimos otra variable binaria $x_i \in \{0, 1\}$ que vale $1$ si logramos avistar al menos una vez a la especie $i$, y $0$ si no.
* **Qué buscamos maximizar:** Queremos maximizar la cantidad de **especies distintas** observadas, es decir, la suma $\sum_{i=1}^{10} x_i$.
* **Cómo funcionan las restricciones:**
  * **Límite de tiempo:** La suma del tiempo $d_j$ que toman los lugares visitados no puede superar los $2$ días disponibles ($\sum d_j \cdot y_j \le 2$).
  * **Vínculo lugar-especie (Cobertura):** Para cada especie $i$, imponemos $x_i \le \sum_{j=1}^{6} A_{ij} \cdot y_j$.
    * Si **no visitamos ningún lugar** donde viva la especie $i$, la suma de la derecha da $0$ y obliga a que $x_i = 0$ (no podemos contar un ave que no vimos).
    * Si **visitamos uno o más lugares** donde vive la especie $i$, la suma da $\ge 1$. Como $x_i \in \{0, 1\}$ es binaria y estamos maximizando $\sum x_i$, el modelo le asignará automáticamente $x_i = 1$ (contando cada especie distinta a lo sumo una vez, aunque la veamos en varios lugares).

```mermaid
flowchart LR
    subgraph Lugares ["Lugares Candidatos (y_j ∈ {0,1})"]
        L1["Lugar 1 (0.5 días)"]
        L2["Lugar 2 (1.0 días)"]
        L3["Lugar 3 (0.5 días)"]
    end
    subgraph Especies ["Especies Avistadas (x_i ∈ {0,1})"]
        E1["Especie 1: x₁ ≤ y₁"]
        E2["Especie 2: x₂ ≤ y₁ + y₂"]
        E3["Especie 3: x₃ ≤ y₂ + y₃"]
    end
    L1 --> E1
    L1 --> E2
    L2 --> E2
    L2 --> E3
    L3 --> E3
```

#### 2. Modelo de Programación Lineal (Listo para la Hoja del Parcial)

1. **Variables de decisión y dominios:**
   * $y_j \in \{0, 1\} \quad \forall j \in \{1, \dots, 6\}$: vale $1$ si Paolo visita el lugar $j$, y $0$ en caso contrario.
   * $x_i \in \{0, 1\} \quad \forall i \in \{1, \dots, 10\}$: vale $1$ si la especie $i$ es observada en al menos un lugar visitado, y $0$ en caso contrario.

2. **Función Objetivo:**
   Maximizar la cantidad de especies distintas observadas:
   $$\max Z = \sum_{i=1}^{10} x_i$$

3. **Restricciones lineales:**
   * **Presupuesto máximo de tiempo (2 días):** (donde $d_j \in \{0.5, 1.0\}$ es la duración del lugar $j$)
     $$\sum_{j=1}^{6} d_j \cdot y_j \le 2$$
   * **Activación de avistamiento por especie:** (donde $A_{ij} \in \{0, 1\}$ vale $1$ si la especie $i$ habita en el lugar $j$)
     $$x_i \le \sum_{j=1}^{6} A_{ij} \cdot y_j \quad \forall i \in \{1, \dots, 10\}$$

#### 3. Cantidad y Tipo de Variables y Restricciones

* **Cantidad y tipo de variables:** Exactamente **$16$ variables binarias** ($6$ variables binarias $y_j$ para los lugares + $10$ variables binarias $x_i$ para las especies; en forma genérica $|L| + |E|$ variables binarias).
* **Cantidad de restricciones:** Exactamente **$11$ restricciones lineales funcionales** ($1$ restricción de presupuesto de tiempo + $10$ restricciones de enlace de cobertura, una por cada especie; en forma genérica $1 + |E|$ restricciones), además de las declaraciones de dominio binario.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Poner igualdad ($x_i = \sum A_{ij} y_j$) en vez de menor o igual ($\le$):</strong> Si ponés $=$, cuando visites 2 lugares donde habita la misma especie $i$, la suma dará $2$. Como $x_i \in \{0, 1\}$ no puede valer $2$, ¡el modelo te prohibiría visitar dos lugares que compartan un ave! Siempre debe ser $\le$.</li>
    <li><strong>No crear las variables $x_i$ y maximizar directamente $\sum_i \sum_j A_{ij} y_j$:</strong> Eso contaría varias veces a una misma especie si aparece en múltiples lugares visitados, cuando el enunciado pide maximizar especies <em>distintas</em>.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 5.2: Cobertura de Celdas con Umbral Porcentual

Problemas de infraestructura (antenas, sensores, cámaras) sobre grillas donde se exige cubrir una fracción mínima del total de objetivos con costo mínimo.

---

### Ejercicio 61 — Cobertura de Antenas Celulares con Umbral del 70% de Vecindarios

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2024-2-3 (10 de diciembre de 2024), Ejercicio 3

**Enunciado**  
Una empresa de telefonía celular colocará antenas en una grilla bidimensional de celdas para prestar servicio a vecindarios distribuidos en un mapa. Si se instala una antena en la celda $(i, j)$, brindará cobertura a un bloque de 9 celdas (la propia celda $(i, j)$ y sus 8 celdas contiguas en vecindad de Moore). Instalar una antena tiene un costo fijo $CTE > 0$ idéntico en cualquier celda. Se dispone de un conjunto $V$ de vecindarios distribuidos en la zona. La empresa exige brindar servicio a **por lo menos el 70% de los vecindarios** minimizando la inversión total. Plantear un modelo de Programación Lineal Entera indicando claramente variables, dominios, función objetivo, restricciones y su conteo exacto.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Dos familias de variables binarias:**
  1. Para cada celda candidata $c \in C$ de la grilla, definimos $y_c \in \{0, 1\}$, que vale $1$ si instalamos una antena en la celda $c$ y $0$ si no.
  2. Para cada vecindario $v \in V$, definimos $x_v \in \{0, 1\}$, que vale $1$ si el vecindario $v$ queda cubierto por al menos una antena y $0$ si queda sin servicio.
* **Qué buscamos minimizar:** La inversión total en antenas instaladas, que es $\sum_{c \in C} CTE \cdot y_c$.
* **Cómo funcionan las restricciones:**
  * **Vínculo antena-vecindario:** Para cada vecindario $v$, llamamos $\text{Cubren}(v) \subseteq C$ al conjunto de hasta $9$ celdas (la celda de $v$ y sus $8$ vecinas inmediatas) desde las cuales una antena alcanza a cubrir a $v$. Imponemos $x_v \le \sum_{c \in \text{Cubren}(v)} y_c$. Si no se instala ninguna antena en esas $9$ celdas, la suma da $0$ y obliga a que $x_v = 0$.
  * **Exigencia del 70%:** Para obligar al modelo a dar servicio a por lo menos el $70\%$ de los vecindarios, exigimos que la suma de vecindarios cubiertos cumpla $\sum_{v \in V} x_v \ge 0.70 \cdot |V|$.

```mermaid
graph TD
    subgraph CeldaAntena ["Antena en Celda (i, j) -> y_c = 1"]
        C["Celda Central (i, j)"]
    end
    subgraph CeldasCubiertas ["Bloque de 9 Celdas Cubiertas (3x3)"]
        V1["(i-1, j-1)"]
        V2["(i-1, j)"]
        V3["(i-1, j+1)"]
        V4["(i, j-1)"]
        V5["(i, j+1)"]
        V6["(i+1, j-1)"]
        V7["(i+1, j)"]
        V8["(i+1, j+1)"]
    end
    C --> V1 & V2 & V3 & V4 & V5 & V6 & V7 & V8
```

#### 2. Modelo de Programación Lineal (Listo para la Hoja del Parcial)

1. **Variables de decisión y dominios:**
   * $y_c \in \{0, 1\} \quad \forall c \in C$: vale $1$ si se instala una antena en la celda $c$, y $0$ si no.
   * $x_v \in \{0, 1\} \quad \forall v \in V$: vale $1$ si el vecindario $v$ recibe cobertura de al menos una antena, y $0$ si no.

2. **Función Objetivo:**
   Minimizar el costo total de instalación de antenas:
   $$\min Z = \sum_{c \in C} CTE \cdot y_c$$

3. **Restricciones lineales:**
   * **Cobertura mínima del 70% de los vecindarios:**
     $$\sum_{v \in V} x_v \ge 0.70 \cdot |V|$$
   * **Vínculo físico de cobertura por vecindario:** (donde $\text{Cubren}(v)$ son las celdas a distancia $\le 1$ en fila y columna del vecindario $v$)
     $$x_v \le \sum_{c \in \text{Cubren}(v)} y_c \quad \forall v \in V$$

#### 3. Cantidad y Tipo de Variables y Restricciones

* **Cantidad y tipo de variables:** **$|C| + |V|$ variables binarias** ($|C|$ variables binarias $y_c$ para las celdas de la grilla + $|V|$ variables binarias $x_v$ para los vecindarios).
* **Cantidad de restricciones:** **$|V| + 1$ restricciones lineales funcionales** ($1$ restricción por el umbral global del $70\%$ + $|V|$ restricciones de enlace de cobertura, una por cada vecindario), además de los dominios binarios.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Maximizar vecindarios en lugar de minimizar costo:</strong> La función objetivo es $\min \sum CTE \cdot y_c$. El $70\%$ no es el objetivo a optimizar, sino una <strong>restricción de piso</strong> ($\ge 0.70 \cdot |V|$).</li>
    <li><strong>Escribir al revés la desigualdad de enlace ($y_c \le x_v$):</strong> La forma correcta es $x_v \le \sum_{c \in \text{Cubren}(v)} y_c$ (sin antenas cercanas no hay cobertura).</li>
  </ul>
</div>

---

### Patrón de Ejercicio 5.3: Flujo de Costo Mínimo / Transporte Multizona

Problemas de balance de oferta y demanda con capacidades máximas y costos de transporte por arista en redes continuas.

---

### Ejercicio 62 — Distribución Energética Multizona con Costos de Transporte (Flujo de Costo Mínimo)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2025-1-1 (27 de mayo de 2025), Ejercicio 3

**Enunciado**  
El sistema interconectado argentino está dividido en 9 regiones eléctricas ($R = \{1, \dots, 9\}$). Para cada región $i$ se conoce su capacidad de generación prevista $G_i \ge 0$ (en MWh) y su demanda requerida $D_i \ge 0$ (en MWh). Desde cualquier región $i$ se puede transmitir energía a otra región $j$ con un costo unitario de transporte $C_{ij} \ge 0$ pesos por MWh. Cada línea de transmisión posee una capacidad máxima de transporte de $CAP_{ij} \ge 0$ MWh/día. Plantear un modelo de Programación Lineal continuo que determine el despacho de energía más económico para satisfacer plenamente la demanda de todas las regiones sin violar capacidades de transporte. Indicar variables y restricciones.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Variables de decisión continuas:** Como la energía eléctrica (MWh) es una magnitud continua y divisible, no necesitamos variables enteras ni binarias. Por cada línea de transmisión dirigida desde una región $i$ hacia otra región $j$ ($i \neq j$), definimos una variable continua no negativa $x_{ij} \ge 0$ que indica cuántos MWh se envían de $i$ a $j$.
* **Qué buscamos minimizar:** El costo total de transporte de energía en todo el país, sumando el costo por MWh $C_{ij}$ multiplicado por la energía enviada $x_{ij}$ en cada línea.
* **Cómo funcionan las restricciones:**
  1. **Conservación / Balance de energía en cada región $i$:** En toda región $i$, la energía que se genera localmente ($G_i$) más toda la energía que entra desde otras regiones ($\sum_k x_{ki}$) menos toda la energía que se envía hacia otras regiones ($\sum_j x_{ij}$) tiene que ser igual a la demanda local $D_i$ (o $\ge D_i$ si se permite no usar el $100\%$ de la generación máxima prevista).
  2. **Tope de cada línea de transmisión:** La energía enviada de $i$ a $j$ no puede superar la capacidad física del cable ($x_{ij} \le CAP_{ij}$).

```mermaid
flowchart LR
    R1["Región 1<br/>Genera G₁, Demanda D₁"] -->|"x₁₂ ≤ CAP₁₂ (Costo C₁₂)"| R2["Región 2<br/>Genera G₂, Demanda D₂"]
    R1 -->|"x₁₃ ≤ CAP₁₃ (Costo C₁₃)"| R3["Región 3<br/>Genera G₃, Demanda D₃"]
    R2 -->|"x₂₃ ≤ CAP₂₃ (Costo C₂₃)"| R3
```

#### 2. Modelo de Programación Lineal (Listo para la Hoja del Parcial)

1. **Variables de decisión y dominios:**
   * $x_{ij} \in \mathbb{R}_{\ge 0} \quad (x_{ij} \ge 0) \quad \forall i, j \in \{1, \dots, 9\}, \; i \neq j$: cantidad de energía (en MWh) transmitida desde la región $i$ hacia la región $j$.

2. **Función Objetivo:**
   Minimizar el costo total de transmisión de energía:
   $$\min Z = \sum_{i=1}^{9} \sum_{\substack{j=1 \\ j \neq i}}^{9} C_{ij} \cdot x_{ij}$$

3. **Restricciones lineales:**
   * **Balance de energía en cada región:** ($\text{Generación}_i + \text{Entra}_i - \text{Sale}_i = \text{Demanda}_i$; usar $\ge D_i$ si $G_i$ es un tope máximo opcional)
     $$G_i + \sum_{\substack{k=1 \\ k \neq i}}^{9} x_{ki} - \sum_{\substack{j=1 \\ j \neq i}}^{9} x_{ij} = D_i \quad \forall i \in \{1, \dots, 9\}$$
   * **Capacidad máxima de transmisión por línea:**
     $$x_{ij} \le CAP_{ij} \quad \forall i, j \in \{1, \dots, 9\}, \; i \neq j$$

#### 3. Cantidad y Tipo de Variables y Restricciones

* **Cantidad y tipo de variables:** Exactamente **$72$ variables continuas no negativas** ($9 \times 8 = 72$ pares ordenados $(i, j)$ con $i \neq j$; o $|E|$ variables continuas si solo existen ciertas líneas conectadas).
* **Cantidad de restricciones:** Exactamente **$81$ restricciones lineales funcionales** ($9$ ecuaciones de balance nodal, una por cada región + $72$ desigualdades de capacidad máxima $x_{ij} \le CAP_{ij}$, una por cada línea dirigida), además de las $72$ condiciones de dominio $x_{ij} \ge 0$.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Declarar variables enteras o binarias:</strong> La energía es continua y el enunciado pide explícitamente un modelo de <em>Programación Lineal continuo</em>. Poner $x_{ij} \in \mathbb{Z}$ o $\{0, 1\}$ está mal conceptualmente.</li>
    <li><strong>Invertir entradas y salidas en el balance:</strong> Revisar siempre los subíndices: $\sum_k x_{ki}$ entra al nodo $i$, mientras que $\sum_j x_{ij}$ sale del nodo $i$.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 5.4: Camino Mínimo Formulado como Flujo Unitario

Formulación de la búsqueda de rutas óptimas en grafos dirigidos como problemas de inyección y extracción de una única unidad de flujo en Programación Lineal continua aprovechando Unimodularidad Total.

---

### Ejercicio 63 — Camino de Mínimo Riesgo (INVAP) como Flujo Unitario en PL

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Parcial 2025-1-2 (17 de junio de 2025), Ejercicio 5

**Enunciado**  
Para el traslado de una carga crítica de alta seguridad de la empresa INVAP desde el centro atómico Ezeiza ($s$) hasta el laboratorio central en Bariloche ($t$), se dispone de un grafo dirigido $G = (V, E)$. Cada tramo carretero $(u, v) \in E$ tiene un costo de póliza de seguro $C_{uv} > 0$. Plantear un modelo de Programación Lineal continuo que determine la ruta de menor costo de seguro. Justificar formalmente por qué no es necesario declarar las variables como binarias para obtener una ruta válida. Indicar la cantidad exacta de variables y restricciones.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Cómo modelar el Camino Mínimo mediante Flujo Unitario:**
  Imaginamos que inyectamos exactamente **$1$ unidad de flujo** en el origen $s$ (Ezeiza) y la extraemos en el destino $t$ (Bariloche). Por cada tramo carretero $(u, v) \in E$ definimos una variable continua no negativa $x_{uv} \ge 0$ que mide cuánto flujo transita por esa arista, y buscamos minimizar el costo total de seguro $\sum_{(u,v) \in E} C_{uv} \cdot x_{uv}$.
* **Balance de conservación en cada nodo:**
  * En **Ezeiza ($s$):** sale $1$ unidad más de la que entra ($\text{Sale}_s - \text{Entra}_s = 1$).
  * En **Bariloche ($t$):** entra $1$ unidad más de la que sale ($\text{Sale}_t - \text{Entra}_t = -1$).
  * En **cualquier ciudad intermedia ($i \notin \{s, t\}$):** todo lo que entra debe salir ($\text{Sale}_i - \text{Entra}_i = 0$).
* **¿Por qué NO hace falta declarar variables binarias?** *(Pregunta obligatoria de examen)*:
  Porque la matriz de restricciones de conservación de flujo en un grafo dirigido (matriz de incidencia nodo-arista) cumple la propiedad de **Unimodularidad Total (TUM)** (todo subdeterminante vale $0, 1$ o $-1$). Cuando la matriz es Totalmente Unimodular y los términos independientes del lado derecho son enteros ($+1, -1$ y $0$), **todos los vértices del poliedro factible son enteros**. Por lo tanto, al resolver el modelo con Programación Lineal continua (por ejemplo con Simplex), el óptimo hallado tendrá automáticamente valores enteros $x_{uv} \in \{0, 1\}$ marcando el camino óptimo sin fraccionar la carga.

```mermaid
flowchart LR
    S_NODE["Ezeiza s<br/>Sale - Entra = +1"] -->|"C = 12"| N1["Neuquén<br/>Sale - Entra = 0"]
    S_NODE -->|"C = 18"| N2["Bahía Blanca<br/>Sale - Entra = 0"]
    N1 -->|"C = 6"| T_NODE["Bariloche t<br/>Sale - Entra = -1"]
    N2 -->|"C = 7"| T_NODE
    N2 -->|"C = 3"| N1
```

#### 2. Modelo de Programación Lineal (Listo para la Hoja del Parcial)

1. **Variables de decisión y dominios:**
   * $x_{uv} \in \mathbb{R}_{\ge 0} \quad (x_{uv} \ge 0) \quad \forall (u, v) \in E$: cantidad de flujo que circula por el tramo $(u, v)$ (en el óptimo valdrá $1$ si el tramo pertenece a la ruta elegida y $0$ si no).

2. **Función Objetivo:**
   Minimizar el costo total de seguro del camino:
   $$\min Z = \sum_{(u, v) \in E} C_{uv} \cdot x_{uv}$$

3. **Restricciones lineales (Conservación de flujo para cada nodo $i \in V$):**
   * **En el origen $s$ (Ezeiza):**
     $$\sum_{v : (s, v) \in E} x_{sv} - \sum_{u : (u, s) \in E} x_{us} = 1$$
   * **En el destino $t$ (Bariloche):**
     $$\sum_{v : (t, v) \in E} x_{tv} - \sum_{u : (u, t) \in E} x_{ut} = -1$$
   * **En los nodos intermedios $i \in V \setminus \{s, t\}$:**
     $$\sum_{v : (i, v) \in E} x_{iv} - \sum_{u : (u, i) \in E} x_{ui} = 0 \quad \forall i \in V \setminus \{s, t\}$$

#### 3. Cantidad y Tipo de Variables y Restricciones

* **Cantidad y tipo de variables:** Exactamente **$|E|$ variables continuas no negativas** ($x_{uv} \ge 0$, una por cada tramo dirigido del grafo).
* **Cantidad de restricciones:** Exactamente **$|V|$ restricciones lineales de igualdad** (una ecuación de conservación de flujo por cada vértice del grafo: $1$ en el origen, $1$ en el destino y $|V| - 2$ en los nodos intermedios), además de las $|E|$ cotas de no negatividad $x_{uv} \ge 0$.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Poner $x_{uv} \in \{0, 1\}$:</strong> El enunciado pide explícitamente un modelo <em>continuo</em> y justificar por qué da entero. La palabra clave que buscan los correctores es <strong>Unimodularidad Total (TUM)</strong> de la matriz de incidencia.</li>
    <li><strong>Olvidar las ecuaciones del origen $s$ y destino $t$:</strong> Si solo escribís que lo que entra es igual a lo que sale ($= 0$), la solución óptima trivial será $x_{uv} = 0$ en todas las aristas con costo $0$.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 5.5: Linealización de Funciones No Lineales (min max)

Transformación de funciones objetivo no lineales como minimax o discrepancias absolutas en sistemas lineales estándar con variables continuas auxiliares.

---

### Ejercicio 64 — 2-Partition Min-Max con Linealización de Variable Auxiliar

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía de Ejercicios 05, Ejercicio 12 / Práctica de Examen

**Enunciado**  
Dado un conjunto de $n$ tareas con tiempos de procesamiento enteros positivos $T = \{T_1, T_2, \dots, T_n\}$, se desea particionar las tareas entre dos procesadores idénticos $P_1$ y $P_2$ de manera que se minimice el *makespan* (el tiempo de finalización de la máquina más cargada):
$$\min \max \left( \sum_{i \in P_1} T_i, \sum_{j \in P_2} T_j \right)$$
Formular el problema como un modelo de Programación Lineal Entera, linealizando rigurosamente el operador $\max$. Indicar variables, dominios y conteo de restricciones.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Variables binarias de partición:** Como cada tarea $i$ debe asignarse sí o sí al procesador $P_1$ o al procesador $P_2$, nos alcanza con una única variable binaria $x_i \in \{0, 1\}$ por tarea:
  * Si $x_i = 1$, la tarea $i$ se ejecuta en $P_1$ (aportando $T_i \cdot x_i$ a la carga de $P_1$).
  * Si $x_i = 0$, la tarea $i$ se ejecuta en $P_2$ (como $1 - x_i = 1$, aporta $T_i \cdot (1 - x_i)$ a la carga de $P_2$).
* **Cómo linealizar la función $\min \max$:**
  En Programación Lineal no está permitido escribir $\max(\dots)$ en la función objetivo. Para linealizarlo, introducimos una **variable continua auxiliar $Z \ge 0$** que representa el *makespan* (la carga del procesador más ocupado) y agregamos dos restricciones de cota superior:
  1. $Z \ge \text{Carga de } P_1$
  2. $Z \ge \text{Carga de } P_2$
  Como $Z$ está obligada a ser mayor o igual que ambas cargas simultáneamente, y la función objetivo pide **minimizar $Z$** ($\min Z$), el optimizador reducirá $Z$ todo lo posible hasta que toque a la mayor de las dos cargas, logrando exactamente $Z = \max(\text{Carga}_{P_1}, \text{Carga}_{P_2})$.

```mermaid
flowchart LR
    P1["Carga P₁ = Σ T_i · x_i"] -->|"Restricción 1: Z ≥ Carga P₁"| Z["Variable Auxiliar Continua Z"]
    P2["Carga P₂ = Σ T_i · (1 - x_i)"] -->|"Restricción 2: Z ≥ Carga P₂"| Z
    MinZ["Función Objetivo: min Z"] -->|"Empuja Z hacia abajo hasta el máximo"| Z
```

#### 2. Modelo de Programación Lineal (Listo para la Hoja del Parcial)

1. **Variables de decisión y dominios:**
   * $x_i \in \{0, 1\} \quad \forall i \in \{1, \dots, n\}$: vale $1$ si la tarea $i$ se asigna al procesador $P_1$, y $0$ si se asigna al procesador $P_2$.
   * $Z \in \mathbb{R}_{\ge 0} \quad (Z \ge 0)$: variable continua auxiliar que representa el tiempo de finalización del procesador más cargado (*makespan*).

2. **Función Objetivo:**
   Minimizar el tiempo de finalización máximo:
   $$\min Z$$

3. **Restricciones lineales:**
   * **Cota superior para el Procesador 1:**
     $$Z \ge \sum_{i=1}^{n} T_i \cdot x_i$$
   * **Cota superior para el Procesador 2:**
     $$Z \ge \sum_{i=1}^{n} T_i \cdot (1 - x_i)$$

#### 3. Cantidad y Tipo de Variables y Restricciones

* **Cantidad y tipo de variables:** **$n + 1$ variables en total**, compuestas por **$n$ variables binarias** ($x_1, \dots, x_n \in \{0, 1\}$) y **$1$ variable continua no negativa** ($Z \ge 0$). *(Nota: si se definieran dos variables binarias $x_{i,1}, x_{i,2}$ por tarea, serían $2n$ binarias + $1$ continua y se agregarían $n$ restricciones $x_{i,1} + x_{i,2} = 1$).*
* **Cantidad de restricciones:** Exactamente **$2$ restricciones lineales funcionales** (una por cada procesador para acotar inferiormente a $Z$), además de los dominios de las variables.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Dejar $\max(\dots)$ escrito dentro de la función objetivo:</strong> La función $\max$ no es lineal. Si no creás la variable $Z$ y las dos desigualdades $Z \ge \dots$, el ejercicio se considera mal resuelto.</li>
    <li><strong>Poner $Z \le \text{Carga}$ en vez de $Z \ge \text{Carga}$:</strong> Si ponés $\le$ y pedís minimizar $Z$, el solver fijará $Z = 0$ sin importar cuánto tarden las máquinas.</li>
  </ul>
</div>

---

### Patrón de Ejercicio 5.6: Cobertura por Ventanas Deslizantes en Secuencias

Problemas sobre rutas o líneas de tiempo donde no se permite dejar más de $k$ posiciones consecutivas sin activar, modelables mediante restricciones de ventana deslizante de tamaño $k + 1$.

---

### Ejercicio 65 — Modelo de Programación Lineal para Ruta de Transporte con Estaciones

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Parcial 2026-2-1 (Enunciados), Ejercicio 5

**Enunciado**  
Realizar un modelo de programación lineal que resuelva el problema del punto 3 (transporte con $N$ estaciones intermedias con tarifa $T_i$, sin poder saltear más de dos estaciones consecutivas, minimizando el costo total de paradas). Indicar la cantidad y tipo de variables del problema, y la cantidad de restricciones del mismo.

#### 1. Idea y Justificación en Lenguaje Natural (Qué escribir en la hoja)

* **Variables de decisión binarias:** Por cada estación intermedia $i \in \{1, 2, \dots, N\}$ definimos una variable binaria $x_i \in \{0, 1\}$, que vale $1$ si el transporte se detiene en la estación $i$ (pagando la tarifa $T_i$) y $0$ si decide saltearla.
* **Qué buscamos minimizar:** La suma de las tarifas de todas las estaciones donde el transporte decide detenerse: $\sum_{i=1}^N T_i \cdot x_i$.
* **Cómo modelar que no se pueden saltear más de 2 estaciones seguidas:**
  No poder saltear más de $2$ estaciones consecutivas significa que **en cualquier bloque o ventana de $3$ estaciones seguidas $(i, \; i+1, \; i+2)$, el transporte está obligado a detenerse en al menos una de las tres** (nunca pueden valer $0$ las tres al mismo tiempo).
  En Programación Lineal Entera, exigir que al menos una de las tres variables binarias consecutivas valga $1$ se escribe directamente sumándolas y pidiendo que den al menos $1$:
  $$x_i + x_{i+1} + x_{i+2} \ge 1 \quad \forall i \in \{1, \dots, N - 2\}$$

```mermaid
flowchart LR
    subgraph Ventana1 ["Ventana 1: x₁ + x₂ + x₃ ≥ 1"]
        E1["Estación 1 (x₁)"] --- E2["Estación 2 (x₂)"] --- E3["Estación 3 (x₃)"]
    end
    subgraph Ventana2 ["Ventana 2: x₂ + x₃ + x₄ ≥ 1"]
        E2 --- E3 --- E4["Estación 4 (x₄)"]
    end
```

#### 2. Modelo de Programación Lineal (Listo para la Hoja del Parcial)

1. **Variables de decisión y dominios:**
   * $x_i \in \{0, 1\} \quad \forall i \in \{1, \dots, N\}$: vale $1$ si el transporte se detiene en la estación intermedia $i$, y $0$ si la saltea.

2. **Función Objetivo:**
   Minimizar el costo total de las paradas realizadas:
   $$\min Z = \sum_{i=1}^{N} T_i \cdot x_i$$

3. **Restricciones lineales:**
   * **Autonomía (al menos 1 parada cada 3 estaciones consecutivas):**
     $$x_i + x_{i+1} + x_{i+2} \ge 1 \quad \forall i \in \{1, 2, \dots, N - 2\}$$

#### 3. Cantidad y Tipo de Variables y Restricciones

* **Cantidad y tipo de variables:** Exactamente **$N$ variables binarias** ($x_i \in \{0, 1\}$, una por cada estación intermedia).
* **Cantidad de restricciones:** Exactamente **$N - 2$ restricciones lineales funcionales** (una por cada ventana de $3$ estaciones consecutivas $(i, i+1, i+2)$ desde $i = 1$ hasta $N - 2$, asumiendo $N \ge 3$), además de las $N$ declaraciones de dominio binario.

<div class="trap-callout">
  <div class="trap-header">⚠️ Trampa Típica de Corrección</div>
  <p><strong>Puntos donde restan puntaje los docentes de FIUBA:</strong></p>
  <ul>
    <li><strong>Responder que hay $N$ restricciones en lugar de $N - 2$:</strong> La última terna de $3$ estaciones es $(N-2, \; N-1, \; N)$, que corresponde a $i = N - 2$. Si pusieras $i$ hasta $N$, aparecerían estaciones inexistentes $x_{N+1}$ y $x_{N+2}$.</li>
    <li><strong>Olvidar aclarar el tipo de las variables:</strong> La consigna pide explícitamente <em>cantidad y tipo</em>; es obligatorio especificar que son <strong>binarias</strong> ($x_i \in \{0, 1\}$).</li>
  </ul>
</div>

---

### Errores Frecuentes en Exámenes sobre Programación Lineal

1. **Multiplicar dos variables de decisión:** Escribir términos como $x_i \cdot y_j$ destruye la linealidad del modelo. En PL/PLI todos los términos deben ser el producto de una constante conocida por una única variable.
2. **Usar operadores $\max$, $\min$ o valores absolutos $|\cdot|$ directamente:** Deben linealizarse obligatoriamente mediante variables auxiliares continuas ($Z$) y sistemas de desigualdades.
3. **No declarar el dominio estricto de las variables:** Omitir si una variable es binaria ($x_i \in \{0, 1\}$), continua no negativa ($x_{ij} \ge 0$) o entera no negativa ($z_k \in \mathbb{Z}_{\ge 0}$) es motivo de descuento directo del $40\%$ del valor de la pregunta.
4. **Omitir el conteo analítico de variables y restricciones:** Si la consigna indica *"indicar variables y restricciones"*, debe especificarse cuántas variables de cada tipo y cuántas restricciones lineales componen el modelo en función de los parámetros de entrada.
"""
