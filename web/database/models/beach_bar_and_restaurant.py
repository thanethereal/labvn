from sqlalchemy import create_engine, Column, String, Integer,  ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class RestaurantInfo(Base):
    __tablename__ = 'RestaurantInfo'

    id = Column(Integer, primary_key=True)
    restaurant_name = Column(String(100))
    beach_bar_hours = Column(String(50))
    restaurant_hours = Column(String(50))
    happy_hour_hours = Column(String(50))
    description = Column(String)

class Food(Base):
    __tablename__ = 'Foods'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    image_url = Column(String)

class Drink(Base):
    __tablename__ = 'Drinks'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    image_url = Column(String)

class RestaurantBarImageColection(Base):
    __tablename__ = 'RestaurantBarImageColection'

    id = Column(Integer, primary_key=True)
    image_url = Column(String)
    overlay_content = Column(String)

class RestaurantBarMenu(Base):
    __tablename__ = 'RestaurantBarMenu'

    id = Column(Integer, primary_key=True)
    image_url = Column(String)

engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeach')
Base.metadata.create_all(engine)
