import random

def get_choices():
  player_choice = input('Enter your choice (Rock, Scissors and Paper) :')
  options = ['rock', 'scissors', 'paper']
  computer_choice = random.choice(options)
  game = {'player': player_choice, 'computer': computer_choice}
  return game

def check_win(player, computer):
  print(f'you choice is {player}, computer choice is {computer}')
  if player == computer:
    return "It's a tie"
  elif player == 'rock':
    if computer == 'scissors':
      return "you win!"
    elif computer == 'paper':
      return "you lose!"
  elif player == 'scissors':
    if computer == 'rock':
      return "you lose!"
    elif computer == 'paper':
      return "you win!"
  elif player == 'paper':
    if computer == 'rock':
      return "you win!"
    elif computer == 'scissors':
      return "you lose!"

choice = get_choices()
result = check_win(choice['player'], choice['computer'])
print(result)
