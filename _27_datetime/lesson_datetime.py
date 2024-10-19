import datetime

current_time = datetime.datetime.now()
print(current_time.year)
print(current_time.month)
print(current_time.day)
print(current_time.hour)
print(current_time.minute)


some_datetime = datetime.datetime(year=2021, month=9, day=4, hour=11, minute=35)
print(some_datetime)


current_date = datetime.date.today()
print(current_date)


current_date = datetime.datetime.now()
current_date = current_date.date()
print(current_date)


current_datetime = datetime.datetime.now()
day_ago = current_datetime - datetime.timedelta(days=1)
print(day_ago)


current_datetime = datetime.datetime.now()
print(current_datetime.strftime("%A, %d %B %Y"))
