#에라토스체네스의 체
che =[2,3,5,7]
testlist=list()
testcase=int(input())

for _ in range(testcase):
    testlist.append(list(map(int,input().split())))

def eratos(j):
    start = j[0]
    result=list()
    while start < j[1]:
        start+=1
        ex=start
        for i in che:
            if ex % i !=0:
                ex%=i
                continue
            else:
                break
            result.append(ex)
            
    return result

for j in testlist:
    print(eratos(j))

