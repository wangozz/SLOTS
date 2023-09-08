from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    player_id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    balance = Column(Float, default=100.0)

    spins = relationship('Spin', back_populates='player')

class Spin(Base):
    __tablename__ = 'spin_records'

    spin_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)
    result = Column(String, nullable=False)
    bet_amount = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    player = relationship('Player', back_populates='spins')

class History(Base):
    __tablename__ = 'history'

    history_id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)
    username = Column(String, nullable=False)
    spins = Column(Integer, nullable=False)
    balance = Column(Float, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    player = relationship('Player')

engine = create_engine('sqlite:///slots_game.db')
Base.metadata.create_all(engine)
