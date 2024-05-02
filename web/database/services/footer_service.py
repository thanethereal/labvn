from database.dal.footer_dal import FooterDAL
class FooterService:
    @staticmethod
    def get_footer_by_id(id):
        try:
            return FooterDAL.get_footer_by_id(id)
        except Exception as e:
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def get_all_footers():
        try:
            return FooterDAL.get_all_footers()
        except Exception as e:
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def add_footer(phone, email, address, link_facebook, link_instagram, link_tiktok):
        try:
            return FooterDAL.add_footer(phone, email, address, link_facebook, link_instagram, link_tiktok)
        except Exception as e:
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def update_footer(item_id, phone, email, address, link_facebook, link_instagram, link_tiktok):
        try:
            return FooterDAL.update_footer(item_id, phone, email, address, link_facebook, link_instagram, link_tiktok)
        except Exception as e:
            # Handle the exception, log it, or re-raise it
            raise e

    @staticmethod
    def delete_footer(id):
        try:
            FooterDAL.delete_footer(id)
        except Exception as e:
            # Handle the exception, log it, or re-raise it
            raise e