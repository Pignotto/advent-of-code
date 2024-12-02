with open("input") as file:
    a = [[int(x) for x in line.split()] for line in file]

b = [[a-b for a, b in zip(r[:-1], r[1:])] for r in a]
c = [[p>0 for p in r] for r in b]
d = [[1<=abs(p)<=3 for p in r] for r in b]
c1 = [all(s) or not any(s) for s in c]
c2 = [all(s) for s in d]
cf = [a and b for a, b in zip(c1, c2)]

print(cf.count(True))

a2 = [[line[:i]+line[i+1:] for i, _ in enumerate(line)] for line in a]
b2 = [[[a-b for a, b in zip(r[:-1], r[1:])] for r in a] for a in a2]
c2 = [[[p>0 for p in r] for r in b] for b in b2]
d2 = [[[1<=abs(p)<=3 for p in r] for r in b] for b in b2]
c12 = [[all(s) or not any(s) for s in c] for c in c2]
c22 = [[all(s) for s in d] for d in d2]
cf2 = [[a and b for a, b in zip(c1, c2)] for c1, c2 in zip(c12, c22)]
cff = [any(a) for a in cf2]

print(cff.count(True))