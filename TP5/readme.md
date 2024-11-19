# TP5: Proceso de Normalización

## Esquema original

**PROGRAMA(radio, año, programa, conductor, gerente, frecuencia_radio)**

### Dependencias Funcionales:

1. (radio, año) → frecuencia_radio
2. (radio, año) → gerente
3. (radio, año, programa) → conductor

### Claves Candidatas:

- (radio, año, programa)

### Clave Primaria Elegida:

- (radio, año, programa), ya que identifica de forma única cada registro.

## Proceso de Normalización

### 1FN:

- La tabla ya cumple con 1FN.

### 2FN:

- Descomposición:
  1. **RADIO_AÑO(radio, año, frecuencia_radio, gerente)**
  2. **PROGRAMA_RADIO(radio, año, programa, conductor)**

### 3FN:

- Ambas tablas cumplen 3FN, ya que no hay dependencias funcionales transitivas.

## Esquema Final:

1. **RADIO_AÑO(radio, año, frecuencia_radio, gerente)**
2. **PROGRAMA_RADIO(radio, año, programa, conductor)**

## Tabla final:

![tabla](./ejer_3.svg)
