from sqlalchemy import func

class Magazine(Base):
    __tablename__ = 'magazines'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    articles = relationship("Article", back_populates="magazine")

    def article_titles(self):
        if not self.articles:
            return None
        return [article.title for article in self.articles]

    def contributing_authors(self):
        if not self.articles:
            return []
        authors_count = {}
        for article in self.articles:
            if article.author in authors_count:
                authors_count[article.author] += 1
            else:
                authors_count[article.author] = 1
        return [author for author, count in authors_count.items() if isinstance(author, Author) and count > 2]
