import sys

v = list(input())
n = int(input())

plus = []

index = len(v)
for i in range(n):
    a = sys.stdin.readline().split()
    if a[0] == 'P':
        v.append(a[1])
    elif a[0] == 'L' and v:
        plus.append(v.pop())
    elif a[0] == 'D' and plus:
        v.append(plus.pop())
    elif a[0] == 'B' and v:
        v.pop()

print(''.join(v + list(reversed(plus))))