import requests
import os


from environs import Env
from pathlib import Path
from functions import send_post, get_random_comic, get_filepath


if __name__ == '__main__':

    env = Env()
    env.read_env()
    chat_id = env.str('CLIENT_ID')
    tg_token = env.str('TG_TOKEN')


    dir = 'pictures'
    Path(dir).mkdir(parents=True, exist_ok=True)

    try:
        last_comic_url = 'https://xkcd.com/info.0.json'

        random_url = f'https://xkcd.com/{get_random_comic(last_comic_url)}/info.0.json'
        random_url_response = requests.get(random_url)
        random_url_response.raise_for_status()

        random_comic_response = random_url_response.json()
        response_img = requests.get(random_comic_response['img'])
        response_img.raise_for_status()

        comment = random_comic_response['alt']
        file_path = get_filepath(random_comic_response, dir)
        send_post(file_path, comment, response_img, chat_id, tg_token)

    finally:
        os.remove(file_path)
