n=int(input())
array=[]
result=0

for i in range​(n):
    array.append(int(input()))

for i in range(n-1,0,-1):
    if array[i] <= array[i-1]:
        result += (array[i-1]-array[i]+1)
        array[i-1] = array[i]-1

print(result)
