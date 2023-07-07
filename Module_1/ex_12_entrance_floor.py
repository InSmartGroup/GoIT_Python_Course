# Given the number of apartment, define the entrance and the floor in a building
# The building has 5 floors and 4 apartments per floor
apt = int(input("Enter the number of apartment: "))

floor = apt // 20 + 1
entrance = apt % 20 // 4 + 1

print(f"Apartment {apt} is on the {floor} floor, entrance {entrance}")
