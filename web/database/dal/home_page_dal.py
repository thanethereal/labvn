from database.models.home_page import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeachvietnam')
Session = sessionmaker(bind=engine)
session = Session()

class HomePageDAL:
    @staticmethod
    def get_description_by_id(id):
        try:
            return session.query(Description).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_descriptions():
        try:
            return session.query(Description).order_by(Description.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_description(text, image_url):
        try:
            new_description = Description(text=text, image_url=image_url)
            session.add(new_description)
            session.commit()
            return new_description
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_description(item_id, text, image_url):
        try:
            item = HomePageDAL.get_description_by_id(item_id)
            item.text = text
            item.image_url = image_url
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_description(id):
        try:
            item = HomePageDAL.get_description_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def get_section_by_id(section_id):
        try:
            return session.query(MainSection).filter_by(id=section_id).first()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def get_all_sections():
        try:
            return session.query(MainSection).order_by(MainSection.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def create_section(title, image_url, link):
        try:
            section = MainSection(title=title, image_url=image_url, link=link)
            session.add(section)
            session.commit()
            return section
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_section(section_id):
        try:
            section = HomePageDAL.get_section_by_id(section_id)
            if section:
                session.delete(section)
                session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_section(item_id, title, image_url, link):
        try:
            item = HomePageDAL.get_section_by_id(item_id)
            item.tile = title
            item.image_url = image_url
            item.link = link
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e