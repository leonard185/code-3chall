from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Magazine(Base):
    __tablename__ = 'magazines'

    id = Column(Integer, primary_key=True)
    _name = Column(String(16))
    _category = Column(String)

    def __init__(self, name, category):
        self.name = name
        self.category = category

    def get_id(self):
        return self.id

    def set_id(self, id):
        if isinstance(id, int):
            self.id = id
        else:
            raise ValueError("ID must be of type int")

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name
        else:
            raise ValueError("Name must be a string between 2 and 16 characters long")

    def get_category(self):
        return self._category

    def set_category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category
        else:
            raise ValueError("Category must be a non-empty string")

    id = property(get_id, set_id)
    name = property(get_name, set_name)
    category = property(get_category, set_category)
