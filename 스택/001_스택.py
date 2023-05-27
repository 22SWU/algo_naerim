import sys

N = int(input())

arr = []

for i in range(N):
    command = sys.stdin.readline().split()
    if command[0] == "push":
        arr.append(command[1])
    elif command[0] == "top":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr[-1])
    elif command[0] == "size":
        print(len(arr))
    elif command[0] == "empty":
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == "pop":
        if len(arr) == 0:
            print(-1)
        else:
            print(arr.pop())