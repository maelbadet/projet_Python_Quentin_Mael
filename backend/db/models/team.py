from sqlalchemy import Column, Integer, String, Date
from .base import Base  # Import de la base commune
import datetime


class Team(Base):
	__tablename__ = "teams"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(255), nullable=False)
	founded = Column(Integer, nullable=True)
	img_path = Column(String(255), nullable=True)
	API_id = Column(Integer, nullable=True)
	country_id = Column(Integer, nullable=True)
	league_id = Column(Integer, nullable=True)
	created_at = Column(Date, default=datetime.date.today)
	updated_at = Column(Date, default=datetime.date.today)
	deleted_at = Column(Date, default=None)
