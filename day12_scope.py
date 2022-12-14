from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}")

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game()



# my attemp version
# from art import logo
# import random

# answer = random.randint(1,100)

# def play_game():
#   level = input("Choose a difficulty. Type 'easy' or 'hard': ")
#   if level == 'easy':
#     attempts = 10
#   elif level == 'hard':
#     attempts = 5
#   return attempts

# def game(attempts, answer):
#   game_continue = True
#   while attempts > 0 and game_continue :
#     print(f"You have {attempts} attempts remaining to guess the number")
#     guess = int(input("Make a guess: "))
#     if guess == answer:
#       print('you got it. you win!')
#       game_continue = False
#     elif guess < answer:
#       print("Too low. \nGuess again.")
#       attempts -= 1
#     elif guess > answer:
#       print("Too high. \nGuess again.")
#       attempts -= 1
#   if attempts == 0:
#     print("You've run out of guessess, you lose!")

# print(logo)
# print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
# game(play_game(),answer)

# 1)print log & make a random answer & choose level - inputs
# 2) Based on the level(if), then start a while loop to make guess
# 3) provide comment elif higher / lower, and deduct the counter
# 4) if the answer == guess then win the game
# 5) if counter = 0, then end game and provide commit
