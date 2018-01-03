import unittest
import datetime

from models import User

class UsersTest(unittest.TestCase):
    """Tests user creation"""

    def successfully_create_user(self):
        user = User("username", "password", "email", datetime.datetime.fromtimestamp(1505446327170), datetime.datetime.fromtimestamp(1505446527170), "last_modified")
