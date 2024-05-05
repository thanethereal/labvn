from sqlalchemy import create_engine, Column, String, Integer,  ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class FooterInfo(Base):
    __tablename__ = 'FooterInfo'

    id = Column(Integer, primary_key=True)
    phone = Column(String)
    email = Column(String)
    address = Column(String)
    link_facebook = Column(String(255))
    link_instagram = Column(String(255))
    link_tiktok = Column(String(255))

engine = create_engine('postgresql://lifesabeach:lifesabeach@db:5432/lifesabeach')
Base.metadata.create_all(engine)
