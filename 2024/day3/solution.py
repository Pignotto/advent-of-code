import re

with open("input", "r") as file:
    a = file.read()

b = re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", a)

s = sum(int(x)*int(y) for x, y in b)

print(s)

b = re.findall(r"(mul\(([0-9]{1,3}),([0-9]{1,3})\))|(do\(\))|(don't\(\))", a)

s = 0
enable = True
for c in b:
    if "do()" in c:
        enable = True
    elif "don't()" in c:
        enable = False
    elif enable:
        _, x, y, _, _ = c
        s += int(x)*int(y)

print(s)
