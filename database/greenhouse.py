from database import auth, get_session
from database.models import Greenhouse


def create() -> Greenhouse:
    greenhouse = Greenhouse()
    with get_session() as session:
        session.add(greenhouse)
        session.commit()
    auth.generate(greenhouse)
    return greenhouse
