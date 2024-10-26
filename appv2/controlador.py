import os
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import QtCore as core
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
    # Creao objeto controlador 
    obj_controlador = Controlador()