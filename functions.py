import telebot

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


