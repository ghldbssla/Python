n=int(input())
sit=input()
cnt=1
L_cnt=0

for i in range(n):
    if(sit[i]=="S"):
        cnt+=1
    elif(sit[i]=="L"):
        L_cnt+=1
        if(L_cnt==2):
            cnt+=1
            L_cnt=0
               
print(min(cnt,n))
