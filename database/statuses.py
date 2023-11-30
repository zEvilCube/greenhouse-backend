from database import get_session
from database.models import Statuses


def update(greenhouse_id: int, lighting: bool, heating: bool, cooling: bool, watering: bool) -> int:
    with get_session() as session:
        statuses = Statuses(
            greenhouse_id=greenhouse_id, lighting=lighting, heating=heating, cooling=cooling, watering=watering
        )
        session.merge(statuses)
        session.commit()
        return statuses.greenhouse_id


def get(greenhouse_id: int) -> dict[str, int] | None:
    with get_session() as session:
        statuses = session.query(Statuses).filter_by(greenhouse_id=greenhouse_id).first()
        if statuses is None:
            return None
        return dict(
            lighting=statuses.lighting, heating=statuses.heating, cooling=statuses.cooling, watering=statuses.watering
        )
