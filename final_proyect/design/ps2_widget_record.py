# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_record.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Record(object):
    def setupUi(self, Record):
        if not Record.objectName():
            Record.setObjectName(u"Record")
        Record.resize(800, 580)
        # Quitar bordes de ventana
        Record.setAttribute(Qt.WA_TranslucentBackground)
        Record.setWindowFlag(Qt.FramelessWindowHint)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Record.sizePolicy().hasHeightForWidth())
        Record.setSizePolicy(sizePolicy)
        Record.setStyleSheet(u"QFrame{\n"
"	background: rgba(250,250,250,255);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgba(27,52,124,255);\n"
"	font-family: Segoe UI;\n"
"	font-size: 10px;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QGraphicsView{\n"
"	border: 0px solid;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"    background-color: rgba(73,93,151,255);\n"
"    color: white;\n"
"	border: 0px solid;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"}\n"
"\n"
"QHeaderView::section:checked{\n"
"    background-color: rgba(27,52,124,255);\n"
"}\n"
"\n"
"QScrollBar:horizontal{\n"
"    border: 0px solid;\n"
"	background-color: transparent;\n"
"    height: 16px;\n"
"    margin: 0px 20px 0px 20px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal{\n"
"    background-color: rgba(27,52,124,255);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"    border: 0px solid;\n"
"    background-color: rgba(27,52,124,255);\n"
"    width: 16px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
""
                        "	border-radius: 8px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal{\n"
"    border: 0px solid;\n"
"    background-color: rgba(27,52,124,255);\n"
"    width: 16px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"    border: 0px solid;\n"
"	background-color: transparent;\n"
"    width: 16px;\n"
"    margin: 20px 0px 20px 0px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical{\n"
"    background-color: rgba(27,52,124,255);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical{\n"
"    border: 0px solid;\n"
"    background-color: rgba(27,52,124,255);\n"
"    height: 16px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical{\n"
"    border: 0px solid;\n"
"    background-color: rgba(27,52,124,255);\n"
"    height: 16px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QFram"
                        "e#frame_principal{\n"
"	background: qlineargradient(spread:pad, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(27,52,124,255), stop:1 rgba(73,93,151,255));\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#frame_container{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#frame_exit{\n"
"	background: transparent;\n"
"}\n"
"\n"
"QLabel#label_title{\n"
"	font-size: 25px;\n"
"	font-family: Segoe UI Black;\n"
"}\n"
"\n"
"QPushButton#btn_exit{\n"
"	background: rgba(250,250,250,255);\n"
"	border-radius: 7px;\n"
"}")
        self.gridLayout = QGridLayout(Record)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_principal = QFrame(Record)
        self.frame_principal.setObjectName(u"frame_principal")
        sizePolicy.setHeightForWidth(self.frame_principal.sizePolicy().hasHeightForWidth())
        self.frame_principal.setSizePolicy(sizePolicy)
        self.frame_principal.setMinimumSize(QSize(800, 580))
        self.frame_principal.setMaximumSize(QSize(800, 580))
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_principal)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(25, 5, 25, 25)
        self.frame_container = QFrame(self.frame_principal)
        self.frame_container.setObjectName(u"frame_container")
        sizePolicy.setHeightForWidth(self.frame_container.sizePolicy().hasHeightForWidth())
        self.frame_container.setSizePolicy(sizePolicy)
        self.frame_container.setMinimumSize(QSize(750, 530))
        self.frame_container.setMaximumSize(QSize(750, 530))
        self.frame_container.setFrameShape(QFrame.StyledPanel)
        self.frame_container.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_container)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.frame_info = QFrame(self.frame_container)
        self.frame_info.setObjectName(u"frame_info")
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_info)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.label_title = QLabel(self.frame_info)
        self.label_title.setObjectName(u"label_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy1)
        self.label_title.setMinimumSize(QSize(0, 30))
        self.label_title.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_5.addWidget(self.label_title, 0, 0, 1, 2)

        self.table_record = QTableWidget(self.frame_info)
        self.table_record.setObjectName(u"table_record")
        sizePolicy.setHeightForWidth(self.table_record.sizePolicy().hasHeightForWidth())
        self.table_record.setSizePolicy(sizePolicy)
        self.table_record.setMinimumSize(QSize(350, 450))
        self.table_record.setMaximumSize(QSize(350, 450))

        self.gridLayout_5.addWidget(self.table_record, 1, 1, 2, 1)


        self.gridLayout_4.addWidget(self.frame_info, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_container, 1, 0, 1, 1)

        self.frame_exit = QFrame(self.frame_principal)
        self.frame_exit.setObjectName(u"frame_exit")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_exit.sizePolicy().hasHeightForWidth())
        self.frame_exit.setSizePolicy(sizePolicy2)
        self.frame_exit.setMinimumSize(QSize(0, 15))
        self.frame_exit.setMaximumSize(QSize(16777215, 15))
        self.frame_exit.setFrameShape(QFrame.StyledPanel)
        self.frame_exit.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_exit)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(731, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.btn_exit = QPushButton(self.frame_exit)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(14, 14))
        self.btn_exit.setMaximumSize(QSize(14, 14))
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_exit, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.frame_exit, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_principal, 0, 0, 1, 1)


        self.retranslateUi(Record)

        QMetaObject.connectSlotsByName(Record)
    # setupUi

    def retranslateUi(self, Record):
        Record.setWindowTitle(QCoreApplication.translate("Record", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("Record", u"Base de datos", None))
        self.btn_exit.setText("")
    # retranslateUi

