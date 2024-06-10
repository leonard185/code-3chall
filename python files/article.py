from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    author_id = Column(Integer, ForeignKey('authors.id'))
    magazine_id = Column(Integer, ForeignKey('magazines.id'))

    author = relationship("Author", back_populates="articles")
    magazine = relationship("Magazine", back_populates="articles")

    def get_author(self):
        return self.author

    def get_magazine(self):
        return self.magazine

class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    articles = relationship("Article", back_populates="author")

    def get_articles(self):
        return self.articles

    def get_magazines(self):
        return [article.magazine for article in self.articles]

class Magazine(Base):
    __tablename__ = 'magazines'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    articles = relationship("Article", back_populates="magazine")

    def get_articles(self):
        return self.articles

    def get_contributors(self):
        return [article.author for article in self.articles]
