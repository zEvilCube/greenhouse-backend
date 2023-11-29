from database import get_session
from database.models import Greenhouse, References


def update(greenhouse: Greenhouse, light: int, temperature: int, humidity: int) -> References:
    references = References(greenhouse_id=greenhouse.id, light=light, temperature=temperature, humidity=humidity)
    with get_session() as session:
        session.merge(references)
        session.commit()
    return references


def get(greenhouse: Greenhouse) -> dict[str, int] | None:
    with get_session() as session:
        references = session.query(References).filter_by(greenhouse=greenhouse).first()
        if references is None:
            return None
        return dict(light=references.light, temperature=references.temperature, humidity=references.humidity)
