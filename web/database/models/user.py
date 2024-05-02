from sqlalchemy import create_engine, Column, String, Integer,  ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, contains_eager
Base = declarative_base()
import datetime

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    password = Column(String, nullable=False)
    profile = relationship("UserProfile", uselist=False, back_populates="user")

class UserProfile(Base):
    __tablename__ = 'UserProfile'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)
    avatar = Column(String(255))
    bio = Column(String(255))
    role = Column(String(50))
    link_facebook = Column(String(255))
    link_instagram = Column(String(255))
    link_zalo = Column(String(255))
    user = relationship("User", back_populates="profile")
    # More profile fields can be added as needed

# Tạo engine để kết nối đến cơ sở dữ liệu PostgreSQL
engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeach')

# Tạo bảng trong cơ sở dữ liệu
Base.metadata.create_all(engine)
