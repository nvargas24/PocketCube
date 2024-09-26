# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulation_load.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 749)
        MainWindow.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(20, 10, 891, 711))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setSpacing(10)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_6)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget_6)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.cbox_port_master = QComboBox(self.verticalLayoutWidget_6)
        self.cbox_port_master.setObjectName(u"cbox_port_master")
        font2 = QFont()
        font2.setPointSize(11)
        self.cbox_port_master.setFont(font2)
        self.cbox_port_master.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.cbox_port_master)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.verticalLayoutWidget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.cbox_port_slave = QComboBox(self.verticalLayoutWidget_6)
        self.cbox_port_slave.setObjectName(u"cbox_port_slave")
        self.cbox_port_slave.setFont(font2)
        self.cbox_port_slave.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.cbox_port_slave)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)

        self.btn_init = QPushButton(self.verticalLayoutWidget_6)
        self.btn_init.setObjectName(u"btn_init")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_init.sizePolicy().hasHeightForWidth())
        self.btn_init.setSizePolicy(sizePolicy)
        self.btn_init.setFont(font1)

        self.horizontalLayout_7.addWidget(self.btn_init)

        self.btn_stop = QPushButton(self.verticalLayoutWidget_6)
        self.btn_stop.setObjectName(u"btn_stop")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy1)
        self.btn_stop.setFont(font1)

        self.horizontalLayout_7.addWidget(self.btn_stop)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.horizontalLayout_7.setStretch(2, 2)
        self.horizontalLayout_7.setStretch(3, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_7)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 2)
        self.verticalLayout_3.setStretch(2, 1)

        self.horizontalLayout_6.addLayout(self.verticalLayout_3)

        self.horizontalLayout_6.setStretch(0, 1)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, 10, 20, 10)
        self.img_logo1 = QLabel(self.verticalLayoutWidget_6)
        self.img_logo1.setObjectName(u"img_logo1")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.img_logo1.sizePolicy().hasHeightForWidth())
        self.img_logo1.setSizePolicy(sizePolicy2)
        self.img_logo1.setPixmap(QPixmap(u"../Imagenes/logotipo_diysatellite.png"))
        self.img_logo1.setScaledContents(True)

        self.horizontalLayout_11.addWidget(self.img_logo1)

        self.img_logo2 = QLabel(self.verticalLayoutWidget_6)
        self.img_logo2.setObjectName(u"img_logo2")
        sizePolicy2.setHeightForWidth(self.img_logo2.sizePolicy().hasHeightForWidth())
        self.img_logo2.setSizePolicy(sizePolicy2)
        self.img_logo2.setPixmap(QPixmap(u"../Imagenes/logotipo_simple_utn_haedo.png"))
        self.img_logo2.setScaledContents(True)
        self.img_logo2.setMargin(4)

        self.horizontalLayout_11.addWidget(self.img_logo2)

        self.horizontalLayout_11.setStretch(0, 2)
        self.horizontalLayout_11.setStretch(1, 7)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10.setStretch(0, 6)
        self.horizontalLayout_10.setStretch(1, 5)

        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(50, -1, 50, -1)
        self.line = QFrame(self.verticalLayoutWidget_6)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_13.addWidget(self.line)


        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox_master = QGroupBox(self.verticalLayoutWidget_6)
        self.groupBox_master.setObjectName(u"groupBox_master")
        self.groupBox_master.setFont(font1)
        self.verticalLayoutWidget = QWidget(self.groupBox_master)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 20, 441, 441))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lcd_timer_total = QLCDNumber(self.verticalLayoutWidget)
        self.lcd_timer_total.setObjectName(u"lcd_timer_total")
        self.lcd_timer_total.setLayoutDirection(Qt.RightToLeft)
        self.lcd_timer_total.setFrameShape(QFrame.NoFrame)
        self.lcd_timer_total.setFrameShadow(QFrame.Plain)
        self.lcd_timer_total.setLineWidth(1)
        self.lcd_timer_total.setSmallDecimalPoint(False)
        self.lcd_timer_total.setDigitCount(8)
        self.lcd_timer_total.setMode(QLCDNumber.Dec)
        self.lcd_timer_total.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_18.addWidget(self.lcd_timer_total)


        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.line_3 = QFrame(self.verticalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_4.setFont(font3)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.value_out1 = QLabel(self.verticalLayoutWidget)
        self.value_out1.setObjectName(u"value_out1")
        self.value_out1.setFont(font1)
        self.value_out1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.value_out1)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.graph_out1 = QVBoxLayout()
        self.graph_out1.setObjectName(u"graph_out1")

        self.verticalLayout_5.addLayout(self.graph_out1)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 10)

        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_5)

        self.value_out2 = QLabel(self.verticalLayoutWidget)
        self.value_out2.setObjectName(u"value_out2")
        self.value_out2.setFont(font1)
        self.value_out2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.value_out2)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.graph_out2 = QVBoxLayout()
        self.graph_out2.setObjectName(u"graph_out2")

        self.verticalLayout_7.addLayout(self.graph_out2)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 10)

        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 12)
        self.verticalLayout.setStretch(3, 12)

        self.horizontalLayout.addWidget(self.groupBox_master)

        self.line_4 = QFrame(self.verticalLayoutWidget_6)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_4)

        self.groupBox_slave = QGroupBox(self.verticalLayoutWidget_6)
        self.groupBox_slave.setObjectName(u"groupBox_slave")
        self.groupBox_slave.setFont(font1)
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_slave)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(20, 20, 381, 441))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lcd_time_rtc = QLCDNumber(self.verticalLayoutWidget_4)
        self.lcd_time_rtc.setObjectName(u"lcd_time_rtc")
        self.lcd_time_rtc.setLayoutDirection(Qt.RightToLeft)
        self.lcd_time_rtc.setFrameShape(QFrame.NoFrame)
        self.lcd_time_rtc.setFrameShadow(QFrame.Plain)
        self.lcd_time_rtc.setLineWidth(1)
        self.lcd_time_rtc.setSmallDecimalPoint(False)
        self.lcd_time_rtc.setDigitCount(8)
        self.lcd_time_rtc.setMode(QLCDNumber.Dec)
        self.lcd_time_rtc.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_2.addWidget(self.lcd_time_rtc)

        self.lcd_date_rtc = QLabel(self.verticalLayoutWidget_4)
        self.lcd_date_rtc.setObjectName(u"lcd_date_rtc")
        font4 = QFont()
        font4.setFamily(u"Courier")
        font4.setBold(True)
        font4.setWeight(75)
        self.lcd_date_rtc.setFont(font4)
        self.lcd_date_rtc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lcd_date_rtc)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_9 = QLabel(self.verticalLayoutWidget_4)
        self.label_9.setObjectName(u"label_9")
        font5 = QFont()
        font5.setPointSize(9)
        self.label_9.setFont(font5)

        self.horizontalLayout_12.addWidget(self.label_9)

        self.set_time_send1 = QTimeEdit(self.verticalLayoutWidget_4)
        self.set_time_send1.setObjectName(u"set_time_send1")
        sizePolicy.setHeightForWidth(self.set_time_send1.sizePolicy().hasHeightForWidth())
        self.set_time_send1.setSizePolicy(sizePolicy)
        self.set_time_send1.setFont(font1)
        self.set_time_send1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.set_time_send1.setAlignment(Qt.AlignCenter)
        self.set_time_send1.setProperty("showGroupSeparator", False)
        self.set_time_send1.setCurrentSection(QDateTimeEdit.HourSection)
        self.set_time_send1.setTime(QTime(0, 0, 10))

        self.horizontalLayout_12.addWidget(self.set_time_send1)

        self.btn_ok_setsend1 = QPushButton(self.verticalLayoutWidget_4)
        self.btn_ok_setsend1.setObjectName(u"btn_ok_setsend1")
        sizePolicy2.setHeightForWidth(self.btn_ok_setsend1.sizePolicy().hasHeightForWidth())
        self.btn_ok_setsend1.setSizePolicy(sizePolicy2)
        self.btn_ok_setsend1.setFont(font5)

        self.horizontalLayout_12.addWidget(self.btn_ok_setsend1)

        self.line_5 = QFrame(self.verticalLayoutWidget_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_12.addWidget(self.line_5)

        self.label_6 = QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_12.addWidget(self.label_6)

        self.text_state = QLabel(self.verticalLayoutWidget_4)
        self.text_state.setObjectName(u"text_state")

        self.horizontalLayout_12.addWidget(self.text_state)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 3)
        self.horizontalLayout_12.setStretch(2, 1)
        self.horizontalLayout_12.setStretch(3, 1)
        self.horizontalLayout_12.setStretch(4, 1)
        self.horizontalLayout_12.setStretch(5, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.table_serial = QTableWidget(self.verticalLayoutWidget_4)
        if (self.table_serial.columnCount() < 4):
            self.table_serial.setColumnCount(4)
        font6 = QFont()
        font6.setPointSize(9)
        font6.setBold(True)
        font6.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font6);
        self.table_serial.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font7 = QFont()
        font7.setFamily(u"MS Shell Dlg 2")
        font7.setBold(True)
        font7.setWeight(75)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font7);
        self.table_serial.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font6);
        self.table_serial.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font6);
        self.table_serial.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_serial.setObjectName(u"table_serial")
        font8 = QFont()
        font8.setPointSize(10)
        self.table_serial.setFont(font8)
        self.table_serial.setLayoutDirection(Qt.LeftToRight)
        self.table_serial.setFrameShape(QFrame.NoFrame)
        self.table_serial.setFrameShadow(QFrame.Raised)
        self.table_serial.setLineWidth(1)
        self.table_serial.setMidLineWidth(0)
        self.table_serial.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_serial.setAutoScrollMargin(4)
        self.table_serial.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_serial.setAlternatingRowColors(True)
        self.table_serial.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_serial.setTextElideMode(Qt.ElideRight)
        self.table_serial.setShowGrid(True)
        self.table_serial.setSortingEnabled(False)
        self.table_serial.setWordWrap(True)
        self.table_serial.setRowCount(0)
        self.table_serial.setColumnCount(4)
        self.table_serial.horizontalHeader().setCascadingSectionResizes(False)
        self.table_serial.horizontalHeader().setDefaultSectionSize(75)
        self.table_serial.horizontalHeader().setStretchLastSection(True)
        self.table_serial.verticalHeader().setVisible(False)
        self.table_serial.verticalHeader().setMinimumSectionSize(20)
        self.table_serial.verticalHeader().setDefaultSectionSize(20)

        self.verticalLayout_4.addWidget(self.table_serial)

        self.line_6 = QFrame(self.verticalLayoutWidget_4)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_6)

        self.prog_bar_eeprom_used = QProgressBar(self.verticalLayoutWidget_4)
        self.prog_bar_eeprom_used.setObjectName(u"prog_bar_eeprom_used")
        self.prog_bar_eeprom_used.setValue(0)

        self.verticalLayout_4.addWidget(self.prog_bar_eeprom_used)

        self.verticalLayout_4.setStretch(0, 6)
        self.verticalLayout_4.setStretch(2, 22)
        self.verticalLayout_4.setStretch(3, 1)

        self.horizontalLayout.addWidget(self.groupBox_slave)

        self.horizontalLayout.setStretch(0, 11)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 10)

        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, 0, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer)

        self.btn_informe = QPushButton(self.verticalLayoutWidget_6)
        self.btn_informe.setObjectName(u"btn_informe")
        self.btn_informe.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.btn_informe.sizePolicy().hasHeightForWidth())
        self.btn_informe.setSizePolicy(sizePolicy2)
        self.btn_informe.setFont(font1)

        self.horizontalLayout_15.addWidget(self.btn_informe)

        self.btn_exit = QPushButton(self.verticalLayoutWidget_6)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy3)
        self.btn_exit.setFont(font1)

        self.horizontalLayout_15.addWidget(self.btn_exit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_2)

        self.horizontalLayout_15.setStretch(0, 2)
        self.horizontalLayout_15.setStretch(1, 1)
        self.horizontalLayout_15.setStretch(2, 1)
        self.horizontalLayout_15.setStretch(3, 2)

        self.verticalLayout_6.addLayout(self.horizontalLayout_15)

        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(1, 4)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(3, 16)
        self.verticalLayout_6.setStretch(4, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Simulaci\u00f3n carga \u00fatil", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Puerto Master:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Puerto Slave:", None))
        self.btn_init.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.img_logo1.setText("")
        self.img_logo2.setText("")
        self.groupBox_master.setTitle(QCoreApplication.translate("MainWindow", u"Slave", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Meas 1", None))
        self.value_out1.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Meas 2", None))
        self.value_out2.setText("")
        self.groupBox_slave.setTitle(QCoreApplication.translate("MainWindow", u"Master", None))
        self.lcd_date_rtc.setText(QCoreApplication.translate("MainWindow", u"24-02-2024", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Set:", None))
        self.set_time_send1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.btn_ok_setsend1.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"State:", None))
        self.text_state.setText("")
        ___qtablewidgetitem = self.table_serial.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_serial.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None));
        ___qtablewidgetitem2 = self.table_serial.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Value[V]", None));
        ___qtablewidgetitem3 = self.table_serial.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"DateTime", None));
        self.btn_informe.setText(QCoreApplication.translate("MainWindow", u"Informe", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

