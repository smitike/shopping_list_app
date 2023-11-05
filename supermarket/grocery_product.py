class GroceryProduct:
    def __init__(self, name, price, discount):
        self.name = name
        self.price = price
        self.discount = discount

    def get_actual_price(self):
        return self.price - (self.price * self.discount / 100)

    def display(self):
        return (
            "Name: " + self.name + "\n" +
            "Price: " + str(self.price) + "\n" +
            "Discount: " + str(self.discount) + "%"
        )

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def get_discount(self):
        return self.discount

    def set_discount(self, discount):
        self.discount = discount

# class DairyProduct(GroceryProduct):
#     def __init__(self, name, price, discount, fat):
#         super().__init__(name, price, discount)
#         self.fat = fat
#
#     def display(self):
#         return super().display() + "\nFat Level: " + self.fat
#
#     def get_fat(self):
#         return self.fat
#
#     def set_fat(self, fat):
#         self.fat = fat
#
# class Beverage(GroceryProduct):
#     def __init__(self, name, price, discount, sugar_level):
#         super().__init__(name, price, discount)
#         self.sugar_level = sugar_level
#
#     def display(self):
#         return super().display() + "\nSugar Level: " + self.sugar_level
#
#     def get_sugar_level(self):
#         return self.sugar_level
#
#     def set_sugar_level(self, sugar_level):
#         self.sugar_level = sugar_level
# class Fat:
#     FULLCREAM = "FULLCREAM"
#     HALFCREAM = "HALFCREAM"
#     SKIMMED = "SKIMMED"
#
# class SugarLevel:
#     LIGHT = "LIGHT"
#     ZERO = "ZERO"
#     ADDED_SUGAR = "ADDED_SUGAR"
#     NO_ADDED_SUGAR = "NO_ADDED_SUGAR"
#
# cart = []
#
# toast = GroceryProduct("Toast", 2.5, 10)
# cart.append(toast)
#
# coke = Beverage("Coke", 1.5, 0, SugarLevel.ZERO)
# cart.append(coke)
#
# milk = DairyProduct("Milk", 4, 0, Fat.FULLCREAM)
# cart.append(milk)
#
# total = sum(item.get_actual_price() for item in cart)

# print("The total cost =", total)
# Note that the Java main method is not needed in Python.
