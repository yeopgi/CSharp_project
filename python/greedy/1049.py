import sys
N,M = map(int,sys.stdin.readline().split())
manual = []

for _ in range(M):
    manual.append(list(map(int,sys.stdin.readline().split())))

min1=manual[0][0]
min2=manual[0][1]

for i in manual:
    if i[0] <= min1:
        min1=i[0]
    if i[1] <= min2:
        min2=i[1]


if N == 6:
    if min1>min2*N:
        print (min2*N)
    else:
        print (min1)
elif N>6:
    if (min1/6)>= min2:
        print(N*min2)
    else:
        if min1*(N//6+1) < min2*N:
            print(min1*(N//6+1))
        else:
            print((min1*(N//6))+(min2*(N%6)))


else:
    if (min1/6) > min2:
        print(N*min2)

    else:
        print(min1)



