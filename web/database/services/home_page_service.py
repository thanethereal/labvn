# In home_page_service.py

from database.dal.home_page_dal import HomePageDAL

class HomePageService:
    @staticmethod
    def get_description_by_id(id):
        return HomePageDAL.get_description_by_id(id)

    @staticmethod
    def get_all_descriptions():
        return HomePageDAL.get_all_descriptions()

    @staticmethod
    def add_description(text, image_url):
        return HomePageDAL.add_description(text, image_url)
    
    @staticmethod
    def update_description(id, text, image_url):
        return HomePageDAL.update_description(id, text, image_url)

    @staticmethod
    def delete_description(id):
        HomePageDAL.delete_description(id)

    @staticmethod
    def get_section_by_id(id):
        return HomePageDAL.get_section_by_id(id)

    @staticmethod
    def get_all_sections():
        return HomePageDAL.get_all_sections()

    @staticmethod
    def add_section(title, image_url, link):
        return HomePageDAL.create_section(title, image_url, link)
    
    @staticmethod
    def update_section(id, title, image_url, link):
        return HomePageDAL.update_section(id, title, image_url, link)

    @staticmethod
    def delete_section(id):
        HomePageDAL.delete_section(id)