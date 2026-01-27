"""
vista.py:
    Módulo encargado de generar la interfaz gráfica de la app. 
"""
__author__ = "Nahuel Vargas"
__maintainer__ = "Nahuel Vargas"
__email__ = "nahuvargas24@gmail.com"
__copyright__ = "Copyright 2024"
__version__ = "0.0.1"

# Librerias para graficos
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QApplication, QDialog

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.ticker import AutoMinorLocator

from Qt.ui_test_attiny import *

# Librerias propias
from modelo import *

# Tiempo de espera para proxima solicitud - si no se recibe respuesta
TIMEOUT = 3.0 

# Extraccion de datetime
TIME_MS_PC = 1
DATE_PC = 0 

# Solcitud a cmd de servicio a Arduino
NO_CMD = 0
CMD_I2C = 1
# Comando especifico del servicio solicitado
CPM = 1
CPS_NOW = 2
TIME = 3
CPS_NOW_ACCUM = 4
CPS_TIME = 5 # id , [CPS_NOW] [TIME]   
CPM_TIME = 6 # id , [CPM] [TIME] 

# Identifican widget a cargar datos
SEND_CPS_APP = 8 # id cargar en datos CPS
SEND_CPM_APP = 9 # id cargar en datos CPM
SEND_LINE_APP = 7 # id para cargar qline de solictudes manuales

class Graph_bar(FigureCanvas):
    def __init__(self):
        self.xlim_init = 1
        self.xlim_fin = 15
        self.ylim_init = -1
        self.ylim_fin = 6

        # Inicializo grilla
        self.grid_lines_v = []
        self.grid_lines_h = []

        self.fig, self.ax = plt.subplots(1, dpi=82, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.16, bottom=.15, right=.95, top=.90) #Ajuste de escala de grafica
        super().__init__(self.fig)

        self.set_graph_style()

        # Listas para cargar datos
        self.x_data = []
        self.y_data = []

        # Crear la línea inicial
        self.bar = self.ax.bar([], [], picker=5)

    def update_graph(self, new_y_value, interval_time):
        """
        Metodo para actualizar grafico
        """
        if self.x_data:
            # Reseteo al llega al limite de intervalo
            if self.x_data[-1] == interval_time:
                self.x_data.clear()
                self.y_data.clear() 
                self.ylim_init = -1
                self.ylim_fin = 6

        # Generar nuevo valor de datos
        if self.x_data:
            next_x = self.x_data[-1] + 1 # Agrego nueva pos en x en la lista
        else:
            next_x = self.xlim_init

        self.x_data.append(next_x)
        self.y_data.append(new_y_value)

        #print(f"x_data: {self.x_data}\ny_data: {self.y_data}")

        # Actualizar datos de la línea
        self.ax.clear()  # Limpiar el gráfico actual

        self.xlim_fin = interval_time+1 # ajusto eje x segun config user

        if self.ylim_fin < new_y_value:
            self.ylim_fin = new_y_value+ round(new_y_value*0.1)

        self.set_graph_style()  # Reaplicar el estilo después de limpiar
        self.bars = self.ax.bar(self.x_data, self.y_data, picker=5)  # Dibujar nuevas barras

        # Ajustar los límites si es necesario
        #if next_x >= self.xlim_fin:
        #    self.xlim_fin = next_x+1

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
        self.ax.set_title("CPS") #####VER-----
        self.ax.set_xlabel("Time[s]", labelpad=1)
        self.ax.set_ylabel("Count Pulse", labelpad=1)
        self.ax.tick_params(axis='both', which='both', labelsize=7)
   
        # Establecer límites del eje X e Y
        self.ax.set_xlim(self.xlim_init-1, self.xlim_fin)
        self.ax.set_ylim(self.ylim_init, self.ylim_fin)

        # Creo grilla
        per_div = 1
        #if self.xlim_fin > 50:
        #    per_div = 1/20

        step_value_x = round((self.xlim_fin-self.xlim_init)/((self.xlim_fin-self.xlim_init))*per_div)
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

class Graph_line(FigureCanvas):
    def __init__(self):
        self.xlim_init = 0
        self.xlim_fin = 30
        self.ylim_init = 0
        self.ylim_fin = 100

        # Inicializo grilla
        self.grid_lines_v = []
        self.grid_lines_h = []

        self.fig, self.ax = plt.subplots(1, dpi=82, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.16, bottom=.15, right=.95, top=.90) #Ajuste de escala de grafica
        super().__init__(self.fig)

        self.set_graph_style()

        # Listas para cargar datos
        self.x_data = []
        self.y_data = []

        # Crear la línea inicial
        self.line, = self.ax.plot([], [], picker=5)

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

        # Ajustar los límites si es necesario
        if next_x >= self.xlim_fin:
            self.xlim_fin = next_x+1
        
        if self.ylim_fin < new_y_value:
            self.ylim_fin = new_y_value + round(new_y_value*0.5)
        
        if self.ylim_init > new_y_value:
            self.ylim_init = new_y_value - round(new_y_value*0.1)

        self.set_graph_style()

        self.draw()

    def set_graph_style(self):
        """
        Metodo que asigna estilo al grafico
        """
        # Eliminar grillas previas
        for line in self.grid_lines_v:
            line.remove()
        for line in self.grid_lines_h:
            line.remove()

        self.grid_lines_v.clear()
        self.grid_lines_h.clear()

        # Fuente
        matplotlib.rcParams['font.size'] = 10

        # Títulos y etiquetas
        self.ax.set_title("CPM")
        self.ax.set_xlabel("Time[min]", labelpad=1)
        self.ax.set_ylabel("Count Pulse", labelpad=1)
        self.ax.tick_params(axis='both', which='both', labelsize=7)

        # Límites
        self.ax.set_xlim(self.xlim_init, self.xlim_fin)
        self.ax.set_ylim(self.ylim_init, self.ylim_fin)

        # Forzar cálculo de ticks
        self.fig.canvas.draw_idle()

        # ===============================
        # Líneas verticales (MAJOR ticks)
        # ===============================
        for x in self.ax.get_xticks():
            line = self.ax.axvline(
                x,
                color='grey',
                linestyle='--',
                linewidth=0.35,
                zorder=0
            )
            self.grid_lines_v.append(line)

        # ===============================
        # Líneas verticales auxiliares (MINOR ticks)
        # ===============================
        self.ax.xaxis.set_minor_locator(AutoMinorLocator(2))  # 1 línea intermedia

        for x in self.ax.xaxis.get_minorticklocs():
            line = self.ax.axvline(
                x,
                color='grey',
                linestyle=':',
                linewidth=0.2,
                zorder=0
            )
            self.grid_lines_v.append(line)

        # ===============================
        # Líneas horizontales (ticks Y)
        # ===============================
        for y in self.ax.get_yticks():
            line = self.ax.axhline(
                y,
                color='grey',
                linestyle='--',
                linewidth=0.25,
                zorder=0
            )
            self.grid_lines_h.append(line)

        # Bordes
        self.ax.spines['bottom'].set_color('0.7')
        self.ax.spines['left'].set_color('0.7')
        self.ax.spines['top'].set_visible(False)
        self.ax.spines['right'].set_visible(False)

        # Colores de ejes
        self.ax.tick_params(axis='x', colors='0.4')
        self.ax.tick_params(axis='y', colors='0.4')

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Datalogger Carga útil - Grupo SyCE UTN-FRH")

        self.setFixedSize(900, 600)
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
        #self.ui.table_serial.setAutoScroll(True)
        #self.ui.table_serial.setVerticalScrollMode(QTableWidget.ScrollPerItem)
        
        # Ajuste de ancho de columna segun contenido
        #self.ui.table_cpm.resizeColumnsToContents()
        #self.ui.table_cps.resizeColumnsToContents()
        
        self.ui.table_cpm.setColumnWidth(0, 40)  # Tamaño para la primera columna
        self.ui.table_cpm.setColumnWidth(1, 40)  # Tamaño para la segunda columna
        self.ui.table_cpm.setColumnWidth(2, 120)  # Tamaño para la tercera columna
        self.ui.table_cpm.setColumnWidth(3, 10)  # Tamaño para la cuarta columna

        self.ui.table_cps.setColumnWidth(0, 50)  # Tamaño para la primera columna
        self.ui.table_cps.setColumnWidth(1, 50)  # Tamaño para la segunda columna
        self.ui.table_cps.setColumnWidth(2, 100)  # Tamaño para la tercera columna
        self.ui.table_cps.setColumnWidth(3, 1)  # Tamaño para la cuarta columna
        
        # Ajuste de alto de fila segun contenido
        self.ui.table_cpm.resizeRowsToContents()

        # Creo objetos 
        self.obj_data_uart = ManagerDataUart()
        self.obj_data_processor = DataProcessor()
        self.obj_file = ManagerFile()

        # Carga de puertos disponibles en combobox
        list_ports = self.obj_data_uart.list_port_com()
        #list_ports.insert(0, " ")

        print(f"Puertos COM disponibles: {list_ports}")
        self.ui.cbox_in_serial.addItems(list_ports)

        # Carga de graficos
        self.graph1 = Graph_bar()
        self.graph2 = Graph_line()

        self.ui.graph_out1.addWidget(self.graph1)
        self.ui.graph_out2.addWidget(self.graph2)

        # Formato de reloj a LCD
        self.ui.lcd_time_pc.display(f"{0:02d}:{0:02d}:{0:02d}.{0:03d}")
        self.ui.lcd_time_duration.display(f"{0:02d}:{0:02d}:{0:02d}")

        # Creo QTimer para actualizar datos cada milisegundo
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_data)

        ## Contadores para segundos y ms una vez iniciado el QTIMER
        self.count1ms = 0
        self.count1s = 0

        # Contador de datos recibido por UART
        self.count_data_reciv = {
            'CPS': 0,
            'CPM':0    
        } 

        # Bandera para controlar espera de respuesta de Arduino   
        self.waiting_response = False  
        
        # Callback de botones
        self.ui.btn_init.clicked.connect(self.init)
        self.ui.btn_stop.clicked.connect(self.stop)
        self.ui.btn_export.clicked.connect(self.create_csv)

        self.ui.btn_accum_CPS.clicked.connect(lambda: self.manual_request("CPS"))
        self.ui.btn_last_CPM.clicked.connect(lambda: self.manual_request("CPM"))
        self.ui.btn_time_s.clicked.connect(lambda: self.manual_request("TIME_S"))
    
    def load_row_table(self, row_data, table):
        if table=="CPM":
            table = self.ui.table_cpm
        elif table=="CPS":
            table = self.ui.table_cps

        current_row = table.rowCount()
        table.insertRow(current_row)
        table.setRowHeight(current_row, 9)

        # Insertar los datos en la nueva fila
        for column in range(len(row_data)):
            item = QTableWidgetItem(row_data[column])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            table.setItem(current_row, column, item)

    def update_data(self):
        """
        Actualiza datos en widgets cada 1 ms 
        OBS.: Se dispara en 'self.init' y se finaliza con 'self.stop'(donde se resetea todos los widgets)
        """
        id_serial = None
        value_serial = None
        request_serial = None

        #--- Reseteo contador de ms cada 1 segundo
        self.count1ms += 1
        if self.count1ms >= 1000:
            self.count1s += 1
            self.count1ms = 0 
        
        ### --- Libera solicitud UART para volver a pedir si supera TIMEOUT
        if self.obj_data_uart.flag_timeout(TIMEOUT):
            self.waiting_response = False
       
        #---- Reloj de PC
        self.ui.lcd_time_pc.display(f"{self.obj_data_processor.datetime_pc()[TIME_MS_PC]}")
        self.ui.lcd_date_pc.setText(f"{self.obj_data_processor.datetime_pc()[DATE_PC]}")

        #---- Reloj de ensayo
        if self.duration_test_seconds <= 0:
            self.stop()

        #--- Se analiza BUFFER UART por si hay datos
        #if self.count1ms % 100 == 0:
            #print(f"+++ Escucha habilitado ---- flag: {self.waiting_response}")
        id_serial, value_serial, request_serial = self.obj_data_uart.reciv_serial("Master")
            #print(f"===========ID serial recibido: {id_serial}, valor: {value_serial}, request:{request_serial}")  
            #self.waiting_response = False
            #print("----#---- Despues de habilitar escuchar")

        #--- Identifico si se recibe algo de algun ID serial    
        if id_serial != None:
            #print(f"****** Identificado para cargar en widgets ---- flag: {self.waiting_response}")
            #print(f"Datos serial de {id_serial}:{value_serial}")
            self.waiting_response = False  # Reseteo bandera de espera de respuesta
            if id_serial == SEND_LINE_APP:
                self.ui.txt_rta_attiny.setText(f"{value_serial}") # carga en widget
            elif id_serial == SEND_CPM_APP:
                self.count_data_reciv['CPM'] += 1
                cpm = value_serial.split(" ")[0]
                time = value_serial.split(" ")[1]
                datetime_pc = self.obj_data_processor.datetime_pc()[TIME_MS_PC]

                row_data_cpm = [
                    f"{self.count_data_reciv['CPM']}",
                    f"{time}",
                    f"{datetime_pc}",
                    f"{cpm}"
                ]

                self.load_row_table(row_data_cpm, "CPM")
                self.ui.table_cpm.scrollToBottom()

            elif id_serial == SEND_CPS_APP:
                self.count_data_reciv['CPS'] += 1
                cps = value_serial.split(" ")[0]
                time = value_serial.split(" ")[1]
                datetime_pc = self.obj_data_processor.datetime_pc()[TIME_MS_PC]

                row_data_cps = [
                    f"{self.count_data_reciv['CPS']}",
                    f"{time}",
                    f"{datetime_pc}",
                    f"{cps}"
                ]

                self.load_row_table(row_data_cps, "CPS")
                self.ui.table_cps.scrollToBottom()


        #--- Solicitudes para tablas CPM y CPS cada 100ms
        if not self.waiting_response: # Si no estoy esperando respuesta de arduino
            if self.count1ms == 500:
                self.manual_request("CPS_TIME")
                print(f"ms: {self.count1ms}")
            if (self.count1s %60 == 0):
                self.manual_request("CPM_TIME")
            
        if self.count1ms == 0: #--- Acciones a realizar cada 1 segundo
            ##---- Reloj de ensayo
            self.duration_test_seconds -= 1

            h_d_test = self.duration_test_seconds//3600
            min_d_test = (self.duration_test_seconds%3600)//60
            s_d_test = self.duration_test_seconds%60

            self.ui.lcd_time_duration.display(f"{h_d_test:02d}:{min_d_test:02d}:{s_d_test:02d}")




    def init(self):
        self.reset_widget()
        # Asigno puertos
        port_m = self.ui.cbox_in_serial.currentText() # Leo puerto de combobox
        port_master = self.obj_data_processor.filter_port(port_m) # Master
        
        # Inicializo puerto serial
        self.obj_data_uart.init_serial(port_master, "Master") #Master es el Arduino

        # Ingreso durancion de ensayo [hh]:[mm] y en segundos (para temporizador)
        time_duration_test = self.ui.time_test.time()
        self.ui.lcd_time_duration.display(time_duration_test.toString("HH:mm:ss"))
        self.duration_test_seconds = (time_duration_test.hour()*3600 +
                                      time_duration_test.minute()*60 +
                                      time_duration_test.second()
                                      )

        # Des/habilito btn
        self.ui.btn_stop.setEnabled(True)
        self.ui.btn_init.setEnabled(False)
        self.ui.btn_export.setEnabled(False)
        self.ui.btn_accum_CPS.setEnabled(True)
        self.ui.btn_last_CPM.setEnabled(True)
        self.ui.btn_time_s.setEnabled(True)

        self.ui.cbox_in_serial.setEnabled(False)
        self.ui.time_test.setEnabled(False)

        # Inicio QTimer
        self.timer.start(1)  # Intervalo de 1 milisegundo


    def stop(self):
       

        self.obj_data_uart.ser["Master"].close()
        self.timer.stop()

        self.ui.lcd_time_duration.display(f"{0:02d}:{0:02d}:{0:02d}")

        self.ui.btn_stop.setEnabled(False)
        self.ui.btn_export.setEnabled(True)
        self.ui.btn_init.setEnabled(True)

    def create_csv(self):
        # Exporto CSV
        self.obj_file.export_csv_df(self.obj_file.df_acumulado_cp, "CountPulse")
        self.obj_file.export_csv_df(self.obj_file.df_acumulado_cps, "CPS")

        # Vacio Dataframe para nueva carga
        self.obj_file.clear_df(self.obj_file.df_acumulado_cp)
        self.obj_file.clear_df(self.obj_file.df_acumulado_cps)

    def manual_request(self, mode):
        """
        Envia solicitud manual por uart a Arduino
        """
        print(f"============= Solicitud de *{mode}* ---- flag: {self.waiting_response}")
        if mode == "CPS":
            self.obj_data_uart.send_serial("Master", CMD_I2C, CPS_NOW_ACCUM)
            self.waiting_response = True
            self.obj_data_uart.register_request_time("last")
        elif mode == "CPM":
            self.obj_data_uart.send_serial("Master", CMD_I2C, CPM)
            self.waiting_response = True
            self.obj_data_uart.register_request_time("last")
        elif mode == "TIME_S":
            self.obj_data_uart.send_serial("Master", CMD_I2C, TIME)
            self.waiting_response = True
            self.obj_data_uart.register_request_time("last")
        elif mode == "CPS_TIME":
            self.obj_data_uart.send_serial("Master", CMD_I2C, CPS_TIME)
            self.waiting_response = True
            self.obj_data_uart.register_request_time("last")
        elif mode == "CPM_TIME":
            self.obj_data_uart.send_serial("Master", CMD_I2C, CPM_TIME)
            self.waiting_response = True
            self.obj_data_uart.register_request_time("last")

    def exit(self):
        QApplication.quit()  # Cierra la aplicación

    def reset_widget(self):
        """
        Resetea los widgets de la app
        """
        # Limpio tablas
        self.ui.table_cpm.clearContents()
        self.ui.table_cps.clearContents()
        self.ui.table_cpm.setRowCount(0)
        self.ui.table_cps.setRowCount(0)

        # Limpio graficos
        self.graph1.x_data.clear()
        self.graph1.y_data.clear()
        self.graph2.x_data.clear()
        self.graph2.y_data.clear()

        # Reseteo contador de pulsos
        self.cont_meas1 = 0

        self.ui.btn_export.setEnabled(False)
        self.ui.btn_accum_CPS.setEnabled(False)
        self.ui.btn_last_CPM.setEnabled(False)
        self.ui.btn_time_s.setEnabled(False)

        self.ui.cbox_in_serial.setEnabled(True)
        self.ui.txt_rta_attiny.clear()
        self.ui.time_test.setEnabled(True)