A=list(input())
B=list(input())

count=len(B)-len(A)

t=50
for i in range(count+1):
    result=0
    for j in range(len(A)):
        if A[j] != B[j+i]:
            result+=1
    if result<t:
        t=result
print(t)   


        