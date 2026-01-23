import os
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6 import QtCore as core
#import win32com.client

from vista import *

class Controlador():
    def __init__(self, ):
        self.menu = MainWindow()
        self.menu.show() 
        try:
            print("Abro app")            
            sys.exit(app.exec_())    # Mantiene abierta la app
        except SystemExit:
            print("Cierro app")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    #app.setStyle("Fusion")
    app.setStyleSheet("""
        QWidget {
            background-color: #1E1E1E;
            color: #000000;        /* Texto negro */
            font-family: Segoe UI;
            font-size: 10pt;
        }

        /* Widgets deshabilitados */
        QWidget:disabled {
            color: #B0B0B0;        /* Gris claro */
        }
    """)
    # Creao objeto controlador 
    obj_controlador = Controlador()