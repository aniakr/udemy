from datetime import datetime as dt
def working_hours(date):
    if ((dt(date.year, date.month, date.day, 17) < date < dt(date.year, date.month, date.day, 23, 30) and date.weekday()<5)
            or(dt(date.year, date.month, date.day, 10) < date < dt(date.year, date.month, date.day, 19) and date.weekday()>5)):
        return True
    else:
        return False