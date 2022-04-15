import datetime


year_input = int(input("Year:"))
month_input = int(input("Month[1-12]:"))
day_input = int(input("Day[1-31]:"))


gDate = datetime.datetime(year_input, month_input, day_input)

# tomorrow
NextDay_Date = gDate + datetime.timedelta(days=1)
NextDay_Date_Formatted = NextDay_Date.strftime ('%Y-%m-%d')
print ('The next date is: ' + str(NextDay_Date_Formatted))


#  yesterday is same just  gDate - datetime.timedelta(days=1)
