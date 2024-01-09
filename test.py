from itertools import zip_longest
a = [[1,2,3,4,5], [1,2,3], [1,2,3,4]]

b = list(zip_longest(*a))
print(b)
c = []
for l in b:
    c.extend(l)

c = [i for i in c if i is not None]
print(c)
