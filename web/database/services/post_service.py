from database.dal.post_dal import PostDAL
class PostService:
    @staticmethod
    def create_post(title, content, image_url, user_id):
        return PostDAL.create_post(title, content, image_url, user_id)
    
    @staticmethod
    def get_post_by_id(post_id):
        return PostDAL.get_post_by_id(post_id)
    
    @staticmethod
    def get_all_posts():
        return PostDAL.get_all_posts()
    
    @staticmethod
    def update_post(post_id, title=None, content=None, image_url=None, user_id=1):
        return PostDAL.update_post(post_id, title, content, image_url, user_id)
    
    @staticmethod
    def delete_post(post_id):
        return PostDAL.delete_post(post_id)
