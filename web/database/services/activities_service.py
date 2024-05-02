from database.dal.activities_dal import ActivitiesDAL
class ActivitiesService:
    @staticmethod
    def get_activity_by_id(id):
        return ActivitiesDAL.get_activity_by_id(id)

    @staticmethod
    def get_all_activities():
        return ActivitiesDAL.get_all_activities()

    @staticmethod
    def add_activity(name, description, image_urls):
        return ActivitiesDAL.add_activity(name, description, image_urls)
    
    @staticmethod
    def update_activity(item_id, name, description, image_urls):
        return ActivitiesDAL.update_activity(item_id, name, description, image_urls)

    @staticmethod
    def delete_activity(id):
        ActivitiesDAL.delete_activity(id)

