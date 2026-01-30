# PocketCube
Proyecto satelital desarrollado por el grupo de investigación **SyCE** (Simulación y Cálculo de Campos Electromagnéticos).
## Objetivo
Instrutivo basico de para uso de app que interactua con ATtiny, permitiendo al usuario verificar su funcionamiento en tiempo real.
A su vez, se detalla funcionamiento interno de ATtiny de forma independiente y uso de la libreria **pocket.cpp** para interacturar con este.
## Aplicacion
![win_app](Imagenes_readme\app_init.png)
Se cuenta con 2 modos: manual y ensayos.
Para iniciar en cualquier de los 2, se debe seleccionar un puerto COM, de no ser el de Arduino no se recibira respuesta alguna. Ya que se envia (queries) y capturan (request) en formatos especificos.

`Query :  [CMD_Arduino], [CMD]`

`Request: [id_widget], [data1] [data2] [...] `

|id_widget| Descripcion |
|---------|-------------|
|SEND_CPS_APP| Carga datos en tabla y grafico de CPS
|SEND_CPM_APP| Carga datos en tabla y grafico de CPM
|SEND_LINE_APP| Carga datos en Qline respuesta directa del ATTiny

|CMD_Arduino| Descripcion |
|---------|-------------|
|CMD_I2C| Indica al Arduino de enviar solicitud por I2C

Los CMD se detalla a cotinuacion para cada modo (manual / ensayo)

### Modo manual
Se inicia al instante de abrir la app, solo si se cuenta con un puerto COM disponible. Permitiendo al usuario enviar comandos especificos (CMD) al puerto COM con los botones.

| Comando (CMD)| Boton asociado   | Request                          | Formato request |
|--------------|------------------|----------------------------------|-----------------|
| CPS_NOW_ACCUM|    CPS actual    | CPS acumulados durante ese minuto| [id_widget], [CPS_NOW_ACCUM]
| CPM          |     Último CPM   | Último CPM registrado por ATtiny | [id_widget], [CPM]
| TIME         |       TIME       |  Tiempo de ATtiny en segundos    | [id_widget], [TIME]


Al final de esta seccion, en la APP, se podra visualizar la respuesta del ATtiny. En este ejemplo se solicito estado del contador actual en el ATtiny.

![Terminal_request](Imagenes_readme\request_terminal.png)

### Modo ensayo
Determinado un tiempo de ensayo **[HH]:[MM]** se pulsa *Iniciar* y arranca este modo, con una cierta demora en la primera consulta.   
![Modo_ensayo_menu](Imagenes_readme\modo_ensayo_menu.png)

En este modo se manda los mismos CMD que en *Modo manual* con la salvedad que es de forma automatica, cada cierto periodo:
| Comando (CMD)| Periodo de consultas  | Request | Formato request |
|--------------|-----------------------|---------|-----------------|
| CPS_TIME     | cada 1 segundo        |Último CPS medido y tiempo de ATtiny en seg.| [id_widget], [CPS] [TIME]
| CPM_TIME     | cada 60 segundos      |Último CPM medido y tiempo de ATtiny en seg.| [id_widget], [CPM] [TIME]

La duracion del ensayo se puedo visualizar en la app y al finalizar este se permite exportar los registros en formato .csv. A su vez, se permite forzar la finalizacion del ensayo de ser necesario.

***ACLARACION:** solo quedan en el .csv aquellos datos que se ven visualmente en la app, puede estar el caso particular que algun dato demore mas de 1segundo y se pierda, ya que la comunicacion es por streaming. Para eso se cuenta con la columna **Seg.** en la tabla que deja explicito el segundo que van realmente contando el ATTiny.*

Los archivos .csv se guardan en la carpeta `LogBG5` del escritorio, con el siguiente formato:  
 `"{id_name}_{datetime}.csv"`  
por ejemplo: `CPS_2026-01-29_11-09-52` y `CPM_2026-01-29_11-09-52`  

***ACLARACION:** No es necesario crear la carpeta, de no existir la APP creara la carpeta*

## Funcionamiento de ATtiny
El ATtiny es independiente a cualquier otro dispositivo, es decir, que con alimentacion procede a la realizar la lectura de pulsos (del sensor BG51) y registro de estos en su memoria interna. Este espera que algun otro dispositivo, por I2C, le realize las solicitudes deseadas para responder con las mediciones almacenadas. 

![Attiny](Imagenes_readme\ATtiny_funcionamiento.png)

**Direccion I2C Attiny85 :** 0x08   
**Timer ISR:** cada 1 segundo    
**PCINT ISR:** detecta pulso al cambiar de estado ascendente en pin PB3

Funcionamiento de TIMER:

| TIMER | ATtiny | contador | 
|-------| -----| ------
|0     | ---   | 0
|1     | Actualiza CPS | 1
|2     | Actualiza CPS | 2
|60 | Actualiza CPM y resetea CPS | 0
|100| Actualiza CPS | 40
|120| Actualiza CPM y resetea CPS | 0
 
***OBS.:** El pin PB3 por PCINT detecto los cambio de flanco ascendete, durante 1 segundo, el TIMER indica cuando actualizar las variables acorde a los pulsos detectados en PB3*

## Ejemplo de libreria Pocket
Para poder realizar consultas al ATtiny se debe conoces la estructura que reconoce las solcicitudes por I2C. Para simplificar esto se cuenta con la libreria `Pocket.cpp` que facilita su comunicación utilizando solo los CMD (comandos) e incluyendo la lectura e interpretacion de estos por terminal.
![Ejemplo](Imagenes_readme\Ejemplo_libreria_pocket.png)

Se cuenta con 2 fucniones principales: `request(const uint8_t)` y `requestFromAppUart(int*, int*)`  

> **requestFromAppUart(ID solicitud, CMD)**: Filtra solicitud a Arduino y CMD para Attiny   
> **requestI2C(CMD)**: Verifica si es un CMD valido y envia request por UART  

Para uso en otros dispositivos bastara con usar `request(const uint8_t)`, el cual envia el CMD con la estructura: `[CMD Arduino],[CMD ATtiny]` por ejemplo: `[CMD_I2C],[CPS_NOW]` 

|CMD           | Uso                      | Query por I2C  |Request por I2C (ejemplo)|Interpretacion request (ejemplo)
|--------------|--------------------------|----------------| ------------------------|-------------------------------------
|CPM           |Solicita ultimo CPM       |1,1             |1,85                     |Detecto 85 pulsos en el ultimo minuto
|CPS_NOW       |Solicita CPS en ese minuto|1,2             |1,148                    |Detecto 148 pulsos durante este segundo
|TIME          |Solicita valor de contador en ATtiny|1,3   |1,27                     |Contador de ATtiny en segundo 27
|CPS_NOW_ACCUM |Solicita ultimo CPM       |1,4             |1,258           |Detecto 258 pulsos hasta el momento en el intervalo de 1 minuto
|CPS_TIME      |Solicita ultimo CPM       |1,5             |1,258 25        |Detecto 258 pulsos hasta el segundo 25
|CPM_TIME      |Solicita ultimo CPM       |1,6             |1,85 32         |Han pasado 32 segundo del ultimo minuto donde se detecto 85 pulsos

