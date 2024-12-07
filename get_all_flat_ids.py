import requests
import time
from utils import RegionId, get_flat_id_link, GetFlatIdParams, generate_random_header


def get_flat_ids(
        city: RegionId = RegionId.KYIV.value,
) -> list[int]:
    page = 0
    flat_ids = []
    while True:
        params = GetFlatIdParams(city_id=city, page=page)
        url = get_flat_id_link(params)
        response = requests.get(
            url=url,
            headers=generate_random_header()
        )
        if response.status_code != 200:
            break

        data = response.json()
        if not data:
            break

        try:
            flat_ids.extend(data['items'])
            page += 1
            time.sleep(2)
        except KeyError:
            break

    return flat_ids


if __name__ == '__main__':
    flat_ids = get_flat_ids()
    print(flat_ids)
