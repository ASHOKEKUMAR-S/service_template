from sqlalchemy import Column, Integer, String
from .db import Base

class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)
    application = Column(String(32))
