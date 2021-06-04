from PySide2.QtWidgets import *
from PySide2.QtGui import *
from design.ps2_widget_login import Ui_Login
from events.window_events import *
import sys
# Abrir ventanas
from main_window import main_window
from register import widget_register
# Importar base de datos parfa validacion
from database.connector_users import data_base

class widget_login(QWidget):
    def __init__(self):
        super(widget_login, self).__init__()
        self.login = Ui_Login()
        self.login.setupUi(self)
        # Conexion data base y login
        self.connect = data_base()
        # Abrir registro
        self.login.btn_new.clicked.connect(self.open_register)
        # Validar usuario y abrir ventana principal
        self.login.btn_login.clicked.connect(self.validate_user)
        # Cerrar ventana
        self.login.btn_exit.clicked.connect(lambda: close_window(self))

    def open_register(self):
        # Cerrar ventana login para poder registrarse
        self.close()
        # Abrir registro
        window_register = widget_register()
        window_register.show()

    def open_main_window(self):
        # Cerrar ventana login para acceder a la aplicacion
        self.close()
        # Abrir aplicacion
        window_main = main_window()
        window_main.show()

    def validate_user(self):
        # Obtener datos ingresados
        email = self.login.line_email.text()
        password = self.login.line_password.text()
        # Validar cuenta
        answer = self.connect.validate_account(email, password)
        # Decidir si se accede a la ventana principal o se envia un mensaje
        if answer[0] == True:
            self.open_main_window()
        else:
            self.login.label_message.setText(answer[1])

if __name__ == '__main__':
    window = QApplication(sys.argv)
    my_window = widget_login()
    my_window.show()
    sys.exit(window.exec_())
