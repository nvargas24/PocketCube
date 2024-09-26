"""
vista.py:
    Módulo encargado de generar la interfaz gráfica de la app. 
"""
__author__ = "Nahuel Vargas"
__maintainer__ = "Nahuel Vargas"
__email__ = "nahuvargas24@gmail.com"
__copyright__ = "Copyright 2024"
__version__ = "0.0.1"

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib

import numpy as np

from modelo import *

from Qt.simulation_load import *

#--- ID
MEAS1 = 1
MEAS2 = 2
RTC = 3
EEPROM_FREE = 4
EEPROM_DATA = 5
STATE = 6

NAME_MEAS1 = "Meas1"
NAME_MEAS2 = "Meas2"

TIMEOUT = 10

class Graph_volt(FigureCanvas):
    def __init__(self):
        self.xlim_init = 0
        self.xlim_fin = 15
        self.ylim_init = -1
        self.ylim_fin = 6

        # Indicador en grafico
        self.flag_send = False

        # Inicializo grilla
        self.grid_lines_v = []
        self.grid_lines_h = []

        self.fig, self.ax = plt.subplots(1, dpi=82, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.18, bottom=.2, right=.95, top=.95) #Ajuste de escala de grafica
        super().__init__(self.fig)

        self.set_graph_style()

        # Listas para cargar datos
        self.x_data = []
        self.y_data = []

        # Crear la línea inicial
        self.line, = self.ax.plot([], [], picker=5)

        #self.test_graph()
        #self.draw()

    def test_graph(self):
        # Generar datos de ejemplo
        voltaje = np.linspace(0, 4, 10)  # Voltaje en voltios (V)
        corriente = np.linspace(0, 1, 10)  # Corriente en amperios (A)
        potencia = voltaje * corriente  # Potencia en vatios (W)

        # Encontrar el punto de máxima potencia
        indice_max_potencia = np.argmax(potencia)
        voltaje_mpp = voltaje[indice_max_potencia]
        corriente_mpp = corriente[indice_max_potencia]
        potencia_mpp = potencia[indice_max_potencia]

        # Graficar potencia vs voltaje
        self.ax.plot(voltaje, potencia, label='Potencia vs Voltaje', color='blue', linewidth=2.5)

        # Marcar el punto MPP
        self.ax.scatter(voltaje_mpp, potencia_mpp, color='red', zorder=2, label='MPP')

    def update_graph(self, new_y_value):
        """
        Metodo para actualizar grafico
        """
        # Generar nuevo valor de datos
        if self.x_data:
            next_x = self.x_data[-1] + 1
        else:
            next_x = self.xlim_init

        self.x_data.append(next_x)
        self.y_data.append(new_y_value)

        # Actualizar datos de la línea
        self.line.set_data(self.x_data, self.y_data)

        # Marca punto en grafico
        if self.flag_send:
            self.ax.scatter(next_x, new_y_value, c='red', s=10, alpha=0.8, picker=True, zorder=2)
            self.flag_send = False

        # Ajustar los límites si es necesario
        if next_x >= self.xlim_fin:
            self.xlim_fin = next_x+1
        
        self.set_graph_style()

        self.draw()

    def set_graph_style(self):
        """
        Metodo que asigna estilo al grafico
        """
        # Eliminar las líneas de la grilla existentes
        for line in self.grid_lines_v:
            line.remove()
        for line in self.grid_lines_h:
            line.remove()

        self.grid_lines_v.clear()
        self.grid_lines_h.clear()

        # Establece nombres de ejes y tamanio
        matplotlib.rcParams['font.size'] = 10
        self.ax.set_xlabel("Time[s]", labelpad=1)
        self.ax.set_ylabel("ADC[V]", labelpad=1)
        self.ax.tick_params(axis='both', which='both', labelsize=7)
   
        # Establecer límites del eje X e Y
        self.ax.set_xlim(self.xlim_init, self.xlim_fin)
        self.ax.set_ylim(self.ylim_init, self.ylim_fin)

        # Creo grilla
        step_value_x = round((self.xlim_fin-self.xlim_init)/20)
        step_value_y = round((self.ylim_fin-self.ylim_init)/10)

        for i in range(self.xlim_init, self.xlim_fin, step_value_x):
            line = self.ax.axvline(i, color='grey', linestyle='--', linewidth=0.25)
            self.grid_lines_v.append(line)

        for j in range(self.ylim_init, self.ylim_fin, step_value_y):   
            line = self.ax.axhline(j, color='grey', linestyle='--', linewidth=0.25)
            self.grid_lines_h.append(line)


        # set colores bordes
        self.ax.spines['bottom'].set_color('0.7')  # Eje x
        self.ax.spines['left'].set_color('0.7')   # Eje y
        self.ax.spines['top'].set_visible(False)    # Oculta el borde superior
        self.ax.spines['right'].set_visible(False)  # Oculta el borde derecho
        
        # set colores ejes
        self.ax.tick_params(axis='x', colors='0.4')  # Cambia el color de los valores en el eje x
        self.ax.tick_params(axis='y', colors='0.4') # Cambia el color de los valores en el eje y

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Simulador - Grupo SyCE UTN-FRH")

        self.setFixedSize(930, 720)
        #self.setWindowIcon(QIcon(".\Imagenes\logotipo_simple_utn_haedo.png"))

        # Cargo icono a app
        self.setWindowIcon(QIcon(r'./Imagenes/logo_utn.png'))

        # Establecer la imagen en el QLabel
        self.ui.img_logo1.setPixmap(QPixmap(r".\Imagenes\logotipo_diysatellite.png"))
        self.ui.img_logo2.setPixmap(QPixmap(r".\Imagenes\logotipo_simple_utn_haedo.png"))

        # Ajustar el tamaño del QLabel al tamaño de la imagen
        self.ui.img_logo1.setScaledContents(True)
        self.ui.img_logo2.setScaledContents(True)

        # Habilitar el autoscroll
        self.ui.table_serial.setAutoScroll(True)
        self.ui.table_serial.setVerticalScrollMode(QTableWidget.ScrollPerItem)
        
        # Ajuste de ancho de columna segun contenido
        self.ui.table_serial.resizeColumnsToContents()

        # Creo objetos 
        self.obj_data_uart = ManagerDataUart()
        self.obj_data_processor = DataProcessor()

        # Carga de puertos disponibles en combobox
        list_ports = self.obj_data_uart.list_port_com()
        list_ports.insert(0, " ")

        self.ui.cbox_port_master.addItems(list_ports)
        self.ui.cbox_port_slave.addItems(list_ports)

        # Carga de graficos
        self.graph1 = Graph_volt()
        self.graph2 = Graph_volt()

        self.ui.graph_out1.addWidget(self.graph1)
        self.ui.graph_out2.addWidget(self.graph2)

        # Formato de reloj a LCD
        self.ui.lcd_timer_total.display(f"{0:02d}:{0:02d}:{0:02d}")        
        self.ui.lcd_time_rtc.display(f"{0:02d}:{0:02d}:{0:02d}")

        # Callback de botones
        self.ui.btn_init.clicked.connect(self.init)
        self.ui.btn_stop.clicked.connect(self.stop)
        self.ui.btn_ok_setsend1.clicked.connect(self.get_time_send1)

        # Asigno avance por segundos
        self.ui.set_time_send1.setCurrentSection(QTimeEdit.SecondSection)

        # Inicializar el tiempo a 00:00:00
        self.time_total = QTime(0, 0, 0)

        # Timer para actualizar grafico #REEMPLAZAR POR DATA DE TIMER ARDUINO
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout_1mseg)
        self.cont= 0 # contador auxiliar para saber cuando llega al segundo
        self.cont_aux = 0 # contador para enviar datos por UART
        self.flag_send_uart = False
        # Inicializo por defecto envio cada 10 seg
        self.set_time1 = QTime(0, 0, 10, 0) 

    def update_reloj_slave(self):
        # Convertir a str QTime
        reloj_str_total = self.time_total.toString("hh:mm:ss")
        # Mostrar tiempo en display
        self.ui.lcd_timer_total.display(reloj_str_total)

        return reloj_str_total

    def verification_set_time(self):
        flag_value = False # Indica que se cumple intervalo de accion
        seconds_total_set = self.to_seconds(self.set_time1)
        
        # Temporizador para enviar datos
        if (seconds_total_timer % seconds_total_set) == 0:
            flag_value = True

        return flag_value

    def dispatch_serial_master_event(self, data):
        
        if data["serial_id"] == RTC:
            # Identifico datos recibidos en la trama
            date, time, serial_id1, value1, serial_id2, value2 = self.obj_data_processor.separate_str(data["value"])
            # Determino nombre de id
            if int(serial_id1) == MEAS1:
                id_name1 = NAME_MEAS1
            if int(serial_id2) == MEAS2:
                id_name2 = NAME_MEAS2            

            # Muestro datos de RTC en display
            self.ui.lcd_time_rtc.display(f"{time}")
            self.ui.lcd_date_rtc.setText(f"{date}")

            # Agregar fila a tabla
            row_data = [serial_id1, id_name1, value1, f"{date} {time}"]
            self.load_row_table(row_data)
            row_data = [serial_id2, id_name2, value2, f"{date} {time}"]
            self.load_row_table(row_data)

            # Scrool automatico al cargarse un nuevo data que sobresalga de la tabla
            self.ui.table_serial.scrollToBottom()
        elif data["serial_id"] == STATE:
            self.ui.text_state.setText(data["value"])
        else:
            print("Master: ID NO IDENTIFICADO")
            print("Data Master: ", data)

    def load_row_table(self, row_data):
        current_row = self.ui.table_serial.rowCount()
        self.ui.table_serial.insertRow(current_row)

        # Insertar los datos en la nueva fila
        for column in range(len(row_data)):
            item = QTableWidgetItem(row_data[column])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            self.ui.table_serial.setItem(current_row, column, item)

    def dispatch_serial_slave_event(self, data):
        if data["serial_id"] == MEAS1:
            self.ui.value_out1.setText(f'Value:{data["value"]}V  Time:{data["time"]}s' )
            value_s = float(data["value"])
            self.graph1.update_graph(value_s)
        elif data["serial_id"] == MEAS2:
            self.ui.value_out2.setText(f'Value:{data["value"]}V  Time:{data["time"]}s')            
            value_s = float(data["value"])
            self.graph2.update_graph(value_s)
        #else:
        #    print("ID NO IDENTIFICADO")
        #    print("Slave: ", data)

    def timeout_1mseg(self):
        """
        Acciones a realizar cada vez que pasa un segundo
        """
        # Cargo datos relevantes en UI        
        reloj_str = self.update_reloj_slave()

        # Lectura de puerto serial
        data_master = {"serial_id": None, "value": None, "time": None}
        data_slave = {"serial_id": None, "value": None, "time": None}
        data_master["serial_id"], data_master["value"]= self.obj_data_uart.reciv_serial("Master")
        data_master["time"] = self.to_seconds(self.time_total)
        data_slave["serial_id"], data_slave["value"] = self.obj_data_uart.reciv_serial("Slave")
        data_slave["time"] = self.to_seconds(self.time_total)
        


        # Acciones a realizar recibir los datos de master y slave
        self.dispatch_serial_master_event(data_master)
        self.dispatch_serial_slave_event(data_slave)

        # Incremento de timer QT -- LUEGO HACERLO CON ARDUINO
        
        self.cont+=TIMEOUT
        
        if self.cont==1000:
            if (self.cont_aux%10) == 0:
                self.flag_send_uart = True #Para enviar solo una vez config por uart
            self.cont_aux +=1
            self.time_total = self.time_total.addMSecs(1000)
            self.cont = 0
        


    def get_value_out1(self):
        """
        Obteniene valor numerico para grafico 1
        """
        # MODO MANUAL PARA CARGAR VALORES
        value_out1 = self.ui.sbox_volt1.value()

        return value_out1

    def get_value_out2(self):
        """
        Obtener valor numerico para grafico 2
        """
        # MODO MANUAL PARA CARGAR VALORES
        value_out2 = self.ui.sbox_volt2.value()

        return value_out2
        
    def get_time_send1(self):
        """
        Envio de data si se cumple temporizador
        """
        # Obtener tiempo para enviar data
        self.set_time1 = self.ui.set_time_send1.time()

    def to_seconds(self, time):
        """
        Convierte a segundos
        """
        seconds_total = time.hour() * 3600 \
                        + time.minute() * 60 \
                        + time.second()
        return seconds_total

    def to_milliseconds(self, time):
        """
        Convierte a milisegundos totales
        """
        milliseconds_total = (time.hour() * 3600 * 1000) \
                            + (time.minute() * 60 * 1000) \
                            + (time.second() * 1000) \
                            + time.msec()
        return milliseconds_total

    def init(self):
        # Inicio timer con actualizacion de datos cada 1mseg
        self.timer.start(TIMEOUT)

        # Asigno puertos
        port_m = self.ui.cbox_port_master.currentText() # Leo puerto de combobox
        port_s = self.ui.cbox_port_slave.currentText() # Leo puerto de combobox
        port_master = self.obj_data_processor.filter_port(port_m) # Master
        port_slave = self.obj_data_processor.filter_port(port_s) # Slave

        # Incializo puerto serial
        self.obj_data_uart.init_serial(port_master, "Master")
        self.obj_data_uart.init_serial(port_slave, "Slave")

    def stop(self):
        # Finalizo timer
        self.timer.stop()

