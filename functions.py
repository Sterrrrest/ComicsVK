import telebot
import requests
import random


def send_post(file_path, comment, response_img, chat_id, tg_token):

    bot = telebot.TeleBot(token=tg_token)
    with open(file_path, 'wb') as file:
        file.write(response_img.content)

    with open(file_path, 'rb') as file:
        bot.send_document(chat_id=chat_id, document=file)

    bot.send_message(chat_id=chat_id, text=comment)


def get_random_comic(url):

    response_last_comic = requests.get(url)
    response_last_comic.raise_for_status()
    last_comic = response_last_comic.json()['num']
    random_comic = random.choice(range(1, last_comic))

    return random_comic


def get_filepath(response, dir):
    filename = response['img'].split(sep='/')[-1]
    file_path = f'{dir}/{filename}'

    return file_path
