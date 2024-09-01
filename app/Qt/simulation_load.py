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
        MainWindow.resize(924, 721)
        MainWindow.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(20, 10, 891, 681))
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
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 441, 401))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lcd_timer = QLCDNumber(self.verticalLayoutWidget)
        self.lcd_timer.setObjectName(u"lcd_timer")
        self.lcd_timer.setLayoutDirection(Qt.RightToLeft)
        self.lcd_timer.setFrameShape(QFrame.NoFrame)
        self.lcd_timer.setFrameShadow(QFrame.Plain)
        self.lcd_timer.setLineWidth(1)
        self.lcd_timer.setSmallDecimalPoint(False)
        self.lcd_timer.setDigitCount(8)
        self.lcd_timer.setMode(QLCDNumber.Dec)
        self.lcd_timer.setSegmentStyle(QLCDNumber.Flat)

        self.horizontalLayout_18.addWidget(self.lcd_timer)

        self.horizontalLayout_18.setStretch(0, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_18)

        self.lcd_timer_total = QLCDNumber(self.verticalLayoutWidget)
        self.lcd_timer_total.setObjectName(u"lcd_timer_total")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.lcd_timer_total.setFont(font3)
        self.lcd_timer_total.setLayoutDirection(Qt.RightToLeft)
        self.lcd_timer_total.setFrameShape(QFrame.NoFrame)
        self.lcd_timer_total.setFrameShadow(QFrame.Plain)
        self.lcd_timer_total.setLineWidth(1)
        self.lcd_timer_total.setSmallDecimalPoint(False)
        self.lcd_timer_total.setDigitCount(8)
        self.lcd_timer_total.setMode(QLCDNumber.Dec)
        self.lcd_timer_total.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout.addWidget(self.lcd_timer_total)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        font4 = QFont()
        font4.setPointSize(9)
        self.label_9.setFont(font4)

        self.horizontalLayout_12.addWidget(self.label_9)

        self.set_time_send1 = QTimeEdit(self.verticalLayoutWidget)
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

        self.btn_ok_setsend1 = QPushButton(self.verticalLayoutWidget)
        self.btn_ok_setsend1.setObjectName(u"btn_ok_setsend1")
        sizePolicy2.setHeightForWidth(self.btn_ok_setsend1.sizePolicy().hasHeightForWidth())
        self.btn_ok_setsend1.setSizePolicy(sizePolicy2)
        self.btn_ok_setsend1.setFont(font4)

        self.horizontalLayout_12.addWidget(self.btn_ok_setsend1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_12.setStretch(0, 4)
        self.horizontalLayout_12.setStretch(1, 1)
        self.horizontalLayout_12.setStretch(2, 4)
        self.horizontalLayout_12.setStretch(3, 1)
        self.horizontalLayout_12.setStretch(4, 4)

        self.verticalLayout.addLayout(self.horizontalLayout_12)

        self.line_3 = QFrame(self.verticalLayoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_4.setFont(font5)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_4)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_19.addWidget(self.label_12)

        self.btn_yes_in1 = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.btn_yes_in1)
        self.btn_yes_in1.setObjectName(u"btn_yes_in1")
        self.btn_yes_in1.setChecked(True)

        self.horizontalLayout_19.addWidget(self.btn_yes_in1)

        self.btn_no_in1 = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup.addButton(self.btn_no_in1)
        self.btn_no_in1.setObjectName(u"btn_no_in1")

        self.horizontalLayout_19.addWidget(self.btn_no_in1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_19.setStretch(0, 2)
        self.horizontalLayout_19.setStretch(1, 1)
        self.horizontalLayout_19.setStretch(2, 1)
        self.horizontalLayout_19.setStretch(3, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_19)

        self.value_out1 = QLabel(self.verticalLayoutWidget)
        self.value_out1.setObjectName(u"value_out1")
        self.value_out1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.value_out1)

        self.graph_out1 = QVBoxLayout()
        self.graph_out1.setObjectName(u"graph_out1")

        self.verticalLayout_7.addLayout(self.graph_out1)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        font6 = QFont()
        font6.setPointSize(10)
        self.label_11.setFont(font6)

        self.horizontalLayout_17.addWidget(self.label_11)

        self.label_send1 = QLabel(self.verticalLayoutWidget)
        self.label_send1.setObjectName(u"label_send1")
        self.label_send1.setFont(font6)

        self.horizontalLayout_17.addWidget(self.label_send1)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 2)

        self.verticalLayout_7.addLayout(self.horizontalLayout_17)

        self.verticalLayout_7.setStretch(0, 1)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_7.setStretch(2, 1)
        self.verticalLayout_7.setStretch(3, 10)
        self.verticalLayout_7.setStretch(4, 1)

        self.horizontalLayout_14.addLayout(self.verticalLayout_7)

        self.line_2 = QFrame(self.verticalLayoutWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_14.addWidget(self.line_2)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font5)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_5)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_14 = QLabel(self.verticalLayoutWidget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_21.addWidget(self.label_14)

        self.btn_yes_in2 = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_2 = QButtonGroup(MainWindow)
        self.buttonGroup_2.setObjectName(u"buttonGroup_2")
        self.buttonGroup_2.addButton(self.btn_yes_in2)
        self.btn_yes_in2.setObjectName(u"btn_yes_in2")
        self.btn_yes_in2.setChecked(True)

        self.horizontalLayout_21.addWidget(self.btn_yes_in2)

        self.btn_no_in2 = QRadioButton(self.verticalLayoutWidget)
        self.buttonGroup_2.addButton(self.btn_no_in2)
        self.btn_no_in2.setObjectName(u"btn_no_in2")

        self.horizontalLayout_21.addWidget(self.btn_no_in2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_8)

        self.horizontalLayout_21.setStretch(0, 2)
        self.horizontalLayout_21.setStretch(1, 1)
        self.horizontalLayout_21.setStretch(2, 1)
        self.horizontalLayout_21.setStretch(3, 2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_21)

        self.value_out2 = QLabel(self.verticalLayoutWidget)
        self.value_out2.setObjectName(u"value_out2")
        self.value_out2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.value_out2)

        self.graph_out2 = QVBoxLayout()
        self.graph_out2.setObjectName(u"graph_out2")

        self.verticalLayout_8.addLayout(self.graph_out2)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font6)

        self.horizontalLayout_20.addWidget(self.label_13)

        self.label_send2 = QLabel(self.verticalLayoutWidget)
        self.label_send2.setObjectName(u"label_send2")
        self.label_send2.setFont(font6)

        self.horizontalLayout_20.addWidget(self.label_send2)

        self.horizontalLayout_20.setStretch(0, 1)
        self.horizontalLayout_20.setStretch(1, 2)

        self.verticalLayout_8.addLayout(self.horizontalLayout_20)

        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 1)
        self.verticalLayout_8.setStretch(2, 1)
        self.verticalLayout_8.setStretch(3, 10)
        self.verticalLayout_8.setStretch(4, 1)

        self.horizontalLayout_14.addLayout(self.verticalLayout_8)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 1)
        self.horizontalLayout_14.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_14)

        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 19)

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
        self.verticalLayoutWidget_4.setGeometry(QRect(20, 30, 371, 391))
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
        font7 = QFont()
        font7.setFamily(u"Courier")
        font7.setBold(True)
        font7.setWeight(75)
        self.lcd_date_rtc.setFont(font7)
        self.lcd_date_rtc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lcd_date_rtc)

        self.verticalLayout_2.setStretch(0, 10)
        self.verticalLayout_2.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.table_serial = QTableWidget(self.verticalLayoutWidget_4)
        if (self.table_serial.columnCount() < 4):
            self.table_serial.setColumnCount(4)
        font8 = QFont()
        font8.setPointSize(9)
        font8.setBold(True)
        font8.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font8);
        self.table_serial.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font9 = QFont()
        font9.setFamily(u"MS Shell Dlg 2")
        font9.setBold(True)
        font9.setWeight(75)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font9);
        self.table_serial.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font8);
        self.table_serial.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font8);
        self.table_serial.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_serial.setObjectName(u"table_serial")
        self.table_serial.setFont(font6)
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

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.verticalLayoutWidget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_10)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(1)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.btn_manual_out1 = QRadioButton(self.verticalLayoutWidget_4)
        self.buttonGroup_3 = QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.btn_manual_out1)
        self.btn_manual_out1.setObjectName(u"btn_manual_out1")
        self.btn_manual_out1.setChecked(True)

        self.verticalLayout_10.addWidget(self.btn_manual_out1)

        self.btn_test_out1 = QRadioButton(self.verticalLayoutWidget_4)
        self.buttonGroup_3.addButton(self.btn_test_out1)
        self.btn_test_out1.setObjectName(u"btn_test_out1")

        self.verticalLayout_10.addWidget(self.btn_test_out1)


        self.horizontalLayout_22.addLayout(self.verticalLayout_10)

        self.sbox_volt1 = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.sbox_volt1.setObjectName(u"sbox_volt1")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.sbox_volt1.sizePolicy().hasHeightForWidth())
        self.sbox_volt1.setSizePolicy(sizePolicy3)
        self.sbox_volt1.setFont(font1)
        self.sbox_volt1.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sbox_volt1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbox_volt1.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.sbox_volt1.setMaximum(5.000000000000000)
        self.sbox_volt1.setSingleStep(0.100000000000000)

        self.horizontalLayout_22.addWidget(self.sbox_volt1)

        self.label_15 = QLabel(self.verticalLayoutWidget_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.horizontalLayout_22.addWidget(self.label_15)

        self.horizontalLayout_22.setStretch(0, 2)
        self.horizontalLayout_22.setStretch(1, 4)
        self.horizontalLayout_22.setStretch(2, 1)

        self.verticalLayout_5.addLayout(self.horizontalLayout_22)

        self.verticalLayout_5.setStretch(0, 1)
        self.verticalLayout_5.setStretch(1, 1)

        self.horizontalLayout_16.addLayout(self.verticalLayout_5)

        self.line_5 = QFrame(self.verticalLayoutWidget_4)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_16.addWidget(self.line_5)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.verticalLayoutWidget_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_8)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setSpacing(1)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.btn_manual_out2 = QRadioButton(self.verticalLayoutWidget_4)
        self.buttonGroup_4 = QButtonGroup(MainWindow)
        self.buttonGroup_4.setObjectName(u"buttonGroup_4")
        self.buttonGroup_4.addButton(self.btn_manual_out2)
        self.btn_manual_out2.setObjectName(u"btn_manual_out2")
        self.btn_manual_out2.setChecked(True)

        self.verticalLayout_11.addWidget(self.btn_manual_out2)

        self.btn_test_out2 = QRadioButton(self.verticalLayoutWidget_4)
        self.buttonGroup_4.addButton(self.btn_test_out2)
        self.btn_test_out2.setObjectName(u"btn_test_out2")

        self.verticalLayout_11.addWidget(self.btn_test_out2)


        self.horizontalLayout_23.addLayout(self.verticalLayout_11)

        self.sbox_volt2 = QDoubleSpinBox(self.verticalLayoutWidget_4)
        self.sbox_volt2.setObjectName(u"sbox_volt2")
        sizePolicy3.setHeightForWidth(self.sbox_volt2.sizePolicy().hasHeightForWidth())
        self.sbox_volt2.setSizePolicy(sizePolicy3)
        self.sbox_volt2.setFont(font1)
        self.sbox_volt2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sbox_volt2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.sbox_volt2.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.sbox_volt2.setMaximum(5.000000000000000)
        self.sbox_volt2.setSingleStep(0.100000000000000)

        self.horizontalLayout_23.addWidget(self.sbox_volt2)

        self.label_16 = QLabel(self.verticalLayoutWidget_4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)

        self.horizontalLayout_23.addWidget(self.label_16)

        self.horizontalLayout_23.setStretch(0, 2)
        self.horizontalLayout_23.setStretch(1, 4)
        self.horizontalLayout_23.setStretch(2, 1)

        self.verticalLayout_9.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_16.addLayout(self.verticalLayout_9)

        self.horizontalLayout_16.setStretch(0, 2)
        self.horizontalLayout_16.setStretch(1, 1)
        self.horizontalLayout_16.setStretch(2, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.verticalLayout_4.setStretch(0, 6)
        self.verticalLayout_4.setStretch(1, 20)
        self.verticalLayout_4.setStretch(2, 1)
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
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Set:", None))
        self.set_time_send1.setDisplayFormat(QCoreApplication.translate("MainWindow", u"HH:mm:ss", None))
        self.btn_ok_setsend1.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Geiger", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Medici\u00f3n real:", None))
        self.btn_yes_in1.setText(QCoreApplication.translate("MainWindow", u"Si", None))
        self.btn_no_in1.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.value_out1.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Send:", None))
        self.label_send1.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Medici\u00f3n real:", None))
        self.btn_yes_in2.setText(QCoreApplication.translate("MainWindow", u"Si", None))
        self.btn_no_in2.setText(QCoreApplication.translate("MainWindow", u"No", None))
        self.value_out2.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Send:", None))
        self.label_send2.setText("")
        self.groupBox_slave.setTitle(QCoreApplication.translate("MainWindow", u"Master", None))
        self.lcd_date_rtc.setText(QCoreApplication.translate("MainWindow", u"24-02-2024", None))
        ___qtablewidgetitem = self.table_serial.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.table_serial.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n", None));
        ___qtablewidgetitem2 = self.table_serial.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Value[V]", None));
        ___qtablewidgetitem3 = self.table_serial.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"DateTime", None));
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"DAC Geiger", None))
        self.btn_manual_out1.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.btn_test_out1.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"DAC Source", None))
        self.btn_manual_out2.setText(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.btn_test_out2.setText(QCoreApplication.translate("MainWindow", u"Test", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.btn_informe.setText(QCoreApplication.translate("MainWindow", u"Informe", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
    # retranslateUi

