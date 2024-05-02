from database.models.our_story import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeachvietnam')
Session = sessionmaker(bind=engine)
session = Session()

class OurStoryDAL:
    @staticmethod
    def get_our_story_by_id(id):
        try:
            return session.query(OurStory).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_our_stories():
        try:
            return session.query(OurStory).order_by(OurStory.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_our_story(text, image_url):
        try:
            new_OurStory = OurStory(text=text, image_url=image_url)
            session.add(new_OurStory)
            session.commit()
            return new_OurStory
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_our_story(item_id, text, image_url):
        try:
            item = OurStoryDAL.get_our_story_by_id(item_id)
            item.text = text
            item.image_url = image_url
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_our_story(id):
        try:
            item = OurStoryDAL.get_our_story_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
class TourismBenefitEveryoneDAL:
    @staticmethod
    def get_tourism_benefit_everyone_by_id(id):
        try:
            return session.query(TourismBenefitEveryone).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_tourism_benefit_everyones():
        try:
            return session.query(TourismBenefitEveryone).order_by(TourismBenefitEveryone.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_tourism_benefit_everyone(text, image_url):
        try:
            new_tourism = TourismBenefitEveryone(text=text, image_url=image_url)
            session.add(new_tourism)
            session.commit()
            return new_tourism
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_tourism_benefit_everyone(item_id, text, image_url):
        try:
            item = TourismBenefitEveryoneDAL.get_tourism_benefit_everyone_by_id(item_id)
            item.text = text
            item.image_url = image_url
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_tourism_benefit_everyone(id):
        try:
            item = TourismBenefitEveryoneDAL.get_tourism_benefit_everyone_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e