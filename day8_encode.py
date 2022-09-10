alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char not in alphabet:
      end_text += char
    else:
      position = alphabet.index(char)
      new_position = position + shift_amount
      if new_position >= 52:
        new_position %= 52
      end_text += alphabet[new_position]

  print(f"Here's the {cipher_direction}d result: {end_text}")

continue_game = True

while continue_game:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  choice = input("Do you want to restart the game? Type 'yes' to restart, type 'no' to quit. \n")
  if choice == 'no':
    continue_game = False
#Longer version:
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# def decrypt(coded_text, shift_amount):
#   decrypted_text = ""
#   for letter in coded_text:
#     position = alphabet.index(letter)
#     reverse_position = position - shift_amount
#     decrypted_text += alphabet[reverse_position]
#   print(f"The decoded text is {decrypted_text}")

# if direction == 'encode':
#   encrypt(plain_text=text, shift_amount=shift)
# else:
#   decrypt(coded_text=text, shift_amount=shift)
