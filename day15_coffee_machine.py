MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# TODO: 1. Print question (loop) and display report (dictionary of list)

machine_turn_on = True
resource = {"water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0}
drinks = []
for key in MENU.keys():
    drinks.append(key)
quarters = 0
dimes = 0
nickles = 0
pennies = 0


def is_drinks(drinks,choice):
    if choice in drinks:
        return True
    else:
        return False

def print_report(item):
    print(f"Water: {item['water']}ml")
    print(f"Milk: {item['milk']}ml")
    print(f"Coffee: {item['coffee']}g")
    print(f"Money: ${item['money']}")

def check_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resource[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def make_coffee(order_ingredients, resource):
    for item in order_ingredients:
        resource[item] -= order_ingredients[item]
    return resource


while machine_turn_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print_report(resource)
    elif choice == "off":
        print("You're turning off the machine.")
        machine_turn_on = False

#TODO: 2. create check_sufficient function and perform if menu[items] asked
# TODO: 3. ask to insert coins#TODO: 3. ask to insert coins
    elif is_drinks(drinks, choice) == True:
        drink = MENU[choice]
        if check_sufficient(drink['ingredients']) == True:

#TODO: 4. create calculation function to check if money sufficient and changes
            money = process_coin()
            payment = MENU[choice]['cost']
            changes = 0
            if money >= payment:
                changes = round((money - payment), 2)
                print(f"here is ${changes} dollars in change.")
                resource["money"] += payment
                resource = make_coffee(drink['ingredients'], resource)
                print(f"Here is your {choice} ☕️. Enjoy!")
                print_report(resource)
            else:
                print("Sorry that's not enough money. Money refunded.")
    else:
        print("Wrong name entered!")
#TODO: 5. Make coffee and deducting the ingredients
