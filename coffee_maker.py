
class CoffeeMaker:

    __resources = None

    def __init__(self):
        self.__resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        for key in self.__resources:
            print(f"{key}: {self.__resources[key]}ml")

    def is_resource_sufficient(self, drink):
        for key in self.__resources.keys():
            if drink.ingredients()[key] > self.__resources[key]:
                return False
        return True

    def make_coffee(self, order):
        for key in order.ingredients():
            self.__resources[key] -= order.ingredients()[key]

    def get_insufficient_resources(self, item):
        lacking = []
        if (not self.is_resource_sufficient(item)):
            for key in self.__resources:
                if item.ingredients()[key] > self.__resources[key]:
                    lacking.append(key)
        return lacking


