# PocketCube
Proyecto satelital desarrollado por el grupo de investigación **SyCE** (Simulación y Cálculo de Campos Electromagnéticos).

## Funcionamiento de la Aplicación
La aplicación se encarga de monitorear las lecturas provenientes de los **2 pines de entrada** habilitados en el **ATtiny85** (Carga Útil).

### Características de la Aplicación
- **Ventanas de monitoreo**: La aplicación cuenta con dos ventanas, una para cada pin del ATtiny85:
  - **Pin PB3**
  - **Pin PB4**
  
- **Recepción de datos**: La aplicación solo presenta los datos procesados y enviados por el **Arduino UNO** (Pocket Main) a través del puerto serial.

## Pocket Main
### Comunicación I2C con la Carga Útil
Se utiliza el protocolo **I2C** para la comunicación entre el **Arduino UNO** (Pocket Main) y la **Carga Útil** (ATtiny85).

### Procesamiento de datos
El **Arduino UNO** es responsable de recibir, procesar y enviar los datos provenientes de la Carga Útil a la aplicación.

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
