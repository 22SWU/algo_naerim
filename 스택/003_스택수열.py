N = int(input())
stack = []
answer = []
find = True

i = 1

for _ in range(N):
    num = int(input())
    while i <= num:
        stack.append(i)
        answer.append('+')
        i += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        find = False

if find:
    for i in answer:
        print(i)
else:
    print('NO')