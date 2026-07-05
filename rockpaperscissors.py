import random as rnd
options = ("rock", "paper", "scissors")
playerPoints = 0
computerPoints = 0

while True:
  computer = rnd.choice(options)
  player = input("Enter rock, paper or scissors(q to quit): ").lower()
  if player == "q":
    break
  elif player not in options:
    print("Not a valid choice!!!")
    continue
  
  print(f"You chose {player}. Computer chose {computer}")

  if player == computer:
    print("Its a tie")

  elif player == "rock" and computer == "paper":
    print("You lose!")
    computerPoints += 1
  elif player == "rock" and computer == "scissors":
    print("You win!")
    playerPoints += 1

  elif player == "paper" and computer == "rock":
    print("You win!")
    playerPoints += 1
  elif player == "paper" and computer == "scissors":
    print("You lose!")
    computerPoints += 1

  elif player == "scissors" and computer == "paper":
    print("You win!")
    playerPoints += 1
  elif player == "scissors" and computer == "rock":
    print("You lose!")
    computerPoints += 1
print("---- Final Score ----")
print(f"Player : {playerPoints}\n Computer: {computerPoints}")