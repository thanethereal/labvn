from sqlalchemy import create_engine, Column, String, Integer,  ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Description(Base):
    __tablename__ = 'Description'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    image_url = Column(String)

class MainSection(Base):
    __tablename__ = 'MainSection'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    image_url = Column(String(255))
    link = Column(String(255))

engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeach')
Base.metadata.create_all(engine)
