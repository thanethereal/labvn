from database.models.header_image import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://lifesabeach:lifesabeach@db:5432/lifesabeach')
Session = sessionmaker(bind=engine)
session = Session()
class HeaderImageDAL:
    @staticmethod
    def get_header_image_by_id(id):
        try:
            return session.query(HeaderImage).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e
        
    def get_header_image_by_name(page_name):
        try:
            return session.query(HeaderImage).filter_by(page_name=page_name).first()
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_header_images():
        try:
            return session.query(HeaderImage).order_by(HeaderImage.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_header_image(page_name, image_urls):
        try:
            getting_here = HeaderImage(page_name=page_name,image_urls=image_urls)
            session.add(getting_here)
            session.commit()
            return getting_here
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_header_image(item_id, page_name, image_urls):
        try:
            item = HeaderImageDAL.get_header_image_by_id(item_id)
            item.page_name = page_name
            item.image_urls = image_urls
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_header_image(id):
        try:
            item = HeaderImageDAL.get_header_image_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e