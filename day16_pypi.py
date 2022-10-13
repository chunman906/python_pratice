# from turtle import Turtle, Screen
# timmy = Turtle()
# man = Turtle()
# print(timmy, man)
# timmy.shape("turtle")
# man.shape("turtle")
# timmy.color("DarkOrange")
# man.color("blue")
# man.forward(30)
# timmy.backward(20)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Pokemon Name","Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Squirtle", "Water"])
table.add_row(["Charmander", "Fire"])

table.align = "l"

print(table)
