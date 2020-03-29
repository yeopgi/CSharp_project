import sys
testcase = int(sys.stdin.readline())

def people(t):
    line = list()
    count=1
    for i in range(t):
        line.append(list(map(int,sys.stdin.readline().split())))
    line.sort(key=lambda x: (x[0]))
    max=line[0][1]
    for j in line:
        if j[1] < max:
            max = j[1]
            count+=1
    return count

for _ in range(testcase):
    t= int (sys.stdin.readline())
    print(people(t))


        
