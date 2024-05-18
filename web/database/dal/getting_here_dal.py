from database.models.getting_here import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeach')
Session = sessionmaker(bind=engine)
session = Session()
class GettingHereDAL:
    @staticmethod
    def get_getting_here_info_by_id(id):
        try:
            return session.query(GettingHereInfo).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_getting_here_infos():
        try:
            return session.query(GettingHereInfo).order_by(GettingHereInfo.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_getting_here_info(title, description):
        try:
            new_getting_here = GettingHereInfo(title=title, description=description)
            session.add(new_getting_here)
            session.commit()
            return new_getting_here
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_getting_here_info(item_id, title, description):
        try:
            item = GettingHereDAL.get_getting_here_info_by_id(item_id)
            item.title = title
            item.description = description
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_getting_here_info(id):
        try:
            item = GettingHereDAL.get_getting_here_info_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_getting_here_by_id(id):
        try:
            return session.query(GettingHere).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_getting_heres():
        try:
            return session.query(GettingHere).order_by(GettingHere.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_getting_here(name, image_urls, links, description):
        try:
            getting_here = GettingHere(name=name,image_urls=image_urls, links=links, description=description)
            session.add(getting_here)
            session.commit()
            return getting_here
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_getting_here(item_id, name, image_urls, links, description):
        try:
            item = GettingHereDAL.get_getting_here_by_id(item_id)
            item.name = name
            if (len(image_urls)) != 0:
                item.image_urls = image_urls
            item.links = links
            item.description = description
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_getting_here(id):
        try:
            item = GettingHereDAL.get_getting_here_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e