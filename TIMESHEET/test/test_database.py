from unittest import TestCase

from TIMESHEET.timesheet_db import Database
from TIMESHEET.timesheet_service import mandays_validation2


class TestDatabase(TestCase):

    test_db = Database('python_test_db')

    def test_user_from_login(self):
        current_user = self.test_db.user_from_login("Ania")
        self.assertEquals("Anna Krach", current_user[0])

    def test_user_not_in_db(self):
        current_user = self.test_db.user_from_login("Dupa")
        self.assertEquals(None, current_user)

    def test_get_all_users(self):
        users = self.test_db.get_all_users()
        self.assertEqual(["Anna Krach","Tommy Tommy" ], users)

    def test_get_all_users_depend(self):
        users = self.test_db.get_all_users_depend("EU")
        self.assertEquals(["Anna Krach", ], users)

    def test_get_hub(self):
        hub = self.test_db.hub_default("Anna Krach")
        self.assertEquals(('EU',), hub)

    def test_all_items(self):
        items = self.test_db.get_all_items('f_name', 'users')
        self.assertEqual([('Anna Krach',), ('Tommy Tommy',)], items)

    def test_entry_set_to_be_displayed(self):
        items = self.test_db.display_month('October', '2018','Tommy Tommy')
        self.assertEqual([(1, 'Tommy Tommy', 'SOX', 'October', '2018', 5.0, None, None)], items)

    def test_mandays_validation2(self):
        result = mandays_validation2("12,3")
        self.assertEqual(result, 0)

