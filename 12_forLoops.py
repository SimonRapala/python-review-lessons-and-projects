for i in reversed(range(1, 11)):
  print(i)
print("Done")

card = "1234-5678-9012-3456"
for x in card[::2]:
  print(x)

for x in range(1,21):
  if x == 13:
    continue
  elif x == 15:
    break
  else:
    print(x)