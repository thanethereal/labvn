from database.dal.beach_bar_restaurant_dal import BeachBarRestaurantDAL

class BeachBarRestaurantService:
    @staticmethod
    def get_restaurant_info_by_id(id):
        return BeachBarRestaurantDAL.get_restaurant_info_by_id(id)
    
    @staticmethod
    def get_all_restaurant_infos():
        return BeachBarRestaurantDAL.get_all_restaurant_infos()
    
    staticmethod
    def add_restaurant_info(restaurant_name, beach_bar_hours, restaurant_hours, happy_hour_hours, description):
        return BeachBarRestaurantDAL.add_restaurant_info(restaurant_name, beach_bar_hours, restaurant_hours, happy_hour_hours, description)

    @staticmethod
    def update_restaurant_info(id, restaurant_name, beach_bar_hours, restaurant_hours, happy_hour_hours, description):
        return BeachBarRestaurantDAL.update_restaurant_info(id, restaurant_name, beach_bar_hours, restaurant_hours, happy_hour_hours, description)

    @staticmethod
    def get_food_by_id(id):
        return BeachBarRestaurantDAL.get_food_by_id(id)

    @staticmethod
    def get_all_foods():
        return BeachBarRestaurantDAL.get_all_foods()

    @staticmethod
    def add_food(name, image_url):
        return BeachBarRestaurantDAL.add_food(name, image_url)
    
    @staticmethod
    def update_food(item_id, name, image_url):
        return BeachBarRestaurantDAL.update_food(item_id, name, image_url)

    @staticmethod
    def delete_food(id):
        BeachBarRestaurantDAL.delete_food(id)

    @staticmethod
    def get_drink_by_id(id):
        return BeachBarRestaurantDAL.get_drink_by_id(id)

    @staticmethod
    def get_all_drinks():
        return BeachBarRestaurantDAL.get_all_drinks()

    @staticmethod
    def add_drink(name, image_url):
        return BeachBarRestaurantDAL.add_drink(name, image_url)
    
    @staticmethod
    def update_drink(item_id, name, image_url):
        return BeachBarRestaurantDAL.update_drink(item_id, name, image_url)

    @staticmethod
    def delete_drink(id):
        BeachBarRestaurantDAL.delete_drink(id)

    @staticmethod
    def get_image_collection_by_id(id):
        return BeachBarRestaurantDAL.get_image_collection_by_id(id)

    @staticmethod
    def get_all_image_collection():
        return BeachBarRestaurantDAL.get_all_image_collection()

    @staticmethod
    def add_image_collection(image_url, overlay_content):
        return BeachBarRestaurantDAL.add_image_collection(image_url, overlay_content)
    
    @staticmethod
    def update_image_collection(item_id, overlay_content, image_url):
        return BeachBarRestaurantDAL.update_image_collection(item_id, overlay_content, image_url)

    @staticmethod
    def delete_image_collection(id):
        BeachBarRestaurantDAL.delete_image_collection(id)

    @staticmethod
    def get_restaurant_menu_by_id(id):
        return BeachBarRestaurantDAL.get_restaurant_menu_by_id(id)

    @staticmethod
    def get_all_restaurant_menu():
        return BeachBarRestaurantDAL.get_all_restaurant_menu()

    @staticmethod
    def add_restaurant_menu(image_url):
        return BeachBarRestaurantDAL.add_restaurant_menu(image_url)
    
    @staticmethod
    def update_restaurant_menu(item_id, image_url):
        return BeachBarRestaurantDAL.update_restaurant_menu(item_id, image_url)

    @staticmethod
    def delete_restaurant_menu(id):
        BeachBarRestaurantDAL.delete_restaurant_menu(id)