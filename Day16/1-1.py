from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("Blue")
# timmy.forward(100)


# myscreen = Screen()
# myscreen.exitonclick()

from prettytable import PrettyTable

# table is object and blueprint is PrettyTable() class and module name is prettytable
# table var now holds the class and it's functions
table = PrettyTable()

# adding column with some values , values should be a list
table.add_column("Pokeman Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

# changing alignment you can use "l" "c" "r"
table.align = "l"

# finally we have our table with column names and values
print(table)
