import unittest
import datetime
from weeknr.weeknrimage import WeekNrImage

class TestWeekNrImage(unittest.TestCase):

    def test_jan1_2019_week1(self):
        i = WeekNrImage(datetime.date(2019, 1, 1))
        self.assertEqual(1, i.weeknr, msg='01-01-2019 should be week 1')

    def test_dec25_2019_week52(self):
        i = WeekNrImage(datetime.date(2018, 12, 25))
        self.assertEqual(52, i.weeknr, msg='25-12-2018 should be week 52')

if __name__ == '__main__':
    unittest.main()