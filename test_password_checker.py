from unittest import TestCase
from while_password import password_checker

class Testpassword_checker(TestCase):
    def test_password_checker_correct_number(self):
        num = "123456"
        quess = "123456"
        result = password_checker(num, quess)
        self.assertEqual(result, "Correct!")
