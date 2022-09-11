from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
information = {}
stopping = False

def find_highest(user_info):
    highest_bid = 0
    winner = ""
    for person in information:
      bid_price = information[person]
      if bid_price > highest_bid:
        highest_bid = bid_price
        winner = person
    print(f"The highest bid is {highest_bid} by {winner}!")

while not stopping:
  name = input("What is your name? \n")
  bid_price = int(input("How much is your bid price? \n"))
  information[name] = bid_price
  next_game = input("Are there other users who want to bid? Type 'yes' or 'no' \n").lower()
  clear()
  if next_game == 'no':
    stopping = True
    find_highest(information)
