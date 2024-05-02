from database.models.accommodation import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeachvietnam')
Session = sessionmaker(bind=engine)
session = Session()
class AccommodationDAL:
    @staticmethod
    def get_accommodation_info_by_id(id):
        try:
            return session.query(AccommodationInfo).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_accommodation_infos():
        try:
            return session.query(AccommodationInfo).order_by(AccommodationInfo.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_accommodation_info(title, description):
        try:
            new_accommodation = AccommodationInfo(title=title, description=description)
            session.add(new_accommodation)
            session.commit()
            return new_accommodation
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_accommodation_info(item_id, title, description):
        try:
            item = AccommodationDAL.get_accommodation_info_by_id(item_id)
            item.title = title
            item.description = description
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_accommodation_info(id):
        try:
            item = AccommodationDAL.get_accommodation_info_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_room_type_by_id(id):
        try:
            return session.query(RoomType).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_room_types():
        try:
            return session.query(RoomType).order_by(RoomType.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_room_type(name, description, image_urls):
        try:
            new_room = RoomType(name=name, description=description, image_urls=image_urls)
            session.add(new_room)
            session.commit()
            return new_room
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_room_type(item_id, name, description, image_urls):
        try:
            item = AccommodationDAL.get_room_type_by_id(item_id)
            item.name = name
            item.description = description
            item.image_urls = image_urls
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_room_type(id):
        try:
            item = AccommodationDAL.get_room_type_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e