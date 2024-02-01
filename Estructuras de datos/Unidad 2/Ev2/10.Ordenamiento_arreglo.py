import random

random_arr = []

i=15

while i > 0:
    random_arr.append(random.randrange(1,100))
    i-=1

print(sorted(random_arr))