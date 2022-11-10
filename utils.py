from datetime import date
from dateutil.relativedelta import relativedelta


class dateUtil:
    def __init__(self) -> None:
        self.date = date.today()
    
    def get_first_day_of_month(self):
        return self.date.replace(day=1)

    def get_last_day_of_month(self):
        return self.date.replace(day=1) + relativedelta(months=1)