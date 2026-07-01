temp = 20
isRaining = False

if temp > 35 and isRaining:
  print("Too hot and is raining")
elif temp < 0 and isRaining:
  print("Too cold and is raining")
elif temp > 35 or temp < 0:
  print("The outdoor event is cancelled")
elif not isRaining:
  print("The event is still scheduled")