

a = [1, 3, 5, 6]
b = [2, 3, 4, 6]

ab = a + b
ab = sorted(ab)
print(ab)
l = len(ab)

if l % 2 == 0:
    print((ab[l//2 - 1] + ab[l//2]) / 2)
else:
    print(ab[l//2])


