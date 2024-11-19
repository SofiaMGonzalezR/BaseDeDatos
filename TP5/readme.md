# TP5: Proceso de Normalización
Realizacion de Ejecicio N3

## Esquema Original

El esquema inicial modela la relación entre los programas de radio, las frecuencias, los conductores y los gerentes:

**PROGRAMA(radio, año, programa, conductor, gerente, frecuencia_radio)**

### Restricciones del Enunciado:

1. Una radio se transmite por una única frecuencia en un año determinado, aunque puede cambiarla en años diferentes.
2. Cada radio tiene un único gerente por año. Sin embargo, un gerente puede repetirse en la misma radio en diferentes años o gestionar varias radios en el mismo año.
3. Un mismo programa puede transmitirse en varias radios y en diferentes años.
4. Un programa transmitido en una radio en un año tiene un único conductor.

---

## Dependencias Funcionales (DFs)

### Análisis:
Con base en las restricciones del enunciado:

1. `(radio, año)` → `frecuencia_radio`  
   Una radio tiene una única frecuencia por año.

2. `(radio, año)` → `gerente`  
   Cada radio tiene un único gerente por año.

3. `(radio, año, programa)` → `conductor`  
   Un programa específico, transmitido en una radio en un año, tiene un único conductor.

---

## Claves Candidatas

Con base en las DFs, la única clave candidata que identifica de forma única cada registro es:  
**(radio, año, programa)**.

---

## Clave Primaria Elegida

Seleccionamos la clave **(radio, año, programa)** como clave primaria, ya que permite identificar de forma única cada programa en una radio en un año específico.

---

## Proceso de Normalización

### Forma Normal 1 (1FN)

El esquema original ya cumple con la 1FN, ya que:
- Todos los atributos son atómicos.
- No existen grupos repetitivos ni datos multivaluados.

---

### Forma Normal 2 (2FN)

Para alcanzar la 2FN, eliminamos las dependencias funcionales parciales, descomponiendo el esquema en dos tablas:

1. **RADIO_AÑO(radio, año, frecuencia_radio, gerente)**  
   - Esta tabla contiene los atributos dependientes exclusivamente de `(radio, año)`.

2. **PROGRAMA_RADIO(radio, año, programa, conductor)**  
   - Esta tabla contiene los atributos dependientes de `(radio, año, programa)`.

Ahora, ambas tablas cumplen la 2FN, ya que cada atributo no clave depende completamente de la clave primaria.

---

### Forma Normal 3 (3FN)

Para alcanzar la 3FN, eliminamos las dependencias funcionales transitivas. En este caso, no existen dependencias transitivas en las tablas descompuestas. Por lo tanto, ambas cumplen con la 3FN.

---

## Esquema Final

El esquema normalizado queda de la siguiente forma:

1. **RADIO_AÑO(radio, año, frecuencia_radio, gerente)**  
   - Clave primaria: `(radio, año)`  
   - Dependencias funcionales: `(radio, año) → frecuencia_radio`, `(radio, año) → gerente`.

2. **PROGRAMA_RADIO(radio, año, programa, conductor)**  
   - Clave primaria: `(radio, año, programa)`  
   - Dependencia funcional: `(radio, año, programa) → conductor`.

---

## Justificación

1. **Descomposición basada en dependencias funcionales:**  
   La tabla inicial fue descompuesta según las DFs identificadas. La separación asegura que cada tabla representa un conjunto de datos único y no redundante.

2. **Claves primarias:**  
   Se eligieron claves que identifican de manera única cada registro en sus respectivas tablas.

3. **Cumplimiento de formas normales:**  
   Las tablas finales cumplen con 3FN, eliminando redundancias y garantizando la integridad referencial.

---

## Diagrama del Esquema

![Esquema de Tablas](./ejer_3.svg)
