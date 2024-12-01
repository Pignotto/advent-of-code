with open("input") as file:
    a = [[int(x) for x in line.split()] for line in file]

x, y = zip(*a)

x = sorted(x)
y = sorted(y)

r = sum([abs(p-q) for p, q in zip(x, y)])

print(r)

s = sum(y.count(k)*k for k in x)

print(s)
