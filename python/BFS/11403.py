N=int(input())
G=list()
W=list()
for _ in range(N):
    G.append(list(map(int,input().split())))

for i in G:
    for j in i:
        if j==1:
            W.append([G.index(i),i.index(j)])

print(W)
