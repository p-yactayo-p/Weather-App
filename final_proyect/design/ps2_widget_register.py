# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widget_register.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(300, 550)
        # Quitar bordes de ventana
        Register.setAttribute(Qt.WA_TranslucentBackground)
        Register.setWindowFlag(Qt.FramelessWindowHint)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Register.sizePolicy().hasHeightForWidth())
        Register.setSizePolicy(sizePolicy)
        Register.setMinimumSize(QSize(300, 550))
        Register.setMaximumSize(QSize(300, 550))
        Register.setStyleSheet(u"QFrame{\n"
"	background: rgba(250,250,250,255);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgba(27,52,124,255);\n"
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
"QLineEdit{\n"
"	color: white;\n"
"	background: rgba(73,93,151,255);\n"
"	font-family: Segoe UI;\n"
"	font-size: 10px;\n"
"	border: 0px solid rgba(73,93,151,255);\n"
"	border-radius: 13px;\n"
"	padding-left: 10px;\n"
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
"QLabel#label_title{\n"
"	font-size: 25px;\n"
"	font-family: Segoe UI Black;\n"
"}\n"
"\n"
"QLabel#label_signup{\n"
"	font-size: 15px;\n"
"	fon"
                        "t-family: Segoe UI Black;\n"
"}\n"
"\n"
"QLabel#label_message{\n"
"	color: red;\n"
"}\n"
"\n"
"QPushButton#btn_exit{\n"
"	background: rgba(250,250,250,255);\n"
"	border-radius: 7px;\n"
"}")
        self.gridLayout = QGridLayout(Register)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_principal = QFrame(Register)
        self.frame_principal.setObjectName(u"frame_principal")
        sizePolicy.setHeightForWidth(self.frame_principal.sizePolicy().hasHeightForWidth())
        self.frame_principal.setSizePolicy(sizePolicy)
        self.frame_principal.setMinimumSize(QSize(300, 550))
        self.frame_principal.setMaximumSize(QSize(300, 550))
        self.frame_principal.setFrameShape(QFrame.StyledPanel)
        self.frame_principal.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_principal)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setVerticalSpacing(5)
        self.gridLayout_7.setContentsMargins(25, 5, 25, 25)
        self.frame_container = QFrame(self.frame_principal)
        self.frame_container.setObjectName(u"frame_container")
        sizePolicy.setHeightForWidth(self.frame_container.sizePolicy().hasHeightForWidth())
        self.frame_container.setSizePolicy(sizePolicy)
        self.frame_container.setMinimumSize(QSize(250, 500))
        self.frame_container.setMaximumSize(QSize(250, 500))
        self.frame_container.setFrameShape(QFrame.StyledPanel)
        self.frame_container.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_container)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 10, 10, 10)
        self.frame_title = QFrame(self.frame_container)
        self.frame_title.setObjectName(u"frame_title")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_title.sizePolicy().hasHeightForWidth())
        self.frame_title.setSizePolicy(sizePolicy1)
        self.frame_title.setMinimumSize(QSize(0, 50))
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_title)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        sizePolicy1.setHeightForWidth(self.label_title.sizePolicy().hasHeightForWidth())
        self.label_title.setSizePolicy(sizePolicy1)
        self.label_title.setMinimumSize(QSize(0, 50))
        self.label_title.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_title, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_title, 1, 0, 1, 1)

        self.frame_buttons = QFrame(self.frame_container)
        self.frame_buttons.setObjectName(u"frame_buttons")
        self.frame_buttons.setFrameShape(QFrame.StyledPanel)
        self.frame_buttons.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_buttons)
        self.gridLayout_5.setSpacing(10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(10, 10, 10, 10)
        self.btn_register = QPushButton(self.frame_buttons)
        self.btn_register.setObjectName(u"btn_register")
        sizePolicy1.setHeightForWidth(self.btn_register.sizePolicy().hasHeightForWidth())
        self.btn_register.setSizePolicy(sizePolicy1)
        self.btn_register.setMinimumSize(QSize(0, 40))
        self.btn_register.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.btn_register, 2, 0, 1, 1)

        self.label_message = QLabel(self.frame_buttons)
        self.label_message.setObjectName(u"label_message")
        sizePolicy1.setHeightForWidth(self.label_message.sizePolicy().hasHeightForWidth())
        self.label_message.setSizePolicy(sizePolicy1)
        self.label_message.setMinimumSize(QSize(0, 15))
        self.label_message.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.label_message, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_buttons, 3, 0, 1, 1)

        self.frame_register = QFrame(self.frame_container)
        self.frame_register.setObjectName(u"frame_register")
        sizePolicy1.setHeightForWidth(self.frame_register.sizePolicy().hasHeightForWidth())
        self.frame_register.setSizePolicy(sizePolicy1)
        self.frame_register.setMinimumSize(QSize(0, 265))
        self.frame_register.setFrameShape(QFrame.StyledPanel)
        self.frame_register.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_register)
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_signup = QLabel(self.frame_register)
        self.label_signup.setObjectName(u"label_signup")
        sizePolicy1.setHeightForWidth(self.label_signup.sizePolicy().hasHeightForWidth())
        self.label_signup.setSizePolicy(sizePolicy1)
        self.label_signup.setMinimumSize(QSize(0, 50))

        self.gridLayout_4.addWidget(self.label_signup, 0, 0, 1, 1)

        self.label_user = QLabel(self.frame_register)
        self.label_user.setObjectName(u"label_user")
        sizePolicy1.setHeightForWidth(self.label_user.sizePolicy().hasHeightForWidth())
        self.label_user.setSizePolicy(sizePolicy1)
        self.label_user.setMinimumSize(QSize(0, 15))

        self.gridLayout_4.addWidget(self.label_user, 1, 0, 1, 1)

        self.line_user = QLineEdit(self.frame_register)
        self.line_user.setObjectName(u"line_user")
        sizePolicy1.setHeightForWidth(self.line_user.sizePolicy().hasHeightForWidth())
        self.line_user.setSizePolicy(sizePolicy1)
        self.line_user.setMinimumSize(QSize(0, 30))
        self.line_user.setMaxLength(50)

        self.gridLayout_4.addWidget(self.line_user, 2, 0, 1, 1)

        self.label_email = QLabel(self.frame_register)
        self.label_email.setObjectName(u"label_email")
        sizePolicy1.setHeightForWidth(self.label_email.sizePolicy().hasHeightForWidth())
        self.label_email.setSizePolicy(sizePolicy1)
        self.label_email.setMinimumSize(QSize(0, 15))

        self.gridLayout_4.addWidget(self.label_email, 3, 0, 1, 1)

        self.line_email = QLineEdit(self.frame_register)
        self.line_email.setObjectName(u"line_email")
        sizePolicy1.setHeightForWidth(self.line_email.sizePolicy().hasHeightForWidth())
        self.line_email.setSizePolicy(sizePolicy1)
        self.line_email.setMinimumSize(QSize(0, 30))
        self.line_email.setMaxLength(50)

        self.gridLayout_4.addWidget(self.line_email, 4, 0, 1, 1)

        self.label_password = QLabel(self.frame_register)
        self.label_password.setObjectName(u"label_password")
        sizePolicy1.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy1)
        self.label_password.setMinimumSize(QSize(0, 15))

        self.gridLayout_4.addWidget(self.label_password, 5, 0, 1, 1)

        self.line_password = QLineEdit(self.frame_register)
        self.line_password.setObjectName(u"line_password")
        sizePolicy1.setHeightForWidth(self.line_password.sizePolicy().hasHeightForWidth())
        self.line_password.setSizePolicy(sizePolicy1)
        self.line_password.setMinimumSize(QSize(0, 30))
        self.line_password.setMaxLength(50)
        self.line_password.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.line_password, 6, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_register, 2, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame_container, 1, 0, 1, 1)

        self.frame_exit = QFrame(self.frame_principal)
        self.frame_exit.setObjectName(u"frame_exit")
        sizePolicy1.setHeightForWidth(self.frame_exit.sizePolicy().hasHeightForWidth())
        self.frame_exit.setSizePolicy(sizePolicy1)
        self.frame_exit.setMinimumSize(QSize(0, 15))
        self.frame_exit.setMaximumSize(QSize(16777215, 15))
        self.frame_exit.setFrameShape(QFrame.StyledPanel)
        self.frame_exit.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_exit)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.btn_exit = QPushButton(self.frame_exit)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(14, 14))
        self.btn_exit.setMaximumSize(QSize(14, 14))
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_6.addWidget(self.btn_exit, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.frame_exit, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_principal, 1, 0, 1, 1)

        QWidget.setTabOrder(self.line_user, self.line_email)
        QWidget.setTabOrder(self.line_email, self.line_password)
        QWidget.setTabOrder(self.line_password, self.btn_register)
        QWidget.setTabOrder(self.btn_register, self.btn_exit)

        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Form", None))
        self.label_title.setText(QCoreApplication.translate("Register", u"WEATHER APP", None))
        self.btn_register.setText(QCoreApplication.translate("Register", u"REGISTRAR CUENTA", None))
        self.label_message.setText("")
        self.label_signup.setText(QCoreApplication.translate("Register", u"REGISTRO", None))
        self.label_user.setText(QCoreApplication.translate("Register", u"NOMBRES Y APELLIDOS", None))
        self.label_email.setText(QCoreApplication.translate("Register", u"CORREO ELECTR\u00d3NICO", None))
        self.label_password.setText(QCoreApplication.translate("Register", u"CONTRASE\u00d1A", None))
        self.btn_exit.setText("")
    # retranslateUi

