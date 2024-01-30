length = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

occupied_space = 0.17

size_of_aquarium = length * width * height
size_in_liters = size_of_aquarium / 1000
liters_water = size_in_liters * (1 - occupied_space)
print(liters_water)
