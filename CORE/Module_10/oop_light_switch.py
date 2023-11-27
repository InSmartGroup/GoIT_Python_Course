# # functional realization of work
# is_turned_on = False
#
#
# def turn_on():
#     global is_turned_on
#     is_turned_on = True
#
#
# def turn_off():
#     global is_turned_on
#     is_turned_on = False
#
#
# print(is_turned_on)
# turn_on()
# print(is_turned_on)
# turn_off()
# print(is_turned_on)


# # OOP realization of work
# class LightSwitch:
#     def __init__(self):
#         self.switch_is_on = False
#
#     def turn_on(self):
#         self.switch_is_on = True
#
#     def turn_off(self):
#         self.switch_is_on = False
#
#
# light_switch = LightSwitch()
# print(light_switch.switch_is_on)
# light_switch.turn_on()
# print(light_switch.switch_is_on)
# light_switch.turn_off()
# print(light_switch.switch_is_on)


# class LightSwitch:
#     def __init__(self):
#         self.turned_on = False
#         self.brightness_level = 0
#
#     def turn_on(self):
#         self.turned_on = True
#
#     def turn_off(self):
#         self.turned_on = False
#
#     def increase_brightness(self, amount):
#         if self.turned_on:
#             self.brightness_level += amount
#
#         if self.brightness_level > 100:
#             self.brightness_level = 100
#
#         print(f"Brightness increased to {self.brightness_level}")
#
#     def decrease_brightness(self, amount):
#         if self.turned_on:
#             self.brightness_level -= amount
#
#         if self.brightness_level < 0:
#             self.brightness_level = 0
#
#         print(f"Brightness decreased to {self.brightness_level}")
#
#     def report(self):
#         print("REPORT".center(25, "-"))
#         if self.turned_on:
#             print("Light switch is on.")
#             print(f"Brightness level: {self.brightness_level}")
#         else:
#             print("Light switch is off.")
#             print(f"Brightness level: {self.brightness_level}")
#         print("".center(25, "_"))
#
#
# light_switch = LightSwitch()
# light_switch.increase_brightness(10)  # won't work
# light_switch.turn_on()
# light_switch.increase_brightness(10)
# light_switch.report()
# light_switch.turn_off()
# light_switch.report()
# light_switch.increase_brightness(50)
# light_switch.report()
# light_switch.turn_on()
# light_switch.increase_brightness(50)
# light_switch.report()
# light_switch.decrease_brightness(200)
# light_switch.report()
