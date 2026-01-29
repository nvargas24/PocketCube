# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_test_attiny.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QComboBox, QFrame, QGroupBox, QHBoxLayout,
    QHeaderView, QLCDNumber, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QTimeEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 591)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"/* =========================\n"
"   BASE\n"
"   ========================= */\n"
"QWidget {\n"
"    background-color: #F3F3F3;\n"
"    color: #1F1F1F;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 10pt;\n"
"}\n"
"\n"
"/* =========================\n"
"   LINE EDIT / TIME EDIT\n"
"   ========================= */\n"
"QLineEdit, QTimeEdit {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D1D1D1;\n"
"    border-radius: 6px;\n"
"    padding: 6px 8px;\n"
"}\n"
"\n"
"QLineEdit:hover, QTimeEdit:hover {\n"
"    border: 1px solid #A8A8A8;\n"
"}\n"
"\n"
"QLineEdit:focus, QTimeEdit:focus {\n"
"    border: 2px solid #2563EB;\n"
"    padding: 5px 7px; /* compensar el borde */\n"
"}\n"
"\n"
"QLineEdit:disabled, QTimeEdit:disabled {\n"
"    background-color: #E5E5E5;\n"
"    color: #9A9A9A;\n"
"}\n"
"\n"
"/* =========================\n"
"   COMBO BOX\n"
"   ========================= */\n"
"QComboBox {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D1D1D1;\n"
"    border-radius: 6px;\n"
"    "
                        "padding: 6px 30px 6px 8px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 1px solid #A8A8A8;\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"    border: 2px solid #2563EB;\n"
"    padding: 5px 29px 5px 7px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 24px;\n"
"    border-left: 1px solid #D1D1D1;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: none;\n"
"    width: 0;\n"
"    height: 0;\n"
"    border-left: 5px solid transparent;\n"
"    border-right: 5px solid transparent;\n"
"    border-top: 6px solid #4A4A4A;\n"
"}\n"
"\n"
"/* Lista desplegable */\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D1D1D1;\n"
"    selection-background-color: #E8F0FE;\n"
"    selection-color: #1F1F1F;\n"
"}\n"
"\n"
"/* =========================\n"
"   PUSH BUTTON\n"
"   ========================= */\n"
"QPushButton {\n"
"    background-color: #798FFC;\n"
"    color: white;\n"
"    border: none;\n"
"    b"
                        "order-radius: 8px;\n"
"    padding: 6px 14px;\n"
"    font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1D4ED8;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1E40AF;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #C7C7C7;\n"
"    color: #8A8A8A;\n"
"}\n"
"\n"
"/* =========================\n"
"   TABLE\n"
"   ========================= */\n"
"QTableView, QTableWidget {\n"
"    background-color: #FFFFFF;\n"
"    border: 1px solid #D1D1D1;\n"
"    border-radius: 8px;\n"
"    gridline-color: #E0E0E0;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #F3F3F3;\n"
"    color: #1F1F1F;\n"
"    padding: 6px;\n"
"    border: none;\n"
"    border-bottom: 1px solid #D1D1D1;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QTableView::item:selected {\n"
"    background-color: #E8F0FE;\n"
"    color: #1F1F1F;\n"
"}\n"
"\n"
"/* Scrollbar estilo Win 11 */\n"
"QScrollBar:vertical {\n"
"    background: t"
                        "ransparent;\n"
"    width: 10px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background: #C4C4C4;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical:hover {\n"
"    background: #A8A8A8;\n"
"}\n"
"\n"
"QScrollBar::add-line,\n"
"QScrollBar::sub-line {\n"
"    height: 0px;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget_9 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_9.setObjectName(u"verticalLayoutWidget_9")
        self.verticalLayoutWidget_9.setGeometry(QRect(20, 20, 841, 551))
        self.verticalLayout_8 = QVBoxLayout(self.verticalLayoutWidget_9)
        self.verticalLayout_8.setSpacing(15)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
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
        self.img_logo1.setPixmap(QPixmap(u"../../../../../.designer/.designer/Documents/PocketCube/app/Imagenes/logotipo_diysatellite.png"))
        self.img_logo1.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.img_logo1)

        self.img_logo2 = QLabel(self.verticalLayoutWidget_9)
        self.img_logo2.setObjectName(u"img_logo2")
        sizePolicy.setHeightForWidth(self.img_logo2.sizePolicy().hasHeightForWidth())
        self.img_logo2.setSizePolicy(sizePolicy)
        self.img_logo2.setPixmap(QPixmap(u"../../../../../.designer/.designer/Documents/PocketCube/app/Imagenes/logotipo_simple_utn_haedo.png"))
        self.img_logo2.setScaledContents(True)
        self.img_logo2.setMargin(4)

        self.horizontalLayout_12.addWidget(self.img_logo2)

        self.horizontalLayout_12.setStretch(0, 2)
        self.horizontalLayout_12.setStretch(1, 7)

        self.horizontalLayout.addLayout(self.horizontalLayout_12)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lcd_time_pc = QLCDNumber(self.verticalLayoutWidget_9)
        self.lcd_time_pc.setObjectName(u"lcd_time_pc")
        self.lcd_time_pc.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lcd_time_pc.setFrameShape(QFrame.Shape.NoFrame)
        self.lcd_time_pc.setFrameShadow(QFrame.Shadow.Plain)
        self.lcd_time_pc.setLineWidth(1)
        self.lcd_time_pc.setSmallDecimalPoint(False)
        self.lcd_time_pc.setDigitCount(12)
        self.lcd_time_pc.setMode(QLCDNumber.Mode.Dec)
        self.lcd_time_pc.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.verticalLayout_5.addWidget(self.lcd_time_pc)

        self.lcd_date_pc = QLabel(self.verticalLayoutWidget_9)
        self.lcd_date_pc.setObjectName(u"lcd_date_pc")
        self.lcd_date_pc.setFont(font)
        self.lcd_date_pc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.lcd_date_pc)

        self.verticalLayout_5.setStretch(0, 6)
        self.verticalLayout_5.setStretch(1, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.horizontalLayout.setStretch(0, 6)
        self.horizontalLayout.setStretch(1, 7)

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
        self.horizontalLayout_18.setContentsMargins(-1, -1, -1, 30)
        self.table_cps = QTableWidget(self.verticalLayoutWidget_9)
        if (self.table_cps.columnCount() < 4):
            self.table_cps.setColumnCount(4)
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.table_cps.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font2 = QFont()
        font2.setBold(True)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font2);
        self.table_cps.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.table_cps.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.table_cps.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_cps.setObjectName(u"table_cps")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.table_cps.sizePolicy().hasHeightForWidth())
        self.table_cps.setSizePolicy(sizePolicy1)
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.table_cps.setFont(font3)
        self.table_cps.setStyleSheet(u"")
        self.table_cps.setFrameShape(QFrame.Shape.Box)
        self.table_cps.setFrameShadow(QFrame.Shadow.Sunken)
        self.table_cps.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_cps.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.table_cps.setAutoScrollMargin(5)
        self.table_cps.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_cps.setTabKeyNavigation(True)
        self.table_cps.setProperty(u"showDropIndicator", True)
        self.table_cps.setDragEnabled(False)
        self.table_cps.setAlternatingRowColors(True)
        self.table_cps.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_cps.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.table_cps.setShowGrid(True)
        self.table_cps.setGridStyle(Qt.PenStyle.SolidLine)
        self.table_cps.setSortingEnabled(False)
        self.table_cps.setWordWrap(True)
        self.table_cps.setCornerButtonEnabled(True)
        self.table_cps.setRowCount(0)
        self.table_cps.horizontalHeader().setCascadingSectionResizes(False)
        self.table_cps.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table_cps.horizontalHeader().setStretchLastSection(True)
        self.table_cps.verticalHeader().setVisible(False)
        self.table_cps.verticalHeader().setCascadingSectionResizes(False)
        self.table_cps.verticalHeader().setProperty(u"showSortIndicator", False)
        self.table_cps.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_18.addWidget(self.table_cps)

        self.horizontalLayout_18.setStretch(0, 12)

        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.verticalLayout_4.setStretch(0, 12)

        self.horizontalLayout_14.addLayout(self.verticalLayout_4)

        self.horizontalLayout_14.setStretch(0, 25)
        self.horizontalLayout_14.setStretch(1, 24)

        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.graph_out2 = QVBoxLayout()
        self.graph_out2.setObjectName(u"graph_out2")

        self.horizontalLayout_15.addLayout(self.graph_out2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 30)
        self.table_cpm = QTableWidget(self.verticalLayoutWidget_9)
        if (self.table_cpm.columnCount() < 3):
            self.table_cpm.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.table_cpm.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.table_cpm.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.table_cpm.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.table_cpm.setObjectName(u"table_cpm")
        self.table_cpm.setFont(font3)
        self.table_cpm.setStyleSheet(u"")
        self.table_cpm.setFrameShape(QFrame.Shape.Box)
        self.table_cpm.setFrameShadow(QFrame.Shadow.Sunken)
        self.table_cpm.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.table_cpm.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.table_cpm.setAutoScrollMargin(5)
        self.table_cpm.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table_cpm.setTabKeyNavigation(True)
        self.table_cpm.setProperty(u"showDropIndicator", True)
        self.table_cpm.setDragDropOverwriteMode(True)
        self.table_cpm.setAlternatingRowColors(True)
        self.table_cpm.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_cpm.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.table_cpm.setRowCount(0)
        self.table_cpm.horizontalHeader().setVisible(True)
        self.table_cpm.horizontalHeader().setCascadingSectionResizes(True)
        self.table_cpm.horizontalHeader().setDefaultSectionSize(100)
        self.table_cpm.horizontalHeader().setHighlightSections(True)
        self.table_cpm.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.table_cpm.horizontalHeader().setStretchLastSection(True)
        self.table_cpm.verticalHeader().setVisible(False)

        self.verticalLayout_6.addWidget(self.table_cpm)

        self.verticalLayout_6.setStretch(0, 5)

        self.horizontalLayout_15.addLayout(self.verticalLayout_6)

        self.horizontalLayout_15.setStretch(0, 25)
        self.horizontalLayout_15.setStretch(1, 24)

        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.verticalLayout_7.setStretch(0, 9)
        self.verticalLayout_7.setStretch(1, 9)

        self.horizontalLayout_16.addLayout(self.verticalLayout_7)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, -1, -1, 30)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.verticalLayoutWidget_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.horizontalLayout_9.addWidget(self.label_6)

        self.cbox_in_serial = QComboBox(self.verticalLayoutWidget_9)
        self.cbox_in_serial.setObjectName(u"cbox_in_serial")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cbox_in_serial.sizePolicy().hasHeightForWidth())
        self.cbox_in_serial.setSizePolicy(sizePolicy2)
        self.cbox_in_serial.setFont(font3)
        self.cbox_in_serial.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.cbox_in_serial)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 7)

        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.gbox_ensayo = QGroupBox(self.verticalLayoutWidget_9)
        self.gbox_ensayo.setObjectName(u"gbox_ensayo")
        self.verticalLayoutWidget_2 = QWidget(self.gbox_ensayo)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(10, 20, 241, 165))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font3)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.time_test = QTimeEdit(self.verticalLayoutWidget_2)
        self.time_test.setObjectName(u"time_test")
        sizePolicy1.setHeightForWidth(self.time_test.sizePolicy().hasHeightForWidth())
        self.time_test.setSizePolicy(sizePolicy1)
        self.time_test.setFont(font3)
        self.time_test.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.time_test.setAutoFillBackground(False)
        self.time_test.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.time_test.setWrapping(False)
        self.time_test.setFrame(True)
        self.time_test.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.time_test.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.time_test.setProperty(u"showGroupSeparator", False)
        self.time_test.setCalendarPopup(False)

        self.horizontalLayout_3.addWidget(self.time_test)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.btn_init = QPushButton(self.verticalLayoutWidget_2)
        self.btn_init.setObjectName(u"btn_init")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_init.sizePolicy().hasHeightForWidth())
        self.btn_init.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(10)
        font4.setWeight(QFont.Medium)
        self.btn_init.setFont(font4)

        self.verticalLayout_3.addWidget(self.btn_init)

        self.line = QFrame(self.verticalLayoutWidget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.lcd_time_duration = QLCDNumber(self.verticalLayoutWidget_2)
        self.lcd_time_duration.setObjectName(u"lcd_time_duration")
        self.lcd_time_duration.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.lcd_time_duration.setFrameShape(QFrame.Shape.NoFrame)
        self.lcd_time_duration.setFrameShadow(QFrame.Shadow.Plain)
        self.lcd_time_duration.setLineWidth(1)
        self.lcd_time_duration.setSmallDecimalPoint(False)
        self.lcd_time_duration.setDigitCount(8)
        self.lcd_time_duration.setMode(QLCDNumber.Mode.Dec)
        self.lcd_time_duration.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)

        self.verticalLayout_3.addWidget(self.lcd_time_duration)

        self.btn_stop = QPushButton(self.verticalLayoutWidget_2)
        self.btn_stop.setObjectName(u"btn_stop")
        self.btn_stop.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.btn_stop.sizePolicy().hasHeightForWidth())
        self.btn_stop.setSizePolicy(sizePolicy3)
        self.btn_stop.setFont(font4)

        self.verticalLayout_3.addWidget(self.btn_stop)

        self.btn_export = QPushButton(self.verticalLayoutWidget_2)
        self.btn_export.setObjectName(u"btn_export")
        self.btn_export.setEnabled(False)
        sizePolicy3.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())
        self.btn_export.setSizePolicy(sizePolicy3)
        self.btn_export.setFont(font4)
        self.btn_export.setCheckable(False)

        self.verticalLayout_3.addWidget(self.btn_export)

        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 3)
        self.verticalLayout_3.setStretch(2, 3)
        self.verticalLayout_3.setStretch(3, 4)
        self.verticalLayout_3.setStretch(4, 3)
        self.verticalLayout_3.setStretch(5, 3)

        self.verticalLayout.addWidget(self.gbox_ensayo)

        self.gbox_manual = QGroupBox(self.verticalLayoutWidget_9)
        self.gbox_manual.setObjectName(u"gbox_manual")
        self.verticalLayoutWidget = QWidget(self.gbox_manual)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 30, 241, 156))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_last_CPM = QPushButton(self.verticalLayoutWidget)
        self.btn_last_CPM.setObjectName(u"btn_last_CPM")
        self.btn_last_CPM.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.btn_last_CPM.sizePolicy().hasHeightForWidth())
        self.btn_last_CPM.setSizePolicy(sizePolicy3)
        self.btn_last_CPM.setFont(font4)

        self.verticalLayout_2.addWidget(self.btn_last_CPM)

        self.btn_accum_CPS = QPushButton(self.verticalLayoutWidget)
        self.btn_accum_CPS.setObjectName(u"btn_accum_CPS")
        sizePolicy3.setHeightForWidth(self.btn_accum_CPS.sizePolicy().hasHeightForWidth())
        self.btn_accum_CPS.setSizePolicy(sizePolicy3)
        self.btn_accum_CPS.setFont(font4)

        self.verticalLayout_2.addWidget(self.btn_accum_CPS)

        self.btn_time_s = QPushButton(self.verticalLayoutWidget)
        self.btn_time_s.setObjectName(u"btn_time_s")
        sizePolicy3.setHeightForWidth(self.btn_time_s.sizePolicy().hasHeightForWidth())
        self.btn_time_s.setSizePolicy(sizePolicy3)
        self.btn_time_s.setFont(font4)

        self.verticalLayout_2.addWidget(self.btn_time_s)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(1)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font3)

        self.verticalLayout_9.addWidget(self.label)

        self.txt_rta_attiny = QLineEdit(self.verticalLayoutWidget)
        self.txt_rta_attiny.setObjectName(u"txt_rta_attiny")
        self.txt_rta_attiny.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.txt_rta_attiny.sizePolicy().hasHeightForWidth())
        self.txt_rta_attiny.setSizePolicy(sizePolicy1)
        self.txt_rta_attiny.setFont(font3)
        self.txt_rta_attiny.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.txt_rta_attiny)

        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout_9)

        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 4)

        self.verticalLayout.addWidget(self.gbox_manual)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 12)
        self.verticalLayout.setStretch(2, 12)

        self.horizontalLayout_16.addLayout(self.verticalLayout)

        self.horizontalLayout_16.setStretch(0, 60)
        self.horizontalLayout_16.setStretch(1, 27)

        self.verticalLayout_8.addLayout(self.horizontalLayout_16)

        self.verticalLayout_8.setStretch(0, 4)
        self.verticalLayout_8.setStretch(1, 20)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.img_logo1.setText("")
        self.img_logo2.setText("")
        self.lcd_date_pc.setText("")
        ___qtablewidgetitem = self.table_cps.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem1 = self.table_cps.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Seg.", None));
        ___qtablewidgetitem2 = self.table_cps.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Datetime", None));
        ___qtablewidgetitem3 = self.table_cps.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"CPS", None));
        ___qtablewidgetitem4 = self.table_cpm.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"#", None));
        ___qtablewidgetitem5 = self.table_cpm.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Datetime", None));
        ___qtablewidgetitem6 = self.table_cpm.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u00daltimo CPM", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Input:", None))
        self.gbox_ensayo.setTitle(QCoreApplication.translate("MainWindow", u"Ensayos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Duraci\u00f3n:", None))
        self.btn_init.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.btn_stop.setText(QCoreApplication.translate("MainWindow", u"Forzar finalizar", None))
        self.btn_export.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.gbox_manual.setTitle(QCoreApplication.translate("MainWindow", u"Consulta manual", None))
        self.btn_last_CPM.setText(QCoreApplication.translate("MainWindow", u"\u00daltimo CPM", None))
        self.btn_accum_CPS.setText(QCoreApplication.translate("MainWindow", u"CPS actual", None))
        self.btn_time_s.setText(QCoreApplication.translate("MainWindow", u"TIME", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Attiny:", None))
    # retranslateUi

