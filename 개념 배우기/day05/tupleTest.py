#tupleTest.py

arTuple=(1,2,3,4,5)
print(arTuple[1])

arTuple+=(6,)# 그냥 6만 쓸 경우 int타입이기 때문에 튜플형태로 만들어 준다.
arTuple+=(7,8)
print(arTuple)

#튜플은 값의 수정이나 삭제가 불가능하다.
#arTuple[2]=1000
#del arTuple[2]

#완전 삭제는 가능
#del arTuple

#튜플의 길이
print(len(arTuple))

def div(num1, num2):
    result1=num1//num2#//는 몫
    result2=num1%num2

    return result1,result2
    #값이 두개인 튜플을 리턴함

result=div(10,3)
print("몫 : ",result[0])
print("나머지 : ",result[1])
