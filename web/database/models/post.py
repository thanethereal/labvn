from sqlalchemy import create_engine, Column, String, Integer,  ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
import datetime
from .user import User

class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    content = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), nullable=False)  # Use User instead of 'User'
    created_at = Column(DateTime, nullable=False, default=datetime.datetime.now())
    image_url = Column(String, nullable=False)

# Tạo engine để kết nối đến cơ sở dữ liệu PostgreSQL
engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeachvietnam')

# Tạo bảng trong cơ sở dữ liệu
Base.metadata.create_all(engine)
