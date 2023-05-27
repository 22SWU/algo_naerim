n = int(input())

for _ in range (n):
    s1 = []
    s2 = []
    v = input()
    for i in v:
        if i == "<":
            if s1:
                s2.append(s1.pop())
        elif i == ">":
            if s2:
                s1.append(s2.pop())
        elif i == "-":
            if s1:
                s1.pop()
        else:
            s1.append(i)

    print(''.join(s1+ list(reversed(s2))))
