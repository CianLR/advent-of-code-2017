from sys import stdin

c = 0
for line in stdin.readlines():
    i = [int(x) for x in line.split()]
    c += max(i) - min(i)

print(c)

