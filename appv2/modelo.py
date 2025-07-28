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
            print(f"Error: {e}")
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

    def convertion_unit(self, dict_config):
        # Estandarizar la distancia a metros
        if dict_config['unit_distance'] == 'cm':
            dict_config['distance'] = dict_config['distance'] / 100  # Convertir cm a metros
            dict_config['unit_distance'] = 'm'  # Cambiar unidad a metros

        # Estandarizar la intensidad a uCi
        if dict_config['unit_intensity'] == 'mCi':
            dict_config['rad_intensity'] = dict_config['rad_intensity'] * 1000  # Convertir mCi a uCi
            dict_config['unit_intensity'] = 'uCi'  # Cambiar unidad a uCi

        # Estandarizar el tiempo a segundos
        if dict_config['unit_time'] == 'min':
            dict_config['interval_time'] = dict_config['interval_time'] * 60  # Convertir minutos a segundos
            dict_config['unit_time'] = 'seg'  # Cambiar unidad a segundos

        return dict_config

    def calcule_cps(self, list_cp):
        print("Calculo de CPS")
        print(f"Lista de CP: {list_cp}")   
        
        if not list_cp:  # Verifica si la lista está vacía
            return 0
        else:
            prom = sum(list_cp) / len(list_cp)
            return round(prom, 2)

    def calcule_dosis(self, cps, dict_config):
        dosis = cps*dict_config["interval_time"]*0.0000001

        return dosis
    
    def datetime_pc(self):
        """
        Obtiene la fecha y hora actual del PC
        """
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        datetime_now = now.strftime("%Y-%m-%d %H:%M:%S")

        return date, time, datetime_now

class ManagerFile():
    def __init__(self):
        self.df_acumulado_cp = pd.DataFrame(columns=['Time', 'Intervalo', 'RTC', 'Count Pulse'])
        self.df_acumulado_dosis = pd.DataFrame(columns=['Intervalo', 'RTC', 'CPS', 'Dosis'])

    def create_csv(self, data):
                # Cargar los datos en un DataFrame
        df = pd.read_csv(StringIO(data), header=None)

        # Mostrar las primeras filas del DataFrame
        print(df)
        # Renombrar las columnas
        df.columns = ['Fecha', 'Hora', 'Meas1', 'Meas2']
        # Ruta donde se guardará el archivo CSV
        csv_file_path = 'data_output.csv'

        # Guardar el DataFrame en un archivo CSV, con encabezados solo si el archivo no existe
        write_header = not pd.io.common.file_exists(csv_file_path)
        df.to_csv(csv_file_path, mode='a', index=False, header=write_header)

    def load_df(self, data, id_name):
        if id_name == "cp":
            df_temporal1 = pd.DataFrame([data], columns=['Time', 'Intervalo', 'RTC', 'Count Pulse'])
            self.df_acumulado_cp = pd.concat([self.df_acumulado_cp, df_temporal1], ignore_index=True)
        if id_name == "dosis":
            df_temporal2 = pd.DataFrame([data], columns=['Intervalo', 'RTC', 'CPS', 'Dosis'])
            self.df_acumulado_dosis = pd.concat([self.df_acumulado_dosis, df_temporal2], ignore_index=True)

    def export_csv_df(self, df, id_name):
        datetime_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        name_file = f"regitro_{id_name}_{datetime_now}.csv"
        try:
            # Obtiene la ruta del escritorio del usuario
            url_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            url_file = os.path.join(url_desktop, name_file)
            # Exporta el DataFrame al archivo CSV
            df.to_csv(url_file, index=False)
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
                print("Conexion exitosa")
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
                print(f"{port_name}: {linea}")
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


