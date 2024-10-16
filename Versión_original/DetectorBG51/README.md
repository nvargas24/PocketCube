# DetectorBG51

El **DetectorBG51** es un sensor que se utiliza en **Laboratorios Bacon** para la 
detección radiación por medio de la detección de pulsos cada 5 segundos. 
Para esto se implementa un contador utilizando interrupciones (ISR) y muestra 
el promedio de los pulsos detectados y maxima cantidad en una pantalla LCD.

## Descripción General

El sistema realiza la detección de pulsos y almacena los valores en un array, 
realizando un promedio sobre los primeros valores. El tiempo de muestreo es 
de 1 segundo, y cada 5 segundos se calcula el promedio de pulsos por segundo (cps) 
en base a las primeras muestras.

### Variables Principales
- `mostrar`: Habilita la visualización de los datos tanto por la terminal como en la LCD.
- `det1`: Pin de entrada digital para la detección de pulsos.
- `pulsos1`: Contador que registra los pulsos detectados.
- `deCPS1[10]`: Array que almacena los pulsos detectados por cada segundo.
- `x`: Índice que indica la posición actual en el array.
- `cps1`: Promedio de las primeras 5 muestras almacenadas en `deCPS1[10]`.
- `cpsMax`: Valor máximo del promedio de pulsos, inicializado en 0.

## Funcionamiento

1. Los pulsos se detectan mediante el pin digital configurado como entrada.
2. Cada segundo, el sistema almacena el número de pulsos en el array `deCPS1[x]`.
3. Cada 5 segundos, el sistema realiza el promedio de las primeros 5 valores almacenados y lo muestra en la pantalla LCD y en la terminal, si está habilitada la variable `mostrar`.
4. El valor máximo del promedio (`cpsMax`) se actualiza si se detecta un nuevo valor más alto.

## Diagrama Funcional

* [Incluir imagen de diagrama en bloques aquí]*

## Ejemplo de Funcionamiento

| Timer [s] | x | decCPS1[0] | decCPS1[1] | decCPS1[2] | decCPS1[3] | decCPS1[4] | cps1 | state         |
|-----------|---|------------|------------|------------|------------|------------|------|---------------|
| 0         | 0 | 0          | 0          | 0          | 0          | 0          | 0    |Init           |
| 1         | 0 | 7          | 0          | 0          | 0          | 0          | 1.4  |Meas           |
| 2         | 1 | 7          | 3          | 0          | 0          | 0          | 2    |Meas           |
| 3         | 2 | 7          | 3          | 2          | 0          | 0          | 2.4  |Meas           |
| 4         | 3 | 7          | 3          | 2          | 9          | 0          | 4.2  |Meas           |
| 5         | 4 | 7          | 3          | 2          | 9          | 5          | 5.2  |Meas/Reset x   |
| 6         | 0 | 1          | ***3**     | ***2**     | ***9**     | ***5**     | 4   |Meas           |
| 7         | 1 | 1          | 7          | ***2**     | ***9**     | ***5**     | 4.8 |Meas           |
| 8         | 2 | 1          | 7          | 1          | ***9**     | ***5**     | 4.6 |Meas           |
| 9         | 3 | 1          | 7          | 1          | 2          | ***5**     | 3.2 |Meas           |
| 10        | 4 | 1          | 7          | 1          | 2          | 9          | 4    |Meas           |

El valor de `cps1` representa el promedio de los pulsos por segundo basado en las últimas 5 muestras almacenadas en el array `deCPS1[]`.
