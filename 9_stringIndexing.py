number = "1234-5678-9012-3456"

print(number[0])
print(number[0:4:2])
print(number[5:9:1])
print(number[len(number)::-1])
print(number[::2])

print(f"Last 4 digits: XXXX-XXXX-XXXX{number[-5:]}")