from sqlalchemy import create_engine, Column, String, Integer,  ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy import ARRAY
class HeaderImage(Base):
    __tablename__ = 'HeaderImage'

    id = Column(Integer, primary_key=True)
    page_name = Column(String)
    image_urls = Column(ARRAY(String))

engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeach')
Base.metadata.create_all(engine)
