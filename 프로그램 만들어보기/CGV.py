#CGV.py
#날짜나 시간에 관련된 모듈 datetime 추가
import datetime
#랜덤에 대한 모듈 random 추가
import random

title="⫸CGV⫷"
mainMsg = "①예매하기\n②구매하기\n③쿠폰등록\n④거래내역\n⑤결제하기\n⑥충전하기\n⑦나가기\n"
foodMsg = "①콜라(3000원)\n②팝콘(7000원)\n③맥주(4000원)\n④뒤로가기\n"
#영화의 제목들이 담겨있는 리스트
movieList=["조제","800","런"]
#상품의 이름들이 담겨있는 리스트
productList = ["콜라","팝콘","맥주"]
#상품의 가격들이 담겨있는 리스트
priceList = [3000,7000,4000]
#프로그램 실행과 동시에 랜덤한 5자리수를 만들어서 쿠폰번호로 설정해 놓는다.
coupon = random.randrange(10000,100000)
#초기자본 설정
money=50000
#모든 예매, 구매한 가격들이 누적될 변수
price=0
#모든 예매, 구매, 결제 등 기록들이 담길 리스트
bookList=[]
#현재 쿠폰을 등록했는지 안했는지를 설정해줄 flag변수
couponFlag=False
#flag기법 : 어느 부분에 들어갔는지, 어떤 정해진 작업을 했는지 여부를 판단할 수 있는 기법
#초기값을 False(True)로 정해놓고, 제어문을 이용해서 True(False)로 값을 바꿔주는 방식으로 사용한다.

print(title)
while True:
    #쿠폰번호 확인을 위해 한번 출력
    print(coupon)
    #위에서 담아놓은 메인메세지 출력하며 입력받기
    choice=int(input(mainMsg))
    
    if choice==1:
        #예매하기
        while True:
            #영화 이름 리스트를 순회하며 모든 이름들 출력
            #출력폼 : 1. 조제
            #         2. 800
            #           ...
            for i in range(len(movieList)):
                print(i+1,". "+movieList[i],sep='')
            #마지막 영화를 출력한 후의 선택지는 뒤로가기 이므로
            #movieList의 길이+1번 은 뒤로가기이다.
            print(len(movieList)+1,". 뒤로가기",sep="")
            #변수의 재사용
            #장점 : 메모리 효율
            #단점 : 헷갈린다, 가독성이 떨어진다.
            choice=int(input())
            #현재시간 구하기
            now = str(datetime.datetime.now())
            if choice==len(movieList)+1:
                #뒤로가기
                print("메인메뉴로 돌아갑니다.")
                break
            elif (choice<1 or choice>len(movieList)+1): 
                print("잘못 입력하셨습니다.")
                continue
            #여기까지 왔다면 제대로 영화를 선택했다는 뜻이므로
            #거래내역에 추가해주어야 한다.
            #'영화 이름' 예매 성공! 을 출력해 주고
            print(movieList[choice-1]+" 예매 성공!")
            #거래내역(bookList)에 폼을 맞춰서 추가(append)해준다.
            #거래내역 폼 : 영화제목 / 현재시간 / 예매
            bookList.append(movieList[choice-1]+" / "+now+" / 예매")
            #예매를 성공했으므로 결제해야할 금액 +12000 누적
            price+=12000
    elif choice==2:
        #구매하기
        while True:
            #상품 구매 메세지 출력해주며 입력받기
            foodChoice=int(input(foodMsg))
            if foodChoice==4:
                print("메인메뉴로 돌아갑니다.")
                break
            elif (foodChoice!=1 and foodChoice!=2 and foodChoice!=3):
                print("잘못 입력하셨습니다.")
                continue
            #맥주는 나이를 검사한 후 거래내역에 추가
            if foodChoice==3:
                age=int(input("당신의 나이는 : "))
                if age<19:
                    print("미성년자는 구입할 수 없습니다.")
                    continue
            now = str(datetime.datetime.now())
            #'상품이름' 구매 성공! 출력
            print(productList[foodChoice-1]+" 구매 성공!")
            #거래내역(bookList)에 폼에맞춰서 추가(append)
            #폼 : 상품이름 / 현재시간 / 구매
            bookList.append(productList[foodChoice-1]+" / "+now+" / 구매")
            #priceList에 같은 index에 존재하는 가격이 내가 고른 상품의 가격이다.
            #따라서 그 방에 있는 가격을 가지고 와서 price에 누적시켜준다.
            price+=priceList[foodChoice-1]
            
    elif choice==3:
        #쿠폰등록
        myCoupon = int(input("쿠폰 번호 입력 : "))
        #위에서 설정한 쿠폰번호와 내가 입력한 쿠폰번호가 같다면
        if coupon == myCoupon:
            #쿠폰등록성공
            #위에서 만들어놓은 flag변수값 변경(깃발들기)
            couponFlag=True
        else:
            print("쿠폰 번호가 잘못되었습니다.")
            
    elif choice==4:
        #거래내역
        #모든 거래내역은 bookList에 담기기 때문에 그 길이만큼 순회하면서
        #안에 들어있는 문자열들 전부 출력하면 된다.
        for i in range(len(bookList)):
            print(bookList[i])
            
    elif choice==5:
        #결제하기
        print("결제를 시작합니다.")
        #결제할 금액이 없는경우에는 아래 내용을 하지 않아야 하므로
        #continue를 이용해서 다음 반복으로 넘어가준다.
        if(price==0):
            print("결제할 내역이 없습니다.")
            continue
        #쿠폰깃발이 들려있는지(True인지)를 비교
        if couponFlag:
            #쿠폰할인 적용
            print("쿠폰 할인(50%) 적용")
            #가격을 절반으로 깎아주고
            price/=2
            #깃발은 다시 내리기
            couponFlag=False
            #쿠폰번호도 재발급 해준다.
            coupon = random.randrange(10000,100000)
        
        print("결제하실 금액 : %d"%price)
        now = str(datetime.datetime.now())
        #내가 갖고있는 money가 결제할 price보다 많거나 같다면
        if money>=price:
            #money에서 price만큼을 누적감소
            money-=price          
            print("결제 성공 / 현재 잔액 %d원\n"%money)
            #거래내역에 append
            bookList.append(str(price)+"원 결제시도 / "+now+" / 성공")
            #결제를 성공했으므로 결제할 금액인 price는 0으로 초기화 해준다.
            price=0
        else:
            print("결제 실패 / 잔액부족")
            #거래내역에 실패로 append
            bookList.append(str(price)+"원 결제시도 / "+now+" / 실패")
    elif choice==6:
        money+=int(input("충전하실 금액 : "))
        print("충전 성공!\n현재 잔액 :",money)
    elif choice==7:
        print("안녕히가세요")
        break
    else:
        print("잘못 입력하셨습니다.")




















