N = int(input())
G = list(map(int,input().split()))
G.sort()

sum=0

for i in G:
    if sum+2 <= i:
        break
    sum+=i

print(sum+1)