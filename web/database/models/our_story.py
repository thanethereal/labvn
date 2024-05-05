from sqlalchemy import create_engine, Column, String, Integer,  ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class OurStory(Base):
    __tablename__ = 'OurStory'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    image_url = Column(String)

class TourismBenefitEveryone(Base):
    __tablename__ = 'TourismBenefitEveryone'
    id = Column(Integer, primary_key=True)
    text = Column(String)
    image_url = Column(String)

# Tạo engine để kết nối đến cơ sở dữ liệu PostgreSQL
engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeach')

# Tạo bảng trong cơ sở dữ liệu
Base.metadata.create_all(engine)