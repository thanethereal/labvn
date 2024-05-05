from database.models.footer import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeach')
Session = sessionmaker(bind=engine)
session = Session()

class FooterDAL:
    @staticmethod
    def get_footer_by_id(id):
        try:
            return session.query(FooterInfo).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_footers():
        try:
            return session.query(FooterInfo).order_by(FooterInfo.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_footer(phone, email, address, link_facebook, link_instagram, link_tiktok):
        try:
            new_footer = FooterInfo(phone=phone, email=email, address=address, link_facebook=link_facebook, link_instagram=link_instagram, link_tiktok=link_tiktok)
            session.add(new_footer)
            session.commit()
            return new_footer
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_footer(item_id, phone, email, address, link_facebook, link_instagram, link_tiktok):
        try:
            item = FooterDAL.get_footer_by_id(item_id)
            item.phone = phone
            item.email = email
            item.address = address
            item.link_facebook = link_facebook
            item.link_instagram = link_instagram
            item.link_tiktok = link_tiktok
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_footer(id):
        try:
            item = FooterDAL.get_footer_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e