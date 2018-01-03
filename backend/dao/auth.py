import bcrypt

def encrypt_password(password: str) -> str:
    """
    Uses bcrypt to encrypt the given string password after adding a prefix
    :param password: str - must be less than 72 characters long
    :return: 
    :raises: 
        - ValueError if password is longer than 72 characters because bcrypt
            truncates passwords greater than 72.
        - ValueError if password has length 0
        - TypeError if password is not of type str
    """
    if not isinstance(password, str):
        raise TypeError("encrypt_password only takes objects of type str, instead received type", type(password))
    if len(password) > 72:
        raise ValueError("password is too long")
    if len(password) is 0:
        raise ValueError("password contains no characters")
    # prefix should be 2b as mentioned in the comments on :ref:`bcrypt.hashpw`
    prefix = '2b'.encode('utf-8')
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(prefix=prefix))
