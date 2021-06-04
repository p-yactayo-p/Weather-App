# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from resources import ps2_resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 580)
        # Quitar bordes de ventana
        MainWindow.setAttribute(Qt.WA_TranslucentBackground)
        MainWindow.setWindowFlag(Qt.FramelessWindowHint)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(0, 580))
        MainWindow.setStyleSheet(u"QFrame{\n"
"	background: rgba(250,250,250,255);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgba(27,52,124,255);\n"
"	background: transparent;\n"
"	font-family: Segoe UI;\n"
"	font-size: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: white;\n"
"	background: rgba(17,33,74,255);\n"
"	font-family: Segoe UI Black;\n"
"	font-size: 12px;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QFrame#frame_principal{\n"
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
"QFrame#frame_info{\n"
"	background: rgba(73,93,151,255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLabel#label_title{\n"
"	font-size: 30px;\n"
"	font-family: Segoe UI Black;\n"
"	color: rgba(250,250,250,255);\n"
"}\n"
"\n"
"QLabel#label_date, QLabel#label_hour{\n"
"	font-size: 15px;\n"
"	color: rgba(250,250,250,255);\n"
"}\n"
"\n"
"QLabel"
                        "#label_temperature{\n"
"	font-size: 60px;\n"
"	font-family: Segoe UI Black;\n"
"}\n"
"\n"
"QLabel#label_state{\n"
"	font-size: 20px;\n"
"}\n"
"\n"
"QLabel#label_place, QLabel#label_forecast{\n"
"	font-size: 20px;\n"
"	font-family: Segoe UI Black;\n"
"}\n"
"\n"
"QLabel#label_message{\n"
"	color: red;\n"
"}\n"
"\n"
"QPushButton#btn_exit{\n"
"	background: rgba(250,250,250,255);\n"
"	border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton#btn_minimize{\n"
"	background: rgba(250,250,250,255);\n"
"	border-radius: 7px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_principal = QFrame(self.centralwidget)
        self.frame_principal.setObjectName(u"frame_principal")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_principal.sizePolicy().hasHeightForWidth())
        self.frame_principal.setSizePolicy(sizePolicy1)
        self.frame_principal.setMinimumSize(QSize(0, 580))
        self.frame_principal.setMaximumSize(QSize(16777215, 580))
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_principal)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(5)
        self.gridLayout_2.setContentsMargins(25, 5, 25, 25)
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
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(10)
        self.gridLayout_3.setVerticalSpacing(0)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(697, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.btn_minimize = QPushButton(self.frame_exit)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QSize(14, 14))
        self.btn_minimize.setMaximumSize(QSize(14, 14))
        self.btn_minimize.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_minimize, 0, 1, 1, 1)

        self.btn_exit = QPushButton(self.frame_exit)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(14, 14))
        self.btn_exit.setMaximumSize(QSize(14, 14))
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_3.addWidget(self.btn_exit, 0, 2, 1, 1)


        self.gridLayout_2.addWidget(self.frame_exit, 0, 0, 1, 1)

        self.frame_container = QFrame(self.frame_principal)
        self.frame_container.setObjectName(u"frame_container")
        sizePolicy1.setHeightForWidth(self.frame_container.sizePolicy().hasHeightForWidth())
        self.frame_container.setSizePolicy(sizePolicy1)
        self.frame_container.setMinimumSize(QSize(0, 530))
        self.frame_container.setMaximumSize(QSize(16777215, 530))
        self.frame_container.setFrameShape(QFrame.StyledPanel)
        self.frame_container.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_container)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_ibm = QLabel(self.frame_container)
        self.label_ibm.setObjectName(u"label_ibm")
        sizePolicy2.setHeightForWidth(self.label_ibm.sizePolicy().hasHeightForWidth())
        self.label_ibm.setSizePolicy(sizePolicy2)
        self.label_ibm.setMinimumSize(QSize(0, 20))
        self.label_ibm.setMaximumSize(QSize(16777215, 20))
        self.label_ibm.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_ibm, 3, 0, 1, 2)

        self.frame_forecast = QFrame(self.frame_container)
        self.frame_forecast.setObjectName(u"frame_forecast")
        sizePolicy.setHeightForWidth(self.frame_forecast.sizePolicy().hasHeightForWidth())
        self.frame_forecast.setSizePolicy(sizePolicy)
        self.frame_forecast.setMinimumSize(QSize(335, 360))
        self.frame_forecast.setMaximumSize(QSize(335, 360))
        self.frame_forecast.setFrameShape(QFrame.StyledPanel)
        self.frame_forecast.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_forecast)
        self.gridLayout_7.setSpacing(10)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(10, 10, 10, 10)
        self.state_day1 = QLabel(self.frame_forecast)
        self.state_day1.setObjectName(u"state_day1")
        sizePolicy.setHeightForWidth(self.state_day1.sizePolicy().hasHeightForWidth())
        self.state_day1.setSizePolicy(sizePolicy)
        self.state_day1.setMinimumSize(QSize(100, 20))

        self.gridLayout_7.addWidget(self.state_day1, 1, 2, 1, 1)

        self.state_day5 = QLabel(self.frame_forecast)
        self.state_day5.setObjectName(u"state_day5")
        sizePolicy.setHeightForWidth(self.state_day5.sizePolicy().hasHeightForWidth())
        self.state_day5.setSizePolicy(sizePolicy)
        self.state_day5.setMinimumSize(QSize(100, 20))

        self.gridLayout_7.addWidget(self.state_day5, 5, 2, 1, 1)

        self.state_day6 = QLabel(self.frame_forecast)
        self.state_day6.setObjectName(u"state_day6")
        sizePolicy.setHeightForWidth(self.state_day6.sizePolicy().hasHeightForWidth())
        self.state_day6.setSizePolicy(sizePolicy)
        self.state_day6.setMinimumSize(QSize(100, 20))

        self.gridLayout_7.addWidget(self.state_day6, 6, 2, 1, 1)

        self.maxmin_day8 = QLabel(self.frame_forecast)
        self.maxmin_day8.setObjectName(u"maxmin_day8")
        sizePolicy.setHeightForWidth(self.maxmin_day8.sizePolicy().hasHeightForWidth())
        self.maxmin_day8.setSizePolicy(sizePolicy)
        self.maxmin_day8.setMinimumSize(QSize(35, 20))

        self.gridLayout_7.addWidget(self.maxmin_day8, 8, 1, 1, 1)

        self.maxmin_day6 = QLabel(self.frame_forecast)
        self.maxmin_day6.setObjectName(u"maxmin_day6")
        sizePolicy.setHeightForWidth(self.maxmin_day6.sizePolicy().hasHeightForWidth())
        self.maxmin_day6.setSizePolicy(sizePolicy)
        self.maxmin_day6.setMinimumSize(QSize(35, 20))

        self.gridLayout_7.addWidget(self.maxmin_day6, 6, 1, 1, 1)

        self.maxmin_day7 = QLabel(self.frame_forecast)
        self.maxmin_day7.setObjectName(u"maxmin_day7")
        sizePolicy.setHeightForWidth(self.maxmin_day7.sizePolicy().hasHeightForWidth())
        self.maxmin_day7.setSizePolicy(sizePolicy)
        self.maxmin_day7.setMinimumSize(QSize(35, 20))

        self.gridLayout_7.addWidget(self.maxmin_day7, 7, 1, 1, 1)

        self.maxmin_day9 = QLabel(self.frame_forecast)
        self.maxmin_day9.setObjectName(u"maxmin_day9")
        sizePolicy.setHeightForWidth(self.maxmin_day9.sizePolicy().hasHeightForWidth())
        self.maxmin_day9.setSizePolicy(sizePolicy)
        self.maxmin_day9.setMinimumSize(QSize(35, 20))

        self.gridLayout_7.addWidget(self.maxmin_day9, 9, 1, 1, 1)

        self.maxmin_day4 = QLabel(self.frame_forecast)
        self.maxmin_day4.setObjectName(u"maxmin_day4")
        sizePolicy.setHeightForWidth(self.maxmin_day4.sizePolicy().hasHeightForWidth())
        self.maxmin_day4.setSizePolicy(sizePolicy)
        self.maxmin_day4.setMinimumSize(QSize(35, 20))

        self.gridLayout_7.addWidget(self.maxmin_day4, 4, 1, 1, 1)

        self.maxmin_day5 = QLabel(self.frame_forecast)
        self.maxmin_day5.setObjectName(u"maxmin_day5")
        sizePolicy.setHeightForWidth(self.maxmin_day5.sizePolicy().hasHeightForWidth())
        self.maxmin_day5.setSizePolicy(sizePolicy)
        self.maxmin_day5.setMinimumSize(QSize(35, 20))

        self.gridLayout_7.addWidget(self.maxmin_day5, 5, 1, 1, 1)

        self.state_day8 = QLabel(self.frame_forecast)
        self.state_day8.setObjectName(u"state_day8")
        sizePolicy.setHeightForWidth(self.state_day8.sizePolicy().hasHeightForWidth())
        self.state_day8.setSizePolicy(sizePolicy)
        self.state_day8.setMinimumSize(QSize(100, 20))

        self.gridLayout_7.addWidget(self.state_day8, 8, 2, 1, 1)

        self.state_day4 = QLabel(self.frame_forecast)
        self.state_day4.setObjectName(u"state_day4")
        sizePolicy.setHeightForWidth(self.state_day4.sizePolicy().hasHeightForWidth())
        self.state_day4.setSizePolicy(sizePolicy)
        self.state_day4.setMinimumSize(QSize(100, 20))

        self.gridLayout_7.addWidget(self.state_day4, 4, 2, 1, 1)

        self.state_day7 = QLabel(self.frame_forecast)
        self.state_day7.setObjectName(u"state_day7")
        sizePolicy.setHeightForWidth(self.state_day7.sizePolicy().hasHeightForWidth())
        self.state_day7.setSizePolicy(sizePolicy)
        self.state_day7.setMinimumSize(QSize(100, 20))

        self.gridLayout_7.addWidget(self.state_day7, 7, 2, 1, 1)

        self.state_day3 = QLabel(self.frame_forecast)
        self.state_day3.setObjectName(u"state_day3")
        sizePolicy.setHeightForWidth(self.state_day3.sizePolicy().hasHeightForWidth())
        self.state_day3.setSizePolicy(sizePolicy)
        self.state_day3.setMinimumSize(QSize(100, 20))

        self.gridLayout_7.addWidget(self.state_day3, 3, 2, 1, 1)

        self.state_day9 = QLabel(self.frame_forecast)
        self.state_day9.setObjectName(u"state_day9")
        sizePolicy.setHeightForWidth(self.state_day9.sizePolicy().hasHeightForWidth())
        self.state_day9.setSizePolicy(sizePolicy)
        self.state_day9.setMinimumSize(QSize(100, 20))

        self.gridLayout_7.addWidget(self.state_day9, 9, 2, 1, 1)

        self.state_day2 = QLabel(self.frame_forecast)
        self.state_day2.setObjectName(u"state_day2")
        sizePolicy.setHeightForWidth(self.state_day2.sizePolicy().hasHeightForWidth())
        self.state_day2.setSizePolicy(sizePolicy)
        self.state_day2.setMinimumSize(QSize(100, 20))

        self.gridLayout_7.addWidget(self.state_day2, 2, 2, 1, 1)

        self.label_day8 = QLabel(self.frame_forecast)
        self.label_day8.setObjectName(u"label_day8")
        sizePolicy.setHeightForWidth(self.label_day8.sizePolicy().hasHeightForWidth())
        self.label_day8.setSizePolicy(sizePolicy)
        self.label_day8.setMinimumSize(QSize(50, 20))

        self.gridLayout_7.addWidget(self.label_day8, 8, 0, 1, 1)

        self.label_day5 = QLabel(self.frame_forecast)
        self.label_day5.setObjectName(u"label_day5")
        sizePolicy.setHeightForWidth(self.label_day5.sizePolicy().hasHeightForWidth())
        self.label_day5.setSizePolicy(sizePolicy)
        self.label_day5.setMinimumSize(QSize(50, 20))

        self.gridLayout_7.addWidget(self.label_day5, 5, 0, 1, 1)

        self.label_day6 = QLabel(self.frame_forecast)
        self.label_day6.setObjectName(u"label_day6")
        sizePolicy.setHeightForWidth(self.label_day6.sizePolicy().hasHeightForWidth())
        self.label_day6.setSizePolicy(sizePolicy)
        self.label_day6.setMinimumSize(QSize(50, 20))

        self.gridLayout_7.addWidget(self.label_day6, 6, 0, 1, 1)

        self.label_day10 = QLabel(self.frame_forecast)
        self.label_day10.setObjectName(u"label_day10")
        sizePolicy.setHeightForWidth(self.label_day10.sizePolicy().hasHeightForWidth())
        self.label_day10.setSizePolicy(sizePolicy)
        self.label_day10.setMinimumSize(QSize(50, 20))

        self.gridLayout_7.addWidget(self.label_day10, 10, 0, 1, 1)

        self.label_day7 = QLabel(self.frame_forecast)
        self.label_day7.setObjectName(u"label_day7")
        sizePolicy.setHeightForWidth(self.label_day7.sizePolicy().hasHeightForWidth())
        self.label_day7.setSizePolicy(sizePolicy)
        self.label_day7.setMinimumSize(QSize(50, 20))

        self.gridLayout_7.addWidget(self.label_day7, 7, 0, 1, 1)

        self.label_day9 = QLabel(self.frame_forecast)
        self.label_day9.setObjectName(u"label_day9")
        sizePolicy.setHeightForWidth(self.label_day9.sizePolicy().hasHeightForWidth())
        self.label_day9.setSizePolicy(sizePolicy)
        self.label_day9.setMinimumSize(QSize(50, 20))

        self.gridLayout_7.addWidget(self.label_day9, 9, 0, 1, 1)

        self.maxmin_day10 = QLabel(self.frame_forecast)
        self.maxmin_day10.setObjectName(u"maxmin_day10")
        sizePolicy.setHeightForWidth(self.maxmin_day10.sizePolicy().hasHeightForWidth())
        self.maxmin_day10.setSizePolicy(sizePolicy)
        self.maxmin_day10.setMinimumSize(QSize(35, 20))

        self.gridLayout_7.addWidget(self.maxmin_day10, 10, 1, 1, 1)

        self.maxmin_day2 = QLabel(self.frame_forecast)
        self.maxmin_day2.setObjectName(u"maxmin_day2")
        sizePolicy.setHeightForWidth(self.maxmin_day2.sizePolicy().hasHeightForWidth())
        self.maxmin_day2.setSizePolicy(sizePolicy)
        self.maxmin_day2.setMinimumSize(QSize(35, 20))

        self.gridLayout_7.addWidget(self.maxmin_day2, 2, 1, 1, 1)

        self.maxmin_day3 = QLabel(self.frame_forecast)
        self.maxmin_day3.setObjectName(u"maxmin_day3")
        sizePolicy.setHeightForWidth(self.maxmin_day3.sizePolicy().hasHeightForWidth())
        self.maxmin_day3.setSizePolicy(sizePolicy)
        self.maxmin_day3.setMinimumSize(QSize(35, 20))

        self.gridLayout_7.addWidget(self.maxmin_day3, 3, 1, 1, 1)

        self.label_day1 = QLabel(self.frame_forecast)
        self.label_day1.setObjectName(u"label_day1")
        sizePolicy.setHeightForWidth(self.label_day1.sizePolicy().hasHeightForWidth())
        self.label_day1.setSizePolicy(sizePolicy)
        self.label_day1.setMinimumSize(QSize(50, 20))

        self.gridLayout_7.addWidget(self.label_day1, 1, 0, 1, 1)

        self.label_day2 = QLabel(self.frame_forecast)
        self.label_day2.setObjectName(u"label_day2")
        sizePolicy.setHeightForWidth(self.label_day2.sizePolicy().hasHeightForWidth())
        self.label_day2.setSizePolicy(sizePolicy)
        self.label_day2.setMinimumSize(QSize(50, 20))

        self.gridLayout_7.addWidget(self.label_day2, 2, 0, 1, 1)

        self.label_day3 = QLabel(self.frame_forecast)
        self.label_day3.setObjectName(u"label_day3")
        sizePolicy.setHeightForWidth(self.label_day3.sizePolicy().hasHeightForWidth())
        self.label_day3.setSizePolicy(sizePolicy)
        self.label_day3.setMinimumSize(QSize(50, 20))

        self.gridLayout_7.addWidget(self.label_day3, 3, 0, 1, 1)

        self.label_day4 = QLabel(self.frame_forecast)
        self.label_day4.setObjectName(u"label_day4")
        sizePolicy.setHeightForWidth(self.label_day4.sizePolicy().hasHeightForWidth())
        self.label_day4.setSizePolicy(sizePolicy)
        self.label_day4.setMinimumSize(QSize(50, 20))

        self.gridLayout_7.addWidget(self.label_day4, 4, 0, 1, 1)

        self.maxmin_day1 = QLabel(self.frame_forecast)
        self.maxmin_day1.setObjectName(u"maxmin_day1")
        sizePolicy.setHeightForWidth(self.maxmin_day1.sizePolicy().hasHeightForWidth())
        self.maxmin_day1.setSizePolicy(sizePolicy)
        self.maxmin_day1.setMinimumSize(QSize(35, 20))

        self.gridLayout_7.addWidget(self.maxmin_day1, 1, 1, 1, 1)

        self.state_day10 = QLabel(self.frame_forecast)
        self.state_day10.setObjectName(u"state_day10")
        sizePolicy.setHeightForWidth(self.state_day10.sizePolicy().hasHeightForWidth())
        self.state_day10.setSizePolicy(sizePolicy)
        self.state_day10.setMinimumSize(QSize(100, 20))

        self.gridLayout_7.addWidget(self.state_day10, 10, 2, 1, 1)

        self.wind_day1 = QLabel(self.frame_forecast)
        self.wind_day1.setObjectName(u"wind_day1")
        sizePolicy.setHeightForWidth(self.wind_day1.sizePolicy().hasHeightForWidth())
        self.wind_day1.setSizePolicy(sizePolicy)
        self.wind_day1.setMinimumSize(QSize(60, 20))

        self.gridLayout_7.addWidget(self.wind_day1, 1, 3, 1, 1)

        self.wind_day2 = QLabel(self.frame_forecast)
        self.wind_day2.setObjectName(u"wind_day2")
        sizePolicy.setHeightForWidth(self.wind_day2.sizePolicy().hasHeightForWidth())
        self.wind_day2.setSizePolicy(sizePolicy)
        self.wind_day2.setMinimumSize(QSize(60, 20))

        self.gridLayout_7.addWidget(self.wind_day2, 2, 3, 1, 1)

        self.wind_day3 = QLabel(self.frame_forecast)
        self.wind_day3.setObjectName(u"wind_day3")
        sizePolicy.setHeightForWidth(self.wind_day3.sizePolicy().hasHeightForWidth())
        self.wind_day3.setSizePolicy(sizePolicy)
        self.wind_day3.setMinimumSize(QSize(60, 20))

        self.gridLayout_7.addWidget(self.wind_day3, 3, 3, 1, 1)

        self.wind_day4 = QLabel(self.frame_forecast)
        self.wind_day4.setObjectName(u"wind_day4")
        sizePolicy.setHeightForWidth(self.wind_day4.sizePolicy().hasHeightForWidth())
        self.wind_day4.setSizePolicy(sizePolicy)
        self.wind_day4.setMinimumSize(QSize(60, 20))

        self.gridLayout_7.addWidget(self.wind_day4, 4, 3, 1, 1)

        self.wind_day5 = QLabel(self.frame_forecast)
        self.wind_day5.setObjectName(u"wind_day5")
        sizePolicy.setHeightForWidth(self.wind_day5.sizePolicy().hasHeightForWidth())
        self.wind_day5.setSizePolicy(sizePolicy)
        self.wind_day5.setMinimumSize(QSize(60, 20))

        self.gridLayout_7.addWidget(self.wind_day5, 5, 3, 1, 1)

        self.wind_day6 = QLabel(self.frame_forecast)
        self.wind_day6.setObjectName(u"wind_day6")
        sizePolicy.setHeightForWidth(self.wind_day6.sizePolicy().hasHeightForWidth())
        self.wind_day6.setSizePolicy(sizePolicy)
        self.wind_day6.setMinimumSize(QSize(60, 20))

        self.gridLayout_7.addWidget(self.wind_day6, 6, 3, 1, 1)

        self.wind_day7 = QLabel(self.frame_forecast)
        self.wind_day7.setObjectName(u"wind_day7")
        sizePolicy.setHeightForWidth(self.wind_day7.sizePolicy().hasHeightForWidth())
        self.wind_day7.setSizePolicy(sizePolicy)
        self.wind_day7.setMinimumSize(QSize(60, 20))

        self.gridLayout_7.addWidget(self.wind_day7, 7, 3, 1, 1)

        self.wind_day8 = QLabel(self.frame_forecast)
        self.wind_day8.setObjectName(u"wind_day8")
        sizePolicy.setHeightForWidth(self.wind_day8.sizePolicy().hasHeightForWidth())
        self.wind_day8.setSizePolicy(sizePolicy)
        self.wind_day8.setMinimumSize(QSize(60, 20))

        self.gridLayout_7.addWidget(self.wind_day8, 8, 3, 1, 1)

        self.wind_day9 = QLabel(self.frame_forecast)
        self.wind_day9.setObjectName(u"wind_day9")
        sizePolicy.setHeightForWidth(self.wind_day9.sizePolicy().hasHeightForWidth())
        self.wind_day9.setSizePolicy(sizePolicy)
        self.wind_day9.setMinimumSize(QSize(60, 20))

        self.gridLayout_7.addWidget(self.wind_day9, 9, 3, 1, 1)

        self.wind_day10 = QLabel(self.frame_forecast)
        self.wind_day10.setObjectName(u"wind_day10")
        sizePolicy.setHeightForWidth(self.wind_day10.sizePolicy().hasHeightForWidth())
        self.wind_day10.setSizePolicy(sizePolicy)
        self.wind_day10.setMinimumSize(QSize(60, 20))

        self.gridLayout_7.addWidget(self.wind_day10, 10, 3, 1, 1)

        self.label_forecast = QLabel(self.frame_forecast)
        self.label_forecast.setObjectName(u"label_forecast")
        sizePolicy1.setHeightForWidth(self.label_forecast.sizePolicy().hasHeightForWidth())
        self.label_forecast.setSizePolicy(sizePolicy1)
        self.label_forecast.setMinimumSize(QSize(0, 40))
        self.label_forecast.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_7.addWidget(self.label_forecast, 0, 0, 1, 4)


        self.gridLayout_4.addWidget(self.frame_forecast, 0, 1, 2, 1)

        self.frame_info = QFrame(self.frame_container)
        self.frame_info.setObjectName(u"frame_info")
        sizePolicy.setHeightForWidth(self.frame_info.sizePolicy().hasHeightForWidth())
        self.frame_info.setSizePolicy(sizePolicy)
        self.frame_info.setMinimumSize(QSize(385, 130))
        self.frame_info.setMaximumSize(QSize(385, 130))
        self.frame_info.setFrameShape(QFrame.StyledPanel)
        self.frame_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_info)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.label_date = QLabel(self.frame_info)
        self.label_date.setObjectName(u"label_date")
        sizePolicy1.setHeightForWidth(self.label_date.sizePolicy().hasHeightForWidth())
        self.label_date.setSizePolicy(sizePolicy1)
        self.label_date.setMinimumSize(QSize(0, 20))
        self.label_date.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_5.addWidget(self.label_date, 1, 0, 1, 1)

        self.label_title = QLabel(self.frame_info)
        self.label_title.setObjectName(u"label_title")
        sizePolicy1.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy1)
        self.label_title.setMinimumSize(QSize(0, 50))
        self.label_title.setMaximumSize(QSize(16777215, 50))
        self.label_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_title, 0, 0, 1, 1)

        self.label_hour = QLabel(self.frame_info)
        self.label_hour.setObjectName(u"label_hour")
        sizePolicy1.setHeightForWidth(self.label_hour.sizePolicy().hasHeightForWidth())
        self.label_hour.setSizePolicy(sizePolicy1)
        self.label_hour.setMinimumSize(QSize(0, 20))
        self.label_hour.setMaximumSize(QSize(16777215, 20))

        self.gridLayout_5.addWidget(self.label_hour, 2, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_info, 0, 0, 1, 1)

        self.frame_buttons = QFrame(self.frame_container)
        self.frame_buttons.setObjectName(u"frame_buttons")
        sizePolicy.setHeightForWidth(self.frame_buttons.sizePolicy().hasHeightForWidth())
        self.frame_buttons.setSizePolicy(sizePolicy)
        self.frame_buttons.setMinimumSize(QSize(335, 110))
        self.frame_buttons.setMaximumSize(QSize(335, 110))
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_buttons)
        self.gridLayout_8.setSpacing(10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(10, 10, 10, 10)
        self.btn_data = QPushButton(self.frame_buttons)
        self.btn_data.setObjectName(u"btn_data")
        self.btn_data.setMinimumSize(QSize(0, 40))
        self.btn_data.setMaximumSize(QSize(16777215, 40))
        self.btn_data.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_8.addWidget(self.btn_data, 0, 0, 1, 1)

        self.btn_update = QPushButton(self.frame_buttons)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMinimumSize(QSize(0, 40))
        self.btn_update.setMaximumSize(QSize(16777215, 40))
        self.btn_update.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_8.addWidget(self.btn_update, 1, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_buttons, 2, 1, 1, 1)

        self.frame_today = QFrame(self.frame_container)
        self.frame_today.setObjectName(u"frame_today")
        sizePolicy.setHeightForWidth(self.frame_today.sizePolicy().hasHeightForWidth())
        self.frame_today.setSizePolicy(sizePolicy)
        self.frame_today.setMinimumSize(QSize(385, 340))
        self.frame_today.setMaximumSize(QSize(385, 340))
        self.frame_today.setFrameShape(QFrame.StyledPanel)
        self.frame_today.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_today)
        self.gridLayout_6.setSpacing(10)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(10, 10, 10, 10)
        self.info_moon = QLabel(self.frame_today)
        self.info_moon.setObjectName(u"info_moon")
        sizePolicy.setHeightForWidth(self.info_moon.sizePolicy().hasHeightForWidth())
        self.info_moon.setSizePolicy(sizePolicy)
        self.info_moon.setMinimumSize(QSize(80, 20))
        self.info_moon.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.info_moon, 6, 4, 1, 1)

        self.label_icon = QLabel(self.frame_today)
        self.label_icon.setObjectName(u"label_icon")
        sizePolicy.setHeightForWidth(self.label_icon.sizePolicy().hasHeightForWidth())
        self.label_icon.setSizePolicy(sizePolicy)
        self.label_icon.setMaximumSize(QSize(125, 125))
        self.label_icon.setPixmap(QPixmap(u":/resources/031-sun.png"))
        self.label_icon.setScaledContents(True)
        self.label_icon.setAlignment(Qt.AlignCenter)

        self.gridLayout_6.addWidget(self.label_icon, 1, 3, 2, 2)

        self.info_visibility = QLabel(self.frame_today)
        self.info_visibility.setObjectName(u"info_visibility")
        sizePolicy.setHeightForWidth(self.info_visibility.sizePolicy().hasHeightForWidth())
        self.info_visibility.setSizePolicy(sizePolicy)
        self.info_visibility.setMinimumSize(QSize(80, 20))
        self.info_visibility.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.info_visibility, 6, 1, 1, 1)

        self.label_temperature = QLabel(self.frame_today)
        self.label_temperature.setObjectName(u"label_temperature")
        sizePolicy1.setHeightForWidth(self.label_temperature.sizePolicy().hasHeightForWidth())
        self.label_temperature.setSizePolicy(sizePolicy1)
        self.label_temperature.setMinimumSize(QSize(0, 83))
        self.label_temperature.setMaximumSize(QSize(16777215, 83))

        self.gridLayout_6.addWidget(self.label_temperature, 1, 0, 1, 2)

        self.label_place = QLabel(self.frame_today)
        self.label_place.setObjectName(u"label_place")
        sizePolicy1.setHeightForWidth(self.label_place.sizePolicy().hasHeightForWidth())
        self.label_place.setSizePolicy(sizePolicy1)
        self.label_place.setMinimumSize(QSize(0, 40))
        self.label_place.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_6.addWidget(self.label_place, 0, 0, 1, 5)

        self.label_state = QLabel(self.frame_today)
        self.label_state.setObjectName(u"label_state")
        sizePolicy1.setHeightForWidth(self.label_state.sizePolicy().hasHeightForWidth())
        self.label_state.setSizePolicy(sizePolicy1)
        self.label_state.setMinimumSize(QSize(0, 32))
        self.label_state.setMaximumSize(QSize(16777215, 32))

        self.gridLayout_6.addWidget(self.label_state, 2, 0, 1, 2)

        self.info_humidity = QLabel(self.frame_today)
        self.info_humidity.setObjectName(u"info_humidity")
        sizePolicy.setHeightForWidth(self.info_humidity.sizePolicy().hasHeightForWidth())
        self.info_humidity.setSizePolicy(sizePolicy)
        self.info_humidity.setMinimumSize(QSize(80, 0))
        self.info_humidity.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.info_humidity, 4, 1, 1, 1)

        self.info_condensation = QLabel(self.frame_today)
        self.info_condensation.setObjectName(u"info_condensation")
        sizePolicy.setHeightForWidth(self.info_condensation.sizePolicy().hasHeightForWidth())
        self.info_condensation.setSizePolicy(sizePolicy)
        self.info_condensation.setMinimumSize(QSize(80, 20))
        self.info_condensation.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.info_condensation, 4, 4, 1, 1)

        self.info_uv = QLabel(self.frame_today)
        self.info_uv.setObjectName(u"info_uv")
        sizePolicy.setHeightForWidth(self.info_uv.sizePolicy().hasHeightForWidth())
        self.info_uv.setSizePolicy(sizePolicy)
        self.info_uv.setMinimumSize(QSize(80, 20))
        self.info_uv.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.info_uv, 5, 4, 1, 1)

        self.info_wind = QLabel(self.frame_today)
        self.info_wind.setObjectName(u"info_wind")
        sizePolicy.setHeightForWidth(self.info_wind.sizePolicy().hasHeightForWidth())
        self.info_wind.setSizePolicy(sizePolicy)
        self.info_wind.setMinimumSize(QSize(80, 20))
        self.info_wind.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.info_wind, 3, 4, 1, 1)

        self.info_maxmin = QLabel(self.frame_today)
        self.info_maxmin.setObjectName(u"info_maxmin")
        sizePolicy.setHeightForWidth(self.info_maxmin.sizePolicy().hasHeightForWidth())
        self.info_maxmin.setSizePolicy(sizePolicy)
        self.info_maxmin.setMinimumSize(QSize(80, 20))
        self.info_maxmin.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.info_maxmin, 3, 1, 1, 1)

        self.label_wind = QLabel(self.frame_today)
        self.label_wind.setObjectName(u"label_wind")
        sizePolicy.setHeightForWidth(self.label_wind.sizePolicy().hasHeightForWidth())
        self.label_wind.setSizePolicy(sizePolicy)
        self.label_wind.setMinimumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.label_wind, 3, 3, 1, 1)

        self.label_condensation = QLabel(self.frame_today)
        self.label_condensation.setObjectName(u"label_condensation")
        sizePolicy.setHeightForWidth(self.label_condensation.sizePolicy().hasHeightForWidth())
        self.label_condensation.setSizePolicy(sizePolicy)
        self.label_condensation.setMinimumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.label_condensation, 4, 3, 1, 1)

        self.label_pressure = QLabel(self.frame_today)
        self.label_pressure.setObjectName(u"label_pressure")
        sizePolicy.setHeightForWidth(self.label_pressure.sizePolicy().hasHeightForWidth())
        self.label_pressure.setSizePolicy(sizePolicy)
        self.label_pressure.setMinimumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.label_pressure, 5, 0, 1, 1)

        self.label_moon = QLabel(self.frame_today)
        self.label_moon.setObjectName(u"label_moon")
        sizePolicy.setHeightForWidth(self.label_moon.sizePolicy().hasHeightForWidth())
        self.label_moon.setSizePolicy(sizePolicy)
        self.label_moon.setMinimumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.label_moon, 6, 3, 1, 1)

        self.label_visibility = QLabel(self.frame_today)
        self.label_visibility.setObjectName(u"label_visibility")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(80)
        sizePolicy3.setVerticalStretch(20)
        sizePolicy3.setHeightForWidth(self.label_visibility.sizePolicy().hasHeightForWidth())
        self.label_visibility.setSizePolicy(sizePolicy3)

        self.gridLayout_6.addWidget(self.label_visibility, 6, 0, 1, 1)

        self.label_uv = QLabel(self.frame_today)
        self.label_uv.setObjectName(u"label_uv")
        sizePolicy.setHeightForWidth(self.label_uv.sizePolicy().hasHeightForWidth())
        self.label_uv.setSizePolicy(sizePolicy)
        self.label_uv.setMinimumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.label_uv, 5, 3, 1, 1)

        self.label_humidity = QLabel(self.frame_today)
        self.label_humidity.setObjectName(u"label_humidity")
        sizePolicy.setHeightForWidth(self.label_humidity.sizePolicy().hasHeightForWidth())
        self.label_humidity.setSizePolicy(sizePolicy)
        self.label_humidity.setMinimumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.label_humidity, 4, 0, 1, 1)

        self.label_maxmin = QLabel(self.frame_today)
        self.label_maxmin.setObjectName(u"label_maxmin")
        sizePolicy.setHeightForWidth(self.label_maxmin.sizePolicy().hasHeightForWidth())
        self.label_maxmin.setSizePolicy(sizePolicy)
        self.label_maxmin.setMinimumSize(QSize(80, 20))

        self.gridLayout_6.addWidget(self.label_maxmin, 3, 0, 1, 1)

        self.info_pressure = QLabel(self.frame_today)
        self.info_pressure.setObjectName(u"info_pressure")
        sizePolicy.setHeightForWidth(self.info_pressure.sizePolicy().hasHeightForWidth())
        self.info_pressure.setSizePolicy(sizePolicy)
        self.info_pressure.setMinimumSize(QSize(80, 20))
        self.info_pressure.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_6.addWidget(self.info_pressure, 5, 1, 1, 1)

        self.line = QFrame(self.frame_today)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_6.addWidget(self.line, 3, 2, 4, 1)


        self.gridLayout_4.addWidget(self.frame_today, 1, 0, 2, 1)


        self.gridLayout_2.addWidget(self.frame_container, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_principal, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_data, self.btn_update)
        QWidget.setTabOrder(self.btn_update, self.btn_minimize)
        QWidget.setTabOrder(self.btn_minimize, self.btn_exit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_minimize.setText("")
        self.btn_exit.setText("")
        self.label_ibm.setText(QCoreApplication.translate("MainWindow", u"Proporcionado por IBM Cloud", None))
        self.state_day1.setText(QCoreApplication.translate("MainWindow", u"Mayormente nublado", None))
        self.state_day5.setText(QCoreApplication.translate("MainWindow", u"Mayormente nublado", None))
        self.state_day6.setText(QCoreApplication.translate("MainWindow", u"Mayormente nublado", None))
        self.maxmin_day8.setText(QCoreApplication.translate("MainWindow", u"00\u00b0/00\u00b0", None))
        self.maxmin_day6.setText(QCoreApplication.translate("MainWindow", u"00\u00b0/00\u00b0", None))
        self.maxmin_day7.setText(QCoreApplication.translate("MainWindow", u"00\u00b0/00\u00b0", None))
        self.maxmin_day9.setText(QCoreApplication.translate("MainWindow", u"00\u00b0/00\u00b0", None))
        self.maxmin_day4.setText(QCoreApplication.translate("MainWindow", u"00\u00b0/00\u00b0", None))
        self.maxmin_day5.setText(QCoreApplication.translate("MainWindow", u"00\u00b0/00\u00b0", None))
        self.state_day8.setText(QCoreApplication.translate("MainWindow", u"Mayormente nublado", None))
        self.state_day4.setText(QCoreApplication.translate("MainWindow", u"Mayormente nublado", None))
        self.state_day7.setText(QCoreApplication.translate("MainWindow", u"Mayormente nublado", None))
        self.state_day3.setText(QCoreApplication.translate("MainWindow", u"Mayormente nublado", None))
        self.state_day9.setText(QCoreApplication.translate("MainWindow", u"Mayormente nublado", None))
        self.state_day2.setText(QCoreApplication.translate("MainWindow", u"Mayormente nublado", None))
        self.label_day8.setText(QCoreApplication.translate("MainWindow", u"Ma\u00f1ana", None))
        self.label_day5.setText(QCoreApplication.translate("MainWindow", u"Ma\u00f1ana", None))
        self.label_day6.setText(QCoreApplication.translate("MainWindow", u"Ma\u00f1ana", None))
        self.label_day10.setText(QCoreApplication.translate("MainWindow", u"Ma\u00f1ana", None))
        self.label_day7.setText(QCoreApplication.translate("MainWindow", u"Ma\u00f1ana", None))
        self.label_day9.setText(QCoreApplication.translate("MainWindow", u"Ma\u00f1ana", None))
        self.maxmin_day10.setText(QCoreApplication.translate("MainWindow", u"00\u00b0/00\u00b0", None))
        self.maxmin_day2.setText(QCoreApplication.translate("MainWindow", u"00\u00b0/00\u00b0", None))
        self.maxmin_day3.setText(QCoreApplication.translate("MainWindow", u"00\u00b0/00\u00b0", None))
        self.label_day1.setText(QCoreApplication.translate("MainWindow", u"Ma\u00f1ana", None))
        self.label_day2.setText(QCoreApplication.translate("MainWindow", u"Ma\u00f1ana", None))
        self.label_day3.setText(QCoreApplication.translate("MainWindow", u"Ma\u00f1ana", None))
        self.label_day4.setText(QCoreApplication.translate("MainWindow", u"Ma\u00f1ana", None))
        self.maxmin_day1.setText(QCoreApplication.translate("MainWindow", u"00\u00b0/00\u00b0", None))
        self.state_day10.setText(QCoreApplication.translate("MainWindow", u"Mayormente nublado", None))
        self.wind_day1.setText(QCoreApplication.translate("MainWindow", u"SSE 00 km/h", None))
        self.wind_day2.setText(QCoreApplication.translate("MainWindow", u"SSE 00 km/h", None))
        self.wind_day3.setText(QCoreApplication.translate("MainWindow", u"SSE 00 km/h", None))
        self.wind_day4.setText(QCoreApplication.translate("MainWindow", u"SSE 00 km/h", None))
        self.wind_day5.setText(QCoreApplication.translate("MainWindow", u"SSE 00 km/h", None))
        self.wind_day6.setText(QCoreApplication.translate("MainWindow", u"SSE 00 km/h", None))
        self.wind_day7.setText(QCoreApplication.translate("MainWindow", u"SSE 00 km/h", None))
        self.wind_day8.setText(QCoreApplication.translate("MainWindow", u"SSE 00 km/h", None))
        self.wind_day9.setText(QCoreApplication.translate("MainWindow", u"SSE 00 km/h", None))
        self.wind_day10.setText(QCoreApplication.translate("MainWindow", u"SSE 00 km/h", None))
        self.label_forecast.setText(QCoreApplication.translate("MainWindow", u"Pron\u00f3stico", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"Fecha:", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"WEATHER APP", None))
        self.label_hour.setText(QCoreApplication.translate("MainWindow", u"Hora:", None))
        self.btn_data.setText(QCoreApplication.translate("MainWindow", u"BASE DE DATOS", None))
        self.btn_update.setText(QCoreApplication.translate("MainWindow", u"ACTUALIZAR", None))
        self.info_moon.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_icon.setText("")
        self.info_visibility.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_temperature.setText(QCoreApplication.translate("MainWindow", u"28\u00b0", None))
        self.label_place.setText(QCoreApplication.translate("MainWindow", u"Tiempo en Lima", None))
        self.label_state.setText(QCoreApplication.translate("MainWindow", u"Soleado", None))
        self.info_humidity.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.info_condensation.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.info_uv.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.info_wind.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.info_maxmin.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_wind.setText(QCoreApplication.translate("MainWindow", u"Viento", None))
        self.label_condensation.setText(QCoreApplication.translate("MainWindow", u"Condensaci\u00f3n", None))
        self.label_pressure.setText(QCoreApplication.translate("MainWindow", u"Presi\u00f3n", None))
        self.label_moon.setText(QCoreApplication.translate("MainWindow", u"Fase lunar", None))
        self.label_visibility.setText(QCoreApplication.translate("MainWindow", u"Visibilidad", None))
        self.label_uv.setText(QCoreApplication.translate("MainWindow", u"\u00efndice UV", None))
        self.label_humidity.setText(QCoreApplication.translate("MainWindow", u"Humedad", None))
        self.label_maxmin.setText(QCoreApplication.translate("MainWindow", u"M\u00e1x./Min.", None))
        self.info_pressure.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

