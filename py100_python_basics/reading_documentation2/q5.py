from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()

print(today_year) # returns year
print(iso_year) # returns iso year, week and weekday