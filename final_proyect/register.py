from PySide2.QtWidgets import *
from PySide2.QtGui import *
from design.ps2_widget_register import Ui_Register
from events.window_events import *
import sys
# Abrir ventanas
from main_window import main_window
# Conexion entre base de datos y registro
from database.connector_users import data_base

class widget_register(QWidget):
    def __init__(self):
        super(widget_register, self).__init__()
        self.register = Ui_Register()
        self.register.setupUi(self)
        # Conexion data base y registro
        self.connect = data_base()
        # Registrar cuenta y abrir ventana principal
        self.register.btn_register.clicked.connect(self.validate_register)
        # Cerrar ventana
        self.register.btn_exit.clicked.connect(lambda: close_window(self))

    def open_main_window(self):
        # Cerrar ventana registro para acceder a la aplicacion
        self.close()
        # Abrir aplicacion
        window_main = main_window()
        window_main.show()

    def validate_register(self):
        # Capturar los datos ingresados
        name = self.register.line_user.text()
        email = self.register.line_email.text()
        password = self.register.line_password.text()
        aux = [name, email, password]
        data = tuple([x for x in aux if x != "" and x != " "])
        # Enviar los datos para el registro
        answer = self.connect.add_data(data)
        # Decidir si se accede a la ventana principal o se envia un mensaje
        if answer[0] == True:
            self.open_main_window()
        else:
            self.register.label_message.setText(answer[1])

if __name__ == '__main__':
    window = QApplication(sys.argv)
    my_window = widget_register()
    my_window.show()
    sys.exit(window.exec_())
