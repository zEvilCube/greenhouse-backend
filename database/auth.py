from secrets import token_urlsafe

from database import get_session
from database.models import Auth, Greenhouse


def generate(greenhouse: Greenhouse) -> Auth:
    auth = Auth(greenhouse_id=greenhouse.id, api_key=token_urlsafe())
    with get_session() as session:
        session.merge(auth)
        session.commit()
    return auth


def get(api_key: str) -> Greenhouse | None:
    with get_session() as session:
        auth = session.query(Auth).filter_by(api_key=api_key).first()
        if auth is None:
            return None
        return auth.greenhouse


def validate(api_key: str) -> bool:
    return get(api_key) is not None
