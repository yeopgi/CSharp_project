import sys

n=int(sys.stdin.readline())
t=0
line=list(map(int,sys.stdin.readline().split()))

line.sort()

for i in range(n):
    for j in range(i+1):
        t +=line[j]
    
print(t)
