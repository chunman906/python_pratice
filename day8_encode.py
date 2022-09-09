alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, choice):
    end_text = ""
    if choice == "decode":
      shift_amount *= -1
    for letter in start_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    print(f"The {choice}d text is {end_text}")

caesar(start_text=text, shift_amount=shift, choice=direction)

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
