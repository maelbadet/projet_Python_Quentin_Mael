from sqlalchemy import Column, Integer, String, Date
from .base import Base


class League(Base):
	__tablename__ = "league"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(255), nullable=False)
	api_id = Column(Integer, nullable=False)
	country_id = Column(Integer, nullable=False)
	image_path = Column(String(255), nullable=True)

