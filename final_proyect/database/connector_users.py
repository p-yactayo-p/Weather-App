import sqlite3

class data_base:
    def __init__(self):
        # Conexion con la base de datos
        self.connector = sqlite3.connect("database/db_users.db")
        self.cursor = self.connector.cursor()

    def validate_account(self, email, password):
        # Obtener cuentas registradas
        self.cursor.execute("SELECT * FROM users ORDER BY id DESC")
        data = self.cursor.fetchall()
        # Validar si la cuenta existe
        for i in data:
            if email == i[2]:
                if password == i[3]:
                    booleano = True
                    message = "Bienvenido"
                else:
                    booleano = False
                    message = "Contraseña incorrecta."
                break
            else:
                booleano = False
                message = "Cuenta no registrada."
        return [booleano, message]

    def validate(self, data):
        # Comprobar si los datos estan completos
        return len(data) == 3

    def add_data(self, data):
        # Obtener cuentas registradas para evitar repetidos
        self.cursor.execute("SELECT * FROM users ORDER BY id DESC")
        accounts = self.cursor.fetchall()
        # Comprobar cuentas existentes
        if self.validate(data):
            for i in accounts:
                if data[1] == i[2]:
                    aux = False
                    break
                else:
                    aux = True
            # Registrar cuenta y enviar respuesta
            if aux:
                self.cursor.execute("INSERT INTO users(name, email, password) VALUES(?, ?, ?)", data)
                self.connector.commit()
                booleano = True
                message = "Bienvenido"
            else:
                booleano = False
                message = "Cuenta existente."
        else:
            booleano = False
            message = "Debe llenar todos los campos."
        return [booleano, message]

if __name__ == '__main__':
    pass
