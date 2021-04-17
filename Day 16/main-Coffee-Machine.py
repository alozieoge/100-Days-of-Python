from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

maker = CoffeeMaker()
drink_menu = Menu()
machine = MoneyMachine()

is_on = True

while is_on:
    choice = input("WHat would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        maker.report()
        machine.report()
    else:
        drink_order = drink_menu.find_drink(choice)
        if maker.is_resource_sufficient(drink_order):
            if machine.make_payment(drink_order.cost):
                maker.make_coffee(drink_order)
