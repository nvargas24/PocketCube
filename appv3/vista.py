"""
vista.py:
    Módulo encargado de generar la interfaz gráfica de la app. 
"""
__author__ = "Nahuel Vargas"
__maintainer__ = "Nahuel Vargas"
__email__ = "nahuvargas24@gmail.com"
__copyright__ = "Copyright 2024"
__version__ = "0.0.1"

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QApplication, QDialog

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib

from modelo import *

from Qt.ui_test_attiny import *

#--- ID
MEAS1 = 1

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
        self.fig.subplots_adjust(left=.16, bottom=.15, right=.95, top=.99) #Ajuste de escala de grafica
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
        self.xlim_fin = 15
        self.ylim_init = -1
        self.ylim_fin = 1

        # Inicializo grilla
        self.grid_lines_v = []
        self.grid_lines_h = []

        self.fig, self.ax = plt.subplots(1, dpi=82, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.16, bottom=.15, right=.95, top=.99) #Ajuste de escala de grafica
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
        # Eliminar las líneas de la grilla existentes
        for line in self.grid_lines_v:
            line.remove()
        for line in self.grid_lines_h:
            line.remove()

        self.grid_lines_v.clear()
        self.grid_lines_h.clear()

        # Establece nombres de ejes y tamanio
        matplotlib.rcParams['font.size'] = 10
        self.ax.set_xlabel("Intervalos", labelpad=1)
        self.ax.set_ylabel("CPS", labelpad=1)
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

        #for j in range(self.ylim_init, self.ylim_fin, step_value_y):   
        #    line = self.ax.axhline(j, color='grey', linestyle='--', linewidth=0.25)
        #    self.grid_lines_h.append(line)


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
        self.ui.table_cpm.resizeColumnsToContents()
        self.ui.table_cps.resizeColumnsToContents()
        self.ui.table_cpm.setColumnWidth(1, 85)  # Tamaño para la segunda columna
        self.ui.table_cpm.setColumnWidth(2, 140)  # Tamaño para la tervera columna
        self.ui.table_cps.setColumnWidth(0, 85)  # Tamaño para la primera columna
        self.ui.table_cps.setColumnWidth(1, 140)  # Tamaño para la segunda columna
        #self.ui.table_cps.setColumnWidth(2, 60)  # Tamaño para la tercera columna
        
        # Ajuste de alto de fila segun contenido
        self.ui.table_cpm.resizeRowsToContents()

        # Creo objetos 
        self.obj_data_uart = ManagerDataUart()
        self.obj_data_processor = DataProcessor()
        self.obj_file = ManagerFile()

        # Carga de puertos disponibles en combobox
        list_ports = self.obj_data_uart.list_port_com()
        list_ports.insert(0, " ")

        self.ui.cbox_in_serial.addItems(list_ports)

        # Carga de graficos
        self.graph1 = Graph_bar()
        self.graph2 = Graph_line()

        self.ui.graph_out1.addWidget(self.graph1)
        self.ui.graph_out2.addWidget(self.graph2)

        # Formato de reloj a LCD
        self.ui.lcd_time_pc.display(f"{0:02d}:{0:02d}:{0:02d}.{0:03d}")
        self.ui.lcd_time_duration.display(f"{0:02d}:{0:02d}:{0:02d}")

        # Callback de botones
        self.ui.btn_init.clicked.connect(self.init)
        self.ui.btn_stop.clicked.connect(self.stop)
        self.ui.btn_export.clicked.connect(self.create_csv)
        #self.ui.btn_reset.clicked.connect(self.reset_widget)


    def load_row_table(self, row_data, table):
        if table=="cp":
            table = self.ui.table_cp
        elif table=="cps":
            table = self.ui.table_dosis

        current_row = table.rowCount()
        table.insertRow(current_row)
        table.setRowHeight(current_row, 9)

        # Insertar los datos en la nueva fila
        for column in range(len(row_data)):
            item = QTableWidgetItem(row_data[column])
            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
            table.setItem(current_row, column, item)


    def init(self):
        # Asigno puertos
        port_m = self.ui.cbox_in_serial.currentText() # Leo puerto de combobox
        port_master = self.obj_data_processor.filter_port(port_m) # Master
        
        # Inicializo puerto serial
        self.obj_data_uart.init_serial(port_master, "Master")

        # Configuro limites de progressbar segun interval
        self.ui.pbar_interval.setMaximum(int(self.dict_config["interval_time"]))
        self.ui.pbar_interval.reset()

        # habilito btn
        self.ui.btn_stop.setEnabled(True)
        self.ui.btn_init.setEnabled(False)

    def stop(self):
        self.obj_data_uart.ser["Master"].close()

        self.ui.btn_stop.setEnabled(False)
        self.ui.btn_reset.setEnabled(True)
        self.ui.btn_csv.setEnabled(True)

    def create_csv(self):
        # Exporto CSV
        self.obj_file.export_csv_df(self.obj_file.df_acumulado_cp, "CountPulse")
        self.obj_file.export_csv_df(self.obj_file.df_acumulado_cps, "CPS")

        # Vacio Dataframe para nueva carga
        self.obj_file.clear_df(self.obj_file.df_acumulado_cp)
        self.obj_file.clear_df(self.obj_file.df_acumulado_cps)

    def exit(self):
        QApplication.quit()  # Cierra la aplicación

    def reset_widget(self):
        """
        Resetea los widgets de la app
        """
        # Limpio tablas
        self.ui.table_cp.clearContents()
        self.ui.table_dosis.clearContents()
        self.ui.table_cp.setRowCount(0)
        self.ui.table_dosis.setRowCount(0)

        # Limpio graficos
        self.graph1.x_data.clear()
        self.graph1.y_data.clear()
        self.graph2.x_data.clear()
        self.graph2.y_data.clear()

        # Reseteo progressbar
        self.ui.pbar_interval.reset()

        # Reseteo contador de pulsos
        self.cont_meas1 = 0

        self.ui.btn_reset.setEnabled(False)
        self.ui.btn_csv.setEnabled(False)
        self.ui.btn_init.setEnabled(True)