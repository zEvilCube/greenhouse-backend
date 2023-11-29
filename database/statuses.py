from database import get_session
from database.models import Greenhouse, Statuses


def update(greenhouse: Greenhouse, lighting: bool, heating: bool, cooling: bool, watering: bool) -> Statuses:
    statuses = Statuses(
        greenhouse_id=greenhouse.id, lighting=lighting, heating=heating, cooling=cooling, watering=watering
    )
    with get_session() as session:
        session.merge(statuses)
        session.commit()
    return statuses


def get(greenhouse: Greenhouse) -> dict[str, int] | None:
    with get_session() as session:
        statuses = session.query(Statuses).filter_by(greenhouse=greenhouse).first()
        if statuses is None:
            return None
        return dict(
            lighting=statuses.lighting, heating=statuses.heating, cooling=statuses.cooling, watering=statuses.watering
        )
