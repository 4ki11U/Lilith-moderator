from database_files.Telegram_DataUsers import TelegramDB
from database_files.randomize import randomize
from datetime import datetime
import random

tg_database = TelegramDB(database_file=r'database_files/tg_datausers.db')
randomize_database = randomize(database_file=r'database_files/randomize.db')

def select_users_from_db(mess_id_to_check) :
    result_from_select = tg_database.select_from_db(mess_id_to_check)

    if not result_from_select :
        return False
    else :
        return True


def select_user_from_db(mess_id_to_check) :
    result_from_select = tg_database.select_from_db(mess_id_to_check.id)

    if not result_from_select :
        return False
    else :
        return True

def add_new_user_into_db(user_data):
    select_user_from_db(user_data)
    if select_user_from_db(user_data) == False :
        now = str(datetime.today().strftime('%d-%m-%Y'))
        tg_database.insert_into_db(user_data.id,
                                   user_data.first_name,
                                   user_data.username,
                                   user_data.last_name,
                                   now)

def antibot_check(chat_member):
    return chat_member['status'] != 'left'



def randomize_number_insert_into_db(randomize_number, user_data):
    randomize_database.insert_into_db(randomize_number, user_data.id)

def randomize_number_select_from_db(user_data):
    return randomize_database.select_from_db(user_data)

def delete_from_db_randomize_number(user_data):
    randomize_database.delete_from_db(user_data)