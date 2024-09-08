from sqlalchemy import Column, Date, Integer, String, Text
from database.database import Base


class Comments(Base):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(255), nullable=False)
    author_image_url = Column(String, nullable=True)
    content = Column(Text, nullable=False)
    date = Column(Date, nullable=False)
    sentiment = Column(String, nullable=True, default=None)
