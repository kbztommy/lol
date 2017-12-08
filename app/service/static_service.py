from ..riot_api.static_api import get_all_item_code
from ..models import ItemCode
from ..extensions import db
def update_item_code():
    item_data = get_all_item_code()
    item_map = item_data.get('data')

    try:
        for _, item in item_map.items():
            db.session.merge(ItemCode(**item))
        db.session.commit()
    except:
        db.session.rollback()
        raise
