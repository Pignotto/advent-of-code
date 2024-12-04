with open("input", "r") as file:
    s = file.read()

s = [list(line+'.') for line in s.split('\n')][:-1]

a = [''.join(row) for row in s]

r = 0
r += sum(len(line.split("XMAS"))-1 for line in a)
r += sum(len(line.split("SAMX"))-1 for line in a)

b = [''.join(column) for column in [*zip(*s)]]

r += sum(len(line.split("XMAS"))-1 for line in b)
r += sum(len(line.split("SAMX"))-1 for line in b)

c = [line[i:]+line[:i] for i, line in enumerate(s)]
c1 = [''.join(column) for column in [*zip(*c)]]

r += sum(len(line.split("XMAS"))-1 for line in c1)
r += sum(len(line.split("SAMX"))-1 for line in c1)

d = [line[-i-1:]+line[:-i-1] for i, line in enumerate(s)]
d1 = [''.join(column) for column in [*zip(*d)]]

r += sum(len(line.split("XMAS"))-1 for line in d1)
r += sum(len(line.split("SAMX"))-1 for line in d1)

print(r)

def x_mas(s, i, j):
    m = [
        "M.M",
        ".A.",
        "S.S"
    ]
    t = [(0, 0), (2, 0), (0, 2), (2, 2), (1, 1)]
    return (
        all(s[i+x][j+y]==m[x][y] if i+x<len(s) and j+y<len(s[i+x]) else False for x, y in t)
     or all(s[i+x][j+y]==m[-x-1][y] if i+x<len(s) and j+y<len(s[i+x]) else False for x, y in t)
     or all(s[i+x][j+y]==m[y][x] if i+x<len(s) and j+y<len(s[i+x]) else False for x, y in t)
     or all(s[i+x][j+y]==m[-y-1][x] if i+x<len(s) and j+y<len(s[i+x]) else False for x, y in t)
    )
        
v = [x_mas(s, i, j) for i, _ in enumerate(s) for j, _ in enumerate(s[i])].count(True)

print(v)