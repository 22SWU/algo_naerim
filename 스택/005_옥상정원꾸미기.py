N = int(input())

arr = []
for i in range(N):
    arr.append(int(input()))

stack = []
answer = 0

for i in arr:
    while stack and stack[-1]<=i:
        stack.pop()
    stack.append(i)
    answer += len(stack)-1

print(answer)
