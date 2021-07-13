from api.dataaccess.user.userdataaccess import UserAccess


class UserService:
    @staticmethod
    def user_all(page, size):
        return UserAccess().user_all(page, size)