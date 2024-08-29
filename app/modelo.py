"""
modelo.py:
    Módulo encargado de la lógica de la app, lo cual implica el manejo de base de datos, CRUD, y eventos. 
"""
__author__ = "Nahuel Vargas"
__maintainer__ = "Nahuel Vargas"
__email__ = "nahuvargas24@gmail.com"
__copyright__ = "Copyright 2024"
__version__ = "0.0.1"

from datetime import datetime
import os
from PIL import Image 
import pandas as pd
#import jinja2
#import pdfkit
#import webbrowser
#import base64
import serial.tools.list_ports
import serial
import re
import time

class DataProcessor():
    def filter_port(self, port_full):
        """
        Filtra numero de puerto
        """
        filter_text = re.search(r"\((.*?)\)", port_full)
        if filter_text:
            port_num = filter_text.group(1)

        return port_num


class ManagerFile(): pass
class ManagerDataUart():
    def __init__(self):
        self.port_master = None # Num de puerto seleccionado
        self.port_slave = None # Num de puerto seleccionado
        self.freq_baud = 115200

    def list_port_com(self):
        list_ports = []

        ports = serial.tools.list_ports.comports()
        for port in ports:
            list_ports.append(port.description)
        return list_ports

    def send_serial(self, id, value):
        try:
            # Configuracion de puerto serial
            ser = serial.Serial(self.port_master, self.freq_baud)
            # Estructuro dato a enviar a formato CSV
            buf = f"{id},{value:.02f}"
            #print(f"A ESP32: {buf}")
            # Envio datos por serial
            ser.write(buf.encode())
            ser.close()
        except ValueError as e:
            print(f"Error al conectar puerto {self.port_master}/n")
            print(e)


    def reciv_serial(self):
        try:
            # Configuracion de puerto serial
            ser = serial.Serial(self.port_master, self.freq_baud, timeout=1)
            #print(ser.in_waiting)
            time.sleep(0.1)
            if ser.in_waiting > 0 :
                linea = ser.readline().decode('utf-8').strip()
                print(f"envio ESP32: {linea}")
            ser.close()
        except serial.SerialException as e:
            print(f"Error al conectar puerto {self.port_master}/n")
            print(e)



