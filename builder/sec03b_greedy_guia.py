"""Módulo 3b: Algoritmos Greedy — Ejercicios de la Guía v1.0 (Ejercicios 19 al 38)."""

def get_content():
    return r"""### Ejercicio 19 — Envíos 1: Mochila por Valor y Peso

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.1

**Enunciado**  
Los hermanos Pill y Tipp montaron su empresa de envíos. Por viaje, su repartidora estrella puede llevar hasta cierto máximo de peso $P$. Tienen objetos con cierto peso y valor monetario. Diseñar un algoritmo greedy que les permita decidir qué objetos darle a su repartidora para maximizar las ganancias.

#### 1. Idea y Justificación en Lenguaje Natural

* **Criterio Voraz:** Para aprovechar al máximo cada kilo de capacidad, calculamos para cada objeto su **ganancia por kilo** (`valor / peso`) y los ordenamos de mayor a menor relación. Luego recorremos la lista metiendo cada objeto que todavía entre en el peso disponible.
* **¿Es óptimo?** Si los objetos no se pueden fraccionar (Mochila 0-1), este criterio es una **heurística aproximada** (no siempre da el óptimo porque puede quedar espacio libre desaprovechado; para asegurar al menos la mitad del óptimo podemos quedarnos con el máximo entre lo juntado y el objeto individual más valioso que entre).

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo EnviosMochilaGreedy(objetos, PesoMax):
    ordenar objetos por (obj.valor / obj.peso) de mayor a menor
    seleccionados = []
    peso_actual = 0

    para cada obj en objetos:
        si peso_actual + obj.peso <= PesoMax:
            agregar obj a seleccionados
            peso_actual = peso_actual + obj.peso

    devolver seleccionados
```

#### 3. Complejidad Temporal

* Ordenar los $n$ objetos cuesta **$O(n \log n)$** y recorrerlos cuesta $O(n)$. Total: **$O(n \log n)$**.

---

### Ejercicio 20 — Envíos 2: Jarras de Igual Valor con Peso y Volumen

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.2

**Enunciado**  
Las mercancías a entregar son jarras de pintura de laca que tienen un cierto volumen y peso, pero que **valen todas lo mismo**. El contenedor soporta hasta un máximo de peso $P$ y volumen $V$. Diseñar un algoritmo greedy para decidir cuáles jarras enviar maximizando la ganancia.

#### 1. Idea y Justificación en Lenguaje Natural

* Como todas las jarras dan la misma ganancia, **maximizar la ganancia equivale a meter la mayor cantidad posible de jarras**.
* Como tenemos dos límites distintos (peso $P$ y volumen $V$), para que una jarra sea comparable en ambas dimensiones medimos **qué porcentaje del contenedor ocupa** combinando su peso relativo y su volumen relativo: `ocupacion(i) = (peso_i / P) + (volumen_i / V)` (o el máximo de ambos porcentajes).
* Ordenamos las jarras de **menor a mayor ocupación** (las más "livianas y chicas" primero) y las vamos agregando mientras alcancen tanto el peso como el volumen restantes. (Es una heurística voraz en $O(n \log n)$).

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo EnviosJarrasGreedy(jarras, P_max, V_max):
    // Ordenar de menor a mayor consumo relativo de recursos
    ordenar jarras por ((j.peso / P_max) + (j.volumen / V_max)) ascendente
    elegidas = []
    p_usado = 0, v_usado = 0

    para cada j en jarras:
        si p_usado + j.peso <= P_max y v_usado + j.volumen <= V_max:
            agregar j a elegidas
            p_usado = p_usado + j.peso
            v_usado = v_usado + j.volumen

    devolver elegidas
```

---

### Ejercicio 21 — Envíos 3: Mochila con Peso, Volumen y Valor

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.3

**Enunciado**  
La repartidora exige ahora no superar un volumen máximo $V$ además del peso máximo $P$, teniendo cada objeto un peso, volumen y valor que pueden ser todos distintos. Modificar el algoritmo greedy para asignar los objetos.

#### 1. Idea y Justificación en Lenguaje Natural

* Ahora cada objeto aporta un `valor` distinto pero consume dos recursos limitados ($P$ y $V$).
* Definimos la **densidad combinada** de cada objeto dividiendo su valor por la fracción total de recursos que consume:
  $$\text{densidad}(i) = \frac{\text{valor}_i}{(\text{peso}_i / P) + (\text{volumen}_i / V)}$$
* Ordenamos de **mayor a menor densidad combinada** y agregamos cada objeto que quepa en ambos límites ($P$ y $V$). Su complejidad es **$O(n \log n)$**.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo MochilaPesoVolumenGreedy(objetos, P_max, V_max):
    ordenar objetos por (obj.valor / ((obj.peso / P_max) + (obj.volumen / V_max))) descendente
    elegidos = []
    p_usado = 0, v_usado = 0

    para cada obj en objetos:
        si p_usado + obj.peso <= P_max y v_usado + obj.volumen <= V_max:
            agregar obj a elegidos
            p_usado = p_usado + obj.peso
            v_usado = v_usado + obj.volumen

    devolver elegidos
```

---

### Ejercicio 22 — Envíos 4: Múltiples Repartidores (Bin Packing 1D)

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.4

**Enunciado**  
A cada repartidor se le puede asignar hasta cierto peso $P$ (igual para todos), y se envían cuantos repartidores hagan falta para enviar todos los ítems. Diseñar un algoritmo greedy que divida los ítems en la mínima cantidad de repartidores posible.

#### 1. Idea y Justificación en Lenguaje Natural

* Es el problema clásico de **Bin Packing**. Si dejamos los objetos pesados para el final, nos van a obligar a abrir repartidores nuevos. Por eso la mejor estrategia voraz es **First-Fit Decreasing (FFD)**:
  1. Ordenar los ítems de **mayor a menor peso** (los más difíciles de ubicar van primero).
  2. Por cada ítem, asignarlo al **primer repartidor ya activo** donde todavía entre; si no entra en ninguno, contratar un nuevo repartidor.
* Complejidad: **$O(n \log n + n \cdot R) = O(n^2)$** (o $O(n \log n)$ usando un árbol de búsqueda).

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo AsignarRepartidoresGreedy(items, P_max):
    ordenar items por peso de mayor a menor
    repartidores = []   // Lista de mochilas/repartidores activos

    para cada it en items:
        asignado = Falso
        para cada rep en repartidores:
            si rep.peso_actual + it.peso <= P_max:
                agregar it a rep
                rep.peso_actual = rep.peso_actual + it.peso
                asignado = Verdadero
                romper ciclo

        si no asignado:
            crear nuevo_rep con it y peso_actual = it.peso
            agregar nuevo_rep a repartidores

    devolver repartidores
```

---

### Ejercicio 23 — Envíos 5: Múltiples Repartidores con Peso y Volumen

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.5

**Enunciado**  
El sindicato fijó un máximo de peso $P$ y un máximo de volumen $V$ igual para cada repartidor. Modificar el algoritmo anterior para dividir todos los ítems minimizando la cantidad de repartidores.

#### 1. Idea y Justificación en Lenguaje Natural

* Extendemos **First-Fit Decreasing** a dos dimensiones: ordenamos los ítems de **mayor a menor tamaño relativo** `(peso / P) + (volumen / V)`, para acomodar primero los paquetes más aparatosos/pesados y rellenar los huecos libres de los repartidores con los paquetes chicos.
* Al intentar meter un ítem en un repartidor activo, verificamos que no supere ni $P$ ni $V$.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo RepartidoresMultivolumenGreedy(items, P_max, V_max):
    ordenar items por ((it.peso / P_max) + (it.volumen / V_max)) de mayor a menor
    repartidores = []

    para cada it en items:
        asignado = Falso
        para cada rep en repartidores:
            si rep.peso + it.peso <= P_max y rep.vol + it.vol <= V_max:
                agregar it a rep
                rep.peso = rep.peso + it.peso
                rep.vol = rep.vol + it.vol
                asignado = Verdadero
                romper ciclo

        si no asignado:
            crear nuevo_rep con it (peso = it.peso, vol = it.vol)
            agregar nuevo_rep a repartidores

    devolver repartidores
```

---

### Ejercicio 24 — Convención 1: Selección de Charlas Completas (CDEA 2027)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★☆☆☆☆ (1/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.6

**Enunciado**  
Camila quiere asistir a la mayor cantidad de charlas posible en la convención CDEA 2027. Una vez empezada una charla no se puede entrar ni salir hasta que finaliza. Tiene la lista con el horario de inicio y fin de cada charla. Diseñar un algoritmo greedy para organizar su agenda.

#### 1. Idea y Justificación en Lenguaje Natural

* Es el problema clásico de **Interval Scheduling**: para asistir a la mayor cantidad de charlas, nos conviene elegir siempre la charla compatible que **termine lo más temprano posible**, porque así liberamos nuestro tiempo cuanto antes para poder entrar a las siguientes.
* Es **100% óptimo** (demostrable por *Greedy Stays Ahead*) y tarda **$O(n \log n)$** por el ordenamiento.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo OrganizarAgendaCharlas(charlas):
    ordenar charlas por hora de fin de menor a mayor
    agenda = []
    ultimo_fin = -infinito

    para cada c en charlas:
        si c.inicio >= ultimo_fin:
            agregar c a agenda
            ultimo_fin = c.fin

    devolver agenda
```

---

### Ejercicio 25 — Convención 2: Charlas con Puntaje de Interés

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.7

**Enunciado**  
Diego asignó a cada charla un puntaje de interés además de sus horarios de inicio y fin. Diseñar un algoritmo greedy para organizar su agenda tratando de maximizar el puntaje total.

#### 1. Idea y Justificación en Lenguaje Natural

* **Regla Voraz:** Ordenamos las charlas por **mayor puntaje por hora** (`puntaje / (fin - inicio)`) o directamente por mayor puntaje, y vamos agregando toda charla que no se pise con las ya elegidas en nuestra agenda.
* **Aclaración clave de cátedra:** Con puntajes distintos, **ningún algoritmo Greedy garantiza el óptimo** (por ejemplo, una charla corta de densidad alta en el medio puede bloquear a dos charlas largas compatibles que juntas sumaban mucho más puntaje; el óptimo exacto requiere Programación Dinámica, ver Ejercicio 58).

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo AgendaConPuntajeGreedy(charlas):
    ordenar charlas por (c.puntaje / (c.fin - c.inicio)) de mayor a menor
    agenda = []

    para cada c en charlas:
        si c no se solapa con ninguna charla ya presente en agenda:
            agregar c a agenda

    devolver agenda
```

---

### Ejercicio 26 — Convención 3: Charlas Cortables (Al menos el 50% en cualquier tramo)

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.8

**Enunciado**  
En CDEA 2028 se permite entrar y salir de las charlas en cualquier momento. Camila quiere maximizar la cantidad de charlas a las que asiste, siempre y cuando pueda presenciar **por lo menos el 50% de la duración** de cada charla elegida. Diseñar un algoritmo greedy.

#### 1. Idea y Justificación en Lenguaje Natural

* Para cada charla $i$ con inicio $s_i$ y fin $f_i$, la duración mínima que Camila debe quedarse es la mitad: $d_i = (f_i - s_i) / 2$.
* Si estamos libres a partir del instante `t_actual`, ¿cuándo nos conviene entrar a una charla candidata? **Lo más temprano posible** (`inicio_real = max(t_actual, s_i)`), para cumplir el 50% requerido y **salir lo antes posible** en `fin_real = inicio_real + d_i` (siempre que `fin_real <= f_i`).
* Por lo tanto, en cada paso elegimos entre las charlas disponibles aquella que nos permita **salir más temprano** (menor `max(t_actual, s_i) + d_i`), o bien ordenamos inicialmente por el tiempo mínimo de salida `s_i + d_i` = punto medio de la charla.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo CharlasCortablesCamila(charlas):
    t_actual = 0
    agenda = []
    pendientes = copiar(charlas)

    mientras pendientes no esté vacío:
        mejor_charla = nulo
        mejor_salida = infinito

        para cada c en pendientes:
            mitad = (c.fin - c.inicio) / 2
            entrada = max(t_actual, c.inicio)
            salida = entrada + mitad
            // Es válida si llegamos a escuchar al menos el 50% antes de que termine
            si salida <= c.fin y salida < mejor_salida:
                mejor_salida = salida
                mejor_charla = c

        si mejor_charla es nulo:
            romper ciclo

        agregar (mejor_charla, mejor_salida - mitad, mejor_salida) a agenda
        t_actual = mejor_salida
        quitar mejor_charla de pendientes

    devolver agenda
```

---

### Ejercicio 27 — Convención 4: Entrar Antes de la Mitad y Quedarse hasta el Final

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.9

**Enunciado**  
Diego quiere entrar a cada charla en cualquier momento **antes de la mitad**, pero como le gusta hacer preguntas a los oradores, **quiere quedarse hasta el final** en cada charla a la que asiste. Todas las charlas le interesan por igual. Diseñar un algoritmo greedy óptimo.

#### 1. Idea y Justificación en Lenguaje Natural

* ¡Este problema tiene una reducción brillante! Como Diego quiere quedarse desde la mitad hasta el final sin falta, y entrar antes de la mitad solo le ocuparía tiempo extra sin necesidad, a Diego le conviene entrar **exactamente en la mitad de la charla** (`mitad_i = (inicio_i + fin_i) / 2`) y quedarse hasta `fin_i`.
* Entonces, **reemplazamos cada charla original $[inicio_i, fin_i]$ por su segunda mitad obligatoria $[mitad_i, fin_i]$**, y aplicamos el algoritmo clásico de *Interval Scheduling* (ordenar por `fin_i` ascendente). ¡Esto da la **solución 100% óptima** en tiempo **$O(n \log n)$**!

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo AgendaDiegoSegundaMitad(charlas):
    // 1. Transformar cada charla a su segunda mitad obligatoria [mitad, fin]
    ordenar charlas por c.fin de menor a mayor
    agenda = []
    ultimo_fin = -infinito

    para cada c en charlas:
        mitad = (c.inicio + c.fin) / 2
        // Si estamos libres antes o justo en la mitad de la charla, entramos
        si mitad >= ultimo_fin:
            agregar (c, desde = mitad, hasta = c.fin) a agenda
            ultimo_fin = c.fin

    devolver agenda
```

---

### Ejercicio 28 — Arquitecto 1: Cobertura de Puertas en el Aeropuerto

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.10 / Guía 02, Ejercicio 13

**Enunciado**  
La terminal A es un pasillo recto con puertas de abordaje. Se quiere colocar puestos de seguridad **en algunas de las puertas**, de modo que ninguna puerta quede a una distancia mayor de $d$ metros de algún puesto. Dado el arreglo con la ubicación de cada puerta en metros, diseñar un algoritmo que asigne la menor cantidad de puestos posible.

#### 1. Idea y Justificación en Lenguaje Natural

* Ordenamos las puertas de menor a mayor posición. Miramos la **primera puerta todavía no cubierta** (llamémosla $p_1$):
* Como el puesto debe instalarse **sobre alguna puerta existente** y cubrir a $p_1$, no nos conviene ponerlo en $p_1$ si podemos estirarnos más a la derecha: **avanzamos todo lo que podamos hacia la derecha hasta encontrar la puerta más lejana $p_k$ que esté a distancia $\le d$ de $p_1$** ($p_k \le p_1 + d$).
* Colocamos el puesto en esa puerta $p_k$. Ese puesto cubre automáticamente a $p_1$ y a todas las puertas subsiguientes hasta $p_k + d$. Saltamos a la primera puerta que supere $p_k + d$ y repetimos.
* Es **óptimo** (por *Greedy Stays Ahead*: cada puesto se ubica lo más a la derecha posible sin dejar descubierta a $p_1$) y tarda **$O(n \log n)$** (o $O(n)$ si las puertas ya vienen ordenadas).

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo CubrirPuertasTerminalA(puertas, d):
    ordenar puertas de menor a mayor
    n = longitud(puertas)
    puestos = []
    i = 0

    mientras i < n:
        puerta_descubierta = puertas[i]

        // 1. Buscar la puerta más a la derecha que aún cubra a puerta_descubierta
        mientras i + 1 < n y puertas[i + 1] <= puerta_descubierta + d:
            i = i + 1

        posicion_puesto = puertas[i]
        agregar posicion_puesto a puestos

        // 2. Saltar todas las puertas hacia la derecha que ya quedan cubiertas por este puesto
        mientras i < n y puertas[i] <= posicion_puesto + d:
            i = i + 1

    devolver puestos
```

---

### Ejercicio 29 — Arquitecto 2: Cobertura de Puertas usando Locales de Duty Free

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.11

**Enunciado**  
En la terminal B los puestos de seguridad solo pueden colocarse en los **locales libres del Duty Free**. Dado un arreglo con la ubicación de las puertas y otro con la ubicación de los locales libres, asignar la menor cantidad de puestos de seguridad para cubrir todas las puertas a distancia $\le d$.

#### 1. Idea y Justificación en Lenguaje Natural

* Es la misma lógica de estirarse lo más a la derecha posible, pero separando quién necesita cobertura (las `puertas`) de dónde podemos instalar (los `locales`):
  1. Ordenamos ambos arreglos (`puertas` y `locales`) de menor a mayor.
  2. Tomamos la primera puerta no cubierta $P$.
  3. Entre los locales libres que están a distancia $\le d$ de $P$ (es decir, locales $L$ tales que $P - d \le L \le P + d$), **elegimos el local $L^*$ que esté más a la derecha**. (Si no existe ningún local en ese rango, es imposible cubrir la puerta $P$).
  4. Instalamos el puesto en $L^*$ y marcamos como cubiertas todas las puertas hasta $L^* + d$.
* Es **óptimo** y su complejidad es **$O(n \log n + m \log m)$**.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo CubrirPuertasConLocales(puertas, locales, d):
    ordenar puertas de menor a mayor
    ordenar locales de menor a mayor
    puestos = []
    i = 0, j = 0   // i recorre puertas, j recorre locales

    mientras i < longitud(puertas):
        P = puertas[i]
        mejor_local = nulo

        // Avanzar por los locales buscando el más a la derecha que cubra a P
        mientras j < longitud(locales) y locales[j] <= P + d:
            si locales[j] >= P - d:
                mejor_local = locales[j]
            j = j + 1

        si mejor_local es nulo:
            devolver "Infactible: no hay local que cubra la puerta " + P

        agregar mejor_local a puestos

        // Saltar todas las puertas cubiertas por mejor_local
        mientras i < longitud(puertas) y puertas[i] <= mejor_local + d:
            i = i + 1

    devolver puestos
```

---

### Ejercicio 30 — Arquitecto 3: Stands Separados en Tablero Discreto

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.12

**Enunciado**  
En el Parque El Rectángulo (tablero de $n \times m$) se tienen marcadas las casillas donde pueden ir stands de comida. No se pueden colocar 2 stands a menos de dos casillas de distancia uno del otro (incluyendo en diagonal). Diseñar un algoritmo greedy que asigne la mayor cantidad de puestos posibles.

#### 1. Idea y Justificación en Lenguaje Natural

* "A menos de 2 casillas incluyendo diagonal" significa que si ponemos un stand en $(f, c)$, bloquea sus 8 casillas vecinas inmediatas (distancia de Chebyshev $< 2$, es decir, $|f_1 - f_2| \le 1$ y $|c_1 - c_2| \le 1$).
* Esto equivale a buscar un **Conjunto Independiente (Independent Set)** en el grafo de conflictos de las casillas candidatas.
* **Criterio Voraz (Menor Grado):** En cada paso elegimos la casilla candidata disponible que **bloquee a la menor cantidad de otras casillas candidatas vecinas** (la que tenga menos vecinos libres a distancia 1), colocamos un stand allí y tachamos sus casillas vecinas a distancia 1. (O recorremos de arriba-izquierda a abajo-derecha colocando siempre que sea válido).

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo AsignarStandsTablero(candidatas):
    stands = []
    libres = copiar(candidatas)

    mientras libres no esté vacío:
        // Regla voraz: elegir la casilla libre que bloquee a menos casillas libres vecinas
        elegir casilla c en libres con menor cantidad de vecinas en libres a distancia <= 1
        agregar c a stands

        // Eliminar a c y a todas las casillas a menos de 2 de distancia (|df| <= 1 y |dc| <= 1)
        para cada otra en libres:
            si max(|c.fila - otra.fila|, |c.col - otra.col|) < 2:
                quitar otra de libres

    devolver stands
```

---

### Ejercicio 31 — Arquitecto 4: Stands Separados en Espacio Continuo (Plaza Euclides)

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★☆☆☆ (2/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.13

**Enunciado**  
En Plaza Euclides los lugares posibles para stands vienen dados como coordenadas $(x, y)$, y la restricción es que no haya dos stands a menos de 5 metros uno del otro. Diseñar un algoritmo greedy para asignar la mayor cantidad de stands.

#### 1. Idea y Justificación en Lenguaje Natural

* Es exactamente el mismo problema de *Independent Set* que el ejercicio anterior, pero usando la **distancia euclídea** $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2} < 5$ para determinar si dos ubicaciones entran en conflicto.
* **Regla Voraz:** En cada paso seleccionamos el lugar candidato disponible que tenga **menor cantidad de otros candidatos libres a menos de 5 metros**, ponemos un stand ahí y descartamos todos los candidatos que estén a menos de 5 metros de él. Complejidad: **$O(n^2)$**.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo AsignarStandsEuclides(lugares):
    stands = []
    libres = copiar(lugares)

    mientras libres no esté vacío:
        // Elegir el punto libre que tenga menos vecinos a menos de 5 metros
        elegir p en libres que minimice cantidad de q en libres con distanciaEuclidea(p, q) < 5
        agregar p a stands

        // Descartar p y todos los puntos a menos de 5 metros
        para cada q en libres:
            si distanciaEuclidea(p, q) < 5:
                quitar q de libres

    devolver stands
```

---

### Ejercicio 32 — Arquitecto 5: Postas de Hidratación y Puntos Críticos

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.14

**Enunciado**  
Dadas las coordenadas 2D de los lugares candidatos para postas de hidratación y de los puntos críticos donde los turistas pasan tiempo al sol, diseñar un algoritmo greedy que ponga la menor cantidad de postas posibles de modo que todo punto crítico quede a distancia $\le d$ de al menos una posta. *(Nota: el enunciado dice coloquialmente "ningún punto crítico quede a menos de cierta distancia", refiriéndose a que ninguno quede desprotegido a más de distancia $d$).*

#### 1. Idea y Justificación en Lenguaje Natural

* Cada posta candidata cubre al subconjunto de puntos críticos que están a distancia euclídea $\le d$ de ella.
* Queremos cubrir todos los puntos críticos con la **menor cantidad de postas**: es el problema clásico de **Set Cover**.
* **Regla Voraz:** Mientras queden puntos críticos sin cubrir, elegimos la posta candidata que **cubra la mayor cantidad de puntos críticos que todavía no están cubiertos**, la instalamos y marcamos esos puntos como cubiertos. Complejidad: **$O(P \cdot C)$** donde $P$ es la cantidad de postas y $C$ la de puntos críticos.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo ColocarPostasHidratacion(postas, puntos_criticos, d):
    sin_cubrir = copiar(puntos_criticos)
    postas_elegidas = []

    mientras sin_cubrir no esté vacío:
        mejor_posta = nulo
        max_cubiertos = 0

        // Elegir la posta que cubra más puntos críticos aún descubiertos
        para cada p en postas:
            cubiertos_por_p = [ c en sin_cubrir tales que distancia(p, c) <= d ]
            si longitud(cubiertos_por_p) > max_cubiertos:
                max_cubiertos = longitud(cubiertos_por_p)
                mejor_posta = p

        si mejor_posta es nulo:
            devolver "Infactible: hay puntos críticos inalcanzables"

        agregar mejor_posta a postas_elegidas
        quitar de sin_cubrir todos los puntos a distancia <= d de mejor_posta

    devolver postas_elegidas
```

---

### Ejercicio 33 — Manager 1: Guardia Mínima Continua en el Spa

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.15

**Enunciado**  
Cada empleado del spa tiene un turno fijo corrido en la semana $[inicio_i, fin_i]$. Reggie quiere mantener al menos un empleado en el spa en todo momento durante toda la semana $[0, T]$, minimizando la cantidad total de trabajadores. Diseñar un algoritmo greedy óptimo.

#### 1. Idea y Justificación en Lenguaje Natural

* Es el problema canónico de **Interval Covering** (cubrir un intervalo $[0, T]$ con la menor cantidad de tramos):
  1. Llevamos una marca `cubierto_hasta` (inicialmente `0`, el inicio de la semana).
  2. Entre todos los empleados cuyo turno **empieza antes o justo en `cubierto_hasta`** ($inicio_i \le \text{cubierto\_hasta}$, para no dejar ningún hueco sin guardia), elegimos al empleado cuyo turno **termine lo más tarde posible** (mayor $fin_i$).
  3. Lo agregamos a la guardia, actualizamos `cubierto_hasta = fin_elegido` y repetimos hasta alcanzar el final de la semana $T$.
* **¿Es óptimo?** **Sí, 100% óptimo** (por *Greedy Stays Ahead*: en cada paso estiramos el horizonte cubierto lo máximo posible). Complejidad: **$O(n \log n)$** ordenando por hora de inicio.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo GuardiaMinimaSpa(empleados, InicioSemana, FinSemana):
    ordenar empleados por emp.inicio de menor a mayor
    guardia = []
    cubierto_hasta = InicioSemana
    i = 0, n = longitud(empleados)

    mientras cubierto_hasta < FinSemana:
        mejor_emp = nulo
        mayor_fin = cubierto_hasta

        // Entre todos los que entran a trabajar antes de que se quede vacío el spa,
        // elegir el que se quede hasta más tarde
        mientras i < n y empleados[i].inicio <= cubierto_hasta:
            si empleados[i].fin > mayor_fin:
                mayor_fin = empleados[i].fin
                mejor_emp = empleados[i]
            i = i + 1

        si mejor_emp es nulo:
            devolver "Infactible: queda un hueco sin cubrir en el spa"

        agregar mejor_emp a guardia
        cubierto_hasta = mayor_fin

    devolver guardia
```

---

### Ejercicio 34 — Manager 2: Guardia Mínima con Múltiples Turnos por Mesero

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.16

**Enunciado**  
En el bar de la pileta, cada mesero puede venir más de un día/horario a la semana (por ejemplo, lunes y miércoles de 8 a 14 y jueves de 12 a 18). Modificar el algoritmo para encontrar un subconjunto de meseros que mantenga la guardia cubierta minimizando la cantidad de meseros.

#### 1. Idea y Justificación en Lenguaje Natural

* Como cada mesero cubre **varios intervalos separados** en la semana, al elegir un mesero cubrimos varios bloques horarios a la vez. Esto transforma el problema en **Set Cover**:
* **Regla Voraz:** En cada paso miramos cuánto tiempo (cantidad de horas) de la semana que **todavía está sin cubrir** aporta cada mesero candidato, y elegimos al mesero que **cubra la mayor cantidad de horas aún descubiertas**, hasta completar toda la semana.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo GuardiaMinimaBarMultiturno(meseros, franjas_semana):
    sin_cubrir = copiar(franjas_semana)
    elegidos = []

    mientras sin_cubrir no esté vacío:
        // Elegir el mesero cuyos turnos cubran la mayor cantidad de horas aún en sin_cubrir
        elegir m en meseros que maximice horasCubiertas(m.turnos, sin_cubrir)
        si horasCubiertas(m.turnos, sin_cubrir) == 0:
            devolver "Infactible"

        agregar m a elegidos
        quitar de sin_cubrir todas las franjas cubiertas por m.turnos

    devolver elegidos
```

---

### Ejercicio 35 — Manager 3: Promoción de Supervisores en Recepción

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.17

**Enunciado**  
Cada empleado de recepción trabaja un único turno $[inicio_i, fin_i]$ en la semana. Reggie quiere promover a algunos empleados a "manager asistente" de modo que **todos los empleados de recepción compartan aunque sea una fracción de su turno con al menos un manager asistente** (un manager asistente se supervisa a sí mismo). Promover a la menor cantidad de empleados posible.

#### 1. Idea y Justificación en Lenguaje Natural

* Queremos elegir la menor cantidad de intervalos para que todo otro intervalo se cruce con al menos uno de los elegidos (*Dominating Set en Grafo de Intervalos*):
  1. Ordenamos los turnos por su **hora de finalización** de menor a mayor.
  2. Miramos al **primer empleado todavía no supervisado** $E_1$, cuyo turno termina en $f_1$. Para que alguien supervise a $E_1$, ese supervisor tiene que haber entrado a trabajar **antes de que $E_1$ se vaya** ($inicio_s \le f_1$).
  3. Entre todos los empleados que entran antes de $f_1$ (y que por lo tanto comparten turno con $E_1$), **promovemos a manager al que su turno termine lo más tarde posible ($f_s$ máximo)**. ¿Por qué? Porque al quedarse hasta más tarde, ese mismo manager supervisará también a la mayor cantidad posible de empleados siguientes.
  4. Marcamos como supervisados a todos los empleados cuyos turnos se crucen con el de este nuevo manager (los que empiezan antes de $f_s$), y repetimos con el próximo empleado no supervisado.
* Es **óptimo** y se ejecuta en **$O(n \log n)$**.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo PromoverSupervisores(empleados):
    ordenar empleados por emp.fin de menor a mayor
    managers = []
    i = 0, n = longitud(empleados)

    mientras i < n:
        // E1 es el empleado no supervisado que se va más temprano
        fin_limite = empleados[i].fin

        // Entre todos los empleados que comparten turno con E1 (inicio <= fin_limite),
        // elegir como manager al que termine su turno más tarde
        mejor_manager = empleados[i]
        para j desde i hasta n - 1:
            si empleados[j].inicio <= fin_limite y empleados[j].fin > mejor_manager.fin:
                mejor_manager = empleados[j]

        agregar mejor_manager a managers

        // Saltar todos los empleados que ya quedan supervisados por mejor_manager
        mientras i < n y empleados[i].inicio <= mejor_manager.fin:
            i = i + 1

    devolver managers
```

---

### Ejercicio 36 — Cambio 1: Monedas y Brazaletes de Rosario

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★☆☆☆☆ (1/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.18

**Enunciado**  
Existen cuentas/brazaletes con valores `1, 5, 10, 20, 50, 120`. Dado el valor de los ítems a vender y la cantidad de cuentas de cada tipo recibidas como pago, diseñar un algoritmo greedy que calcule cuántas cuentas de cada tipo dar de cambio minimizando la cantidad de cuentas.

#### 1. Idea y Justificación en Lenguaje Natural

* Primero sumamos el dinero total entregado por el cliente multiplicando la cantidad de cada cuenta por su valor, y le restamos el costo de los ítems para obtener el `vuelto` a devolver.
* **Regla Voraz del Cajero:** Recorremos las denominaciones de **mayor a menor** (`[120, 50, 20, 10, 5, 1]`) y de cada una entregamos la mayor cantidad entera posible (`vuelto // moneda`) sin pasarnos del vuelto restante.
* *(Nota de cátedra: Con la moneda de 120 y 50, para un vuelto de 150 el algoritmo voraz entrega `120 + 20 + 10` = 3 cuentas, que es igual de óptimo que `50 + 50 + 50` = 3 cuentas, porque 1, 5, 10, 20, 50, 120 es un sistema canónico).*

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo CalcularCambioCuentas(valor_items, pago_cuentas):
    denominaciones = [120, 50, 20, 10, 5, 1]
    total_pagado = sumatoria de (valor * cantidad) en pago_cuentas
    vuelto = total_pagado - valor_items
    cambio = []

    para cada mon en denominaciones:
        si vuelto >= mon:
            cant = division_entera(vuelto, mon)
            agregar (mon, cant) a cambio
            vuelto = vuelto % mon

    devolver cambio
```

---

### Ejercicio 37 — Cambio 2: Trueque por Valor Total Arbitrario

**Clasificación:** 🟡 IMPORTANTE  
**Dificultad:** ★☆☆☆☆ (1/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.19

**Enunciado**  
Modificar el algoritmo anterior para que, en vez de recibir la cantidad de cuentas de cada tipo dadas como pago, reciba directamente el valor entero positivo total ofrecido como pago en trueque y devuelva el vuelto a dar.

#### 1. Idea y Justificación en Lenguaje Natural

* Es aún más directo: restamos `vuelto = valor_pago - valor_items` en $O(1)$ y aplicamos exactamente el mismo ciclo voraz desde la moneda más grande (`120`) hasta la más chica (`1`). Como solo hay 6 denominaciones fijas, su complejidad es **$O(1)$**.

#### 2. Semi-Pseudocódigo Simplificado

```text
Algoritmo CalcularCambioTrueque(valor_items, valor_pago):
    denominaciones = [120, 50, 20, 10, 5, 1]
    vuelto = valor_pago - valor_items
    cambio = []

    para cada mon en denominaciones:
        si vuelto >= mon:
            cant = division_entera(vuelto, mon)
            agregar (mon, cant) a cambio
            vuelto = vuelto % mon

    devolver cambio
```

---

### Ejercicio 38 — Cambio 3: Reforma Monetaria de Verdania (Base Siempre Óptima)

**Clasificación:** 🔴 IMPRESCINDIBLE  
**Dificultad:** ★★★☆☆ (3/5)  
**Origen:** Guía v1.0 (Curso Echevarría), Ejercicio 2.20 (Bonus)

**Enunciado**  
En el reino de Verdania tenían un sistema monetario con la propiedad de que el algoritmo greedy para calcular el vuelto devolvía **siempre** el vuelto más eficiente en cantidad de monedas para cualquier monto. Encontrar una base monetaria que tenga esta propiedad y demostrarlo.

#### 1. Idea y Demostración en Lenguaje Natural

* **Base Monetaria Propuesta:** Tomamos las **potencias de 2** (o de cualquier base entera $b \ge 2$):
  $$M = \{1, 2, 4, 8, 16, \dots, 2^k\}$$
* **¿Por qué Greedy es SIEMPRE óptimo en esta base? (Demostración sencilla):**
  1. En cualquier solución óptima $OPT$, para cada moneda $2^i$ con $i < k$, **nunca puede haber 2 o más monedas iguales de valor $2^i$**, porque si hubiera dos monedas de $2^i$, las podríamos cambiar por una sola moneda de $2^{i+1}$ (que vale el doble: $2^i + 2^i = 2^{i+1}$), usando una moneda menos, lo cual contradiría que $OPT$ era óptima.
  2. Por lo tanto, cualquier solución óptima usa **a lo sumo 1 moneda** de cada valor $1, 2, 4, \dots, 2^{k-1}$.
  3. La suma máxima que se puede juntar con a lo sumo una moneda de cada una de las más chicas es:
     $$1 + 2 + 4 + \dots + 2^{k-1} = 2^k - 1 < 2^k$$
  4. Esto demuestra que **es imposible formar el valor $2^k$ usando las monedas más chicas en una solución óptima**. Así que siempre que el vuelto sea $\ge 2^k$, cualquier solución óptima está **100% obligada a usar la moneda más grande $2^k$**, exactamente igual que hace el algoritmo Greedy (de hecho, para $v < 2^{k+1}$ equivale a la descomposición binaria única del número). $\blacksquare$

---

### Errores Frecuentes en Exámenes sobre Greedy

1. **Afirmar que Greedy es óptimo sin demostrarlo:** Poner *"es óptimo porque siempre elijo lo mejor en cada paso"* es causal de pérdida total de puntos. Se debe presentar *Greedy Stays Ahead* o *Argumento de Intercambio*.
2. **Dar un contraejemplo sin números:** Un contraejemplo exige nodos, aristas y costos numéricos explícitos.
3. **No justificar por qué el algoritmo es voraz:** Se debe explicitar que la decisión es local, miope e irrevocable.
4. **Confundir Interval Scheduling con Interval Scheduling Ponderado:** Si las tareas tienen valores o beneficios distintos, ordenar por tiempo de fin no es óptimo.
"""
