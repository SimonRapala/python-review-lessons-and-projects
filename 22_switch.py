def dayOfWeek(day):
  match day:
    case 1:
      return "It is Sunday"
    case 2:
      return "It is Monday"
    case 3:
      return "It is Tuesday"
    case 4:
      return "It is Wednesday"
    case 5:
      return "It is Thursday"
    case 6:
      return "It is Friday"
    case 7:
      return "It is Saturday"
    case _:
      return "Not Valid"
    
def isWeekend(day):
  match day:
    case 1:
      return True
    case 2:
      return False
    case 3:
      return False
    case 4:
      return False
    case 5:
      return False
    case 6:
      return False
    case 7:
      return True
    case _:
      return "Not Valid"
    
print(dayOfWeek(1))
print(dayOfWeek("Pizza"))