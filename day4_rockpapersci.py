import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
options = [rock, paper, scissors]
player_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_option >= 3 or player_option < 0:
  print("Sorry, you've entered wrong number")
else:
  print(options[player_option])
  computer_option = random.randint(0,2)
  print(f"Computer chose: \n {options[computer_option]}")

  if player_option == 0 and computer_option == 2:
    print("You win!")
  elif computer_option == 0 and player_option == 2:
    print("You lose!")
  elif player_option > computer_option:
    print("You win!")
  elif computer_option > player_option:
    print("You lose!")
  elif player_option == computer_option:
    print("It's a tie!")
