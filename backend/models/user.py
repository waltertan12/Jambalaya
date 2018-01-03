import datetime

from dao.auth import encrypt_password
from utils.params_utils import all_params_are_of_type

DEFAULT_ROLES = ['USER']

class User(object):
    """
    User object for modeling user data
    """
    def __init__(self, username: str, password: str, email: str, last_login: datetime, last_modified: datetime, roles=DEFAULT_ROLES) -> None:
        """
        ctor.
        :param username:  
        :param password: 
        :param email: 
        :param last_login: 
        :param last_modified: 
        :param roles: 
        """
        all_params_are_of_type([username, password, email], str)
        all_params_are_of_type([last_login, last_modified], datetime)
        if not isinstance(roles, list):
            raise TypeError("expected list but received", type(roles))
        self.username = username
        self.password = self.__set_password(password)
        self.email = email
        self.last_login = last_login
        self.last_modified = last_modified
        self.roles = roles

    def __set_password(self, password: str) -> str:
        """
        Returns the encrypted password
        :param password: 
        :return: the encrypted password
        """
        if not isinstance(password, str):
            raise TypeError('expected type str, but received type', type(password))
        return encrypt_password(self.password)
