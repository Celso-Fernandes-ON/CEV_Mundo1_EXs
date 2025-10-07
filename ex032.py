from datetime import date
year = int(input(": "))
if year == 0:
  year = date.today().year
if ((year % 4) == 0 and (year % 100 != 0)) or (year % 400 == 0):
  print(f"{year} bissexto")
else:
  print(f"{year} não bissexto")