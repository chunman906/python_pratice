from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable format: name, description and country"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  # print(f'{name}: {account["follower_count"]}')
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess
  and returns True if they got it right.
  Or False if they got it wrong."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"


def game():
  print(logo)
  score = 0
  game_should_continue = True
  account_a = get_random_account()
  account_b = get_random_account()

  while game_should_continue:
    account_a = account_b
    account_b = get_random_account()

    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      game_should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()



# my attempt
#1) display logo, compare A & B (dictionies value) and question
# from art import logo, vs
# from game_data import data

# #2) compare followers and determine if it is right, then add score
# def compare_followers(item1,item2):
#   if item1['follower_count'] > item2['follower_count']:
#     return 'A'
#   elif item2['follower_count'] > item1['follower_count']:
#     return 'B'

# A = 0
# B = 1
# score = 0
# game_continue = True
# print(logo)

# while game_continue == True:
#   print(f"Compare A: {data[A]['name']}, a {data[A]['description']}, from {data[A]['country']}. ")
#   print(vs)
#   print(f"Against B: {data[B]['name']}, a {data[B]['description']}, from {data[B]['country']}. ")
#   guess = input("Who has more followers? Type 'A' or 'B': ").upper()
#   if guess == compare_followers(data[A],data[B]):
#     score += 1
#     print(logo)
#     print(f"You're right! Current score: {score}.")
#     A += 1
#     B += 1
#   else:
#     print(f"Sorry, that's wrong. Final score: {score}.")
#     game_continue = False


#3) move up B into A and display new B to compare
