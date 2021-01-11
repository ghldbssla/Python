#Quiz.py
choice=0
while True:
    print("다음 중 프로그래밍 언어가 아닌것은?(종료하려면 0)")
    print("1.파이썬")
    print("2.Java")
    print("3.망둥어")
    print("4.C언어")
    choice=int(input("정답 입력 : "))
    
    if(choice==3):
        result="정답입니다."
    elif(choice==1 or choice==2 or choice==4):
        result ="다시 한번 생각해보세요."
    elif(choice==0):
        #무한반복 탈출
        break
    else:
        result= "잘못 입력하셨습니다."
        
    print(result)
