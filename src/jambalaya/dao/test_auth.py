import unittest
import bcrypt
from auth import encrypt_password

class EncryptPasswordTest(unittest.TestCase):
    """ Tests for password encryption """

    def test_successful_case(self):
        """Test password is successfully hashed"""
        raw = 'password'
        self.assertTrue(bcrypt.checkpw(raw.encode('utf-8'), encrypt_password(raw)))

    def test_raises_valueError_for_long_passwords(self):
        password = 'x' * 73
        with self.assertRaises(ValueError):
            encrypt_password(password)

    def test_raises_typeError_for_non_string(self):
        with self.assertRaises(TypeError):
            encrypt_password(52)

    def test_raises_value_error_for_empty_string(self):
        with self.assertRaises(ValueError):
            encrypt_password("")

if __name__ == '__main__':
    unittest.main()
