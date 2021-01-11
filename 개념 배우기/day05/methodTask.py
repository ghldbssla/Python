#mathodTask.py

#==============1====================
#1~10 출력하는 메소드
from unittest import result

def print1To10():
    for i in range(10):
        print(i+1,end="")
    print()
print1To10()

#1~10까지 합 출력하는 메소드
def sum1To10():
    result=0
    for i in range(10):
        result+=(i+1)
    print(result)
sum1To10()
#==============2====================

#n입력받아서 1~n까지의 합 구해주는 메소드
def sum1ToN(n):
    result=0
    for i in range(1,n+1,1):
        result+=i
    return result
n=int(input("n : "))
print(sum1ToN(n))

#두정수의 나눗셈 메소드
def div(num1, num2):
    if(num1>num2):
        return num1/num2
    else:
        return num2/num1
print(div(10,3))
#==============3====================

#소문자를 대문자로 바꿔주는 메소드("문자열".upper())
def toUpper(msg):
    length=len(msg)
    result=""
    for i in range(length):
        if('a'<=msg[i] and msg[i]<='z'):
            result+=chr(ord(msg[i])-32)
        else:
            result+=msg[i]
    return result
print(toUpper('hellO'))

#문자열을 거꾸로 출력해주는 메소드
def reverse(string):
    result=""
    for i in range(len(string)-1,-1,-1):
        result+=string[i]
    print(result)
reverse("abcd")


#정수를 한글로 바꿔주는 메소드(1024->일공이사)

def toHangle(num):
    data=str(num)
    result=""
    #       0 1 2 3 4 5 6 7 8 9
    hangle="영일이삼사오육칠팔구"
    for i in range(len(data)):
        ch=data[i]
        index=ord(ch)-48
        result+=hangle[index]
    return result
print(toHangle(1234))


















