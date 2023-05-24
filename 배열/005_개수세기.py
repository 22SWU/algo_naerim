N = int(input())
arr = list(map(int, input().split()))
X = int(input())

answer = 0
answer = sum(1 for i in arr if i==X)

print(answer)