from enum import Enum

class Color(Enum):
    red = 1
    orange = 2
    yellow = 3
    green = 4
    blue = 5
    indigo = 6
    purple = 7

#print(Color(1))

#print(Color['red'])

red_member = Color.red
print(red_member.name)
print(red_member.value)

print(type(Color.red))

print("#"*80)

for color in Color:
    print(color)

print("#"*80)

for color in Color.__members__.items():
    print(color)
