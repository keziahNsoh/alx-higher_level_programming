#!/usr/bin/python3
"""
Module containing City class definition.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class that represents the cities table in the database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    
    # Define the relationship to State
    state = relationship("State", back_populates="cities")

    def __str__(self):
        """
        Return a string representation of the City object.
        """
        return f"({self.id}) {self.name}"

