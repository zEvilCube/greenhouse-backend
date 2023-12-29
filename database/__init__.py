from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from config import config
from database import models

engine: Engine = create_engine(config.db_url.get_secret_value())


def init():
    models.init(engine)


def get_session() -> Session:
    return Session(bind=engine)
