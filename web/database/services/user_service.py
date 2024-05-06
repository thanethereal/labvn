# In user_service.py

from database.models.user import User
from database.dal.user_dal import UserDAL, UserProfileDAL
class UserService:
    @staticmethod
    def create_user(name, email, password):
        return UserDAL.create_user(name, email, password)

    @staticmethod
    def get_user_by_email(email):
        return UserDAL.get_user_by_email(email)
    
    @staticmethod
    def get_user_by_id(user_id):
        return UserDAL.get_user_by_email(user_id)
    
    @staticmethod
    def get_all_users():
        return UserDAL.get_all_users()

    @staticmethod
    def delete_user(user_id):
       return UserDAL.delete_user(user_id)
    
    @staticmethod
    def login(email, password):
       return UserDAL.login(email, password)

class UserProfileService:
    @staticmethod
    def create_profile(user_id, avatar=None, bio=None, role=None, link_facebook=None, link_instagram=None, link_zalo=None):
        return UserProfileDAL.create_profile(user_id, avatar, bio, role, link_facebook, link_instagram, link_zalo)
    
    @staticmethod
    def get_profile_by_user_id(user_id):
        return UserProfileDAL.get_profile_by_user_id(user_id)
    
    @staticmethod
    def update_profile(user_id, avatar=None, bio=None, role=None, link_facebook=None, link_instagram=None, link_zalo=None):
        return UserProfileDAL.update_profile(user_id, avatar, bio, role, link_facebook, link_instagram, link_zalo)
    
    @staticmethod
    def delete_profile(user_id):
        return UserProfileDAL.delete_profile(user_id)
    
    @staticmethod
    def get_all_profiles():
        return UserProfileDAL.get_all_profiles()

    @staticmethod
    def merge_user_user_profile():
        return UserProfileDAL.merge_user_user_profile()
    
    @staticmethod
    def join_user_profile():
        return UserProfileDAL.join_user_profile()