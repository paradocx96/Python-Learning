import datetime

x = datetime.datetime.now()
print(x)  # 2023-01-16 19:00:48.445586

print(x.year)  # 2023
print(x.month)  # 1
print(x.day)  # 16
print(x.hour)  # 19
print(x.minute)  # 4
print(x.second)  # 43

print(x.strftime("%a"))  # Mon
print(x.strftime("%A"))  # Monday
print(x.strftime("%w"))  # 1
print(x.strftime("%d"))  # 16
print(x.strftime("%b"))  # Jan
print(x.strftime("%B"))  # January
print(x.strftime("%m"))  # 01
print(x.strftime("%y"))  # 23
print(x.strftime("%Y"))  # 2023
print(x.strftime("%H"))  # 19
print(x.strftime("%I"))  # 07
print(x.strftime("%p"))  # PM
print(x.strftime("%M"))  # 04
print(x.strftime("%S"))  # 43
print(x.strftime("%f"))  # 132652
print(x.strftime("%z"))  # +0000
print(x.strftime("%Z"))  # UTC
print(x.strftime("%j"))  # 016
print(x.strftime("%U"))  # 03
print(x.strftime("%W"))  # 03
print(x.strftime("%c"))  # Mon Jan 16 19:04:43 2023
print(x.strftime("%C"))  # 20
print(x.strftime("%x"))  # 01/16/23
print(x.strftime("%X"))  # 19:04:43
print(x.strftime("%%"))  # %
print(x.strftime("%G"))  # 2023
print(x.strftime("%u"))  # 1
print(x.strftime("%V"))  # 03

# Create a date object
y = datetime.datetime(2023, 1, 17)
print(y)  # 2023-01-17 00:00:00
print(y.strftime("%B"))  # January
