from sqlalchemy import Boolean, Column, Engine, ForeignKey, Integer, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Greenhouse(Base):
    __tablename__ = "greenhouse"

    id = Column(Integer, primary_key=True, autoincrement=True)

    auth = relationship(lambda: Auth, back_populates=__tablename__)
    readings = relationship(lambda: Readings, back_populates=__tablename__)
    statuses = relationship(lambda: Statuses, back_populates=__tablename__)
    references = relationship(lambda: References, back_populates=__tablename__)


class Auth(Base):
    __tablename__ = "auth"

    greenhouse = relationship(Greenhouse, back_populates=__tablename__)
    greenhouse_id = Column(Integer, ForeignKey(f"{Greenhouse.__tablename__}.id"), primary_key=True)

    api_key = Column(Text, nullable=False, unique=True)


class Readings(Base):
    __tablename__ = "readings"

    greenhouse = relationship(Greenhouse, back_populates=__tablename__)
    greenhouse_id = Column(Integer, ForeignKey(f"{Greenhouse.__tablename__}.id"), primary_key=True)

    light = Column(Integer, nullable=True)
    temperature = Column(Integer, nullable=True)
    humidity = Column(Integer, nullable=True)


class Statuses(Base):
    __tablename__ = "statuses"

    greenhouse = relationship(Greenhouse, back_populates=__tablename__)
    greenhouse_id = Column(Integer, ForeignKey(f"{Greenhouse.__tablename__}.id"), primary_key=True)

    lighting = Column(Boolean, nullable=True)
    heating = Column(Boolean, nullable=True)
    cooling = Column(Boolean, nullable=True)
    watering = Column(Boolean, nullable=True)


class References(Base):
    __tablename__ = "references"

    greenhouse = relationship(Greenhouse, back_populates=__tablename__)
    greenhouse_id = Column(Integer, ForeignKey(f"{Greenhouse.__tablename__}.id"), primary_key=True)

    light = Column(Integer, nullable=True)
    temperature = Column(Integer, nullable=True)
    humidity = Column(Integer, nullable=True)


def init(engine: Engine):
    Base.metadata.create_all(bind=engine)
