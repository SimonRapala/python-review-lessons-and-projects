def hello (greeting, title, first, last):
  print(f"{greeting} {title}.{first} {last}")

hello("Hello", "Mr", "Simon", "Rapala")
hello("Hello",first="Simon", last ="Rapala", title= "Mr" )

for x in range(1,11):
  print(x, end="|")
  print(x)

  def getPhone(country, area, first,last):
    return f"{country}-{area}-{first}-{last}"
print(getPhone(country=1,area=123,last=7890, first=456))