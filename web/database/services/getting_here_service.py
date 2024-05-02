from database.dal.getting_here_dal import GettingHereDAL
class GettingHereService:
    @staticmethod
    def get_getting_here_info_by_id(id):
        return GettingHereDAL.get_getting_here_info_by_id(id)

    @staticmethod
    def get_all_getting_here_infos():
        return GettingHereDAL.get_all_getting_here_infos()

    @staticmethod
    def add_getting_here_info(title, description):
        return GettingHereDAL.add_getting_here_info(title, description)
    
    @staticmethod
    def update_getting_here_info(item_id, title, description):
        return GettingHereDAL.update_getting_here_info(item_id, title, description)

    @staticmethod
    def delete_getting_here_info(id):
        GettingHereDAL.delete_getting_here_info(id)
    
    @staticmethod
    def get_getting_here_by_id(id):
        return GettingHereDAL.get_getting_here_by_id(id)

    @staticmethod
    def get_all_getting_heres():
        return GettingHereDAL.get_all_getting_heres()

    @staticmethod
    def add_getting_here(name, image_urls, links, description):
        return GettingHereDAL.add_getting_here(name, image_urls, links, description)
    
    @staticmethod
    def update_getting_here(item_id, name, image_urls, links, description):
        return GettingHereDAL.update_getting_here(item_id, name, image_urls, links, description)

    @staticmethod
    def delete_getting_here(id):
        GettingHereDAL.delete_getting_here(id)

