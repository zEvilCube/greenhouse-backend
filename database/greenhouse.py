from typing import Tuple

from database import auth, get_session
from database.models import Greenhouse


def create() -> Tuple[int, str]:
    with get_session() as session:
        greenhouse = Greenhouse()
        session.add(greenhouse)
        session.commit()
        return greenhouse.id, auth.generate(greenhouse.id)
