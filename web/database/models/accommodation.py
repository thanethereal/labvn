from sqlalchemy import create_engine, Column, String, Integer,  ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import ARRAY
class AccommodationInfo(Base):
    __tablename__ = 'AccommodationInfo'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

class RoomType(Base):
    __tablename__ = 'RoomType'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    image_urls = Column(ARRAY(String))

engine = create_engine('postgresql://lifesabeach:lifesabeach@db:5432/lifesabeach')
Base.metadata.create_all(engine)
