from database.dal.header_image_dal import HeaderImageDAL
class HeaderImageService:
    @staticmethod
    def get_header_image_by_id(id):
        return HeaderImageDAL.get_header_image_by_id(id)
    
    @staticmethod
    def get_header_image_by_name(page_name):
        return HeaderImageDAL.get_header_image_by_name(page_name)

    @staticmethod
    def get_all_header_images():
        return HeaderImageDAL.get_all_header_images()

    @staticmethod
    def add_header_image(page_name, image_urls):
        return HeaderImageDAL.add_header_image(page_name, image_urls)
    
    @staticmethod
    def update_header_image(item_id, page_name, image_urls):
        return HeaderImageDAL.update_header_image(item_id, page_name, image_urls)

    @staticmethod
    def delete_header_image(id):
        HeaderImageDAL.delete_header_image(id)
