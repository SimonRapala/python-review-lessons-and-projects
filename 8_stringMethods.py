# name = input("Enter full name: ")
# #len includes spaces
# print(len(name))
# #finds first index of selected char
# print(name.find(" "))
# #find last occurance
# print(name.rfind("S"))
# #capitalizes first char
# print(name.capitalize())
# #makes all upcase or lowercase
# print(name.lower())
# print(name.upper())
# #checks if all chars are digits
# print(name.isdigit())
# #checks if all chars are alphabetical chars
# print(name.isalpha())

# phoneNumber = input("Enter Phone Number: ")
# print(phoneNumber.count("-"))

# print(phoneNumber.replace("-", " "))

# print(help(str))

isValid = False
while not isValid:
  username = input("Enter your username: ")
  if len(username) > 12 or username.find(" ") != -1 or username.isalpha() != 1:
    isValid = False
  else:
    isValid = True