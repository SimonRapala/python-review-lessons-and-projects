capitals = {"USA":"Washington",
            "Canada":"Ottawa",
            "Poland":"Warsaw",
            "India":"New Delhi"}
print(capitals.get("USA"))

if capitals.get("Japan"):
  print("That capital DNE")
else:
  print("That capital exists")

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Detroit"})
print(capitals)
capitals.pop("USA")
print(capitals)

keys = capitals.keys()
for key in keys:
  print(capitals.get(key))

values = capitals.values()
for value in values:
  print(value)