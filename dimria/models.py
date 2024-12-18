from typing import Dict, Any

from db.models import Realty


class DimriaRealty:
    def __init__(self, **kwargs):
        self.realty_id = kwargs.get("realty_id")
        self.city_name_uk = kwargs.get("city_name_uk")
        self.floor = kwargs.get("floor")
        self.floors_count = kwargs.get("floors_count")
        self.realty_sale_type = kwargs.get("realty_sale_type")
        self.price = kwargs.get("price")
        self.street_name_uk = kwargs.get("street_name_uk")
        self.realty_type_parent_name_uk = kwargs.get("realty_type_parent_name_uk")
        self.beautiful_url = kwargs.get("beautiful_url")
        self.advert_type_name_uk = kwargs.get("advert_type_name_uk")
        self.district_name_uk = kwargs.get("district_name_uk")
        self.district_id = kwargs.get("district_id")
        self.is_commercial = kwargs.get("is_commercial")
        self.currency_type_uk = kwargs.get("currency_type_uk")
        self.city_id = kwargs.get("city_id")
        self.street_id = kwargs.get("street_id")
        self.district_type_id = kwargs.get("district_type_id")
        self.total_square_meters = kwargs.get("total_square_meters")
        self.realty_type_name_uk = kwargs.get("realty_type_name_uk")
        self.rooms_count = kwargs.get("rooms_count")
        self.is_developer = kwargs.get("is_developer")
        self.type = kwargs.get("type")

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DimriaRealty":
        return cls(
            realty_id=data.get("realty_id"),
            city_name_uk=data.get("city_name_uk"),
            floor=data.get("floor"),
            floors_count=data.get("floors_count"),
            realty_sale_type=data.get("realty_sale_type"),
            price=data.get("price"),
            street_name_uk=data.get("street_name_uk"),
            realty_type_parent_name_uk=data.get("realty_type_parent_name_uk"),
            beautiful_url=data.get("beautiful_url"),
            advert_type_name_uk=data.get("advert_type_name_uk"),
            district_name_uk=data.get("district_name_uk"),
            district_id=data.get("district_id"),
            is_commercial=bool(data.get("is_commercial")),
            currency_type_uk=data.get("currency_type_uk"),
            city_id=data.get("city_id"),
            street_id=data.get("street_id"),
            district_type_id=data.get("district_type_id"),
            total_square_meters=data.get("total_square_meters"),
            realty_type_name_uk=data.get("realty_type_name_uk"),
            rooms_count=data.get("rooms_count"),
            is_developer=bool(data.get("is_developer")),
            type=data.get("type"),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "realty_id": self.realty_id,
            "city_name_uk": self.city_name_uk,
            "floor": self.floor,
            "floors_count": self.floors_count,
            "realty_sale_type": self.realty_sale_type,
            "price": self.price,
            "street_name_uk": self.street_name_uk,
            "realty_type_parent_name_uk": self.realty_type_parent_name_uk,
            "beautiful_url": self.beautiful_url,
            "advert_type_name_uk": self.advert_type_name_uk,
            "district_name_uk": self.district_name_uk,
            "district_id": self.district_id,
            "is_commercial": self.is_commercial,
            "currency_type_uk": self.currency_type_uk,
            "city_id": self.city_id,
            "street_id": self.street_id,
            "district_type_id": self.district_type_id,
            "total_square_meters": self.total_square_meters,
            "realty_type_name_uk": self.realty_type_name_uk,
            "rooms_count": self.rooms_count,
            "is_developer": self.is_developer,
            "type": self.type,
        }

    def to_db_model(self) -> Realty:
        return Realty(
            realty_id=self.realty_id,
            city_name_uk=self.city_name_uk,
            floor=self.floor,
            floors_count=self.floors_count,
            realty_sale_type=self.realty_sale_type,
            price=self.price,
            street_name_uk=self.street_name_uk,
            realty_type_parent_name_uk=self.realty_type_parent_name_uk,
            beautiful_url=self.beautiful_url,
            advert_type_name_uk=self.advert_type_name_uk,
            district_name_uk=self.district_name_uk,
            district_id=self.district_id,
            is_commercial=self.is_commercial,
            currency_type_uk=self.currency_type_uk,
            city_id=self.city_id,
            street_id=self.street_id,
            district_type_id=self.district_type_id,
            total_square_meters=self.total_square_meters,
            realty_type_name_uk=self.realty_type_name_uk,
            rooms_count=self.rooms_count,
            is_developer=self.is_developer,
            type=self.type,
        )
