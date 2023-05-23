S = input()
dic = dict()

for i in 'abcdefghijklmnopqrstuvwxyz':
    dic[i] = 0

for i in S:
    dic[i] += 1

for v in dic.values():
    print(v, end=" ")