import requests

from utils import generate_random_header


def get_flat_info(flat_id: int) -> dict:
    url = f'https://dom.ria.com/realty/data/{flat_id}?lang_id=4'
    response = requests.get(url=url, headers=generate_random_header())
    if response.status_code != 200:
        return {}
    return response.json()
