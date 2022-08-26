#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print("Welcome to the tips calculator!")
total_bill = input("What was the total bill? ")
tips = input("What percentage of tips would you like to give? 10, 12 or 15? ")
tips_num = 1 + (int(tips) / 100)
num_people = input("How many people to split the bill? ")
bill_per_head = float(int(total_bill) / int(num_people) * tips_num)
result = "{:.2f}".format(bill_per_head)
print(f"Each person should pay: ${result}")
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
