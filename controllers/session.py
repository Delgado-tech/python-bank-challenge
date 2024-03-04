from controllers.user import User
from mocks.account_mockup import AccountMockup
from mocks.user_mockup import UserMockup


class Session:
    user_id: int = 1
    account_number: str

    def get_user():
        return UserMockup.get_user(id=Session.user_id)
    
    def get_account():
        account = AccountMockup.get_account(account_number=Session.account_number)

        if account:
            if len(account) > 0:
                return account[0]
            
        return None