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

FREQ_BAUD = 115200

class DataProcessor():
    def filter_port(self, port_full):
        """
        Filtra numero de puerto
        """
        filter_text = re.search(r"\((.*?)\)", port_full)
        if filter_text:
            port_num = filter_text.group(1)

        return port_num

    def extract_value(self, data_str):
        try:
            # Divide la cadena en partes usando la coma como delimitador
            parts = data_str.split(',')
            
            # Verifica que la cadena tenga al menos dos partes (id y value)
            if len(parts) < 2:
                raise ValueError("La cadena no contiene un valor válido.")
            
            # Extrae la parte correspondiente al valor y lo convierte a float
            id_str = parts[0]
            value_str = parts[1]
            
            id_serial = int(id_str)
            
            return id_serial, value_str
            
        except ValueError as e:
            # Manejo de errores: la cadena no es válida o el valor no puede convertirse a float
            print(f"Error: {e}")
            return None, None

    def separate_str(self, str_full):
        date, time, serial_id1, value1, serial_id2, value2 = str_full.split()

        return date, time, serial_id1, value1, serial_id2, value2

class ManagerFile(): pass
class ManagerDataUart(DataProcessor):
    def __init__(self):
        self.ser = {
            "Master": None,
            "Slave": None
        }

    def list_port_com(self):
        list_ports = []

        ports = serial.tools.list_ports.comports()
        for port in ports:
            list_ports.append(port.description)
        return list_ports

    def init_serial(self, port_num, port_name):
        try:
            # Configuro e identifico puerto serial
            if port_name in self.ser:
                self.ser[port_name] = serial.Serial(port_num, FREQ_BAUD)
        except ValueError as e:
            print(f"Error al conectar puerto {port_num}/n")
            print(e)

    def send_serial(self, port_name, id_serial, value):
        try:
            # Estructuro dato a enviar a formato CSV
            buf = f"{id_serial},{value:.02f}"
            #print(f"Enviar a {port_name}: {buf}")
            # Envio datos por serial
            self.ser[port_name].write(buf.encode())
            time.sleep(0.01)
            #ser.close()
        except ValueError as e:
            print(f"Error en {port_name}/n")
            print(e)

    def reciv_serial(self, port_name):
        id_serial = None
        value = None
        try:
            if self.ser[port_name].in_waiting > 0 :
                #time.sleep(0.01)
                linea = self.ser[port_name].readline().decode('utf-8').strip()
                #print(f"{port_name}: {linea}")
                id_serial, value = self.extract_value(linea)

        except serial.SerialException as e:
            print(f"Error en {port_name}/n")
            print(e)

        return id_serial, value
    
    def close_ports(self, event):
        if self.ser["Master"]:
            self.ser["Master"].close()
        if self.ser["Slave"]:
            self.ser["Slave"].close()
        event.accept()


