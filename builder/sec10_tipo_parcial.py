"""Módulo 10: Ejercicios Tipo Parcial Generados (Nuevos, Estilo Cátedra)."""

def get_content():
    return r"""## 12. Ejercicios Tipo Parcial Generados

Esta sección contiene ejercicios nuevos creados específicamente siguiendo la estructura, terminología, nivel de dificultad y estilo narrativo de los exámenes reales de la cátedra Echevarría.

---

### Ejercicio 37 — Despacho de Drones de Emergencia con Ventanas de Batería

**Tipo:** Ejercicio generado a partir de patrones de parciales  
**Clasificación:** 🔴 IMPRESCINDIBLE  
**Paradigma:** Redes de Flujo (Matching Bipartito con Restricción de Recursos)

**Enunciado**  
El sistema de emergencias médicas de una provincia dispone de una flota de D drones para transportar medicamentos urgentes a P puestos sanitarios aislados. Cada dron i tiene una base de despegue y una autonomía de batería que le permite realizar vuelos únicamente dentro de un intervalo horario específico [t_i^inicio, t_i^fin]. Además, por limitaciones de carga térmica de sus baterías, cada dron puede realizar a lo sumo 2 entregas durante su turno de operación. Por su parte, cada puesto sanitario j requiere exactamente 1 entrega de medicamentos y define una ventana horaria estricta [h_j^min, h_j^max] en la cual puede recibirla. Se conoce qué drones son compatibles con qué puestos (distancia de vuelo factible).  
1. Diseñar un algoritmo mediante Redes de Flujo que determine una asignación que maximice la cantidad total de puestos sanitarios abastecidos.  
2. Detallar la construcción formal de la red (nodos, aristas, fuentes, sumideros y capacidades).  
3. Indicar y justificar la complejidad temporal del algoritmo.

**Qué está evaluando**  
Modelado de capacidades intermedias heterogéneas (c = 2 en drones), verificación temporal de compatibilidad previa a la red, y flujo máximo con cotas unitarias en puestos.

**Idea de resolución**  
* La compatibilidad temporal y geográfica se precalcula: el dron i puede atender al puesto j si la distancia es alcanzable y la ventana [h_j^min, h_j^max] cae dentro de la autonomía [t_i^inicio, t_i^fin].
* Construcción de la red:
  * Super-fuente s.
  * Capa de drones: nodo d_i por cada dron. Arista s → d_i con **capacidad 2** (cada dron puede hacer hasta 2 entregas).
  * Capa de puestos sanitarios: nodo p_j por cada puesto.
  * Para cada par compatible (i, j): arista d_i → p_j con **capacidad 1**.
  * Super-sumidero t: aristas desde cada puesto p_j → t con **capacidad 1** (cada puesto solo necesita 1 entrega).
* Flujo máximo mediante Ford-Fulkerson o Edmonds-Karp. Por integralidad, el flujo resultante asigna cada puesto a un dron válido sin superar las 2 entregas por dron.

**Pseudocódigo**

```text
FUNCION AsignarDronesEmergencia(drones, puestos, matriz_distancias):
    INICIALIZAR Red como grafo dirigido con capacidades
    s <- "SUPER_FUENTE"
    t <- "SUPER_SUMIDERO"

    // 1. Aristas de la fuente a cada dron (capacidad 2)
    PARA CADA d EN drones:
        AgregarArista(Red, s, d.id, capacidad=2)

    // 2. Aristas de drones a puestos sanitarios compatibles (capacidad 1)
    PARA CADA d EN drones:
        PARA CADA p EN puestos:
            // Verificación de autonomía y ventana horaria
            SI EsCompatibleDistancia(d, p, matriz_distancias) Y 
               d.inicio_bateria <= p.hora_min Y p.hora_max <= d.fin_bateria:
                AgregarArista(Red, d.id, p.id, capacidad=1)

    // 3. Aristas de puestos al sumidero (capacidad 1)
    PARA CADA p EN puestos:
        AgregarArista(Red, p.id, t, capacidad=1)

    // 4. Ejecución de flujo máximo
    (max_puestos, flujo) <- EdmondsKarp(Red, s, t)

    // 5. Reconstrucción de la asignación
    INICIALIZAR asignacion como lista vacía
    PARA CADA d EN drones:
        PARA CADA p EN puestos:
            SI flujo[(d.id, p.id)] = 1:
                INSERTAR (dron=d.id, puesto=p.id) EN asignacion

    RETORNAR (max_puestos, asignacion)
```

**Complejidad**  
* Nodos: |V| = 2 + D + P.  
* Aristas: |E| ≤ D + D · P + P.  
* Cota de flujo máximo: |f*| ≤ min(2D, P) ≤ P.  
* Complejidad temporal con Ford-Fulkerson con capacidades enteras: O(|E| · |f*|) = O(D · P²) (o O(V · E²) con Edmonds-Karp).

---

### Ejercicio 38 — Plan de Publicidad Digital con Días de Enfriamiento y Presupuesto

**Tipo:** Ejercicio generado a partir de patrones de parciales  
**Clasificación:** 🔴 IMPRESCINDIBLE  
**Paradigma:** Programación Dinámica (Exclusión Multidía con Restricción de Presupuesto)

**Enunciado**  
Una empresa de marketing digital planifica su campaña durante los próximos n días. Para cada día i dispone de una propuesta de pauta publicitaria que cuesta C[i] pesos y genera una conversión estimada de B[i] nuevos clientes. El presupuesto total asignado para los n días es de P pesos. Por políticas de fatiga de audiencia, si se pauta en el día i, **no se puede volver a pautar durante los siguientes 2 días** (es decir, tras pautar el día i, los días i + 1 e i + 2 deben ser de enfriamiento obligatorio; recién se podría pautar nuevamente el día i + 3). Desarrollar un algoritmo de Programación Dinámica que maximice la cantidad total de conversiones sin exceder el presupuesto. Detallar estado, casos base, recurrencia, complejidad y reconstrucción.

**Qué está evaluando**  
Combinación del patrón de exclusión espaciada (i - 3) con restricción de capacidad tipo mochila (P), y reconstrucción de días elegidos.

**Idea de resolución**  
* *Definición del Estado:*  
  OPT(i, p): Conversión máxima obtenible considerando los primeros i días (1 ≤ i ≤ n) con un presupuesto restante de p pesos (0 ≤ p ≤ P).
* *Opciones en el día i:*  
  1. **No pautar el día i:** El valor es OPT(i - 1, p).
  2. **Pautar el día i:** Requiere C[i] ≤ p. Otorga B[i] conversiones y obliga a que la pauta previa haya sido como máximo en el día i - 3. El valor acumulado es OPT(i - 3, p - C[i]) + B[i].
* *Recurrencia:*  
  > **OPT(i, p) = OPT(i - 1, p)** (si C[i] > p)  
  > **OPT(i, p) = max(OPT(i - 1, p), OPT(max(0, i - 3), p - C[i]) + B[i])** (si C[i] ≤ p)
* *Casos Base:*  
  OPT(0, p) = 0 para todo 0 ≤ p ≤ P.

**Pseudocódigo**

```text
FUNCION CampanaPublicitariaOptima(C, B, n, P):
    INICIALIZAR DP como matriz de (n + 1) x (P + 1) en 0

    PARA i <- 1 HASTA n:
        costo_dia <- C[i - 1]
        beneficio_dia <- B[i - 1]

        PARA p <- 0 HASTA P:
            // Opcion 1: No pautar el día i
            DP[i][p] <- DP[i - 1][p]

            // Opcion 2: Pautar el día i si hay presupuesto
            SI costo_dia <= p:
                dia_previo <- maximo(0, i - 3)
                con_pauta <- DP[dia_previo][p - costo_dia] + beneficio_dia
                SI con_pauta > DP[i][p]:
                    DP[i][p] <- con_pauta

    // Reconstrucción de los días elegidos
    INICIALIZAR dias_pauta como lista vacía
    idx_dia <- n
    idx_p <- P

    MIENTRAS idx_dia > 0:
        costo_dia <- C[idx_dia - 1]
        beneficio_dia <- B[idx_dia - 1]
        dia_previo <- maximo(0, idx_dia - 3)

        SI idx_p >= costo_dia Y DP[idx_dia][idx_p] = DP[dia_previo][idx_p - costo_dia] + beneficio_dia:
            INSERTAR idx_dia AL INICIO DE dias_pauta
            idx_p <- idx_p - costo_dia
            idx_dia <- dia_previo
        SINO:
            idx_dia <- idx_dia - 1

    RETORNAR (DP[n][P], dias_pauta)
```

**Complejidad**  
* **Tiempo:** O(n · P) operaciones (llena una tabla de (n + 1) × (P + 1) con comparaciones O(1)).  
* **Espacio:** O(n · P) para la tabla bidimensional.

---

### Ejercicio 39 — Ubicación de Servidores Edge con Resiliencia del 80%

**Tipo:** Ejercicio generado a partir de patrones de parciales  
**Clasificación:** 🔴 IMPRESCINDIBLE  
**Paradigma:** Programación Lineal Entera (Set Cover Ponderado con Umbral y Presupuesto)

**Enunciado**  
Una compañía de telecomunicaciones debe instalar servidores Edge en un conjunto de S ubicaciones posibles para dar cobertura de baja latencia a U usuarios industriales. Cada servidor instalado en el sitio i ∈ S tiene un costo de instalación K_i y una capacidad máxima de tráfico de T_i Gbps. Cada usuario j ∈ U demanda d_j Gbps y define un subconjunto de sitios candidatos S_j ⊆ S que cumplen con el límite de latencia de 5 milisegundos. La compañía exige que **al menos el 80% de los usuarios industriales reciban servicio**. Plantear un modelo de Programación Lineal Entera que determine qué servidores abrir y cómo asignar a los usuarios atendidos al menor costo de instalación posible. Indicar variables y restricciones.

**Modelo Matemático Formal**

```text
CONJUNTOS Y PARÁMETROS:
  S                       // Sitios candidatos para servidores
  U                       // Usuarios industriales
  K_i > 0        ∀ i ∈ S  // Costo de abrir servidor en sitio i
  T_i > 0        ∀ i ∈ S  // Capacidad de tráfico del servidor i
  d_j > 0        ∀ j ∈ U  // Demanda de tráfico del usuario j
  S_j ⊆ S        ∀ j ∈ U  // Sitios con latencia <= 5ms para el usuario j

VARIABLES DE DECISIÓN:
  y_i ∈ {0, 1}   ∀ i ∈ S        // 1 si se instala servidor en sitio i, 0 si no
  x_ji ∈ {0, 1}  ∀ j ∈ U, i ∈ S_j // 1 si el usuario j es abastecido por el servidor i, 0 si no
  u_j ∈ {0, 1}   ∀ j ∈ U        // 1 si el usuario j recibe servicio, 0 si no

FUNCIÓN OBJETIVO:
  MINIMIZAR Costo = ∑_{i ∈ S} (K_i * y_i)

RESTRICCIONES:
  // 1. Umbral mínimo de resiliencia del 80% de los usuarios
  ∑_{j ∈ U} u_j >= 0.80 * |U|

  // 2. Un usuario atendido se asigna a exactamente un servidor compatible
  ∑_{i ∈ S_j} x_ji = u_j    ∀ j ∈ U

  // 3. Capacidad de tráfico de cada servidor instalado
  ∑_{j ∈ U: i ∈ S_j} (d_j * x_ji) <= T_i * y_i    ∀ i ∈ S
```

**Conteo de Variables y Restricciones**  
* **Variables:** |S| variables y_i + |U| variables u_j + ∑_j |S_j| variables de asignación x_ji.
* **Restricciones:** 1 de umbral + |U| de asignación + |S| de capacidad. Total: 1 + |U| + |S| restricciones.

---

### Ejercicio 40 — NP-Completitud del Problema de Asignación de Frecuencias

**Tipo:** Ejercicio generado a partir de patrones de parciales  
**Clasificación:** 🔴 IMPRESCINDIBLE  
**Paradigma:** Reducciones Polinomiales (K-Coloring a Asignación de Frecuencias)

**Enunciado**  
Se define el problema de **Asignación de Frecuencias (AF)** de la siguiente manera: Dado un conjunto de antenas de transmisión y una lista de pares de antenas que interfieren entre sí si transmiten en frecuencias cercanas, junto con un número entero de canales disponibles k, determinar si es posible asignar una frecuencia a cada antena de modo que ninguna antena adyacente comparta frecuencia. Demostrar formalmente que AF es un problema NP-Completo reduciendo desde **k-Coloring de Grafos**.

**Demostración Paso a Paso**

1. **Paso 1: AF ∈ NP:**
   * *Certificado:* Un vector C de tamaño n donde C[i] ∈ {1, ..., k} indica la frecuencia asignada a la antena i. Tamaño polinomial O(n).
   * *Verificador:* Recorre todas las aristas de interferencia (u, v). Si para alguna arista C[u] = C[v], retorna `NO`. Si todas son distintas, retorna `SI`. Tiempo: O(V + E) (polinomial). Por ende, **AF ∈ NP**.
2. **Paso 2: Problema Conocido:**  
   k-Coloring de grafos (k ≥ 3), conocido NP-Completo: *¿Se puede colorear G = (V, E) con a lo sumo k colores sin que dos vértices adyacentes compartan color?*
3. **Paso 3: Transformación Polinomial:**  
   Dada la instancia de k-Coloring (G = (V, E), k):
   * Cada vértice v ∈ V representa una antena.
   * Cada arista (u, v) ∈ E representa un par de antenas con interferencia mutua.
   * Los k colores corresponden a los k canales de frecuencia disponibles.
   * La transformación es la identidad estructural (f(G, k) = (G, k)) y se realiza en tiempo O(1).
4. **Paso 4: Equivalencia Bidireccional:**  
   * (⟹) Si G es k-coloreable, existe una partición de V en k clases independientes. Asignar la frecuencia c a todos los vértices de color c produce una asignación sin interferencias, pues no hay aristas entre vértices del mismo color.
   * (⟸) Si existe una asignación válida de k frecuencias sin interferencias, cada frecuencia define una clase de color donde ningún par de vértices adyacentes coincide. Esto define un k-coloreo válido para G.
5. **Conclusión:** AF es NP-Completo.
"""
