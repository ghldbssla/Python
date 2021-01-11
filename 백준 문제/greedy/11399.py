n=int(input())
man=list(map(int,input().split()))
man.sort()
wait=0
result=0

for i in range(n):
    wait+=man[i]
    result+=wait

print(result)
