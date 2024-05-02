from database.models.post import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeach')
Session = sessionmaker(bind=engine)
session = Session()

class PostDAL:
    @staticmethod
    def create_post(title, content, image_url, user_id):
        try:
            post = Post(title=title, content=content, image_url=image_url, user_id=user_id)
            session.add(post)
            session.commit()
            return post
        except SQLAlchemyError as e:
            session.rollback()
            raise e
    
    @staticmethod
    def get_post_by_id(post_id):
        try:
            return session.query(Post).filter_by(id=post_id).first()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_all_posts():
        try:
            return session.query(Post).order_by(Post.created_at).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
    
    @staticmethod
    def update_post(post_id, title, content, image_url, user_id):
        try:
            post = PostDAL.get_post_by_id(post_id)
            post.title = title
            post.content = content
            post.image_url = image_url
            post.user_id = user_id
            session.commit()
            return post
        except SQLAlchemyError as e:
            session.rollback()
            raise e
    
    @staticmethod
    def delete_post(post_id):
        try:
            post = PostDAL.get_post_by_id(post_id)
            if post:
                session.delete(post)
                session.commit()
                return True
            else:
                return False
        except SQLAlchemyError as e:
            session.rollback()
            raise e
