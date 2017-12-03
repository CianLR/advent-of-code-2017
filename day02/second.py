from sys import stdin

c = 0
for line in stdin.readlines():
    i = [int(x) for x in line.split()]
    for j, a in enumerate(i):
        for b in i[j+1:]:
            if a % b == 0:
                c += a // b
                break
            elif b % a == 0:
                c += b // a
                break

print(c)

