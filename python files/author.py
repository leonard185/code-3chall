from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Magazine(Base):
    __tablename__ = 'magazines'

    id = Column(Integer, primary_key=True)
    name = Column(String(16))
    category = Column(String)

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __repr__(self):
        return f"<Magazine(name='{self.name}', category='{self.category}')>"
