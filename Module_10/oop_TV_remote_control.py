class Remote:
    def __init__(self, brand_name: str, model_name: str):
        self.brand_name = brand_name.title()
        self.model_name = model_name.title()
        self.battery = 100
        self.volume_level = 0
        self.channel = 1
        self.is_turned_on = False

    def turn_on(self):
        self.is_turned_on = True

    def turn_off(self):
        self.is_turned_on = False

    def check_battery_status(self):
        if self.is_turned_on:
            if self.battery < 1:
                self.battery = 0
                self.is_turned_on = False
                print("Low batteries. Please replace.")

    def show_info(self):
        self.check_battery_status()

        if self.is_turned_on:
            print("".center(20, "_"))
            print(f"{self.brand_name} {self.model_name}")
            print("".center(20, "_"))
            print(f"Battery charge: {self.battery}%")
            print(f"Volume level: {self.volume_level}")
            print(f"Current channel: {self.channel}")
            print()

    def volume_up(self, new_volume_value):
        self.check_battery_status()

        if self.is_turned_on:
            self.volume_level += new_volume_value
            self.battery -= 1

            if self.volume_level > 100:
                self.volume_level = 100

    def volume_down(self, new_volume_value):
        self.check_battery_status()

        if self.is_turned_on:
            self.volume_level -= new_volume_value
            self.battery -= 1

            if self.volume_level < 0:
                self.volume_level = 0

    def switch_channel(self, new_channel: int):
        self.check_battery_status()

        if self.is_turned_on:
            self.channel = new_channel
            self.battery -= 1

            if self.channel > 50:
                self.channel = 50

            elif self.channel < 1:
                self.channel = 1


remote = Remote(brand_name='Samsung', model_name='TGS 2500')
remote.turn_on()
remote.show_info()
remote.volume_up(7)
remote.show_info()
remote.volume_down(2)
remote.show_info()
remote.volume_up(200)
remote.show_info()
remote.volume_down(500)
remote.volume_up(12)
remote.switch_channel(120)
remote.switch_channel(-10)
remote.switch_channel(7)
remote.show_info()

for i in range(50):
    remote.volume_up(i)
    remote.show_info()
    remote.switch_channel(i)
