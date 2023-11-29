from database import get_session
from database.models import Greenhouse, Readings


def update(greenhouse: Greenhouse, light: int, temperature: int, humidity: int) -> Readings:
    readings = Readings(greenhouse_id=greenhouse.id, light=light, temperature=temperature, humidity=humidity)
    with get_session() as session:
        session.merge(readings)
        session.commit()
    return readings


def get(greenhouse: Greenhouse) -> dict[str, int] | None:
    with get_session() as session:
        readings = session.query(Readings).filter_by(greenhouse=greenhouse).first()
        if readings is None:
            return None
        return dict(light=readings.light, temperature=readings.temperature, humidity=readings.humidity)
