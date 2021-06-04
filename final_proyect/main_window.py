from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from design.ps2_main_window import Ui_MainWindow
import sys
# Importar datos webscraping
from web_scraping.code_actual import send_data_actual
from web_scraping.code_forecast import send_data_forecast
# Importar hora y fecha actual
from events.date_events import *
# Importar eventos
from events.window_events import *
# Importar ventana base de datos
from record import widget_record
# Importar base de datos para agregar y editar informacion
from database.connector_record import data_base

class main_window(QMainWindow):
    def __init__(self):
        super(main_window, self).__init__()
        self.main = Ui_MainWindow()
        self.main.setupUi(self)
        # Actualizar el tiempo
        hour = QTimer(self)
        hour.timeout.connect(lambda: send_date(self.main.label_date, self.main.label_hour))
        hour.start(1000)
        # Minimizar ventana
        self.main.btn_minimize.clicked.connect(lambda: minimize_window(self))
        # Cerrar ventana
        self.main.btn_exit.clicked.connect(lambda: close_window(self))
        # Conexion data base y main
        self.connect = data_base()
        # Llenar datos actuales
        self.fill_data()
        # Definir el icono de estado
        self.change_icon(self.main.label_state.text(), self.main.label_icon)
        # Llenar datos predicciones
        self.forecast_data()
        # Abrir base de datos
        self.main.btn_data.clicked.connect(self.open_db)
        # Actualizar datos actuales
        self.main.btn_update.clicked.connect(self.update_data)

    def fill_data(self):
        # Obtener datos de webscraping
        data = send_data_actual()
        # Llenar datos
        self.main.label_temperature.setText(data[0])
        self.main.label_state.setText(data[1])
        self.main.info_maxmin.setText(data[2])
        self.main.info_wind.setText(data[3])
        self.main.info_humidity.setText(data[4])
        self.main.info_condensation.setText(data[5])
        self.main.info_pressure.setText(data[6])
        self.main.info_uv.setText(data[7])
        self.main.info_visibility.setText(data[8])
        self.main.info_moon.setText(data[9])

    def update_data(self):
        # Actualizar informacion actual y pronostico
        self.fill_data
        self.forecast_data
        # Obtener ultimo data guardado en la base de datos
        last_data = self.connect.get_data()[0]
        # Editar base de datos
        # Obtener temperatura y viento del dia
        pronostico = send_data_forecast()
        actual = []
        # Obtener datos para enviar a la base de datos
        for i in range(5):
            actual.append(pronostico[i][0])
        dia = self.main.label_date.text()[7::]
        temp = actual[1] + "/" + actual[2]
        viento = actual[4]
        # Comprobar si hay datos guardados en el dia
        if last_data[1] == dia:
            # Si hay datos almacenados actualizamos
            if actual[0] == "Hoy":
                self.connect.update_data((temp, viento, dia))
            # No se guarda datos de la noche
            else:
                pass
        else:
            # Si no hay datos guardados se debe agregar
            if temp[0:2] == "--":
                temp = str(int(temp[3:5]) + 4) + "°" + temp[2::]
                self.connect.add_data((dia, temp, viento))
            else:
                self.connect.add_data((dia, temp, viento))

    def open_db(self):
        # Abrir registro
        window_db = widget_record()
        window_db.show()


    def forecast_data(self):
        # Obtener datos de webscraping
        data = send_data_forecast()
        # Llenar label dias
        for i in range(1, 11):
            exec('self.main.label_day' + str(i) + '.setText(data[0][' + str(i) + '])')
        # Llenar label max/min
        for i in range(1, 11):
            exec('self.main.maxmin_day' + str(i) + '.setText(data[1][' + str(i) + '] + "/" + data[2][' + str(i) + '])')
        # Llenar label estado
        for i in range(1, 11):
            exec('self.main.state_day' + str(i) + '.setText(data[3][' + str(i) + '])')
        # Llenar label viento
        for i in range(1, 11):
            exec('self.main.wind_day' + str(i) + '.setText(data[4][' + str(i) + '])')

    def change_icon(self, state, label):
        if state == "Soleado":
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            label.setMaximumSize(QSize(125, 125))
            label.setPixmap(QPixmap(u":/resources/031-sun.png"))
            label.setScaledContents(True)
            label.setAlignment(Qt.AlignCenter)
        elif state == "Mayormente soleado":
            self.main.label_state.setStyleSheet("font-size: 17px")
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            label.setMaximumSize(QSize(125, 125))
            label.setPixmap(QPixmap(u":/resources/031-sun-1.png"))
            label.setScaledContents(True)
            label.setAlignment(Qt.AlignCenter)
        elif state == "Parcialmente nublado":
            self.main.label_state.setStyleSheet("font-size: 17px")
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            label.setMaximumSize(QSize(125, 125))
            label.setPixmap(QPixmap(u":/resources/031-sun-4.png"))
            label.setScaledContents(True)
            label.setAlignment(Qt.AlignCenter)

        elif state == "Muy nublado":
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            label.setMaximumSize(QSize(125, 125))
            label.setPixmap(QPixmap(u":/resources/031-cloudy.png"))
            label.setScaledContents(True)
            label.setAlignment(Qt.AlignCenter)
        elif state == "Chubascos":
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            label.setMaximumSize(QSize(125, 125))
            label.setPixmap(QPixmap(u":/resources/031-rainy-1.png"))
            label.setScaledContents(True)
            label.setAlignment(Qt.AlignCenter)
        elif state == "Lluvia por la tarde":
            self.main.label_state.setStyleSheet("font-size: 17px")
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            label.setMaximumSize(QSize(125, 125))
            label.setPixmap(QPixmap(u":/resources/031-rainy.png"))
            label.setScaledContents(True)
            label.setAlignment(Qt.AlignCenter)
        else:
            sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
            sizePolicy.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
            label.setSizePolicy(sizePolicy)
            label.setMaximumSize(QSize(125, 125))
            label.setPixmap(QPixmap(u":/resources/031-fog.png"))
            label.setScaledContents(True)
            label.setAlignment(Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    my_app = main_window()
    my_app.show()
    sys.exit(app.exec_())
