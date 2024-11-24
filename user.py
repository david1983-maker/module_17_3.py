from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean,Float
from sqlalchemy.orm import relationship
from app.models import __init__


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(Integer)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    task = relationship('Task', back_populates='user')

from sqlalchemy.schema import CreateTable
print(CreateTable(User.__table__))



