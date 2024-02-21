from user import User
from developer import Developer


class Member(User, Developer):
    def __init__(self, username, email):
        super().__init__(username, email)

