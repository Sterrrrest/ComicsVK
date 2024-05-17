import requests
import os


from environs import Env
from pathlib import Path
from functions import send_post, get_random_comics, get_filepath


if __name__ == '__main__':

    env = Env()
    env.read_env()
    chat_id = env.str('CLIENT_ID')
    tg_token = env.str('TG_TOKEN')


    dir = 'pictures'
    Path(dir).mkdir(parents=True, exist_ok=True)

    try:
        last_comics_url = 'https://xkcd.com/info.0.json'

        response_random_url = f'https://xkcd.com/{get_random_comics(last_comics_url)}/info.0.json'
        response_random_comics = requests.get(response_random_url)
        response_random_comics.raise_for_status()

        response_random_comics_json = response_random_comics.json()
        response_img = requests.get(response_random_comics_json['img'])
        response_img.raise_for_status()

        comment = response_random_comics_json['alt']
        file_path = get_filepath(response_random_comics_json, dir)
        send_post(file_path, comment, response_img, chat_id, tg_token)

    finally:
        os.remove(file_path)
