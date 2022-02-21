# design a class that represents a cell phone
# create an init method that accepts arguments for the manufacturer, model number, and retail price


class cellphone:

    # the init method initializes the attributes

    def __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

    # the set manufact method accepts an argument for the phone's manufacturer

    def set_manufact(self, manufact):
        self.__manufact = manufact

    def set_model(self, model):
        self.__model = model

    def set_price(self, price):
        self.__price = price

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price

    def set_model(self):
        self.__model

    def set_retail_price(self):
        self.__retail_price
