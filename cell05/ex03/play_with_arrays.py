og = [5, 9, 9, 8, 4, 52, 4, -25]
new = set([])
for i in og:
    x = i+2
    if x >= 10:
        new.add(x)
print(og)
print(new)