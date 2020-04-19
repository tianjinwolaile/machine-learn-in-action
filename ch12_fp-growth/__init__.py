a = list(range(20))

print(a)

for i, v in enumerate(a):
    if v % 2 == 0:
        # a.remove(i)
        del(a[i])

print(a)


b = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
print(b)
b = {k: v for k, v in b.items() if v > 2}
print(b)
# for k in b.keys():
#     if b[k] < 3:
#         del(b[k])


