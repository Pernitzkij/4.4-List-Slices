import random

nums = [random.randint(1, 999) for _ in range(20)]

a = 4
b = 9

name_rid = [nums[x - 1] for x in range(a, b + 1)]
print(name_rid)
