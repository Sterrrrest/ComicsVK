import random
import requests
import os

from pathlib import Path
from functions import send_post


if __name__ == '__main__':

    dir = 'pictures'
    Path(dir).mkdir(parents=True, exist_ok=True)

    try:
        last_comics_url = 'https://xkcd.com/info.0.json'
        response_last_comics = requests.get(last_comics_url)
        response_last_comics.raise_for_status()
        last_comics = response_last_comics.json()['num']

        random_comics = random.choice(range(1, last_comics))

        response_random_url = f'https://xkcd.com/{random_comics}/info.0.json'
        response_random_comics = requests.get(response_random_url)
        response_random_comics.raise_for_status()

        response_img = requests.get(response_random_comics.json()['img'])
        response_img.raise_for_status()

        filename = response_random_comics.json()['img'].split(sep='/')[-1]
        file_path = f'{dir}/{filename}'
        comment = response_random_comics.json()['alt']

        send_post(file_path, comment, response_img)

    finally:

        os.remove(file_path)
