from sqlalchemy import create_engine, Column, String, Integer,  ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import ARRAY
class Activities(Base):
    __tablename__ = 'Activities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    image_urls = Column(ARRAY(String))

engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeachvietnam')
Base.metadata.create_all(engine)