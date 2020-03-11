import sys
n= int(sys.stdin.readline())
so = []
for i in range(n):
    so.append(list(map(int,sys.stdin.readline().split())))
so.sort(key=lambda y: (y[1], y[0]))
for i in so:
    print(i[0],i[1])