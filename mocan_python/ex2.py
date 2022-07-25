from datetime import datetime

today = datetime.now()
print("Azi: ", today)

year = datetime(day = 31, month = 12, year = 2022)
delta = year - today
print("Au mai ramas ", delta.days, " zile pana la sfarsitul anului")