from unittest import TestCase

from TIMESHEET.timesheet_db import Database


class TestDatabase(TestCase):
    db = Database()

    def test_user_from_login(self):
        current_user = self.db.user_from_login("Ania")
        self.assertEquals("Anna", current_user[0])

    def test_user_not_in_db(self):
        current_user = self.db.user_from_login("Dupa")
        self.assertEquals(None,current_user)

    def test_get_all_users(self):
        users = self.db.get_all_users()
        self.assertEquals(["Anna",],users)

    def test_get_hub(self):
        hub = self.db.hub_default("Anna")
        self.assertEquals(('EU',),hub)

    def test_all_items(self):
        items = self.db.get_all_items('f_name','users')
        self.assertEquals(['Anna',],items)

    def test_entry_set_to_be_displayed(self):
        items = self.db.display_month('October','2018')
        self.assertEquals((13,'Tommy Tommy','SOX','October','2018',None),items)
