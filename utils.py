from enum import Enum
from urllib.parse import urlencode
from dataclasses import dataclass
from faker import Faker

BASE_FLAT_ID_URL = "https://dom.ria.com/node/searchEngine/v2/"


class RegionId(int, Enum):
    KYIV = 10


@dataclass
class GetFlatIdParams:
    category: int = 1
    realty_type: int = 2
    operation: int = 1
    state_id: int = 0
    city_id: "RegionId" = RegionId.KYIV.value
    in_radius: int = 0
    with_newbuilds: int = 0
    price_cur: int = 1
    wo_dupl: int = 1
    complex_inspected: int = 0
    sort: str = "inspected_sort"
    period: int = 0
    notFirstFloor: int = 0
    notLastFloor: int = 0
    with_map: int = 0
    photos_count_from: int = 0
    firstIteraction: str = "false"
    fromAmp: int = 0
    withoutResetPage: str = "false"
    withDeleteModal: str = "true"
    excludeSold: int = 0
    operation_type: int = 1
    limit: int = 1000
    page: int = 0


def get_flat_id_link(params: GetFlatIdParams) -> str:
    query_string = urlencode(params.__dict__)
    return f"{BASE_FLAT_ID_URL}?{query_string}"


def generate_random_header():
    fake = Faker()
    headers = {
        "User-Agent": fake.user_agent(),
        "Accept": fake.mime_type(),
        "Accept-Language": fake.language_code(),
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        # "Host": fake.hostname(),
        "Referer": fake.url(),
        "X-Forwarded-For": fake.ipv4(),
    }
    return headers
