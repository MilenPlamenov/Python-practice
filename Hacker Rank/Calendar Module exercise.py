import datetime
import calendar

date = input()


def findDay(date):
    born = datetime.datetime.strptime(date, '%m %d %Y').weekday()
    return calendar.day_name[born].upper()


print(findDay(date))
