# Proyecto padre : PocketCube
Proyecto satelital desarrollado por el grupo de investigación **SyCE** (Simulación y Cálculo de Campos Electromagnéticos).

# Proyecto modular : Carga útil
El proyecto padre cuenta con varios módulos de que se combinan en un único producto final. En este módulo se abarca la **Carga útil**, el cual consta de un sensor BG51 del cual se adquieren datos por medio de un Attiny85 y transmitidos al módulo principal por I2C.

El Attiny85 opera contando pulsos por PCINT que a diferencia de los ISR son menos precisos. Se tuvo que recurrir a estos, debido a las limitaciones fisicas del Attiny85 se comparten pines con I2C, generando problemas de comunicación.

| Pin ATtiny85 | Tipo de pin   | Modo de operación | Función  |
|--------------|---------------|-------------------|----------|
| PB3          | PCINT3        | CHANGE            | MEAS1    ||


## Funcionamiento de la App
La aplicación se encarga de monitorear la lectura de pulsos registrados por segundo (**CPS**) del BG51 interpretados por el Attiny85.

Contando con herramientas para establecer una ventana de tiempo (en segundos) para registrar los datos. 

*Por ejemplo: si se establece una ventana de tiempo de 7 segundos, el Attiny85 enviara al modulo principal cada 7 segundos el total de CPS registrados.*

Para asegurar tiempos de ensayo se cuenta con el tiempo de ensayo, el cual permite al operador establecer un tiempo limite de para cada ensayo. 

*Por ejemplo: Si se selecciona 2 minutos de ensayo y una ventana de tiempo de 7 segundos, el Attiny respondera cada 7 segundos con los CPS totales, hasta que se cumplan los 2 minutos, sin importar que haya la ultima lectura no disponible (por no cumplirse los 7 segundos)*


## Prototipo modular para ensayos
Este *poncho* fue desarrollado especificamente para el Arduino UNO R3, con los componentes que se utilizarán en el módulo final. 

*ACLARACIÓN: en una anterior oportunidad se probo con el modelo SMD del Attiny85 pero no se obtuvo los resultados esperados como si lo fueron en su formato SOIP*

### Desarrollo de poncho

El poncho cuenta con varias etapas que cumplen diferentes roles.

**Alimentación:** Se utilizan los 5VDC disponibles del Arduino para el regulador de tensión de 3.3VDC para todo el circuito del poncho. La única excepción es la alimentación de sensor BG51 que cuenta con una etapa previa de filtrado, como indica el fabricante para evitar medidas erroneas.

**Adaptador de nivel:** actuaLmente *NO UTILIZADO*, ya que no hubo incovenietes con el Arduino UNO R3 pero se deja en el PCB como medida de seguridad.

**Comunicación:** Se cuenta con 3 tipos, por UART, I2C y SPI. 
 - UART esta deshabiltado por software, sólo están disponibles los pines por si llega a una instancia que desea saber el estado del Attiny85 sin utilizar como intermediario al Arduino UNO R3. 
 - I2C habilitado para transmitir lectura procesadas por el Attiny85 al Arduino UNO R3.

    | Attiny85 | Arduino UNO  | Función  |
    |----------|--------------|----------|
    | PB0      | A4           | SDA      |
    | PB2      | A5           | SCL/SCK  |

    *ACLARACIÓN: se agregaron resistencias de pull-up externas, sin importar que el ARDUINO UNO R3 ya cuente con estos, pensando en el módulo final.*

 - SPI utilizado para debuggear Attiny85 por medio del Arduino UNO R3, para esto hay que tener en cuenta la siguiente conexión (utilizando un cable externo):

    | Poncho | Arduino UNO   | Función  |      Descripción    |
    |--------|---------------|----------|---------------------|
    | 1      | 10            | SS       | Slave Select        |
    | 2      | 11            | MOSI     | Master Out Slave In |
    | 3      | 12            | MISO     | Master In Slave Out |
    | 4      | 13            | SCK      | Serial Clock        |

    *ACLARACIÓN: fue diseñado de esta forma considerando que luego se utilizara otra placa que no sea el Arduino UNO R3 en el modelo final*
