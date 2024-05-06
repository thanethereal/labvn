from database.models.user import *
import bcrypt
from bcrypt import hashpw, gensalt
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, relationship, contains_eager, aliased
from sqlalchemy import select
engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeach')
Session = sessionmaker(bind=engine)
session = Session()

class UserDAL:
    def create_user(name, email, password):
        try:
            hashed_password = UserDAL.hash_password(password)
            user = User(name=name, email=email, password=hashed_password)
            session.add(user)
            session.commit()
            return user
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    
    @staticmethod
    def get_user_by_email(email):
        try:
            return session.query(User).filter_by(email=email).first()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_user_by_id(user_id):
        try:
            return session.query(User).filter_by(id=user_id).first()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_all_users():
        try:
            return session.query(User).order_by(User.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
    
    @staticmethod
    def login(email, password):
        try:
            user = UserDAL.get_user_by_email(email)
            if user:
                if UserDAL.verify_password(user.password, password):
                    return user
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def hash_password(password):
        # Generate a salt and hash the password with it
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password.decode('utf-8')
    
    @staticmethod
    def verify_password(hashed_password, user_password):
        return bcrypt.checkpw(user_password.encode('utf-8'), hashed_password.encode('utf-8'))

class UserProfileDAL:
    @staticmethod
    def create_profile(user_id, avatar=None, bio=None, role=None, link_facebook=None, link_instagram=None, link_zalo=None):
        try:
            profile = UserProfile(
                user_id=user_id,
                avatar=avatar,
                bio=bio,
                role=role,
                link_facebook=link_facebook,
                link_instagram=link_instagram,
                link_zalo=link_zalo
            )
            session.add(profile)
            session.commit()
            return profile
        except SQLAlchemyError as e:
            session.rollback()
            raise e
    
    @staticmethod
    def get_profile_by_user_id(user_id):
        try:
            return session.query(UserProfile).filter_by(id=user_id).first()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_all_profiles():
        try:
            return session.query(UserProfile).order_by(UserProfile.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
    
    @staticmethod
    def update_profile(user_id, avatar=None, bio=None, role=None, link_facebook=None, link_instagram=None, link_zalo=None):
        try:
            profile = UserProfileDAL.get_profile_by_user_id(user_id)
            if profile:
                if avatar:
                    profile.avatar = avatar
                if bio:
                    profile.bio = bio
                if role:
                    profile.role = role
                if link_facebook:
                    profile.link_facebook = link_facebook
                if link_instagram:
                    profile.link_instagram = link_instagram
                if link_zalo:
                    profile.link_zalo = link_zalo
                session.commit()
                return profile
            else:
                profile = UserProfileDAL.create_profile(user_id=user_id, avatar=avatar, bio=bio, role=role, link_facebook=link_instagram, link_instagram=link_instagram, link_zalo=link_zalo)
        except SQLAlchemyError as e:
            session.rollback()
            raise e
    
    @staticmethod
    def delete_profile(user_id):
        try:
            profile = UserProfileDAL.get_profile_by_user_id(user_id)
            if profile:
                session.delete(profile)
                session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def merge_user_user_profile():
        return session.query(User, UserProfile).filter(User.id == UserProfile.user_id)
    
    @staticmethod
    def join_user_profile():
        user_alias = aliased(User)
        stmt = select(User, UserProfile).outerjoin(user_alias, User.id == UserProfile.user_id)

        # Thực thi truy vấn và lấy kết quả
        return session.execute(stmt).all()