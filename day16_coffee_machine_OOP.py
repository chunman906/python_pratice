from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_turn_on = True
menu = Menu()

while machine_turn_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options}: ").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        print("You're turning off the machine.")
        machine_turn_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
