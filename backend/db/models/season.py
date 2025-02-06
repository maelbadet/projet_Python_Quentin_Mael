from sqlalchemy import Column, Integer, String, Date
from .base import Base  # Import de la base commune


class Season(Base):
	__tablename__ = "seasons"

	id = Column(Integer, primary_key=True, index=True)
	API_id_season = Column(Integer, nullable=False)
	date_season = Column(Date, nullable=True)
	name = Column(String(255), nullable=True)
