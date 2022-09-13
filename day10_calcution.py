def subtract(n1,n2):
  """subtract the numbers"""
  return n1 - n2

def add(n1,n2):
  return n1 + n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1,n2):
  return n1 / n2

operation = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
}
def calculation():
  continue_cal = True
  num1 = float(input("What is the first number? "))
  for symbol in operation:
      print(symbol)
  while continue_cal == True:
    to_do = str(input("Pick an operation. Type '+', '-', '/' or '*' \n"))
    num_next = float(input("What is the next number? "))
    cal_function = operation[to_do]
    answer = cal_function(num1,num_next)
    print(f"{num1} {to_do} {num_next} = {answer}")
    option = input(f"Type 'y' to continue calculate with {answer}, or type 'n' to exit: ")
    if option == 'y':
      num1 = answer
    elif option == 'n':
      continue_cal = False
      calculation()

calculation()
