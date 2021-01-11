n=int(input())
change=1000-n
bill=[500,100,50,10,5,1]
cnt=0

for i in range(len(bill)):
    if(bill[i]<=change):
        cnt+=change//bill[i]
        change%=bill[i]
    if(change<=0):
        break

print(cnt)
