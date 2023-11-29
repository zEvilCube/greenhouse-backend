from database import auth, get_session
from database.models import Greenhouse


def create() -> int:
    with get_session() as session:
        greenhouse = Greenhouse()
        session.add(greenhouse)
        session.commit()
        return auth.generate(greenhouse.id)
