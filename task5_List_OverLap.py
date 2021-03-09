#task5 two list overlap, new list the common

import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 21]
c = []

# Random list generator
a = random.sample(range(20),random.randint(5, 20))
b = random.sample(range(20),random.randint(5, 20))

for elem in a:
    if elem in b and elem not in c:
        c.append(elem)

print(c)
