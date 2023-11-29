from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import Session

from database import models

engine: Engine = create_engine("sqlite:///database/.db")


def init():
    models.init(engine)


def get_session() -> Session:
    return Session(bind=engine)
