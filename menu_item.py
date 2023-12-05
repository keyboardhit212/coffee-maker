
class MenuItem:

    __name = None
    __cost = None
    __ingredients = None

    def __init__(self, name, cost, water, milk, coffee):
        self.__name = str(name)
        self.__cost = float(cost)
        self.__ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee,
        }

    def name(self):
        return self.__name

    def cost(self):
        return self.__cost

    def ingredients(self):
        return self.__ingredients
