import random as r

# print(set(r.sample(range(1, 46), 6)))

s = set([])
l = 0
while l < 6:
    num = int(r.random() * 45) + 1
    s.add(num)
    l = len(s)

print(s)
