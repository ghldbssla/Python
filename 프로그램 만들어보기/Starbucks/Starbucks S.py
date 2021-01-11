#Starbucks.py

#Controller.py에 있는 모든 내용 추가해줘!
from Controller import *

title="★☆★☆★☆★☆스타벅스 역삼★☆★☆★☆★☆"
loginMsg="1. 메뉴 주문\n2. 관리자 로그인\n3. 나가기\n"
adminMsg="1. 메뉴 추가하기\n2. 메뉴 수정하기\n3. 메뉴 삭제하기\n4. 메뉴 목록보기\n5. 나가기\n"
orderMsg="1. 주문하기\n2. 장바구니\n3. 뒤로가기"
basketmsg="1. 결제하기\n2. 목록 삭제\n3. 장바구니 비우기\n4. 전체 목록보기\n5. 잔액 충전\n6. 나가기\n"

#################################################################

def adminView():
    while True:
        #1. 메뉴 추가하기\n2. 메뉴 수정하기\n3. 메뉴 삭제하기\n4. 메뉴 목록보기\n5. 나가기
        choice=int(input(adminMsg))
        if choice==1:
            #메뉴추가하기
            name=input("추가할 메뉴 이름 : ")
            price=int(input("추가할 메뉴 가격 : "))
            #위에서 입력받은 메뉴 이름과 가격을 insert()메소드에 넘겨준다.
            insert(name,price)
            
        elif choice==2:
            #메뉴수정하기
            name=input("수정할 메뉴 이름 : ")
            price=input("수정할 메뉴 가격 : ")
            #update()에 입력받은 이름과 새로운 가격을 넘겨준다
            update(name,price)
            
        elif choice==3:
            #메뉴삭제하기
            name=input("삭제할 메뉴 이름 : ")
            price=input("삭제할 메뉴 가격 : ")
            delete(name)
            
        elif choice==4:
            #메뉴목록보기
            print("============현재 메뉴============")
            selectAll()
            print("================================")
        elif choice==5:
            #나가기
            break
def orderView():
    while True:
        #1. 주문하기\n2. 장바구니\n3. 뒤로가기
        choice=int(input(orderMsg))
        
        if choice==1:
            #메뉴주문
            print("============메뉴판============")
            selectAll()
            print("=============================")
            name=input("주문하실 메뉴 : ")
            order(name)
            
        elif choice==2:
            #장바구니
            basketView()
            
        elif choice==3:
            break

def basketView():
    while True:
        choice=int(input(basketMsg))
        if choice==1:
            #결제하기
            pay()
        elif choice==2:
            #목록삭제
            getList()
            idx=int(input("취소하실 주문번호 : "))
            del basket[idx-1]
        elif choice==3:
            #장바구니 비우기
            basket.clear
            print("비우기 완료!")
        elif choice==4:
            #전체 목록
            print("===========장바구니===========")
            getList()
            print("=============================")
        elif choice==5:
            #잔액 충전
            money=int(input("충전하실 금액 : "))
            #입력받은 금액을 deposit()에 넘겨준다.
            deposit(money)
        elif choice==6:
            #나가기
            if getTotal()!=0:
                print("결제하실 금액이 남았습니다.")
            else:
                break
##################################################################
def mainView():
    print(title)
    while True:
        #1. 메뉴 주문\n2. 관리자 로그인\n3. 나가기\n
        choice=int(input(loginMsg))
        if(choice==1):
            #메뉴주문
            orderView()
            
        elif(choice==2):
            #관리자 로그인
            id=input("아이디 : ")
            pw=input("비밀번호 : ")
            #위에서 입력받은 id와 pw를 login 메소드에 넘겨준다.
            if(login(id,pw)):
               #로그인 성공시 구현
                print("로그인 성공!")
                adminView()
            else:
                print("아이디/비밀번호 확인 바랍니다.")
                
        elif(choice==3):
            print("다음에 또 오세요~~~")
            break
















