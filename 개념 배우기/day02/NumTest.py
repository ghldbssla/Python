#NumTest.py

#print("잘 입력했어요")if num>10 else print("다시 한번 생각해봐")

#print("잘 입력했어요")if num>10 else print("다시 한번 생각해봐")

#두 수 입력받아서 비교후 큰 수 출력해주기

#첫번째 정수 :
#두번째 정수 :

#첫번째 수가 큽니다.
#두번째 수가 큽니다.
#두 수가 같습니다.

#입력 - 두 정수 입력

num1 = int(input("첫번째 수 입력해봐 : "))
num2 = int(input("두번째 수 입력해봐 : "))
#처리 - 두 수 비교(num1, num2)
result="첫번째 수가 큽니다."if num1>num2 else( "두번째 수가 큽니다."if num2>num1 else "두 수가 같습니다.")
#   -첫번째 수가 큽니다.
#   -두번째 수가 큽니다.
#   -두 수가 같습니다.
#출력
print(result)

