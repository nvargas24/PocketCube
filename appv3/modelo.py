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
import csv
import os
import pandas as pd
from io import StringIO
from PIL import Image 
import pandas as pd
from pathlib import Path
#import jinja2
#import pdfkit
#import webbrowser
#import base64
import serial.tools.list_ports
import serial
import re
import time

FREQ_BAUD = 9600

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
            #print(f"Error: {e}")
            return None, None

    def separate_str(self, str_full):
        date, time, value1, value2 = str_full.split()

        return date, time, value1, value2

    def extract_meas(self, str_full):
        datetime, value = str_full.rsplit(" ", 1)

        return datetime, value
    
    def format_tocsv(self, str):
        str_format = str.replace(";","\n")
        str_format  = str_format.replace(" ", ",")
        
        return str_format

    def id_text_descrip(self):
        pass

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

    def calcule_cps(self, list_cp):
        """
        Calcula promedio de cps - en base a la cantidad de pulsos registrados en el intervalo establecido.
        :param list_cp: Lista de valores de cps
        """
        if not list_cp:  # Verifica si la lista está vacía
            return 0
        else:
            prom = sum(list_cp) / len(list_cp)
            return round(prom, 2)

    def datetime_pc(self):
        """
        Obtiene la fecha y hora actual del PC
        """
        now = datetime.now()
        miliseconds = now.microsecond//1000
        date = now.strftime(r"%Y-%m-%d")
        time = now.strftime(r"%H:%M:%S") + f".{miliseconds:03d}"

        datetime_now = now.strftime("%Y-%m-%d %H:%M:%S")

        return date, time, datetime_now


        
class ManagerFile():
    def __init__(self):
        self.df_acumulado_cp = pd.DataFrame(columns=['Time', 'Intervalo', 'RTC', 'Count Pulse'])
        self.df_acumulado_cps = pd.DataFrame(columns=['Intervalo', 'RTC', 'CPS'])

    def load_df(self, data, id_name):
        if id_name == "cp":
            df_temporal1 = pd.DataFrame([data], columns=['Time', 'Intervalo', 'RTC', 'Count Pulse'])
            self.df_acumulado_cp = pd.concat([self.df_acumulado_cp, df_temporal1], ignore_index=True)
        if id_name == "cps":
            df_temporal2 = pd.DataFrame([data], columns=['Intervalo', 'RTC', 'CPS'])
            self.df_acumulado_cps = pd.concat([self.df_acumulado_cps, df_temporal2], ignore_index=True)

    def export_csv_df(self, df, id_name):
        datetime_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name_file = f"{id_name}_{datetime_now}.csv"
        try:
            # Obtiene la ruta del escritorio del usuario
            url_desktop = Path.home() / "Desktop"

            # Crea la carpeta "LogBG51" si no existe
            url_log_folder =  url_desktop / "LogBG51"
            url_log_folder.mkdir(exist_ok=True)

            file_path = url_log_folder / name_file

            # Exporta el DataFrame al archivo CSV
            df.to_csv(file_path, index=False)
            print(f"DataFrame exportado con éxito a {name_file}")
        except Exception as e:
            print(f"Error al exportar el DataFrame: {e}")

    def clear_df(self, df):
        # Vacia el DataFrame manteniendo sus columnas
        df.drop(df.index, inplace=True)
        print("DataFrame vaciado con éxito")       

class ManagerDataUart(DataProcessor):
    def __init__(self):
        self.ser = {
            "Master": None,
            "Slave": None
        }

        self.register_timeout_serial = {
            "last": time.time() , 
            "now": time.time()
        }

    def list_port_com(self):
        """
        Lista puertos COM disponibles
        """
        list_ports = []

        try:
            ports = serial.tools.list_ports.comports()

            if not ports:
                return []  # o podés devolver None / ["No hay puertos disponibles"]

            for port in ports:
                list_ports.append(port.description)

        except Exception as e:
            print(f"Error al listar puertos COM: {e}")
            return []  # fallback seguro

        return list_ports
    

    def init_serial(self, port_num, port_name):
        try:
            # Configuro e identifico puerto serial
            if port_name in self.ser:
                self.ser[port_name] = serial.Serial(port_num, FREQ_BAUD)
                print("Conexion exitosa")
        except ValueError as e:
            print(f"Error al conectar puerto {port_num}/n")
            print(e)

    def send_serial(self, port_name, id_serial, value):
        """
        Envia datos por puerto serial seleccionado
        
        :param port_name: puerto COM a utilizar
        :param id_serial: ID de servicio solicitado a Arduino (ej.:I2C)
        :param value: comando a enviar 
        """
        try:
            #### Estructuro dato a enviar a formato CSV
            #### buf = f"{id_serial},{value:.02f}"
            buf = f"{id_serial},{value}"
            print(f"Enviar a {port_name}: {buf}")
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
        linea = ""

        try:
            if self.ser[port_name].in_waiting > 0 :
                #time.sleep(0.01)
                linea = self.ser[port_name].readline().decode('utf-8').strip()
                #print(f"{port_name}: {linea}") # Muestra full dato recibido por UART
                id_serial, value = self.extract_value(linea)

        except serial.SerialException as e:
            print(f"Error en {port_name}/n")
            print(e)

        return id_serial, value, linea
    
    def close_ports(self, event):
        if self.ser["Master"]:
            self.ser["Master"].close()
        if self.ser["Slave"]:
            self.ser["Slave"].close()
        event.accept()


    ### Para TIMEOUT en caso de no recibir respuesta Serial
    def register_request_time(self, register):
        """
        Registro time que se envia dato para calcular TIMEOUT
        """
        self.register_timeout_serial[register] = time.time()

    def flag_timeout(self, timeout):
        
        diff_time = time.time() - self.register_timeout_serial["last"] 

        #print(f"=====TIMEOUT : {timeout}  --- DIFF : {diff_time}")

        if diff_time > timeout:
            return True
        else:
            return False