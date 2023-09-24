class CoffeeMachine:
    def __init__(self):
        self.turned_on = False
        self.water = 0
        self.coffee = 0
        self.milk = 0
        self.cash = 0
        self.trash = 0

    def turn_on(self):
        self.turned_on = True

    def turn_off(self):
        self.turned_on = False

    def add_water(self, amount):
        self.water += amount

    def add_coffee(self, amount):
        self.coffee += amount

    def add_milk(self, amount):
        self.milk += amount

    def add_cash(self, amount):
        self.cash += amount

    def dispose_trash(self):
        self.trash = 0

    def show_report(self):
        print("REPORT".center(30, "-"))
        print(f"Water left: {self.water}")
        print(f"Coffee left: {self.coffee}")
        print(f"Milk left: {self.milk}")
        print(f"Cash: {self.cash}")
        print(f"Disposal tray: {self.trash}")
        print("".center(30, "_"))

    def make_espresso(self):
        water = 30
        coffee = 20
        price = 2
        disposal = coffee / 2

        water_ready = False
        coffee_ready = False
        cash_ready = False
        disposal_ready = False

        if self.turned_on:
            if self.cash >= price:
                cash_ready = True
                self.cash -= price
            else:
                print(f"Not enough cash. Please deposit additional {price - self.cash} USD.")

            if self.water >= water:
                if cash_ready:
                    water_ready = True
                    self.water -= water
            else:
                print("Not enough water. Please refill.")

            if self.coffee >= coffee:
                if cash_ready:
                    coffee_ready = True
                    self.coffee -= coffee
            else:
                print("Not enough coffee. Please refill.")

            if self.trash < 300:
                if cash_ready:
                    disposal_ready = True
                    self.trash += disposal
            else:
                print("The disposal tray is full. Please empty the disposal tray.")

        if water_ready and coffee_ready and disposal_ready and cash_ready:
            print("Preparing espresso...\n")

    def make_latte(self):
        water = 50
        coffee = 30
        milk = 50
        price = 5
        disposal = coffee / 2

        water_ready = False
        coffee_ready = False
        milk_ready = False
        cash_ready = False
        disposal_ready = False

        if self.turned_on:
            if self.cash >= price:
                cash_ready = True
                self.cash -= price
            else:
                print(f"Not enough cash. Please deposit additional {price - self.cash} USD.")

            if self.water >= water:
                if cash_ready:
                    water_ready = True
                    self.water -= water
            else:
                print("Not enough water. Please refill.")

            if self.coffee >= coffee:
                if cash_ready:
                    coffee_ready = True
                    self.coffee -= coffee
            else:
                print("Not enough coffee. Please refill.")

            if self.milk >= milk:
                if cash_ready:
                    milk_ready = True
                    self.milk -= milk
            else:
                print("Not enough milk. Please refill.")

            if self.trash < 300:
                if cash_ready:
                    disposal_ready = True
                    self.trash += disposal
            else:
                print("The disposal tray is full. Please empty the disposal tray.")

        if water_ready and coffee_ready and disposal_ready and cash_ready and milk_ready:
            print("Preparing latte...\n")

    def make_capuccino(self):
        water = 50
        coffee = 50
        milk = 50
        price = 7
        disposal = coffee / 2

        water_ready = False
        coffee_ready = False
        milk_ready = False
        cash_ready = False
        disposal_ready = False

        if self.turned_on:
            if self.cash >= price:
                cash_ready = True
                self.cash -= price
            else:
                print(f"Not enough cash. Please deposit additional {price - self.cash} USD.")

            if self.water >= water:
                if cash_ready:
                    water_ready = True
                    self.water -= water
            else:
                print("Not enough water. Please refill.")

            if self.coffee >= coffee:
                if cash_ready:
                    coffee_ready = True
                    self.coffee -= coffee
            else:
                print("Not enough coffee. Please refill.")

            if self.milk >= milk:
                if cash_ready:
                    milk_ready = True
                    self.milk -= milk
            else:
                print("Not enough milk. Please refill.")

            if self.trash < 300:
                if cash_ready:
                    disposal_ready = True
                    self.trash += disposal
            else:
                print("The disposal tray is full. Please empty the disposal tray.")

        if water_ready and coffee_ready and disposal_ready and cash_ready and milk_ready:
            print("Preparing capuccino...\n")


coffee_machine = CoffeeMachine()

coffee_machine.turn_on()
coffee_machine.show_report()
coffee_machine.make_latte()

coffee_machine.add_coffee(500)
coffee_machine.add_water(1000)
coffee_machine.add_milk(200)
coffee_machine.add_cash(13)
coffee_machine.make_latte()
coffee_machine.make_capuccino()
coffee_machine.show_report()
