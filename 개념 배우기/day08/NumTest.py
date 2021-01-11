#NumTest.py

#두 정수를 입력 받아서 앞의수를 뒤의수로 나누는 프로그램
while True:
    try:
        num1=int(input("첫번째 정수 : "))
        num2=int(input("두번째 정수 : "))
        print(num1/num2)
    except ValueError:
        print("정수좀 입력해라")
    except ZeroDivisionError:
        print("0으로 나눌 수 없습니다.")
    except KeyboardInterrupt:
        print("안녕히 가세요")
        break
    
while True:
    try:
        num1=int(input("첫번째 정수 : "))
        num2=int(input("두번째 정수 : "))
        print(num1/num2)
    except Exception:
        print("알 수 없는 오류 발생!!")
