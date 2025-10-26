# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_read_bg51.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QButtonGroup,
    QComboBox, QFrame, QHBoxLayout, QHeaderView,
    QLCDNumber, QLabel, QMainWindow, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1029, 799)
        MainWindow.setStyleSheet(u"background-color: rgb(230, 230, 230);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_9 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(20, 20, 981, 761))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(20, 10, 20, 10)
        self.img_logo1 = QLabel(self.verticalLayoutWidget_9)
        self.img_logo1.setObjectName(u"img_logo1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_logo1.sizePolicy().hasHeightForWidth())
        self.img_logo1.setSizePolicy(sizePolicy)
        self.img_logo1.setPixmap(QPixmap(u"../.designer/Documents/PocketCube/app/Imagenes/logotipo_diysatellite.png"))
        self.img_logo1.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.img_logo1)

        self.img_logo2 = QLabel(self.verticalLayoutWidget_9)
        self.img_logo2.setObjectName(u"img_logo2")
        sizePolicy.setHeightForWidth(self.img_logo2.sizePolicy().hasHeightForWidth())
        self.img_logo2.setSizePolicy(sizePolicy)
        self.img_logo2.setPixmap(QPixmap(u"../.designer/Documents/PocketCube/app/Imagenes/logotipo_simple_utn_haedo.png"))
        self.img_logo2.setScaledContents(True)
        self.img_logo2.setMargin(4)

        self.horizontalLayout_12.addWidget(self.img_logo2)

        self.horizontalLayout_12.setStretch(0, 2)
        self.horizontalLayout_12.setStretch(1, 7)

        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.lcd_time_rtc = QLCDNumber(self.verticalLayoutWidget_9)
        self.lcd_time_rtc.setObjectName(u"lcd_time_rtc")
        self.lcd_time_rtc.setLayoutDirection(Qt.RightToLeft)
        self.lcd_time_rtc.setFrameShape(QFrame.NoFrame)
        self.lcd_time_rtc.setFrameShadow(QFrame.Plain)
        self.lcd_time_rtc.setLineWidth(1)
        self.lcd_time_rtc.setSmallDecimalPoint(False)
        self.lcd_time_rtc.setDigitCount(8)
        self.lcd_time_rtc.setMode(QLCDNumber.Dec)
        self.lcd_time_rtc.setSegmentStyle(QLCDNumber.Flat)

        self.verticalLayout_5.addWidget(self.lcd_time_rtc)

        self.lcd_date_rtc = QLabel(self.verticalLayoutWidget_9)
        self.lcd_date_rtc.setObjectName(u"lcd_date_rtc")
        font = QFont()
        font.setFamilies([u"Courier"])
        font.setBold(True)
        self.lcd_date_rtc.setFont(font)
        self.lcd_date_rtc.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lcd_date_rtc)

        self.verticalLayout_5.setStretch(0, 8)
        self.verticalLayout_5.setStretch(1, 4)
        self.verticalLayout_5.setStretch(2, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 30, -1, 30)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.verticalLayoutWidget_9)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_6.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.cbox_in_serial = QComboBox(self.verticalLayoutWidget_9)
        self.cbox_in_serial.setObjectName(u"cbox_in_serial")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cbox_in_serial.sizePolicy().hasHeightForWidth())
        self.cbox_in_serial.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(12)
        self.cbox_in_serial.setFont(font2)
        self.cbox_in_serial.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.cbox_in_serial)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_5 = QLabel(self.verticalLayoutWidget_9)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.sbox_time_intervalo = QSpinBox(self.verticalLayoutWidget_9)
        self.sbox_time_intervalo.setObjectName(u"sbox_time_intervalo")
        sizePolicy1.setHeightForWidth(self.sbox_time_intervalo.sizePolicy().hasHeightForWidth())
        self.sbox_time_intervalo.setSizePolicy(sizePolicy1)
        self.sbox_time_intervalo.setFont(font2)
        self.sbox_time_intervalo.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sbox_time_intervalo.setAlignment(Qt.AlignCenter)
        self.sbox_time_intervalo.setMinimum(1)
        self.sbox_time_intervalo.setMaximum(60)
        self.sbox_time_intervalo.setValue(1)

        self.horizontalLayout_6.addWidget(self.sbox_time_intervalo)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.rbtn_seg = QRadioButton(self.verticalLayoutWidget_9)
        self.buttonGroup_3 = QButtonGroup(MainWindow)
        self.buttonGroup_3.setObjectName(u"buttonGroup_3")
        self.buttonGroup_3.addButton(self.rbtn_seg)
        self.rbtn_seg.setObjectName(u"rbtn_seg")
        sizePolicy1.setHeightForWidth(self.rbtn_seg.sizePolicy().hasHeightForWidth())
        self.rbtn_seg.setSizePolicy(sizePolicy1)
        self.rbtn_seg.setFont(font2)
        self.rbtn_seg.setChecked(True)

        self.horizontalLayout_7.addWidget(self.rbtn_seg)

        self.rbtn_min = QRadioButton(self.verticalLayoutWidget_9)
        self.buttonGroup_3.addButton(self.rbtn_min)
        self.rbtn_min.setObjectName(u"rbtn_min")
        sizePolicy1.setHeightForWidth(self.rbtn_min.sizePolicy().hasHeightForWidth())
        self.rbtn_min.setSizePolicy(sizePolicy1)
        self.rbtn_min.setFont(font2)

        self.horizontalLayout_7.addWidget(self.rbtn_min)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 1)

        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 3)
        self.horizontalLayout_6.setStretch(2, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_7 = QLabel(self.verticalLayoutWidget_9)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font1)
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setTextFormat(Qt.PlainText)
        self.label_7.setScaledContents(True)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_7)

        self.sbox_time_test = QSpinBox(self.verticalLayoutWidget_9)
        self.sbox_time_test.setObjectName(u"sbox_time_test")
        sizePolicy1.setHeightForWidth(self.sbox_time_test.sizePolicy().hasHeightForWidth())
        self.sbox_time_test.setSizePolicy(sizePolicy1)
        self.sbox_time_test.setFont(font2)
        self.sbox_time_test.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sbox_time_test.setAlignment(Qt.AlignCenter)
        self.sbox_time_test.setMinimum(1)
        self.sbox_time_test.setMaximum(60)
        self.sbox_time_test.setValue(1)

        self.horizontalLayout_10.addWidget(self.sbox_time_test)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(3)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.rbtn_seg_2 = QRadioButton(self.verticalLayoutWidget_9)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.rbtn_seg_2)
        self.rbtn_seg_2.setObjectName(u"rbtn_seg_2")
        sizePolicy1.setHeightForWidth(self.rbtn_seg_2.sizePolicy().hasHeightForWidth())
        self.rbtn_seg_2.setSizePolicy(sizePolicy1)
        self.rbtn_seg_2.setFont(font2)
        self.rbtn_seg_2.setChecked(False)

        self.horizontalLayout_11.addWidget(self.rbtn_seg_2)

        self.rbtn_min_2 = QRadioButton(self.verticalLayoutWidget_9)
        self.buttonGroup.addButton(self.rbtn_min_2)
        self.rbtn_min_2.setObjectName(u"rbtn_min_2")
        sizePolicy1.setHeightForWidth(self.rbtn_min_2.sizePolicy().hasHeightForWidth())
        self.rbtn_min_2.setSizePolicy(sizePolicy1)
        self.rbtn_min_2.setFont(font2)
        self.rbtn_min_2.setChecked(True)

        self.horizontalLayout_11.addWidget(self.rbtn_min_2)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)

        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10.setStretch(0, 2)
        self.horizontalLayout_10.setStretch(1, 3)
        self.horizontalLayout_10.setStretch(2, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_init = QPushButton(self.verticalLayoutWidget_9)
        self.btn_init.setObjectName(u"btn_init")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_init.sizePolicy().hasHeightForWidth())
        self.btn_init.setSizePolicy(sizePolicy3)
        self.btn_init.setFont(font2)

        self.verticalLayout_2.addWidget(self.btn_init)

        self.btn_stop = QPushButton(self.verticalLayoutWidget_9)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy3)
        self.btn_stop.setFont(font2)

        self.verticalLayout_2.addWidget(self.btn_stop)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 30, -1, 30)
        self.btn_reset = QPushButton(self.verticalLayoutWidget_9)
        self.btn_reset.setObjectName(u"btn_reset")
        self.btn_reset.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.btn_reset.sizePolicy().hasHeightForWidth())
        self.btn_reset.setSizePolicy(sizePolicy3)
        self.btn_reset.setFont(font2)

        self.verticalLayout_10.addWidget(self.btn_reset)

        self.btn_csv = QPushButton(self.verticalLayoutWidget_9)
        self.btn_csv.setObjectName(u"btn_csv")
        self.btn_csv.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.btn_csv.sizePolicy().hasHeightForWidth())
        self.btn_csv.setSizePolicy(sizePolicy3)
        self.btn_csv.setFont(font2)
        self.btn_csv.setCheckable(False)

        self.verticalLayout_10.addWidget(self.btn_csv)

        self.verticalLayout_10.setStretch(0, 1)
        self.verticalLayout_10.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_10)

        self.horizontalLayout.setStretch(0, 14)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 4)

        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.graph_out1 = QVBoxLayout()
        self.graph_out1.setObjectName(u"graph_out1")

        self.horizontalLayout_14.addLayout(self.graph_out1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.table_cp = QTableWidget(self.verticalLayoutWidget_9)
        if (self.table_cp.columnCount() < 4):
            self.table_cp.setColumnCount(4)
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font3);
        __qtablewidgetitem.setBackground(QColor(255, 255, 255));
        self.table_cp.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font3);
        self.table_cp.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font3);
        self.table_cp.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font3);
        self.table_cp.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_cp.setObjectName(u"table_cp")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.table_cp.sizePolicy().hasHeightForWidth())
        self.table_cp.setSizePolicy(sizePolicy4)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(9)
        self.table_cp.setFont(font4)
        self.table_cp.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.table_cp.setFrameShape(QFrame.Box)
        self.table_cp.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_cp.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.table_cp.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_cp.setTabKeyNavigation(True)
        self.table_cp.setProperty(u"showDropIndicator", True)
        self.table_cp.setAlternatingRowColors(True)
        self.table_cp.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_cp.setTextElideMode(Qt.ElideMiddle)
        self.table_cp.setShowGrid(True)
        self.table_cp.setGridStyle(Qt.SolidLine)
        self.table_cp.setWordWrap(True)
        self.table_cp.setCornerButtonEnabled(True)
        self.table_cp.setRowCount(0)
        self.table_cp.horizontalHeader().setCascadingSectionResizes(False)
        self.table_cp.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table_cp.horizontalHeader().setStretchLastSection(True)
        self.table_cp.verticalHeader().setVisible(False)
        self.table_cp.verticalHeader().setCascadingSectionResizes(False)
        self.table_cp.verticalHeader().setProperty(u"showSortIndicator", False)
        self.table_cp.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_18.addWidget(self.table_cp)

        self.horizontalLayout_18.setStretch(0, 12)

        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.pbar_interval = QProgressBar(self.verticalLayoutWidget_9)
        self.pbar_interval.setObjectName(u"pbar_interval")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(7)
        self.pbar_interval.setFont(font5)
        self.pbar_interval.setLayoutDirection(Qt.RightToLeft)
        self.pbar_interval.setValue(0)
        self.pbar_interval.setAlignment(Qt.AlignCenter)
        self.pbar_interval.setTextVisible(True)
        self.pbar_interval.setOrientation(Qt.Horizontal)
        self.pbar_interval.setInvertedAppearance(True)
        self.pbar_interval.setTextDirection(QProgressBar.BottomToTop)

        self.verticalLayout_4.addWidget(self.pbar_interval)

        self.verticalLayout_4.setStretch(0, 12)
        self.verticalLayout_4.setStretch(1, 1)

        self.horizontalLayout_14.addLayout(self.verticalLayout_4)

        self.horizontalLayout_14.setStretch(0, 25)
        self.horizontalLayout_14.setStretch(1, 18)

        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.graph_out2 = QVBoxLayout()
        self.graph_out2.setObjectName(u"graph_out2")

        self.horizontalLayout_15.addLayout(self.graph_out2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.table_dosis = QTableWidget(self.verticalLayoutWidget_9)
        if (self.table_dosis.columnCount() < 3):
            self.table_dosis.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font3);
        self.table_dosis.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font3);
        self.table_dosis.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font3);
        self.table_dosis.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.table_dosis.setObjectName(u"table_dosis")
        self.table_dosis.setFont(font4)
        self.table_dosis.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.table_dosis.setFrameShape(QFrame.Box)
        self.table_dosis.setFrameShadow(QFrame.Sunken)
        self.table_dosis.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_dosis.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_dosis.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_dosis.setTabKeyNavigation(True)
        self.table_dosis.setProperty(u"showDropIndicator", True)
        self.table_dosis.setDragDropOverwriteMode(True)
        self.table_dosis.setAlternatingRowColors(True)
        self.table_dosis.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_dosis.setTextElideMode(Qt.ElideMiddle)
        self.table_dosis.setRowCount(0)
        self.table_dosis.horizontalHeader().setVisible(True)
        self.table_dosis.horizontalHeader().setCascadingSectionResizes(True)
        self.table_dosis.horizontalHeader().setDefaultSectionSize(100)
        self.table_dosis.horizontalHeader().setHighlightSections(True)
        self.table_dosis.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table_dosis.horizontalHeader().setStretchLastSection(True)
        self.table_dosis.verticalHeader().setVisible(False)

        self.verticalLayout_6.addWidget(self.table_dosis)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_9 = QLabel(self.verticalLayoutWidget_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_9)

        self.label_state = QLabel(self.verticalLayoutWidget_9)
        self.label_state.setObjectName(u"label_state")
        self.label_state.setFont(font2)
        self.label_state.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_state)

        self.horizontalLayout_13.setStretch(0, 1)
        self.horizontalLayout_13.setStretch(1, 3)

        self.verticalLayout_6.addLayout(self.horizontalLayout_13)

        self.verticalLayout_6.setStretch(0, 5)
        self.verticalLayout_6.setStretch(1, 1)

        self.horizontalLayout_15.addLayout(self.verticalLayout_6)

        self.horizontalLayout_15.setStretch(0, 25)
        self.horizontalLayout_15.setStretch(1, 18)

        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.verticalLayout_7.setStretch(0, 9)
        self.verticalLayout_7.setStretch(1, 9)

        self.horizontalLayout_16.addLayout(self.verticalLayout_7)

        self.horizontalLayout_16.setStretch(0, 25)

        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.verticalLayout_8.setStretch(0, 3)
        self.verticalLayout_8.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_logo1.setText("")
        self.img_logo2.setText("")
        self.lcd_date_rtc.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Input Data:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Intervalo:", None))
        self.rbtn_seg.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.rbtn_min.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Duraci\u00f3n \n"
" de ensayo:", None))
        self.rbtn_seg_2.setText(QCoreApplication.translate("MainWindow", u"s", None))
        self.rbtn_min_2.setText(QCoreApplication.translate("MainWindow", u"min", None))
        self.btn_init.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"Finalizar", None))
        self.btn_reset.setText(QCoreApplication.translate("MainWindow", u"Nuevo \n"
"ensayo", None))
        self.btn_csv.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        ___qtablewidgetitem = self.table_cp.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Time[s]", None));
        ___qtablewidgetitem1 = self.table_cp.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Int.[s]", None));
        ___qtablewidgetitem2 = self.table_cp.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Datetime", None));
        ___qtablewidgetitem3 = self.table_cp.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Count Pulse", None));
        ___qtablewidgetitem4 = self.table_dosis.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Int.[s]", None));
        ___qtablewidgetitem5 = self.table_dosis.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Datetime", None));
        ___qtablewidgetitem6 = self.table_dosis.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"CPS", None));
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.label_state.setText(QCoreApplication.translate("MainWindow", u"Lectura", None))
    # retranslateUi

