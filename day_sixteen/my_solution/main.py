from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
current_menu = Menu()
money_system = MoneyMachine()

while True:
    command = input('What would you like? (espresso/latte/cappuccino): ')
    if command == 'off':
        break
    elif command == 'report':
        machine.report()
        money_system.report()
    else:
        selected_drink = current_menu.find_drink(order_name=command)
        if selected_drink:
            enough_resources = machine.is_resource_sufficient(drink=selected_drink)
            if enough_resources:
                enough_money_inserted = money_system.make_payment(cost=selected_drink.cost)
                if enough_money_inserted:
                    machine.make_coffee(order=selected_drink)


