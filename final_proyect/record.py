from PySide2.QtCore import QRectF
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from design.ps2_widget_record import Ui_Record
from events.window_events import *
import sys
# Importar base de datos para obtener la informacion
from database.connector_record import data_base
# Importar libreria para crear graficos
from PySide2.QtCharts import QtCharts

class widget_record(QWidget):
    def __init__(self):
        super(widget_record, self).__init__()
        self.record = Ui_Record()
        self.record.setupUi(self)
        # Conexion data base y record
        self.connect = data_base()
        # Mostrar los datos en la tabla
        self.show_data()
        # Mostrar grafico semanal y mensual
        self.show_graphics()
        # Cerrar ventana
        self.record.btn_exit.clicked.connect(lambda: close_window(self))

    def show_data(self):
        # Obtaner datos metereologicos
        data = self.connect.get_data()
        # Limpiar tabla
        self.record.table_record.clearContents()
        self.record.table_record.setRowCount(0)
        # Eliminar id de los datos
        main_data = [x[1::] for x in data]
        # Setear filas, columnas y encabezados
        column = len(main_data[0])
        row = len(main_data)
        self.record.table_record.setColumnCount(column)
        self.record.table_record.setRowCount(row)
        self.record.table_record.setHorizontalHeaderLabels(("Fecha", "C°", "Viento"))
        # Mostrar datos en la tabla
        for r in range(row):
            for c in range(column):
                self.record.table_record.setItem(r, c, QTableWidgetItem(str(main_data[r][c])))
        # Solo lectura de datos para evitar cambioos del usuario
        self.record.table_record.setEditTriggers(QTableWidget.NoEditTriggers)
        # Ajustar celdas al tamaño del contenido
        self.record.table_record.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

    def show_graphics(self):
        # Crear estilo para los titulos de grafica
        font = QFont()
        font.setStyleName("Segoe UI")
        font.setWeight(75)
        font.setPixelSize(15)
        # Editar el estilo de la linea
        pen = QPen()
        pen.setColor("orange")
        pen.setWidth(5)
        # Obtener datos almacenados
        data = self.connect.get_data()
        # Separar datos de los ultimos 7 dias
        data_week = []
        for i in data:
            data_week.append((i[1][0:2], i[2][0:2]))
            if len(data_week) == 7:
                break
        data_week.reverse()
        # Plotear grafica semanal con los datos seleccionados
        series_week = QtCharts.QLineSeries(self)
        for i in data_week:
            series_week.append(int(i[0]), int(i[1]))
        # Crear y editar la grafica
        chart_week = QtCharts.QChart()
        chart_week.setBackgroundVisible(False)
        chart_week.setTitleFont(font)
        series_week.setPen(pen)
        # Animaciones de la grafica
        chart_week.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        # Agregar los datos
        chart_week.addSeries(series_week)
        # Añadir ejes
        chart_week.createDefaultAxes()
        # Editar ttitulo
        chart_week.setTitle("Últimos 7 días")
        # Quitar leyenda
        chart_week.legend().setVisible(False)
        # Crear visibilidad
        chartview_week = QtCharts.QChartView(chart_week)
        # Suavizar la grafica
        chartview_week.setRenderHint(QPainter.Antialiasing, True)
        # Ejes maximos y minimos
        axis_x = QtCharts.QValueAxis()
        axis_x.setRange(14, 24)
        # Insertar grafica en frame_info
        self.record.gridLayout_5.addWidget(chartview_week, 1, 0, 1, 1)
        
        # Separar datos del mes actual
        data_month = []
        for i in data:
            if i[1][3:6] == data[0][1][3:6]:
                data_month.append((i[1][0:2], i[2][0:2]))
            elif i[1][3:6] != data[0][3:6]:
                break
        data_month.reverse()
        # Plotear grafica mensual con los datos seleccionados
        series_month = QtCharts.QLineSeries(self)
        for i in data_month:
            series_month.append(int(i[0]), int(i[1]))
        # Crear y editar la grafica
        chart_month = QtCharts.QChart()
        chart_month.setBackgroundVisible(False)
        chart_month.setTitleFont(font)
        series_month.setPen(pen)
        # Animaciones de la grafica
        chart_month.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        # Agregar los datos
        chart_month.addSeries(series_month)
        # Añadir ejes
        chart_month.createDefaultAxes()
        # Editar ttitulo
        chart_month.setTitle("Mes actual")
        # Quitar leyenda
        chart_month.legend().setVisible(False)
        # Crear visibilidad
        chartview_month = QtCharts.QChartView(chart_month)
        # Suavizar la grafica
        chartview_month.setRenderHint(QPainter.Antialiasing, True)
        # Insertar grafica en frame_info
        self.record.gridLayout_5.addWidget(chartview_month, 2, 0, 1, 1)

if __name__ == '__main__':
    window = QApplication(sys.argv)
    my_window = widget_record()
    my_window.show()
    sys.exit(window.exec_())
