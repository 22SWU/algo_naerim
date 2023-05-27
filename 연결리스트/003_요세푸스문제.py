N,K = map(int, input().split())

index = 0
arr = list(n for n in range(1, N+1))
answer = []

while len(arr) != 0:
    index += K-1
    index = index%len(arr)
    answer.append(str(arr.pop(index)))

print("<", end="")
print(", ".join(answer), end="")
print(">")