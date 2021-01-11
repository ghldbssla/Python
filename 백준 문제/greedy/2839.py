n=int(input())
cnt=0

for i in range(n):
    for i in range(n):
        if(i*5+j*3==n):
            cnt=i+j
            
if(cnt==0):
    cnt=-1
print(cnt)
