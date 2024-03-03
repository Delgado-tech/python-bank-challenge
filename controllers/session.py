from controllers.user import User
from mocks.user_mockup import UserMockup


class Session:
    user_id: int = 1

    def get_user():
        return UserMockup.get_user(id=Session.user_id)