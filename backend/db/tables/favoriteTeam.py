from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .base import Base
import datetime


class FavoriteTeam(Base):
	__tablename__ = "favorite_team"  # Convention snake_case pour le nom des tables

	# Colonnes du modèle
	id = Column(Integer, primary_key=True, index=True)
	user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
	team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)

	created_at = Column(DateTime, default=datetime.date.today)
	updated_at = Column(DateTime, default=datetime.date.today, onupdate=datetime.date.today)
	deleted_at = Column(DateTime, default=None, nullable=True)

	# Relations
	user = relationship("User", back_populates="favorite_teams")
	team = relationship("Team", back_populates="favorite_teams")
