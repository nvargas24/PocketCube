# PocketCube
Proyecto satelital desarrollado por el grupo de investigación **SyCE** (Simulación y Cálculo de Campos Electromagnéticos).

## Funcionamiento de la Aplicación
La aplicación se encarga de monitorear las lecturas provenientes de los **2 pines de entrada** habilitados en el **ATtiny85** (Carga Útil).

### Características de la Aplicación
![win_app](Imagenes/win_app.jpg)
- **Selección de puerto**: Se identifican los dispositivos conectados al ordenador, el usuario debe seleccionar el correspondiente al Arduino UNO (Pocket Main)

- **Recepción de datos**: Solo se presentan los datos procesados y enviados por el **Arduino UNO** (Pocket Main) a través del puerto serial. 

- **Ventanas de monitoreo**: Se cuenta con dos ventanas, una para cada pin del ATtiny85:
  - **Pin PB3** -> **Pin ISR**
  - **Pin PB4** -> **Pin ADC**
  
- **Indicación de estado**: en forma simple el Arduino puede indicar algun estado en particular
  - **Read EEPROM**: Lectura de memoria EEPROM
  - **Clear EEPROM**: Vacio de memoria EEPROM
  - **Read MEAS**: Lectura de datos matcheados con RTC
  - **Error**: Estado particular cuando no se reonoce ID

- **Tabla de registro de datos**: Pariticularmente sólo presenta los datos recibidos en un formato extendido (ver ##Pocket Main ###Procesamiento de datos) identificando por ID, mostrando tanto sus descripción como el datetime del instante que se recibio.

- **Barra de espacio de memoria**: Indica el espacio de la memoria EEPROM
- **Displays LCD**: Se cuenta con 2 display para mostrar tiempos
  - **Display 1**: Muestra la marca de tiempo del TIMER del ATtiny85
  - **Display 2**: Muestra tiempo real recibido por el RTC.

## Pocket Main
### Comunicación I2C con la Carga Útil
Se utiliza el protocolo **I2C** para la comunicación entre el **Arduino UNO** (Pocket Main) y la **Carga Útil** (ATtiny85).
  - **Pin PB0** -> **Pin A4** -> **SDA**
  - **Pin PB2** -> **Pin A5** -> **SCL/SCK**

### Procesamiento de datos
El **Arduino UNO** es responsable de recibir, procesar y enviar los datos provenientes de la Carga Útil a la aplicación.
Los datos se muestran en uno de los siguientes formatos para optimizar tramas de datos:
  - **Formato simple**: `{ID},{value}`
  - **Formato extendido**: `{ID},{datetime} {value1} {value2}`

  ### Asignación de IDs
  Para simplificar la identificación de los diferentes datos, se han asignado los siguientes **ID**:

  | ID    | Descripción     |
  |-------|-----------------|
  | 1     | MEAS1           |
  | 2     | MEAS2           |
  | 3     | RTC             |
  | 4     | EEPROM_USED     |
  | 5     | EEPROM_DATA     |
  | 6     | STATE           |

  Estos formatos permiten identificar fácilmente el origen de los datos (`ID`) y el valor asociado (`value`). En el formato extendido, se incluye además información adicional como la marca de tiempo (`datetime`) y múltiples valores (`value1`, `value2`).
  
## Carga Útil con ATtiny85
La Carga Útil opera con dos modos, seleccionables según la necesidad: **Modo ISR** (PB3) y **Modo ADC** (PB4).

- **Recomendación**: Aunque es posible utilizar ambos pines simultáneamente, no se recomienda hacerlo debido a la falta de una correcta aislación, lo que puede generar efectos de carga u otros fenómenos indeseables. Por lo tanto, es preferible no conectar la misma entrada en ambos pines.

### Modo ISR
En este modo, el pin **PB3** del ATtiny85 está configurado como interrupción por flanco ascendente (**RISING**).

### Modo ADC
En este modo, el pin **PB4** del ATtiny85 está configurado para conversión analógica-digital (**ADC**), con las siguientes características:
- **Resolución**: 10 bits
- **Frecuencia de muestreo**: Hasta 1kHz

---

# Esquemáticos de Conexión

## Pinout de I2C para Arduino Uno y ATtiny85

Esta sección proporciona una descripción del pinout I2C en el **Arduino Uno** y el **ATtiny85**.

### Arduino Uno

El **Arduino Uno** utiliza los siguientes pines para la comunicación I2C:

- **SDA (Data):** Pin A4
- **SCL (Clock):** Pin A5

![Pinout Arduino Uno I2C](Imagenes/arduino_uno_pinout.avif)

Estos pines están conectados internamente al módulo TWI (Two Wire Interface) del microcontrolador.

### ATtiny85

El **ATtiny85** utiliza los siguientes pines para la comunicación I2C:

![Attiny85 Pinout](Imagenes/attiny85_pinout.jpeg)

---

# Montaje de Ponchos

Esta sección describe el montaje de los ponchos para conectar los componentes del PocketCube.

---

# Pruebas Reales

Aquí se documentarán los resultados de las pruebas realizadas con el sistema en condiciones reales de funcionamiento.


## Referencias

Para más información, consulta la documentación oficial de [attitny85](https://www.microchip.com/en-us/product/attiny85) y [Arduino Uno](https://www.arduino.cc/en/Main/ArduinoBoardUno).
