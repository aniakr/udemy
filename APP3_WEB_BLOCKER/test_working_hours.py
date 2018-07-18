from unittest import TestCase
from working_hours import working_hours
from datetime import datetime

class TestWorking_hours(TestCase):
    def test_working_hours(self):
        self.fail()


class TestWorking_hours(TestCase):
    def test_morning_weekend(self):
        date=datetime(2018, 7, 1, 9, 45)
        result = working_hours(date)
        self.assertEqual(result,False)

class TestWorking_hours(TestCase):
    def test_evening_weekend(self):
        date = datetime(2018, 7, 1, 20, 45)
        result = working_hours(date)
        self.assertEqual(result, False)

class TestWorking_hours(TestCase):
    def test_morning_working(self):
        date=datetime(2018, 7, 4, 11, 45)
        result = working_hours(date)
        self.assertEqual(result,True)

class TestWorking_hours(TestCase):
    def test_evening_working(self):
        date=datetime(2018, 7, 4, 23, 45)
        result = working_hours(date)
        self.assertEqual(result,False)

