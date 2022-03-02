from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
# item = MenuItem()
maker = CoffeeMaker()
machine = MoneyMachine()

isOn = True

while isOn:
    print("'REPORT' for more info \n")
    print(menu.get_items())
    abc = input("What do you want? ").lower()

    if abc == 'off':
        isOn = False
    elif abc == 'report':
        machine.report()
        maker.report()
    else:
        drink = menu.find_drink(abc)
        if maker.is_resource_sufficient(drink):
            if machine.make_payment(drink.cost):
                maker.make_coffee(drink)
