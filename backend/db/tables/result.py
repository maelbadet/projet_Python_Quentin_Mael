from sqlalchemy import Column, Integer, String, Date
from .base import Base  # Import de la base commune


class Result(Base):
	__tablename__ = "results"

	id = Column(Integer, primary_key=True, index=True)
	season_id = Column(Integer, nullable=False)
	name = Column(String(255), nullable=False)
	starting_at = Column(Date, nullable=False)
	result_info = Column(String(255), nullable=True)
	goal_conceded = Column(Integer, nullable=True)
	goal_set = Column(Integer, nullable=True)
