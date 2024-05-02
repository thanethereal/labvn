from sqlalchemy import create_engine, Column, String, Integer,  ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import ARRAY
class GettingHereInfo(Base):
    __tablename__ = 'GettingHereInfo'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)

class GettingHere(Base):
    __tablename__ = 'GettingHere'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    image_urls = Column(ARRAY(String))
    links = Column(ARRAY(String))
    description = Column(String)

engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeachvietnam')
Base.metadata.create_all(engine)
