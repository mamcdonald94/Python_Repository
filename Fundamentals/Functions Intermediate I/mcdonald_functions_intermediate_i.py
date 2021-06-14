import random


def randInt(min=0, max=100):
    if min == 0:
        num = random.random() * max
    elif min != 0:
        num = random.random() * (max - min) + min
    return num


print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
print(randInt(min=50, max=-45))