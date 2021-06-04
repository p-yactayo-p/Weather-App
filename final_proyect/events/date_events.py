from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

def send_date(label_day, label_hour):
    update_time(label_hour)
    update_date(label_day)

def update_date(label_day):
    current_date = QDate.currentDate()
    display_text = current_date.toString("dd MMM yyyy")
    label_day.setText("Fecha: {}".format(display_text))

def update_time(label_hour):
    current_time = QTime.currentTime()
    display_text = current_time.toString("hh:mm")
    label_hour.setText("Hora: {}".format(display_text))
