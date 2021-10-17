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
    },
}
# empty money variable
profit = 0

# available resource
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough = False
    return is_enough


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("please insert coins.")
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.1
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the rerouces."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️ Enjoy!")


# while machine is true it continues to run 24/7 😁
machine_is_on = True

while machine_is_on:
    # Coffee machine asks users which coffee they want to drink!
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    # To turn off the the machine we enter our secrete code off instead latte
    if choice == "off":
        # This changes machine_is_on to False and machine gets turned off as while loop triggers from True to false.
        machine_is_on = False
        # or else if we ask report we get the latest report using dict keys and values
    elif choice == "report":
        # resource is dict key with [inside their values]
        # using f string to f"{}"
        print(f"water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        # assign ingredients to drink from menu dict the choice is act as dict key.
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
