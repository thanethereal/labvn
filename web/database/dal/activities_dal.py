from database.models.activities import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeachvietnam')
Session = sessionmaker(bind=engine)
session = Session()
class ActivitiesDAL:
    @staticmethod
    def get_activity_by_id(id):
        try:
            return session.query(Activities).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_activities():
        try:
            return session.query(Activities).order_by(Activities.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_activity(name, description, image_urls):
        try:
            new_room = Activities(name=name, description=description, image_urls=image_urls)
            session.add(new_room)
            session.commit()
            return new_room
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_activity(item_id, name, description, image_urls):
        try:
            item = ActivitiesDAL.get_activity_by_id(item_id)
            item.name = name
            item.description = description
            item.image_urls = image_urls
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_activity(id):
        try:
            item = ActivitiesDAL.get_activity_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e