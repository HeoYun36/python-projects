from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_process = MoneyMachine()

while True:
    customer_drink = input(f"What would you like to drink? ({menu.get_items()}): ")
    if customer_drink == "off":
        break
    elif customer_drink == "report":
        coffee_machine.report()
        money_process.report()
        continue
    elif customer_drink == "espresso" or customer_drink == "latte" or customer_drink == "cappuccino":
        drink = menu.find_drink(customer_drink)
        if coffee_machine.is_resource_sufficient(drink):
            if money_process.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
    else:
        print('You ordered wrongly')
