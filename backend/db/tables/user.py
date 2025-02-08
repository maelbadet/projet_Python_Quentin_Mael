
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from .base import Base  # Import de la base commune
import datetime


class User(Base):
	__tablename__ = "users"  # Table en snake_case

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(60), nullable=False)
	surname = Column(String(60), nullable=False)
	email = Column(String(255), nullable=False, unique=True)
	telephone = Column(String(20), nullable=True)
	password = Column(String(255), nullable=False)
	created_at = Column(Date, default=datetime.date.today)
	updated_at = Column(Date, default=datetime.date.today, onupdate=datetime.date.today)
	deleted_at = Column(Date, nullable=True)

	# Relation avec FavoriteTeam
	favorite_teams = relationship("FavoriteTeam", back_populates="user", cascade="all, delete-orphan")
