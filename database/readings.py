from database import get_session
from database.models import Readings


def update(greenhouse_id: int, light: int, temperature: int, humidity: int) -> int:
    with get_session() as session:
        readings = Readings(greenhouse_id=greenhouse_id, light=light, temperature=temperature, humidity=humidity)
        session.merge(readings)
        session.commit()
        return readings.greenhouse_id


def get(greenhouse_id: int) -> dict[str, int] | None:
    with get_session() as session:
        readings = session.query(Readings).filter_by(greenhouse_id=greenhouse_id).first()
        if readings is None:
            return None
        return dict(light=readings.light, temperature=readings.temperature, humidity=readings.humidity)
