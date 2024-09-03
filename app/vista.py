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
DAC1 = 4
DAC2 = 5

NAME_MEAS1 = "Meas1"
NAME_MEAS2 = "Meas2"

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
            self.ax.scatter(next_x-1, new_y_value, c='red', s=10, alpha=0.8, picker=True, zorder=2)
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
        self.setWindowIcon(QIcon('./Imagenes/logo_utn.png'))

        # Establecer la imagen en el QLabel
        self.ui.img_logo1.setPixmap(QPixmap(".\Imagenes\logotipo_diysatellite.png"))
        self.ui.img_logo2.setPixmap(QPixmap(".\Imagenes\logotipo_simple_utn_haedo.png"))

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
        self.ui.lcd_timer.display(f"{0:02d}:{0:02d}:{0:02d}")
        self.ui.lcd_timer_total.display(f"{0:02d}:{0:02d}:{0:02d}")        
        self.ui.lcd_time_rtc.display(f"{0:02d}:{0:02d}:{0:02d}")

        # Callback de botones
        self.ui.btn_init.clicked.connect(self.init)
        self.ui.btn_stop.clicked.connect(self.stop)
        self.ui.btn_ok_setsend1.clicked.connect(self.get_time_send1)

        # Deteccion de buttongroup seleccionado
        self.ui.buttonGroup.buttonClicked.connect(self.mostrar_seleccionado)

        # Asigno avance por segundos
        self.ui.set_time_send1.setCurrentSection(QTimeEdit.SecondSection)

        # Inicializar el tiempo a 00:00:00
        self.time = QTime(0, 0, 0)
        self.time_total = QTime(0, 0, 0)

        # Timer para actualizar grafico #REEMPLAZAR POR DATA DE TIMER ARDUINO
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout_1seg)

        # Inicializo por defecto envio cada 10 seg
        self.set_time1 = QTime(0, 0, 10, 0) 

    def mostrar_seleccionado(self, boton_seleccionado):
        # Obtener el texto del botón seleccionado
        texto_seleccionado = boton_seleccionado.text()
        print(f'Seleccionaste: {texto_seleccionado}')

    def timeout_1seg(self):
        """
        Acciones a realizar cada vez que pasa un segundo
        """
        flag_value = False # Indica que se cumple intervalo de accion

        # Convertir a str QTime
        reloj_str = self.time.toString("hh:mm:ss")
        reloj_str_total = self.time_total.toString("hh:mm:ss")
        # Mostrar tiempo en display
        self.ui.lcd_timer.display(reloj_str)        
        self.ui.lcd_timer_total.display(reloj_str_total)
        
        # Obtengo segundos para setear envios y del time
        seconds_total_timer = self.to_seconds(self.time)
        seconds_total_set = self.to_seconds(self.set_time1)
        
        # Temporizador para enviar datos
        if (seconds_total_timer % seconds_total_set) == 0:
            flag_value = True

        # Lectura de datos de UI
        self.get_value_out1(reloj_str, flag_value)
        self.get_value_out2(reloj_str, flag_value)

        # Lectura de puerto serial
        id_m = 0
        id_s = 0

        id_m, value_m = self.obj_data_uart.reciv_serial("Master")
        id_s, value_s = self.obj_data_uart.reciv_serial("Slave")

        if id_s == MEAS1:
            self.ui.value_out1.setText(value_s)            
            value_s = float(value_s)
            self.graph1.update_graph(value_s)
        if id_s == MEAS2:
            self.ui.value_out2.setText(value_s)            
            value_s = float(value_s)
            self.graph2.update_graph(value_s)
        if id_m == RTC:
            date, time, id, value = self.obj_data_processor.separate_str(value_m)
            self.ui.lcd_time_rtc.display(f"{time}")
            self.ui.lcd_date_rtc.setText(f"{date}")

            # Determino nombre de id
            if int(id) == MEAS1:
                id_name = NAME_MEAS1
            elif int(id) == MEAS2:
                id_name = NAME_MEAS2

            # Agregar fila a tabla
            row_data = [id, id_name, value, f"{date} {time}"]
            current_row = self.ui.table_serial.rowCount()
            self.ui.table_serial.insertRow(current_row)

            # Insertar los datos en la nueva fila
            for column in range(len(row_data)):
                item = QTableWidgetItem(row_data[column])
                item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.ui.table_serial.setItem(current_row, column, item)

            self.ui.table_serial.scrollToBottom()

        # Incremento de timer QT -- LUEGO HACERLO CON ARDUINO
        self.time = self.time.addMSecs(1000)        
        self.time_total = self.time_total.addMSecs(1000)

    def get_value_out1(self, reloj_str, flag=False):
        """
        Obteniene valor numerico para grafico 1
        """
        # MODO MANUAL PARA CARGAR VALORES
        value_out1 = self.ui.sbox_volt1.value()
        
        self.obj_data_uart.send_serial("Master", DAC1, value_out1); # envio por UART a ESP32

        # Temporizador para enviar datos
        if flag:
            self.ui.label_send1.setText(f"{reloj_str} {value_out1:.02f}")
            self.graph1.flag_send = True # Marca en grafico
            flag = False

    def get_value_out2(self, reloj_str, flag=False):
        """
        Obtener valor numerico para grafico 2
        """
        # MODO MANUAL PARA CARGAR VALORES
        value_out2 = self.ui.sbox_volt2.value()

        # Temporizador para enviar datos
        if flag:
            self.ui.label_send2.setText(f"{reloj_str} {value_out2:.02f}")
            self.graph2.flag_send = True # Marca en grafico
            flag = False
        
    def get_time_send1(self):
        """
        Envio de data si se cumple temporizador
        """
        # Reseteo time
        self.time = QTime(0, 0, 0, 0)
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

    def init(self):
        # Inicio timer con actualizacion de datos cada 1 seg
        self.timer.start(1000)

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

