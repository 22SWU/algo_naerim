N,M = map(int, input().split())
arr = [0]*12

for i in range(N):
    gender,grade = map(int, input().split())
    if gender == 0:
        arr[2 * grade - 2] += 1
    else:
        arr[2 * grade - 1] += 1

answer = sum(-(-n//M) for n in arr)
print(answer)