import requests
from my_consts import MY_CATS_API_KEY


def get_thecats(breed_id,api_key):
    url = f'https://api.thecatapi.com/v1/images/search?limit=1&breed_ids={breed_id}&api_key={api_key}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
