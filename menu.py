from menu_item import MenuItem

class Menu:

    __menu = None

    def __init__(self):
        self.__menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3),
        ]

    def get_items(self):
        options = ""
        for item in self.__menu:
            options += f"{item.name()}/"
        return options

    def find_drink(self, order_name):
        for item in self.__menu:
            if str(order_name).lower() == str(item.name()).lower():
                return item;
        return None
