from database.dal.our_story_dal import OurStoryDAL, TourismBenefitEveryoneDAL

class OurStoryService:
    @staticmethod
    def get_our_story_by_id(id):
        return OurStoryDAL.get_our_story_by_id(id)

    @staticmethod
    def get_all_our_stories():
        return OurStoryDAL.get_all_our_stories()

    @staticmethod
    def add_our_story(text, image_url):
        return OurStoryDAL.add_our_story(text, image_url)
    
    @staticmethod
    def update_our_story(id, text, image_url):
        return OurStoryDAL.update_our_story(id, text, image_url)

    @staticmethod
    def delete_our_story(id):
        OurStoryDAL.delete_our_story(id)

class TourismBenefitEveryoneService:
    @staticmethod
    def get_tourism_benefit_everyone_by_id(id):
        return TourismBenefitEveryoneDAL.get_tourism_benefit_everyone_by_id(id)

    @staticmethod
    def get_all_tourism_benefit_everyones():
        return TourismBenefitEveryoneDAL.get_all_tourism_benefit_everyones()

    @staticmethod
    def add_tourism_benefit_everyone(text, image_url):
        return TourismBenefitEveryoneDAL.add_tourism_benefit_everyone(text, image_url)
    
    @staticmethod
    def update_tourism_benefit_everyone(id, text, image_url):
        return TourismBenefitEveryoneDAL.update_tourism_benefit_everyone(id, text, image_url)

    @staticmethod
    def delete_tourism_benefit_everyone(id):
        TourismBenefitEveryoneDAL.delete_tourism_benefit_everyone(id)