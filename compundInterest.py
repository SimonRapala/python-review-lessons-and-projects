investment = -1
rate = -1
time = -1
while investment <= 0:
  investment = float(input("Enter Initial Investment: "))
  if investment <= 0:
    print("Investment cant be less than or equal to 0.")
  
while rate <= 0:
  rate = float(input("Enter Interest Rate: "))
  if rate <= 0:
    print("Rate cant be less than or equal to 0.")
  rate /= 100
  
while time <= 0:
  time = int(input("Over What Period Of Time: "))
  if time <= 0:
    print("Time cant be less than or equal to 0.")

total = investment * pow((1+rate), time)
print(f"Total Amount after {time} years is {total:.2f}")
#could make work with 0 by making while loop infinite and breaking whne got correct ans