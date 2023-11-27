from time import sleep


class CoffeeMachine:
    def __init__(self):
        self.coffee = 0
        self.water = 0
        self.milk = 0
        self.cashier = 0
        self.enough_coffee = False
        self.enough_water = False
        self.enough_milk = False

    def get_report(self):
        print(f"Coffee: {self.coffee}")
        print(f"Water: {self.water}")
        print(f"Milk: {self.milk}")
        print(f"Cashier: {self.cashier}")

    def make_espresso(self):
        espresso = {"coffee": 30, "water": 15, "price": 1.25}

        self.cashier += espresso["price"]

        if self.coffee >= espresso["coffee"]:
            self.enough_coffee = True
            self.coffee -= espresso["coffee"]
        else:
            self.enough_coffee = True
            print(f"Not enough coffee. Please refill.")

        if self.water >= espresso["water"]:
            self.enough_water = True
            self.water -= espresso["water"]
        else:
            self.enough_water = False
            print(f"Not enough water. Please refill.")

        if self.enough_coffee and self.enough_water:
            message = "Preparing your espresso"

            for i in range(3):
                print(message)
                sleep(1)
                message += "."

            print("Your espresso is ready. Enjoy!")

    def make_latte(self):
        latte = {"coffee": 50, "water": 30, "milk": 50, "price": 3.5}

        self.cashier += latte["price"]

        if self.coffee >= latte["coffee"]:
            self.enough_coffee = True
            self.coffee -= latte["coffee"]
        else:
            self.enough_coffee = False
            print(f"Not enough coffee. Please refill.")

        if self.water >= latte["water"]:
            self.enough_water = True
            self.water -= latte["water"]
        else:
            self.enough_water = False
            print(f"Not enough water. Please refill.")

        if self.milk >= latte["milk"]:
            self.enough_milk = True
            self.milk -= latte["milk"]
        else:
            self.milk = False
            print(f"Not enough milk. Please refill.")

        if self.enough_coffee and self.enough_water and self.enough_milk:
            message = "Preparing your latte"

            for i in range(3):
                print(message)
                sleep(1)
                message += "."

            print("Your latte is ready. Enjoy!")

    def refill_ingredients(self, coffee, water, milk):
        self.coffee += coffee
        self.water += water
        self.milk += milk

    def withdraw_cash(self):
        message = "Withdrawing the cashier, please wait"

        for i in range(3):
            sleep(1)
            message += "."

        print(f"${self.cashier} have been withdrawn.")
        self.cashier = 0


coffee_machine = CoffeeMachine()
print(coffee_machine.cashier)
coffee_machine.refill_ingredients(1000, 3000, 1000)
coffee_machine.get_report()
coffee_machine.make_espresso()
coffee_machine.make_latte()
coffee_machine.make_latte()
coffee_machine.get_report()

coffee_machine.withdraw_cash()