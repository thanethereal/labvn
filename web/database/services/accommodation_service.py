from database.dal.accommodation_dal import AccommodationDAL
class AccommodationService:
    @staticmethod
    def get_accommodation_info_by_id(id):
        return AccommodationDAL.get_accommodation_info_by_id(id)

    @staticmethod
    def get_all_accommodation_infos():
        return AccommodationDAL.get_all_accommodation_infos()

    @staticmethod
    def add_accommodation_info(title, description):
        return AccommodationDAL.add_accommodation_info(title, description)
    
    @staticmethod
    def update_accommodation_info(item_id, title, description):
        return AccommodationDAL.update_accommodation_info(item_id, title, description)

    @staticmethod
    def delete_accommodation_info(id):
        AccommodationDAL.delete_accommodation_info(id)
    
    @staticmethod
    def get_room_type_by_id(id):
        return AccommodationDAL.get_room_type_by_id(id)

    @staticmethod
    def get_all_room_types():
        return AccommodationDAL.get_all_room_types()

    @staticmethod
    def add_room_type(name, description, image_urls):
        return AccommodationDAL.add_room_type(name, description, image_urls)
    
    @staticmethod
    def update_room_type(item_id, name, description, image_urls):
        return AccommodationDAL.update_room_type(item_id, name, description, image_urls)

    @staticmethod
    def delete_room_type(id):
        AccommodationDAL.delete_room_type(id)

