import datetime

class WeekNrImage(object):

    def __init__(self, date):
        self.weeknr = self._get_week_nr(date)
        
    def _get_week_nr(self, date):
        return date.isocalendar()[1]

