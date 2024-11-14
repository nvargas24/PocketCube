# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'view_serial.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SerialData(object):
    def setupUi(self, SerialData):
        if not SerialData.objectName():
            SerialData.setObjectName(u"SerialData")
        SerialData.resize(481, 396)
        self.verticalLayoutWidget = QWidget(SerialData)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 30, 431, 351))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.table_serial_2 = QTableWidget(self.verticalLayoutWidget)
        if (self.table_serial_2.columnCount() < 3):
            self.table_serial_2.setColumnCount(3)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font);
        self.table_serial_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setBold(True)
        font1.setWeight(75)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font1);
        self.table_serial_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font);
        self.table_serial_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.table_serial_2.setObjectName(u"table_serial_2")
        font2 = QFont()
        font2.setPointSize(10)
        self.table_serial_2.setFont(font2)
        self.table_serial_2.setLayoutDirection(Qt.LeftToRight)
        self.table_serial_2.setFrameShape(QFrame.NoFrame)
        self.table_serial_2.setFrameShadow(QFrame.Raised)
        self.table_serial_2.setLineWidth(1)
        self.table_serial_2.setMidLineWidth(0)
        self.table_serial_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.table_serial_2.setAutoScrollMargin(4)
        self.table_serial_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_serial_2.setAlternatingRowColors(True)
        self.table_serial_2.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table_serial_2.setTextElideMode(Qt.ElideRight)
        self.table_serial_2.setShowGrid(True)
        self.table_serial_2.setSortingEnabled(False)
        self.table_serial_2.setWordWrap(True)
        self.table_serial_2.setRowCount(0)
        self.table_serial_2.setColumnCount(3)
        self.table_serial_2.horizontalHeader().setCascadingSectionResizes(False)
        self.table_serial_2.horizontalHeader().setDefaultSectionSize(75)
        self.table_serial_2.horizontalHeader().setStretchLastSection(True)
        self.table_serial_2.verticalHeader().setVisible(False)
        self.table_serial_2.verticalHeader().setMinimumSectionSize(20)
        self.table_serial_2.verticalHeader().setDefaultSectionSize(20)

        self.horizontalLayout_2.addWidget(self.table_serial_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(10)
        self.pushButton.setFont(font3)

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.btn_volver = QPushButton(self.verticalLayoutWidget)
        self.btn_volver.setObjectName(u"btn_volver")
        sizePolicy.setHeightForWidth(self.btn_volver.sizePolicy().hasHeightForWidth())
        self.btn_volver.setSizePolicy(sizePolicy)
        self.btn_volver.setFont(font3)
        self.btn_volver.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout_3.addWidget(self.btn_volver)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(0, 6)
        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(SerialData)

        QMetaObject.connectSlotsByName(SerialData)
    # setupUi

    def retranslateUi(self, SerialData):
        SerialData.setWindowTitle(QCoreApplication.translate("SerialData", u"Dialog", None))
        ___qtablewidgetitem = self.table_serial_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("SerialData", u"ID", None));
        ___qtablewidgetitem1 = self.table_serial_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("SerialData", u"Descripci\u00f3n", None));
        ___qtablewidgetitem2 = self.table_serial_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("SerialData", u"Value[V]", None));
        self.pushButton.setText(QCoreApplication.translate("SerialData", u"Exportar csv", None))
        self.btn_volver.setText(QCoreApplication.translate("SerialData", u"Volver", None))
    # retranslateUi

