from secrets import token_urlsafe

from database import get_session
from database.models import Auth


def generate(greenhouse_id: int) -> str:
    with get_session() as session:
        api_key = token_urlsafe()
        auth = Auth(greenhouse_id=greenhouse_id, api_key=api_key)
        session.merge(auth)
        session.commit()
        return api_key


def get(api_key: str) -> int | None:
    with get_session() as session:
        auth = session.query(Auth).filter_by(api_key=api_key).first()
        if auth is None:
            return None
        return auth.greenhouse_id


def validate(api_key: str) -> bool:
    return get(api_key) is not None
