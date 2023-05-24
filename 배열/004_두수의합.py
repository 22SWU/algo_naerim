N = int(input())
arr = list(map(int, input().split()))
X = int(input())

answer = 0

arr.sort()

i = 0
j = N-1

while i<j:
    if arr[i]+arr[j] == X:
        answer += 1
        i += 1
    elif arr[i]+arr[j] > X:
        j -= 1
    else:
        i += 1

print(answer)