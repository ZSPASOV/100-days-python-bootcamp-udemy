QUARTERS_VALUE = 0.25
DIMES_VALUE = 0.10
NICKLES_VALUE = 0.05
PENNIES_VALUE = 0.01

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def report():
    '''
    :return: an f string with the info per resources and money
    '''
    result = f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}"
    return result


def check_resources(water: int, milk: int, coffee: int):
    '''
    A function that checks whether there are enough resources
    :param water: int
    :param milk: int
    :param coffee: int
    :return: bool expression, True if there are enough resourses to make a drink.
    '''
    return water <= resources['water'] and milk <= resources['milk'] and coffee <= resources['coffee']


def process_coins(n_quarters: int, n_dimes: int, n_nickles: int, n_pennies: int):
    '''
    Takes number of each type of coin and multiplies the value to get the final sum.
    :param n_quarters:
    :param n_dimes:
    :param n_nickles:
    :param n_pennies:
    :return: The amount of money.
    '''
    return n_quarters * QUARTERS_VALUE + n_dimes * DIMES_VALUE + n_nickles * NICKLES_VALUE + n_pennies * PENNIES_VALUE


def check_transaction(inserted_money: float, price: float, type_of_drink: str):
    if inserted_money >= price:
        global money
        money += price
        change = inserted_money - price
        return f'Here is ${change:.2f} in change.\nHere is your {type_of_drink} ☕. Enjoy!'
    else:
        return "Sorry that's not enough money. Money refunded."

while True:
    command = input('What would you like? (espresso/latte/cappuccino): ')
    if command == 'off':
        break
    elif command == 'report':
        result = report()
        print(result)

    elif command == 'espresso':
        if check_resources(water=MENU['espresso']['ingredients']['water'], milk=0, coffee=MENU['espresso']['ingredients']['coffee']):
            print('Please insert coins.')
            paid_quarters = int(input('how many quarters?: '))
            paid_dimes = int(input('how many dimes?: '))
            paid_nickles = int(input('how many nickles?: '))
            paid_pennies = int(input('how many pennies?: '))
            paid_total = process_coins(n_quarters=paid_quarters, n_dimes=paid_dimes, n_nickles=paid_nickles, n_pennies=paid_pennies)
            result_of_payment = check_transaction(inserted_money=paid_total, price=MENU['espresso']['cost'], type_of_drink='espresso')
            print(result_of_payment)
            if result_of_payment != "Sorry that's not enough money. Money refunded.":
                resources['water'] -= MENU['espresso']['ingredients']['water']
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
        else:
            print('Sorry there are not enough resources.')

    elif command == 'latte':
        if check_resources(water=MENU['latte']['ingredients']['water'], milk=MENU['latte']['ingredients']['milk'], coffee=MENU['latte']['ingredients']['coffee']):
            print('Please insert coins.')
            paid_quarters = int(input('how many quarters?: '))
            paid_dimes = int(input('how many dimes?: '))
            paid_nickles = int(input('how many nickles?: '))
            paid_pennies = int(input('how many pennies?: '))
            paid_total = process_coins(n_quarters=paid_quarters, n_dimes=paid_dimes, n_nickles=paid_nickles, n_pennies=paid_pennies)
            result_of_payment = check_transaction(inserted_money=paid_total, price=MENU['latte']['cost'], type_of_drink='latte')
            print(result_of_payment)
            if result_of_payment != "Sorry that's not enough money. Money refunded.":
                resources['water'] -= MENU['latte']['ingredients']['water']
                resources['milk'] -= MENU['latte']['ingredients']['milk']
                resources['coffee'] -= MENU['latte']['ingredients']['coffee']
        else:
            print('Sorry there are not enough resources.')


    elif command == 'cappuccino':
        if check_resources(water=MENU['cappuccino']['ingredients']['water'], milk=MENU['cappuccino']['ingredients']['milk'], coffee=MENU['cappuccino']['ingredients']['coffee']):
            print('Please insert coins.')
            paid_quarters = int(input('how many quarters?: '))
            paid_dimes = int(input('how many dimes?: '))
            paid_nickles = int(input('how many nickles?: '))
            paid_pennies = int(input('how many pennies?: '))
            paid_total = process_coins(n_quarters=paid_quarters, n_dimes=paid_dimes, n_nickles=paid_nickles, n_pennies=paid_pennies)
            result_of_payment = check_transaction(inserted_money=paid_total, price=MENU['cappuccino']['cost'], type_of_drink='cappuccino')
            print(result_of_payment)
            if result_of_payment != "Sorry that's not enough money. Money refunded.":
                resources['water'] -= MENU['cappuccino']['ingredients']['water']
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
                resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
        else:
            print('Sorry there are not enough resources.')

