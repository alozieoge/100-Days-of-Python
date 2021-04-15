QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

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

RESOURCE_UNITS = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g"
}


# TODO: 3. Print report of all coffee machine resources.
def show_report(resources, money):
    """
    Shows the status of the coffee machine resources.
    :param resources: Coffee machine resources.
    :param money: Total amount of money in the coffee machine in dollars.
    :return: None
    """
    for item in resources:
        print(f"{item.title()}: {resources[item]}{RESOURCE_UNITS[item]}")
    print(f"Money: ${money}")


# TODO: 4. Check resources sufficient to make drink order.
def check_resources(drink, resources):
    """
    Checks if the resources are sufficient to make the drink order and returns the result.
    :param drink: Drink order.
    :param resources: Coffee machine resources.
    :return: True or False
    """
    for menu_item in MENU:
        if drink == menu_item:
            for ingredient in MENU[menu_item]["ingredients"]:
                if resources[ingredient] < MENU[menu_item]["ingredients"][ingredient]:
                    print(f"Sorry there is not enough {ingredient}.")
                    return False
    return True


def calculate_amount_paid(quarters, dimes, nickles, pennies):
    """
    Calculates the total amount of money based on the number of each type of coins provided.
    :param quarters: Number of quarters.
    :param dimes: Number of dimes.
    :param nickles: Number of nickles.
    :param pennies: Number of pennies.
    :return: Total amount in dollars.
    """
    return (quarters * QUARTER) + (dimes * DIME) + (nickles * NICKLE) + (pennies * PENNY)


def calculate_menu_cost(drink):
    """
    Returns the cost of the drink.
    """
    return MENU[drink]["cost"]


# TODO: 6. Check transaction successful.
def check_transaction(drink, paid):
  """
  Checks if the money is enough to pay for the menu item.
  :param drink: Drink order.
  :param paid: Amount paid in dollars.
  :return: True or False
  """
    for menu_item in MENU:
        if drink == menu_item:
            cost = MENU[menu_item]["cost"]
            if paid < cost:
                print("Sorry that's not enough money. Money refunded.")
                return False
            else:
                return True


def calculate_machine_money(paid, money):
    """
    Returns the total money in the machine after payment.
    """
    return paid + money


def calculate_change(paid, cost):
    """
    Returns the change after payment.
    """
    print(f"Here is ${round(paid - cost, 2)} in change.")


# TODO: 7. Make coffee.
def deduct_ingredients(drink, resources):
    for menu_item in MENU:
        if drink == menu_item:
            for ingredient in MENU[menu_item]["ingredients"]:
                resources[ingredient] -= MENU[menu_item]["ingredients"][ingredient]
    print(f"Here is your {drink} ☕. Enjoy!")
    return resources


def coffee_machine():
    machine_resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100
    }

    machine_money = 0
    machine_on = True

    while machine_on:
        # TODO: 1. Prompt user with welcome message.
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        # TODO: 2. Turn off coffee machine by entering 'off' at starting prompt.
        if user_input == "off":
            machine_on = False

        # TODO: 3. Print report of all coffee machine resources.
        elif user_input == "report":
            show_report(machine_resources, machine_money)

        elif user_input in MENU.keys():
            resources_enough = check_resources(user_input, machine_resources)

            if resources_enough:
                # TODO: 5. Process coins.
                print("Please insert coins.")
                num_quarters = int(input(" How many quarters?: "))
                num_dimes = int(input(" How many dimes?: "))
                num_nickles = int(input(" How many nickles?: "))
                num_pennies = int(input(" How many pennies?: "))

                amount_paid = calculate_amount_paid(num_quarters, num_dimes, num_nickles, num_pennies)
                menu_cost = calculate_menu_cost(user_input)

                transaction_successful = check_transaction(user_input, amount_paid)
                if transaction_successful:
                    machine_money = calculate_machine_money(amount_paid, machine_money)
                    calculate_change(amount_paid, menu_cost)
                    machine_resources = deduct_ingredients(user_input, machine_resources)

        else:
            print("Invalid entry. Please try again.\n")


coffee_machine()
