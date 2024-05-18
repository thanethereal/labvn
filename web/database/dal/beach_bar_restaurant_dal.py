from database.models.beach_bar_and_restaurant import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://lifesabeach:lifesabeach@localhost:5432/lifesabeach')
Session = sessionmaker(bind=engine)
session = Session()

class BeachBarRestaurantDAL:
    @staticmethod
    def get_restaurant_info_by_id(id):
        try:
            return session.query(RestaurantInfo).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_restaurant_infos():
        try:
            return session.query(RestaurantInfo).order_by(RestaurantInfo.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_restaurant_info(restaurant_name, beach_bar_hours, restaurant_hours, happy_hour_hours, description):
        try:
            new_description = RestaurantInfo(restaurant_name=restaurant_name, 
                                             beach_bar_hours=beach_bar_hours,
                                             restaurant_hours=restaurant_hours, 
                                             happy_hour_hours=happy_hour_hours, 
                                             description=description, 
                                             )
            session.add(new_description)
            session.commit()
            return new_description
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_restaurant_info(item_id, restaurant_name, beach_bar_hours, restaurant_hours, happy_hour_hours, description):
        try:
            item = BeachBarRestaurantDAL.get_restaurant_info_by_id(item_id)
            item.restaurant_name=restaurant_name
            item.beach_bar_hours=beach_bar_hours
            item.restaurant_hours=restaurant_hours 
            item.happy_hour_hours=happy_hour_hours
            item.description=description
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_restaurant_info(id):
        try:
            item = BeachBarRestaurantDAL.get_restaurant_info_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_food_by_id(id):
        try:
            return session.query(Food).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_foods():
        try:
            return session.query(Food).order_by(Food.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_food(name, image_url):
        try:
            new_food = Food(name=name, image_url=image_url)
            session.add(new_food)
            session.commit()
            return new_food
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_food(item_id, name, image_url):
        try:
            item = BeachBarRestaurantDAL.get_food_by_id(item_id)
            item.name = name
            item.image_url = image_url
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_food(id):
        try:
            item = BeachBarRestaurantDAL.get_food_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_drink_by_id(id):
        try:
            return session.query(Drink).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_drinks():
        try:
            return session.query(Drink).order_by(Drink.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_drink(name, image_url):
        try:
            new_drink = Drink(name=name, image_url=image_url)
            session.add(new_drink)
            session.commit()
            return new_drink
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_drink(item_id, name, image_url):
        try:
            item = BeachBarRestaurantDAL.get_drink_by_id(item_id)
            item.name = name
            if image_url:
                item.image_url = image_url
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_drink(id):
        try:
            item = BeachBarRestaurantDAL.get_drink_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_image_collection_by_id(id):
        try:
            return session.query(RestaurantBarImageColection).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_image_collection():
        try:
            return session.query(RestaurantBarImageColection).order_by(RestaurantBarImageColection.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_image_collection(image_url, overlay_content):
        try:
            new_image_collection = RestaurantBarImageColection(image_url=image_url, overlay_content=overlay_content)
            session.add(new_image_collection)
            session.commit()
            return new_image_collection
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_image_collection(item_id, overlay_content, image_url):
        try:
            item = BeachBarRestaurantDAL.get_image_collection_by_id(item_id)
            if image_url:
                item.image_url = image_url
            item.overlay_content = overlay_content
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_image_collection(id):
        try:
            item = BeachBarRestaurantDAL.get_image_collection_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def get_restaurant_menu_by_id(id):
        try:
            return session.query(RestaurantBarMenu).get(id)
        except SQLAlchemyError as e:
            session.rollback()
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_restaurant_menu():
        try:
            return session.query(RestaurantBarMenu).order_by(RestaurantBarMenu.id).all()
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def add_restaurant_menu(image_url):
        try:
            restaurant_menu = RestaurantBarMenu(image_url=image_url)
            session.add(restaurant_menu)
            session.commit()
            return restaurant_menu
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        
    @staticmethod
    def update_restaurant_menu(item_id, image_url):
        try:
            item = BeachBarRestaurantDAL.get_restaurant_menu_by_id(item_id)
            if image_url:
                item.image_url = image_url
            session.commit()
            return item
        except SQLAlchemyError as e:
            session.rollback()
            raise e

    @staticmethod
    def delete_restaurant_menu(id):
        try:
            item = BeachBarRestaurantDAL.get_restaurant_menu_by_id(id)
            session.delete(item)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e