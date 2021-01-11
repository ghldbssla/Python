n=int(input())
l=list(map(int,input().split()))
ll=0
result=0

for i in range​(n):
    ll+=l[i]

for i in range(n):
    if(ll==0):
        break
    ll-=l[i]
    result+=(l[i]*ll)
     
print(result)
