from database import get_session
from database.models import References


def update(greenhouse_id: int, light: int, temperature: int, humidity: int) -> int:
    with get_session() as session:
        references = References(greenhouse_id=greenhouse_id, light=light, temperature=temperature, humidity=humidity)
        session.merge(references)
        session.commit()
        return references.greenhouse_id


def get(greenhouse_id: int) -> dict[str, int] | None:
    with get_session() as session:
        references = session.query(References).filter_by(greenhouse_id=greenhouse_id).first()
        if references is None:
            return None
        return dict(light=references.light, temperature=references.temperature, humidity=references.humidity)
