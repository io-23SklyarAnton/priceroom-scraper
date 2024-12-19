from db.models import Realty
from dimria.models import DimriaRealty
from get_flat_info import get_flat_info
from get_all_flat_ids import get_flat_ids
from utils import BATCH_SIZE
import time
from db.utils import get_db
from db.crud.realty import save_realty
from notifications import Notification

notification = Notification()


def main():
    notification.telegram('SCRAP RUN STARTED')
    flat_ids = get_flat_ids()
    notification.telegram(f'Got {len(flat_ids)} flat ids')
    for i in range(0, len(flat_ids), BATCH_SIZE):
        session = get_db()
        try:
            batch = flat_ids[i:i + BATCH_SIZE]
            for flat_id in batch:
                flat_info = get_flat_info(flat_id)
                dimria_realty: DimriaRealty = DimriaRealty.from_dict(flat_info)
                dimria_db_model: Realty = dimria_realty.to_db_model()
                save_realty(
                    realty=dimria_db_model,
                    session=session
                )
                notification.telegram(f'Flat with id {flat_id} saved')
                time.sleep(2)
            session.commit()

        except Exception as e:
            notification.telegram(f'Error while saving flat with id {flat_id}')
            print(e)
            session.rollback()
        finally:
            notification.telegram(f'Saved {len(batch)} flats')
            session.close()


if __name__ == '__main__':
    main()
