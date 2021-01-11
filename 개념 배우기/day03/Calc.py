#Calc.py
#전체 계산 기록을 누적시켜 담을 history변수
history=""
while True:
    print("1.계산하러 가기\n2.계산기록 보기\n3.계산기록 초기화\n4.나가기")
    choice=int(input())
    if choice==4:
        print("안녕히 가세요.")
        break
    elif choice==1:
        #계산하러 가기
        num1 = int(input("첫번째 정수 : "))
        num2 = int(input("첫번째 정수 : "))
        op = input("연산자 : ")
        #각 알맞은 계산결과를 담을 변수
        result=""
        #op(연산자가 담긴 변수)의 값에 따라서 길 나눠주기
        if op =='+':
            #더하기
            #result 변수에 알맞은 폼대로 결과 문자열을 담아준다
            result="%d+%d=%d"%(num1,num2,num1+num2)
        elif op =='-':
            #빼기
            result="%d-%d=%d"%(num1,num2,num1-num2)
        elif op =='*':
            #곱하기
            result="%d*%d=%d"%(num1,num2,num1*num2)
        elif op =='/':
            #나누기
            #나누는 수가 0이면 아래의 계산이나 history 누적을 하지 않아야
            #하므로 cntinue를 이용해서 while문의 다음 반복으로 넘어간다
            if(num2==0):
                continue
            result="%d/%d=%.3f"%(num1,num2,num1/num2)
        else:
            print("연산자가 아닙니다.")
            #연산을 하지 않았으므로 result를 출력하거나 history 연결해주면
            #안된다. 따라서 이경우도 continue를 통해 아래 내용들을 하지 않는다.
            continue
        #위에서 결과에 맞게 폼으로 맞춰준 문자열 출력
        print(result)
        #그 문자열에 enter까지 연결해서 history에 누적
        history+=result+"\n"
    elif choice==2:
        #계산기록 보기
        print("========계산기록========")
        #history 변수에 아무런 문자열이 없다면, 빈 문자열(초기값)이라면
        #계산을 거치지 않았다라는 뜻이므로
        if(history==""):
            #해당 문자열 출력
            print("계산 기록이 없습니다.")
        else:
            print(history,end="")
        print("=======================")
    elif choice==3:
    #계산기록 초기화
        #input()은 통채로가 사용자가 입력한 문자열 값이다. 따라서 다른 문장
        #안에서도 사용이 가능하고 그 통채로가 입력했을 때의 문자열 값일 것임로
        #바로'Y' 무낮열과 같은지를 비교할 수 있다. 같을때만 if문
        #내부 내용들을 수행하게 된다.
        if(input("기록을 초기화 하시겠습니까?(Y/N)")=='Y'):
            history=""
            
    else:
        print("잘못 입력하셨습니다.")
