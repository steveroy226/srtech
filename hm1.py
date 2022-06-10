m=int(input())
count=0
for i in range(1,m):
    if(i%5==0):
        count+=1
        print(count,end=" ")