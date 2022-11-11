from datetime import date
from dateutil.relativedelta import relativedelta
from babel.numbers import format_currency as fc

class Curency:
    @staticmethod
    def convert(type) -> str:
        if type != None:
            return fc(type,'IDR',locale='id')
        else:
            return '-'




class dateUtil:
    def __init__(self) -> None:
        self.date = date.today()
    
    def get_first_day_of_month(self):
        return self.date.replace(day=1)

    def get_last_day_of_month(self):
        return self.date.replace(day=1) + relativedelta(months=1)