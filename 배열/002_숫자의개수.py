A = int(input())
B = int(input())
C = int(input())

mul = A*B*C
dic = {}

for i in '0123456789':
    dic[i] = 0

for i in str(mul):
    dic[i] += 1

for i in dic.values():
    print(i)