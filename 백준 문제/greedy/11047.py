n,k=map(int,input().split())
bill=list()

for i in range(n):
bill.append(int(input()))

cnt=0
bill.reverse()

for i in range(len(bill)):
    if(bill[i]<=k):
        cnt+=k//bill[i]
        k%=bill[i]
    if(k<=0):
        break
print(cnt)
