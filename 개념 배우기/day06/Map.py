#Map.py
#맵을 이용해 모든 정수들을 문자열로 바꿈
mapData=list(map(str,[1,2,3,4,5,6,7,8,9]))
print(mapData)

#맵을 이용해 모든 문자열들을 숫자로 바꿈
mapData=list(map(int,['1','2','3','4','5','6','7','8','9']))
print(mapData)

a,b=input("두 정수를 입력하세요(10,20) : ").split(",")
a=int(a)
b=int(b)
print(a,b)

#"문자열".split()은 통채로가 문자열이 담겨있는 문자열리스트이므로
#map을 통해서 한번에 형변환을 해줄 수 있다.
a,b=map(int,input("두 정수를 입력하세요(10,20) : ").split(","))
print(a,b)
