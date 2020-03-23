#플로이드-워셜 알고리즘 - 모든 정점에서 모든 정점으로의 알고리즘 
#다익스트라 알고리즘 - 하나의 정점에서 모든 정점으로의 알고리즘
N=int(input())
G=list()
for _ in range(N):
    G.append(list(map(int,input().split())))


for k in range(N):
    for i in range(N):
        for j in range(N):
            if G[i][j] == 1 or (G[i][k]==1 and G[k][j]==1):
                G[i][j]=1

for t in G:
    for p in t:
        print(p, end=' ')
    print()





            
    