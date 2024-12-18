from sqlalchemy.orm import Session

from db.models import Realty
from db.utils import write_session


@write_session
def save_realty(
        session: Session,
        realty: Realty,
) -> Realty:
    session.add(realty)
    return realty
