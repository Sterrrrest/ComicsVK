import telebot
import requests
import random

from environs import Env



def send_post(file_path, comment, response_img):

    env = Env()
    env.read_env()
    chat_id = env.str('CLIENT_ID')
    tg_token = env.str('TG_TOKEN')
    bot = telebot.TeleBot(token=tg_token)

    with open(file_path, 'wb') as file:
        file.write(response_img.content)

    with open(file_path, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)

    bot.send_message(chat_id=chat_id, text=comment)

def get_random_comics(url):

    response_last_comics = requests.get(url)
    response_last_comics.raise_for_status()
    last_comics = response_last_comics.json()['num']
    random_comics = random.choice(range(1, last_comics))

    return random_comics


def get_filepath(response, dir):
    filename = response['img'].split(sep='/')[-1]
    file_path = f'{dir}/{filename}'

    return file_path