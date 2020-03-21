N = int(input())
G = list(map(int,input().split()))
G.sort(reverse=True)
j=0
count=0
while True:
    for i in G:
        if j-i >= 0:
            j-=i
    if j is not 0:
        print(count)
        break
    count+=1
    j+=count
   



