import sqlite3

class data_base:
    def __init__(self):
        # Conexion con la base de datos
        self.connector = sqlite3.connect("database/db_record.db")
        self.cursor = self.connector.cursor()

    def get_data(self):
        # Obtener datos metereologicos
        self.cursor.execute("SELECT * FROM record ORDER BY id DESC")
        data = self.cursor.fetchall()
        return data

    def validate(self, data):
        # Comprobar si los datos estan completos
        return len(data) == 3

    def add_data(self, data):
        # Se agregan los datos obtenidos
        self.cursor.execute("INSERT INTO record(day, temperature, wind) VALUES(?, ?, ?)", data)
        self.connector.commit()

    def update_data(self, data):
        # Se actualizan los datos
        self.cursor.execute("UPDATE record SET temperature = ?, wind = ? WHERE day = ?", data)
        self.connector.commit()

if __name__ == '__main__':
    pass
