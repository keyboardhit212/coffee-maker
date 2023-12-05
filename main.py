from coffee_maker import CoffeeMaker
from menu import Menu
from menu_item import MenuItem
from money_machine import MoneyMachine

if __name__ == '__main__':
    menu = Menu()
    money_machine = MoneyMachine()
    coffee_maker = CoffeeMaker()

    while True:
        order = input(f"What would you like? {menu.get_items()}: ")
        item = menu.find_drink(order)
        if item is not None:
            if coffee_maker.is_resource_sufficient(item):
                if money_machine.make_payment(item.cost()):
                    coffee_maker.make_coffee(item)
                    print(f"Here is your {item.name()}. Enjoy!")
            else:
                [print(f"Sorry there is not enough {key}") for key in coffee_maker.get_insufficient_resources(item)]
        else:
            if order == "off":
                print("Turning off...")
                exit(1)
            elif order == "report":
                coffee_maker.report()
                money_machine.report()
            else:
                print("Sorry that item is not available")