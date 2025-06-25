# from datetime import datetime, date, time, timedelta, timezone
# from zoneinfo import ZoneInfo

# print(datetime.now(timezone.utc))
# print(datetime.now(ZoneInfo("Asia/Kathmandu")))


# print(datetime.now(timedelta))

# print(datetime.now(timezone.utc))

# print(date.today())
# print(time(hour=12, minute=30, second=45))

# print((time(hour=12, minute=30, second=45)).microsecond)


# due_date = datetime.now() + timedelta(days=7)


# print(timedelta(days=7))

# print(due_date)

# print(type(due_date))


# print(datetime.now()+datetime(2004, 12, 31))


# user_date = int(input("Enter a due days:"))

# due_date = datetime.now() + timedelta(days=user_date)


# print(due_date)

# year, month, day = 2025, 6, 24

# user_date = datetime(year=year, month=month, day=day)

# print(user_date)

# print(user_date.year)
# print(user_date.month)
# print(user_date.day)



# import time

# print(time.time())


# print(datetime.fromtimestamp(time.time()))


from datetime import time, timezone, timedelta, datetime


tz = timezone(timedelta(hours=5, minutes=45))

print(datetime.now(timezone.utc))

print(datetime.now(tz))


print(time(14, 30, tzinfo=tz))

print(time(14, 30, 45, tzinfo=tz).second)