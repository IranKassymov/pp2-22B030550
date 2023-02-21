import math

n = int(input())
s = int(input())

a = s / (2 * math.tan(math.pi/n))

print(s*n/2 * a)