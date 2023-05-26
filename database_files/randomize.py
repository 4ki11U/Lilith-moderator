import sqlite3


class randomize :
    def __init__(self, database_file):
        """Инициализация соединения с Базой Данных"""
        self.connection = sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS randomize (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
		randomize_number INT NOT NULL,
		telegram_id INT NOT NULL
		)""")
        self.connection.commit()

    def select_from_db(self, telegram_id):

        try:
            result = self.cursor.execute("""SELECT * FROM randomize WHERE telegram_id = '{}' """.format(telegram_id))
            return result.fetchall()
        except sqlite3.Error as e:
            print("Error SQLite3 : ", e)

    def insert_into_db(self, randomize_number, telegram_id):

        try:
            self.cursor.execute("""INSERT INTO randomize (randomize_number, telegram_id) VALUES (?,?)""", (randomize_number,telegram_id,))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Error SQLite3 : ", e)

    def delete_from_db(self, telegram_id):
        try:
            self.cursor.execute("""DELETE FROM randomize WHERE telegram_id = '{}' """.format(telegram_id))
            self.connection.commit()
        except sqlite3.Error as e:
            print("Error SQLite3 : ", e)
