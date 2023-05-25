N = int(input())
answer = []

for i in range(N):
    a,b = input().split()
    if len(a) != len(b):
        answer.append("Impossible")
    else:
        a = sorted(a)
        b = sorted(b)
        if ''.join(a) == ''.join(b):
            answer.append("Possible")
        else:
            answer.append("Impossible")

for v in answer:
    print(v)