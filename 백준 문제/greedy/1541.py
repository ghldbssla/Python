array=list(input().split('-'))
result=0

for i in range(len(array)):
    if i==0:
        for j in array[i].split("+"):
            result+=int(j)
    else:
        for j in array[i].split("+"):
            result-=int(j)
                
print(result)
