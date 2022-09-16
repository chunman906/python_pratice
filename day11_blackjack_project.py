import random
from replit import clear
from art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  cards_len = len(cards)
  random_card = cards[random.randint(0,cards_len-1)]
  return random_card

def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and computer_score > 21:
    return "You went over. You lose 😤"

  if user_score == computer_score:
    return "Draw 🙃"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game():
  user = []
  computer = []
  is_game_over = False

  for i in range(2):
    user.append(deal_card())
    computer.append(deal_card())

  while not is_game_over:
    computer_score = calculate_score(computer)
    user_score = calculate_score(user)
    print(f"Your cards: {user}, current score: {user_score}")
    print(f"Computer's first card: {computer[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user.append(deal_card())
      else:
        is_game_over = True
  while computer_score != 0 and computer_score < 17:
    computer.append(deal_card())
    computer_score = calculate_score(computer)

  print(f"   Your final hand: {user}, final score: {user_score}")
  print(f"   Computer's final hand: {computer}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a blackjack game? Type 'y' to start or 'n' to quit: ") == 'y':
  clear()
  play_game()
