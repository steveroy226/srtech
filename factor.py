m=int(input())
print("Factors of",m)
for i in range(1,m+1):
    if(m%i==0):
        print(i,end=" ")