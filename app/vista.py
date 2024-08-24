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

class Graph_volt(FigureCanvas):
    def __init__(self):
        self.xlim_init = 0
        self.xlim_fin = 15
        self.ylim_init = -1
        self.ylim_fin = 6

        self.fig, self.ax = plt.subplots(1, dpi=80, figsize=(12,12), sharey=True, facecolor="none")
        self.fig.subplots_adjust(left=.12, bottom=.12, right=.98, top=.9) #Ajuste de escala de grafica
        super().__init__(self.fig)

        #self.freq_initial = np.arange(0, SAMPLES_FFT*37, 37)
        #self.mag_initial = np.zeros(SAMPLES_FFT)
        
        self.set_graph_fft_style()
        # Crear la línea inicial
        #self.line, = self.ax.plot(self.freq_initial, self.mag_initial, picker=5)

        self.test_graph()
        self.draw()

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

    def update_graph_fft(self, freq, mag):
        """
        Metodo para actualizar listas de puntos para grafico fft
        """
        self.set_graph_fft_style()

        self.line, = self.ax.plot(freq, mag, picker=5)
        self.draw()

    def set_graph_fft_style(self):
        """
        Metodo que asigna estilo al grafico
        """
        # Establecer límites del eje X e Y
        self.ax.set_xlim(self.xlim_init, self.xlim_fin)
        self.ax.set_ylim(self.ylim_init, self.ylim_fin)

        # Creo grilla
        step_value_fft_x = round((self.xlim_fin-self.xlim_init)/20)
        step_value_fft_y = round((self.ylim_fin-self.ylim_init)/10)
        for i in range(self.xlim_init, self.xlim_fin, step_value_fft_x):
            self.ax.axvline(i, color='grey', linestyle='--', linewidth=0.25)
        for j in range(self.ylim_init, self.ylim_fin, step_value_fft_y):   
            self.ax.axhline(j, color='grey', linestyle='--', linewidth=0.25)

        # Establece nombres de ejes y tamanio
        matplotlib.rcParams['font.size'] = 2
        self.ax.set_xlabel("Time[s]")
        self.ax.set_ylabel("V[mV]")

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

        self.setFixedSize(900, 660)
        #self.setWindowIcon(QIcon(".\Imagenes\logotipo_simple_utn_haedo.png"))

        # Cargo icono a app
        self.setWindowIcon(QIcon('./Imagenes/logo_utn.png'))

        # Establecer la imagen en el QLabel
        self.ui.img_logo1.setPixmap(QPixmap(".\Imagenes\logotipo_diysatellite.png"))
        self.ui.img_logo2.setPixmap(QPixmap(".\Imagenes\logotipo_simple_utn_haedo.png"))

        # Ajustar el tamaño del QLabel al tamaño de la imagen
        self.ui.img_logo1.setScaledContents(True)
        self.ui.img_logo2.setScaledContents(True)
        
        # Carga de puertos disponibles en combobox
        obj_data_uart = ManagerDataUart()

        list_ports = obj_data_uart.list_port_com()
        list_ports.insert(0, " ")

        self.ui.cbox_port_master.addItems(list_ports)
        self.ui.cbox_port_slave.addItems(list_ports)

        # Carga de graficos
        self.graph1 = Graph_volt()
        self.graph2 = Graph_volt()

        self.ui.graph_out1.addWidget(self.graph1)
        self.ui.graph_out2.addWidget(self.graph2)

        self.ui.lcd_timer.display(f"{0:02d}:{0:02d}:{0:02d}")
        self.ui.lcd_time_rtc.display(f"{0:02d}:{0:02d}:{0:02d}")
