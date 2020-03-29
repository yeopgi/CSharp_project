import sys
n,m = map(int,sys.stdin.readline().split())
DNA=list()
HD=list()
alpha=['A','C','G','T']
total=0
for i in range(n):
    DNA.append(list(sys.stdin.readline()))

def compare(t):
    line=list()
    max=0
    result=list()
    for i in range(n):
        line.append(DNA[i][t])
        if line.count(DNA[i][t])>max:
            max=line.count(DNA[i][t])
            result=[max,DNA[i][t]]
        elif line.count(DNA[i][t])==max:            
            if alpha.index(DNA[i][t])<alpha.index(result[1]):
                result=[max,DNA[i][t]]
            
    return result

for i in range(m):
    HD.append(compare(i))
    print(HD[i][1],end='')
    total += n-HD[i][0]
print("\n"+"%d"%total) 
